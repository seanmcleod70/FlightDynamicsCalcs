import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo, plot_std_atmosphere):
    mo.md(
        rf"""
    # X-15 Max Q

    I previously wrote about [Max Q - Maximum Dynamic Pressure](https://seanmcleod70.github.io/FlightDynamicsCalcs/MaxQ.html) comparing the Max Q experienced by a SpaceX rocket during launch, the Space Shuttle and a typical airliner. Now let’s take a look at the Max Q that was experienced by the X-15 while it went about setting various speed and altitude records during it’s research.

    To recap, the dynamic pressure or Q is the product of the air-density and the velocity squared of the object travelling through the air.

    $$\mathrm{{Dynamic\ Pressure\ }} (Q) = \frac{{1}}{{2}} \rho V^2$$

    The SI unit for pressure is the pascal. One pascal is the pressure exerted by a force of magnitude of one newton perpendicularly upon an area of one square meter.

    The following graph shows how the density and the speed of sound vary in the standard atmosphere over the altitude range that the X-15 operated in.

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
def _(dynamic_pressure, mo, plot_altitude_mission, plot_speed_mission):
    mo.md(
        rf"""
    ## Dynamic Pressure Variation

    So after digitizing the altitude and Mach data from the two graphs in the X-15 report we can plot how the dynamic pressure varied during the two flight profiles, and also check when Max Q was achieved and how large Max Q was for each of the two profiles.

    {plot_altitude_mission()}

    {plot_speed_mission()}

    |Aircraft Mission|Time|Altitude|Mach|Max-Q|
    |-------|----|--------|----|-----|
    |X-15 Altitude|30s|52,300ft|1.72|{dynamic_pressure(52300, 1.72)}|
    |X-15 Speed|45s|69,000ft|2.91|{dynamic_pressure(69000, 2.91)}|
    |SR-71|N/A|80,000ft|3.5|{dynamic_pressure(80000, 3.5)}|
    |Concorde|N/A|60,000ft|2.04|{dynamic_pressure(60000, 2.04)}|
    |Airliner|N/A|37,000ft|0.85|{dynamic_pressure(37000, 0.85)}|
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
        rhos = []
        speed_of_sounds = []

        for h in range(0, 260001, 1000):
            _, rho, temp, speed_of_sound = ISA.state(h*0.3048) # ft to m

            alts.append(h)
            rhos.append(rho)
            speed_of_sounds.append(speed_of_sound*1.944012) # m/s to knots

        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()

        host.set_ylim(-0.05, 1.5)
        par1.set_ylim(400, 700)

        host.set_xlabel('Altitude (ft)')
        host.set_ylabel(r'Density $\frac{kg}{m^3}$')
        par1.set_ylabel('Speed of Sound (kt)')

        p1, = host.plot(alts, rhos, label=r'Density $\frac{kg}{m^3}$')
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
    return altitude_mission_altitude, load_mission_mach


@app.cell
def _(plot_mission):
    def plot_altitude_mission():
        return plot_mission('Altitude Mission', 'upper left', 'x-15-altitude-mission-mach.csv')

    def plot_speed_mission():
        return plot_mission('Speed Mission', 'upper right', 'x-15-speed-mission-mach.csv')    
    return plot_altitude_mission, plot_speed_mission


@app.cell
def _(ISA, altitude_mission_altitude, load_mission_mach, mo, np, plt):
    def plot_mission(title, legend_location, mach_file):
        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()
        par2 = host.twinx()

        host.set_ylim(0, 280)
        par1.set_ylim(0, 7)
        par2.set_ylim(0, 30)

        host.set_xlabel('Time (s)')
        host.set_ylabel('Altitude (1000 ft)')
        par1.set_ylabel('Mach')
        par2.set_ylabel('Dynamic Pressure (kPa)')

        times = []
        maxq = 0
        maxq_time = 0
        maxq_mach = 0
        maxq_alt = 0

        # Altitude
        alts = []

        for t in range(0, 261, 1):
            alt = altitude_mission_altitude(t)
            times.append(t)
            alts.append(alt)    

        # Mach
        mach_times, machs_raw = load_mission_mach(f'data/X-15-MaxQ/{mach_file}')    
        machs = []
        for t in range(0, 261, 1):
            mach = np.interp(t, mach_times, machs_raw)
            machs.append(mach)

        # Dynamic pressure
        qs = []
        for i in range(0, len(times)):
            mach = machs[i]
            h = alts[i] * 1000

            _, rho, temp, speed_of_sound = ISA.state(h*0.3048) # ft to m

            v = mach * speed_of_sound

            q = 0.5 * rho * v**2
            qs.append(q/1000) # kPa

            if q > maxq:
                maxq = q
                maxq_time = i
                maxq_mach = mach
                maxq_alt = h

        p1, = host.plot(times, alts, label='Altitude (1000 ft)')
        p2, = par1.plot(times, machs, color='r', label='Mach')
        p3, = par2.plot(times, qs, color='g', label='Dynamic Pressure (kPa)' )

        #plt.axvline(x=maxq_time)
        #print(maxq_time, maxq_alt, maxq_mach, maxq/1000)

        lns = [p1, p2, p3]
        host.legend(handles=lns, loc=legend_location)

        par2.spines['right'].set_position(('outward', 40)) 

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())
        par2.yaxis.label.set_color(p3.get_color())

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
    return (dynamic_pressure,)


if __name__ == "__main__":
    app.run()
