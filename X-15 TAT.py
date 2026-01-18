import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo, plot_std_atmosphere):
    mo.md(
        rf"""
    # X-15 TAT (Total Air Temperature)

    I previously wrote about [Max Q - Maximum Dynamic Pressure](https://seanmcleod70.github.io/FlightDynamicsCalcs/MaxQ.html) comparing the Max Q experienced by a SpaceX rocket during launch, the Space Shuttle and a typical airliner. Followed up by looking at the Max Q experienced by the X-15 during it's
    speed mission flights and altitude mission flights in - [X-15 MaxQ]().

    [Rodney Rodriguez Robles](https://www.linkedin.com/in/rodneyrodriguezrobles/) created a [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7414421278973136896/) mentioning the X-15 speed record flight.

    > On October 3, 1967, Pete Knight pushed the X-15A-2 to Mach 6.7, a number that still feels unreal today‼️

    > It was not just a hashtag#speed record, it was a deliberate step into a hashtag#thermal regime where aerodynamics, structures, and materials stop being comfortable theory and start becoming survival problems.

    >The aircraft paid the price, and the ablative coating did exactly what it was designed to do and burned away under extreme heating, but not without consequences. .....

    [How 'Speedy Pete' Piloted the Fastest Flight Ever Made by a Manned Aircraft](https://www.historynet.com/how-speedy-pete-piloted-the-fastest-flight-ever-made-by-a-manned-aircraft/) is a fairly detailed description of the build up to the record flight, the flight itself and some of the history after the flight.

    > Per procedure, after coming to a halt, Knight recorded his final instrumentation readings, wondering why his ground team was looking toward the airplane and not helping him out. The answer became clear when he saw the blackened back end.

    > The damage stunned NASA engineers. The Flight Research Center’s Jack Kolf told me in 1977, “If there had been any question that the airplane was going to come back in that shape, we never would have flown it.” FRC thermodynamicist Joe Watts saw the flight’s major lesson as teaching engineers to take “extreme care in the design of hypersonic vehicles where shock impingement and interference effects are present because of the extremely high temperatures encountered.” NASA’s John Becker—father of the X-15—agreed, urging future designers to pay “maximum attention to aerothermodynamic detail in design and pre-flight testing.” 

    Using the same flight profile data for the design altitude mission and the design speed mission I'll calculate the Total
    Air Temperature (TAT) that the X-15 would've experienced.

    TAT refers to the temperature of the air around the aircraft including the kinetic heating effect based on the aircraft's
    velocity through the air. The Static Air Temperature (SAT) is the ambient air temperature.

    Given the SAT, $\gamma$ and the Mach number TAT can be calculated using:

    $$\mathrm{{TAT}} = \mathrm{{SAT}} \times \left( 1 + \frac{{\gamma - 1}}{{2}} \cdot M^2 \right)$$

    With $\gamma$ approximately 1.4 for dry air we have:

    $$\mathrm{{TAT}} = \mathrm{{SAT}} \times \left( 1 + 0.2 \cdot M^2 \right)$$

    Using Kelvin for SAT and TAT.

    The following graph shows how the air temperature and the speed of sound vary in the standard atmosphere over the altitude range that the X-15 operated in.

    {plot_std_atmosphere()}


    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## X-15 Report

    I came across a reference to an X-15 report while watching Ben Dickinson’s YouTube video - [X-15 Space Plane - A Review for 6DOF Model Development | Flight Simulation Tutorial - Section 2.1](https://www.youtube.com/watch?v=iQrN6hgh8e0).

    The [Design and Operation of the X-15 Hypersonic Research Airplane](https://apps.dtic.mil/sti/tr/pdf/AD0279830.pdf) report includes two graphs showing a plot of altitude vs time and Mach vs time for the two types of profiles flown. One profile targetting high altitude and one profile targetting high speed.

    {mo.image("public/X-15-MaxQ/x-15-report-graphs.png", width=600)}
    """
    )
    return


@app.cell(hide_code=True)
def _(SAT, TAT, mo, plot_altitude_mission, plot_speed_mission):
    mo.md(
        rf"""
    ## TAT Variation

    So after digitizing the altitude and Mach data from the two graphs in the X-15 report we can plot how the TAT varied during the two flight profiles, and also check when the maximum TAT was achieved and what the maximum TAT was for each of the two profiles.

    {plot_altitude_mission()}

    {plot_speed_mission()}

    The following table lists the maximum TAT experienced during the X-15's design altitude and speed missions, plus the TAT
    experienced by the X-15 speed record at it's maximum Mach of 6.7. TAT values are also calculated for a number of other
    aircraft types at their cruising altitudes for comparison.

    |Aircraft Mission|Altitude|Mach|SAT|TAT|
    |-------|----|----|-----|----|
    |X-15 Altitude Profile|126,300ft|6.03|{SAT(126300)}|{TAT(126300, 6.03)}|
    |X-15 Speed Profile|114,465ft|6.45|{SAT(114465)}|{TAT(114465, 6.45)}|
    |X-15 Speed Record|102,100ft|6.7|{SAT(102100)}|{TAT(102100, 6.7)}|
    |SR-71|80,000ft|3.5|{SAT(80000)}|{TAT(80000, 3.5)}|
    |Concorde|60,000ft|2.04|{SAT(60000)}|{TAT(60000, 2.04)}|
    |Airliner|37,000ft|0.85|{SAT(37000)}|{TAT(37000, 0.85)}|
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Code""")
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from ISA import ISAtmosphere

    ISA = ISAtmosphere()
    return ISA, mo, np, plt


