import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # International Standard Atmosphere

    The ISA model is a static atmosphere model based on average conditions at mid latitudes and assuming dry air.

    The atmosphere is split into a number of layers with an assumed linear distribution of absolute tempertaure $T$
    against geopotential altitude $h$.

    Specifying a geometric altitude $z$ the following atmospheric properties can be computed and returned:

    |Atmospsheric Property|
    |---------------------|
    |Tempertaure $T$      |
    |Pressure $p$         |
    |Density $\rho$       |
    |Speed of sound $c$   |

    The atmospheric properties are calculated using a set of 6 constants, 6 equations and the layer data.

    ## Non-Standard Days

    > Non-standard (hot or cold) days are modeled by adding a specified temperature delta to the standard temperature at altitude, but pressure is taken as the standard day value. Density and viscosity are recalculated at the resultant temperature and pressure using the ideal gas equation of state.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Constants

    |Constant|Symbol|Value|Units|
    |--------|------|-----|-----|
    |Gravitational acceleration|$g$|$9.80665$|$m \cdot s^{-2}$|
    |Specific gas constant|$R_{specific}$|$287.0528$|$J \cdot kg^{-1} \cdot K^{-1}$|
    |Air specific heat ratio|$\gamma$|$1.4$||
    |Earth radius|$r_0$|$6356766$|m|
    |Standard sea-level pressure|$p_0$|$101325$|$Pa$|
    |Standard sea-level speed of sound|$a_0$|$340.294$|$m \cdot s^{-1}$|
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Layers

    |Layer|Layer Name|Base geopotential altitude ($h (m)$)|Lapse rate ($^{\circ}C/km$)|Base temp ($^{\circ}C$)|Base pressure ($Pa$)|
    |-----|----------|------------------------------------|-------------------|---------------|--------------------|
    |0    |Troposphere|0|6.5|15.0|101,325|
    |1    |Tropopause|11,000|0.0|-56.5|22,632|
    |2    |Stratosphere|20,000|-1.0|-56.5|5,474.9|
    |3    |Stratosphere|32,000|-2.8|-44.5|868.02|
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Equations

    ### Geometric and Geopotential Altitudes

    The geopotential altitude is based on a model that adjusts the altitude to include the variation of gravity with height, 
    while geometric altitude is the standard direct vertical distance above mean sea level (MSL).  

    $$z = \frac{r_0 h}{r_0 - h} \tag{1}$$

    Where $z$ is the geometric altitude and $h$ is the geopotential altitude.

    ### Temperature

    $T_0$ is the temperature at start of the layer, $a$ is the lapse rate for the layer, $p_0$ is the atmospheric
    pressure at the start of the layer and $dh$ is the altitude above the start of the layer.

    $$T = T_0 + a \cdot dh \tag{2}$$

    ### Pressure

    When the lapse rate is not 0.

    $$p = p_0 \left( \frac{T}{T_0} \right)^{-g/{aR}} \tag{3}$$

    When the lapse rate is 0.

    $$\large p = p_0 e^{{-g dh}/{RT}} \tag{4}$$

    ### Density

    $$\rho = \frac{p}{RT} \tag{5}$$

    ### Speed of Sound

    $$c = \sqrt{\gamma R T} \tag{6}$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Python Implementation""")
    return


@app.cell
def _():
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

    return ISAtmosphere, math


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Airspeed Utility Functions

    Utility functions to convert between calibrated airspeed (CAS), true airspeed (TAS) and Mach (M) are provided. These
    utlity functions make use of the ISA Python class for part of their calculations.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### CAS to Mach""")
    return


@app.cell
def _(ISAtmosphere, math):
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
    return (CAStoMach,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### CAS to TAS""")
    return


@app.cell
def _(CAStoMach, ISAtmosphere):
    def CAStoTAS(cas, altitude, delta_temp=0):
        """Assume m/s for input and output velocities and m for altitude."""

        mach = CAStoMach(cas, altitude)
        ISA = ISAtmosphere()
        _, _, _, speed_of_sound = ISA.state(altitude, delta_temp)
        return mach * speed_of_sound
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### TAS to CAS""")
    return


@app.cell
def _(ISAtmosphere, math):
    def TAStoCAS(tas, altitude, delta_temp=0):
        """Assume m/s for input and output velocities and m for altitude."""

        ISA = ISAtmosphere()
        pressure, _, _, speed_of_sound = ISA.state(altitude, delta_temp)

        mach = tas / speed_of_sound
        qc = pressure * ( math.pow(1 + 0.2*mach**2, 7/2) - 1)
        cas = ISA.StdSL_speed_of_sound * math.sqrt( 5 * ( math.pow(qc/ISA.StdSL_pressure + 1, 2/7) - 1) ) 
        return cas
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Plotting the ISA

    The plots for temperature, pressure, density and speed of sound versus geometric altitude are produced by making 
    use of the ISA Python class. Included in the plots are outputs for the ISA standard day as well as two non-standard days. 
    One being +15C above standard day and one being -15C below standard day.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ### Temperature

    Effectively showing the linear lapse rates for the layers.
    """
    )
    return


@app.cell
def _(plotISA):
    plotISA('temps')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Speed of Sound

    Since the speed of sound is proportional to the temperature the shape of the speed of sound curves mirrors the 
    temperature curves.
    """
    )
    return


@app.cell
def _(plotISA):
    plotISA('cs')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Density""")
    return


@app.cell
def _(plotISA):
    plotISA('densities')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Pressure

    Given the definition of a non-standard day as expected the pressure versus altitude is identical for all 3 cases.
    """
    )
    return


@app.cell
def _(plotISA):
    plotISA('pressures')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Plotting Routine""")
    return


@app.cell
def _(ISAtmosphere, np, plt):
    def plotISA(property):

        ISA = ISAtmosphere()

        alts = np.linspace(0, 20000, 200)

        msTokt = 1.944012

        titles_units = {
            'pressures': { 'title': 'Pressure vs Altitude', 'xaxis': '$Pa$'},
            'densities': { 'title': 'Density vs Altitude', 'xaxis': '$kg \cdot m^{-3}$'},
            'temps': { 'title': 'Temperature vs Altitude', 'xaxis': '$^{\circ}C$'},
            'cs': { 'title': 'Speed of Sound vs Altitude', 'xaxis': '$kt$'}
        }

        results = {
            'Std': { 'toffset': 0, 'pressures': [], 'densities': [], 'temps': [], 'cs': [], 'color': 'black', 'label': 'Std' },
            'Hot': { 'toffset': 15, 'pressures': [], 'densities': [], 'temps': [], 'cs': [], 'color': 'red', 'label': '+15C' },
            'Cold': { 'toffset': -15, 'pressures': [], 'densities': [], 'temps': [], 'cs': [], 'color': 'blue', 'label': '-15C' }
        }

        for alt in alts:
            for day in results.keys():
                tempOffset = results[day]['toffset']
                pressure, density, temp, c = ISA.state(alt, tempOffset)
                results[day]['pressures'].append(pressure)
                results[day]['densities'].append(density)
                results[day]['temps'].append(temp - 272.15)
                results[day]['cs'].append(c * msTokt)

        plt.figure()

        for day in results.keys():
            plt.plot(results[day][property], alts, color=results[day]['color'], label=results[day]['label'])

        plt.title(titles_units[property]['title'])
        plt.xlabel(titles_units[property]['xaxis'])
        plt.ylabel('Geometric Altitude (m)')

        plt.legend()

        return plt.gca()
    return (plotISA,)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


if __name__ == "__main__":
    app.run()
