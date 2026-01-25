import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo, plot_airliner, plot_nasa_sts124, plot_spacex_jcsat14):
    mo.md(
        rf"""
    # Max Q - Maximum Dynamic Pressure

    During a rocket launch the commentator will often call out “Max Q” at a specific point in time during the launch. This is the point at which the dynamic pressure acting on the rocket will be at it’s maximum.

    The dynamic pressure or Q is the product of the air-density and the velocity squared of the object travelling through the air.

    $$\mathrm{{Dynamic\ Pressure\ }} (Q) = \frac{{1}}{{2}} \rho V^2$$

    The SI unit for pressure is the pascal. One pascal is the pressure exerted by a force of magnitude of one newton perpendicularly upon an area of one square meter.

    SpaceX provide a webcast of their launches which includes a simple telemetry display showing the rocket’s current speed and altitude.

    {mo.image("public/MaxQ/spacexjcsat14webcast.png", width=800)}

    Using the International Standard Atmosphere model to lookup the density at each altitude reported in the telemetry and using the reported velocity at that point we can calculate the dynamic pressure for each telemetry point. Plotting the dynamic pressure for the telemetry points we’ll be able to see at which point in terms of altitude and velocity the rocket experiences it’s maximum dynamic pressure.

    Here is a graph based on telemetry data from SpaceX’s JCSAT-14 launch.

    {plot_spacex_jcsat14()}

    The maximum dynamic pressure (Max-Q) experienced is roughly 30 kPa at an altitude of roughly 11.5 km while travelling at a speed of 1500 km/h.

    As a comparison here is a graph for the Space Shuttle launch STS-124. The telemetry supplied also includes the throttle position, and you’ll notice that the main engines of the Space Shuttle are actually throttled back significantly to 72% for a couple of seconds.

    This is done to limit the maximum dynamic pressure that the Space Shuttle will need to handle during a launch.

    {plot_nasa_sts124()}

    The maximum dynamic pressure experienced by the Space Shuttle is roughly 35 kPa at an altitude of roughly 10.8 km and travelling at a speed of roughly 1550 km/h. So in the same ballpark in terms of altitude and speed and dynamic pressure as the SpaceX rocket.

    You’ll notice a kink in the velocity squared line at around about the 40 km mark even though the main engine throttle percentage doesn’t change. This is due to the separation of the two solid rocket boosters.

    I thought it would be interesting to compare the maximum dynamic pressure experienced by an airliner. So I used some data from the Flightradar24 website that tracks ADS-B broadcast by airliners broadcasting their altitude, ground speed etc.

    So assuming there isn’t any significant wind I’m assuming that the ground speed matches the true airspeed. Then again using the International Standard Atmosphere (ISA) we can lookup the density for the specific altitude and use that to calculate the dynamic pressure.

    {plot_airliner()}

    So it looks like the maximum dynamic pressure is experienced at cruising altitude and cruising speed and roughly peaks around 25 kPa. In other words an airliner’s maximum dynamic pressure that it experiences is roughly in the same ball park as experienced by a SpaceX rocket and the Space Shuttle and the airliner experiences it at roughly the same altitude.

    Actually on further review, a TAS of 642kt at 32,000ft would equate to Mach 1.1, so there definitely was a large wind
    component. Assuming a typical maximum Mach of 0.85 for an airliner at cruising altitude, that equates to a dynamic
    pressure of 11 kPa, so actually a little less than half compared to the SpaceX rocket and the Space Shuttle.

    To get a feel for how much pressure 25 - 35 kPa is remember it’s the equivalent to 25,000 - 35,000 $\frac{{N}}{{m^2}}$.
    Which is roughly 2,500 - 3,500 kg sitting on a 1 square meter surface.

    Now the palm of your hand is roughly 10 x 10 cm, i.e. 0.01 $m^2$, so it’s the equivalent of holding 25 - 35 kg in the palm of your hand.
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
    import matplotlib.pyplot as plt
    from ISA import ISAtmosphere

    ISA = ISAtmosphere()
    return ISA, mo, plt


@app.cell
def _(ISA):
    def std_atmosphere_densities(start, end, increment):
        alts = []
        rhos = []

        for h in range(start, end, increment):
            _, rho, _, _ = ISA.state(h)    
            alts.append(h/1000)
            rhos.append(rho)

        return (alts, rhos)
    return (std_atmosphere_densities,)


@app.cell
def _(ISA, mo, plt, std_atmosphere_densities):
    def plot_spacex_jcsat14():
        (alts, rhos) = std_atmosphere_densities(0, 66000, 500)

        spacex_alts = []
        velocities = []
        velocities_squared = []
        qs = []

        csv = open('data/MaxQ/SpaceX - JCSAT14 Launch.csv', 'r')

        for line in csv.readlines():
            vals = line.split(',')
            alt = float(vals[2]) 
            spacex_alts.append(alt)
            velocity = float(vals[1])
            velocities.append(velocity)
            velocities_squared.append(velocity*velocity)

            _, rho, _, _ = ISA.state(alt*1000) # km to m

            velocity_ms = (velocity * 1000) / (60 * 60)
            dynamic_pressure = 0.5 * rho * velocity_ms**2
            qs.append(dynamic_pressure / 1000)  # kilo pascals

        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()
        par2 = host.twinx()

        host.set_ylim(-0.05, 1.5)
        par1.set_ylim(0, 70000000)
        par2.set_ylim(0, 32)

        host.set_xlabel('Altitude (km)')
        host.set_ylabel('Density')
        par1.set_ylabel('Velocity Squared')
        par2.set_ylabel('Dynamic Pressure')

        p1, = host.plot(alts, rhos, label='Density $\mathrm{(kg/m^3)}$')
        p2, = par1.plot(spacex_alts, velocities_squared, color='r', label='Velocity Squared (km/h)')
        p3, = par2.plot(spacex_alts, qs, color='g', label='Dynamic Pressure (kPa)')

        lns = [p1, p2, p3]
        host.legend(handles=lns, loc='upper center')

        par2.spines['right'].set_position(('outward', 60))      

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())
        par2.yaxis.label.set_color(p3.get_color())

        plt.title('SpaceX - JCSAT14 - Standard Atmosphere')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_spacex_jcsat14,)


@app.cell
def _(ISA, mo, plt, std_atmosphere_densities):
    def plot_nasa_sts124():
        (alts, rhos) = std_atmosphere_densities(0, 66000, 500)

        nasa_alts = []
        nasa_throttles = []
        velocities = []
        velocities_squared = []
        qs = []

        csv = open('data/MaxQ/NASA Shuttle - STS124 Launch.csv', 'r')

        for line in csv.readlines():
            vals = line.split(',')
            throttle = float(vals[1])
            alt = float(vals[2]) 
            velocity = float(vals[3])

            nasa_alts.append(alt)
            nasa_throttles.append(throttle)

            velocities.append(velocity)
            velocities_squared.append(velocity*velocity)

            _, rho, _, _ = ISA.state(alt*1000) # km to m
            velocity_ms = (velocity * 1000) / (60 * 60)
            dynamic_pressure = 0.5 * rho * velocity_ms**2
            qs.append(dynamic_pressure / 1000)  # kilo pascals

        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()
        par2 = host.twinx()
        par3 = host.twinx()

        host.set_ylim(-0.05, 1.5)
        par1.set_ylim(0, 30000000)
        par2.set_ylim(0, 40)
        par3.set_ylim(0, 110)

        host.set_xlabel('Altitude (km)')
        host.set_ylabel('Density')
        par1.set_ylabel('Velocity Squared')
        par2.set_ylabel('Dynamic Pressure')
        par3.set_ylabel('Throttle')

        p1, = host.plot(alts, rhos, label='Density $\mathrm{(kg/m^3)}$')
        p2, = par1.plot(nasa_alts, velocities_squared, color='r', label='Velocity Squared (km/h)')
        p3, = par2.plot(nasa_alts, qs, color='g', label='Dynamic Pressure (kPa)')
        p4, = par3.plot(nasa_alts, nasa_throttles, color='black', label='Throttle (%)')

        lns = [p1, p2, p3, p4]
        host.legend(handles=lns, loc='center right')

        par2.spines['right'].set_position(('outward', 60))      

        # Move throttle axis to the left side    
        par3.spines['left'].set_position(('outward', 60))      
        par3.spines["left"].set_visible(True)
        par3.yaxis.set_label_position('left')
        par3.yaxis.set_ticks_position('left')

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())
        par2.yaxis.label.set_color(p3.get_color())
        par3.yaxis.label.set_color(p4.get_color())

        plt.title('NASA - STS124 - Standard Atmosphere')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_nasa_sts124,)


@app.cell
def _(ISA, mo, plt, std_atmosphere_densities):
    def plot_airliner():
        (alts, rhos) = std_atmosphere_densities(0, 10500, 500)    

        # Convert from m to ft
        for i in range(0, len(alts)):
            alts[i] = alts[i] * 3280.84

        airliner_alts = []
        airliner_speeds = []
        qs = []

        csv = open('data/MaxQ/Airliner.csv', 'r')

        for line in csv.readlines():
            vals = line.split(',')
            alt = float(vals[0]) 
            velocity = float(vals[1])

            airliner_alts.append(alt)
            airliner_speeds.append(velocity)

            _, rho, _, _ = ISA.state(alt*0.3048) # ft to m
            velocity_ms = velocity * 0.5144  # knots to m/s
            dynamic_pressure = 0.5 * rho * velocity_ms**2
            qs.append(dynamic_pressure / 1000)  # kilo pascals

        fig = plt.figure(layout='constrained', figsize=(10, 5))
        host = fig.add_subplot(111)

        par1 = host.twinx()
        par2 = host.twinx()

        host.set_ylim(-0.05, 1.5)
        par1.set_ylim(0, 700)
        par2.set_ylim(0, 30)

        host.set_xlabel('Altitude (ft)')
        host.set_ylabel('Density')
        par1.set_ylabel('Ground Speed')
        par2.set_ylabel('Dynamic Pressure')

        p1, = host.plot(alts, rhos, label='Density $\mathrm{(kg/m^3)}$')
        p2, = par1.plot(airliner_alts, airliner_speeds, color='r', label='Ground Speed (kt)')
        p3, = par2.plot(airliner_alts, qs, color='g', label='Dynamic Pressure (kPa)')

        lns = [p1, p2, p3]
        host.legend(handles=lns, loc='center right')

        par2.spines['right'].set_position(('outward', 60))      

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())
        par2.yaxis.label.set_color(p3.get_color())

        plt.title('Airliner - Standard Atmosphere')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airliner,)


if __name__ == "__main__":
    app.run()