@app.cell
def _(ISA, mo, plt):
    def plot_std_atmosphere():
        alts = []
        sats = []
        speed_of_sounds = []

        for h in range(0, 260001, 1000):
            _, _, oat, speed_of_sound = ISA.state(h*0.3048) # ft to m

            alts.append(h)
            sats.append(oat-273.15)
            speed_of_sounds.append(speed_of_sound*1.944012) # m/s to knots

        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()

        host.set_ylim(-80, 20)
        par1.set_ylim(400, 700)

        host.set_xlabel('Altitude (ft)')
        host.set_ylabel('SAT (C)')
        par1.set_ylabel('Speed of Sound (kt)')

        p1, = host.plot(alts, sats, label='SAT (C)')
        p2, = par1.plot(alts, speed_of_sounds, color='r', label='Speed of sound (kt)')

        lns = [p1, p2]
        host.legend(handles=lns, loc='upper center')

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())

        plt.title('Standard Atmosphere')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_std_atmosphere,)


@app.cell
def _():
    def altitude_mission_altitude(t):
        return 27.6113 - 0.145776*t + 0.0657895*t**2 - 0.00196133*t**3 + 3.91021e-5*t**4 - 4.40397e-7*t**5 + 2.80813e-9*t**6 - 1.01645e-11*t**7 + 1.94942e-14*t**8 - 1.53729e-17*t**9

    def speed_mission_altitude(t):
        return 31.0556 - 0.343199*t + 0.0910034*t**2 - 0.00334765*t**3 + 7.12152e-05*t**4 - 8.67785e-07*t**5 + 6.08275e-09*t**6 -2.4314e-11*t**7 + 5.15945e-14*t**8 - 4.51568e-17*t**9

    def load_mission_mach(csv_filename):
        csv = open(csv_filename, 'r')

        times = []
        machs = []

        for line in csv.readlines():
            vals = line.split(',')
            t = float(vals[0])     
            mach = float(vals[1])
            times.append(t)
            machs.append(mach)

        return (times, machs)
    return load_mission_mach, speed_mission_altitude


@app.cell
def _(plot_mission):
    def plot_altitude_mission():
        return plot_mission('Altitude Mission', 'upper left', 'x-15-altitude-mission-mach.csv')

    def plot_speed_mission():
        return plot_mission('Speed Mission', 'upper right', 'X-15-speed-mission-mach.csv')
    return plot_altitude_mission, plot_speed_mission


@app.cell
def _(ISA, load_mission_mach, mo, np, plt, speed_mission_altitude):
    def plot_mission(title, legend_location, mission_mach_filename):
        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()
        par2 = host.twinx()
        par3 = host.twinx()

        host.set_ylim(0, 280)
        par1.set_ylim(0, 7)
        par2.set_ylim(-50, 2000)
        par3.set_ylim(-80, 100)

        host.set_xlabel('Time (s)')
        host.set_ylabel('Altitude (1000 ft)')
        par1.set_ylabel('Mach')
        par2.set_ylabel('TAT (C)')
        par3.set_ylabel('SAT (C)')

        times = []
        sats = []
        tats = []  

        # Altitude
        alts = []

        for t in range(0, 261, 1):
            alt = speed_mission_altitude(t)
            times.append(t)
            alts.append(alt)    

        # Mach
        mach_times, machs_raw = load_mission_mach(f'data/X-15-MaxQ/{mission_mach_filename}')    
        machs = []
        for t in range(0, 261, 1):
            mach = np.interp(t, mach_times, machs_raw)
            machs.append(mach)

        # Temps (SAT and TAT)
        qs = []
        for i in range(0, len(times)):
            mach = machs[i]
            h = alts[i] * 1000

            _, _, sat, speed_of_sound = ISA.state(h*0.3048) # ft to m
        
            tat = sat*(1 + 0.2*mach**2)
        
            sats.append(sat - 273.15) # Kelvin to Celsius
            tats.append(tat - 273.15) # Kelvin to Celsius

        max_index = np.argmax(tats)
        #print(max_index, times[max_index], tats[max_index], alts[max_index], machs[max_index])        

        p1, = host.plot(times, alts, label='Altitude (1000 ft)')
        p2, = par1.plot(times, machs, color='r', label='Mach')
        p3, = par2.plot(times, tats, color='g', label='TAT (C)' )
        p4, = par3.plot(times, sats, color='orange', label='SAT (C)' )

        lns = [p1, p2, p3, p4]
        host.legend(handles=lns, loc=legend_location)

        par2.spines['right'].set_position(('outward', 95)) 
        par3.spines['right'].set_position(('outward', 40)) 

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())
        par2.yaxis.label.set_color(p3.get_color())
        par3.yaxis.label.set_color(p4.get_color())

        plt.title(title)

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_mission,)


@app.cell
def _(ISA):
    def dynamic_pressure(altitude, mach):
        _, rho, _, speed_of_sound = ISA.state(altitude*0.3048) # ft to m
        v = mach * speed_of_sound
        q = 0.5 * rho * v**2

        return f'{q/1000:.1f} kPa' 
    return


@app.cell
def _(ISA):
    def TAT(altitude, mach):
        _, _, sat, _ = ISA.state(altitude*0.3048) # ft to m
        tat = sat*(1 + 0.2*mach**2)

        return f'{(tat-273.15):.0f}C'
    return (TAT,)


@app.cell
def _(ISA):
    def SAT(altitude):
        _, _, sat, _ = ISA.state(altitude*0.3048) # ft to m
    
        return f'{(sat-273.15):.0f}C'    
    return (SAT,)


if __name__ == "__main__":
    app.run()
