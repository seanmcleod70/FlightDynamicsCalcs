import math
from collections import namedtuple

class ISAtmosphere:
    # Constants
    R = 287.0528    # Specific gas constant
    g0 = 9.80665    # Gravitational acceleration 
    gamma = 1.4     # Air specific heat ratio
    r0 = 6356766    # Earth radius

    StdSL_pressure = 101325         # Pa
    StdSL_speed_of_sound = 340.294  # m/s

    # Atmosphere bands
    AtmosphereBand = namedtuple('AtmosphereBand', ['start_alt', 'end_alt', 
                                                   'base_temperature', 'base_pressure',
                                                   'lapse_rate'])
    
    atmosphere_bands = [
        AtmosphereBand(0,     11000, 288.15, 101325,    -0.0065),
        AtmosphereBand(11000, 20000, 216.65, 22632,     0.0),
        AtmosphereBand(20000, 32000, 216.65, 5474.9,    0.001),
        AtmosphereBand(32000, 47000, 228.65, 868.02,    0.0028),
        AtmosphereBand(47000, 51000, 270.65, 110.91,    0.0),
        AtmosphereBand(51000, 71000, 270.65, 66.939,    -0.0028),
        AtmosphereBand(71000, 84852, 214.65, 3.9564,    -0.002),
        ]

    def geopotential_altitude(self, geometric_altitude):
        return (geometric_altitude * self.r0)/(self.r0 + geometric_altitude)
    
    def geometric_altitude(self, geopotential_altitude):
        return (self.r0 * geopotential_altitude)/(self.r0 - geopotential_altitude)

    def state(self, geometric_altitude, delta_temp=0):
        geopot_altitude = self.geopotential_altitude(geometric_altitude)
        band_data = self.get_atmosphere_band(geopot_altitude)
        
        dh = geopot_altitude - band_data.start_alt
        lapse_rate = band_data.lapse_rate
        
        temp = 0
        pressure = 0
        density = 0
        speed_of_sound = 0

        if lapse_rate != 0.0:
            temp = band_data.base_temperature + lapse_rate * dh
            pressure = band_data.base_pressure * math.pow(temp/band_data.base_temperature, -self.g0/(lapse_rate * self.R))
        else:
            temp = band_data.base_temperature
            pressure = band_data.base_pressure * math.exp((-self.g0 * dh)/(self.R * temp))

        density = pressure/(self.R * (temp + delta_temp))
        speed_of_sound = math.sqrt(self.gamma * self.R * (temp + delta_temp))

        return (pressure, density, temp + delta_temp, speed_of_sound)
        
    def get_atmosphere_band(self, geopot_altitude):
        for band in self.atmosphere_bands:
            if geopot_altitude >= band.start_alt and geopot_altitude <= band.end_alt:
                return band
        raise IndexError('Altitude out of range')


# Airspeed Utils

def CAStoMach(cas, altitude):
    """Convert Calibrated airspeed to Mach value.

    Assume m/s for cas and m for altitude.

    Based on the formulas in the US Air Force Aircraft Performance Flight
    Testing Manual (AFFTC-TIH-99-01), in particular sections 4.6 to 4.8.

    The subsonic and supersonic Mach number equations are used with the simple
    substitutions of (Vc/asl) for M and Psl for P. However, the condition for
    which the equations are used is no longer subsonic (M < 1) or supersonic
    (M > 1) but rather calibrated airspeed being less or greater than the
    speed of sound ( asl ), standard day, sea level (661.48 knots).
    """
    ISA = ISAtmosphere()

    pressure, _, _, _ = ISA.state(altitude)

    if cas < ISAtmosphere.StdSL_speed_of_sound:
        # Bernoulli's compressible equation (4.11)
        qc = ISAtmosphere.StdSL_pressure * (
            math.pow(1 + 0.2 * math.pow(cas / ISAtmosphere.StdSL_speed_of_sound, 2), 3.5) - 1
        )
    else:
        # Rayleigh's supersonic pitot equation (4.16)
        qc = ISAtmosphere.StdSL_pressure * (
            (
                (166.9215801 * math.pow(cas / ISAtmosphere.StdSL_speed_of_sound, 7))
                / math.pow(7 * math.pow(cas / ISAtmosphere.StdSL_speed_of_sound, 2) - 1, 2.5)
            )
            - 1
        )

    # Solving for M in equation (4.11), also used as initial condition for supersonic case
    mach = math.sqrt(5 * (math.pow(qc / pressure + 1, 2 / 7) - 1))

    if mach > 1:
        # Iterate equation (4.22) since M appears on both sides of the equation
        for i in range(7):
            mach = 0.88128485 * math.sqrt((qc / pressure + 1) * math.pow(1 - 1 / (7 * mach * mach), 2.5))

    return mach    

def CAStoTAS(cas, altitude):
    """Assume m/s for input and output velocities and m for altitude."""

    mach = CAStoMach(cas, altitude)
    ISA = ISAtmosphere()
    _, _, _, speed_of_sound = ISA.state(altitude)
    return mach * speed_of_sound

def TAStoCAS(tas, altitude):
    """Assume m/s for input and output velocities and m for altitude."""

    ISA = ISAtmosphere()
    pressure, _, _, speed_of_sound = ISA.state(altitude)

    mach = tas / speed_of_sound
    qc = pressure * ( math.pow(1 + 0.2*mach**2, 7/2) - 1)
    cas = ISA.StdSL_speed_of_sound * math.sqrt( 5 * ( math.pow(qc/ISA.StdSL_pressure + 1, 2/7) - 1) ) 
    return cas

def CAStoEAS(cas, altitude):
    """Assume m/s for input and output velocities and m for altitude."""
    ISA = ISAtmosphere()
    _, density, _, _ = ISA.state(altitude)
    _, rho0, _, _ = ISA.state(0)  # Standard sea level density
    eas = CAStoTAS(cas, altitude) * math.sqrt(density / rho0)
    return eas

def EAStoTAS(eas, altitude):
    """Assume m/s for input and output velocities and m for altitude."""
    ISA = ISAtmosphere()
    _, density, _, _ = ISA.state(altitude)
    _, rho0, _, _ = ISA.state(0)  # Standard sea level density
    tas = eas * math.sqrt(rho0 / density)
    return tas

def MachtoCAS(mach, altitude):
    """Assume m for altitude."""
    ISA = ISAtmosphere()
    _, _, _, speed_of_sound = ISA.state(altitude)
    return TAStoCAS(mach * speed_of_sound)
