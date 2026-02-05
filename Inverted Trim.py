import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    # Inverted Trim

    [Agostino De Marco](https://www.facebook.com/agostino.demarco) posted a [video](https://www.facebook.com/share/p/1Bfpg5QsSM/) of a Red Bull sponsored aerobatic aircraft flying inverted above a Red Bull Formula 1 car and asked for a guess of the angle of attack (AoA) of the aircraft.

    {mo.image("public/InvertedTrim/RedBullInverted.png", width=800)}

    In particular the sign convention for AoA when the aircraft is inverted.

    I decided to test out [JSBSim](https://github.com/JSBSim-Team/jsbsim) to confirm that all the sign conventions worked out in terms of being able to fly the aircraft inverted in trim etc. and to also confirm whether the trim routines could calculate a trim solution for an inverted aircraft.

    Although the Red Bull sponsored aerobatic aircraft more than likely has a symmetrical, i.e. uncambered airfoil I decided to make things more interesting in terms of using a cambered airfoil. So I chose the A4 Skyhawk model that is included with JSBSim.

    {mo.image("public/InvertedTrim/A4.jpg", width=800)}

    Which has the following $C_L$ vs AoA data.

    {mo.image("public/InvertedTrim/A4ClvsAoA.png", width=800)}

    I then wrote the following Python code to calculate a trim solution for a range airspeeds for both the upright case and the inverted case.
    """
    )
    return


@app.cell
def _(jsbsim, math, mo, plt):
    def trim_inverted_upright():

        # Avoid flooding the console with log messages
        jsbsim.FGJSBBase().debug_lvl = 0

        fdm = jsbsim.FGFDMExec(None)

        # Load the aircraft 
        fdm.load_model('A4') 

        # Set the engine running
        fdm['propulsion/engine[0]/set-running'] = 1

        # Set alpha range for trim solutions
        fdm['aero/alpha-max-rad'] = math.radians(12)
        fdm['aero/alpha-min-rad'] = math.radians(-12.0)

        fig = plt.figure(layout='constrained', figsize=(10, 5))

        # Roll angle, label and results array of tuples (speed, aoa)
        configs = [ (0, 'Upright', []), (180, 'Inverted', []) ]

        for config in configs:
            for speed in range(160, 460, 10):
                fdm['ic/h-sl-ft'] = 250
                fdm['ic/vc-kts'] = speed
                fdm['ic/gamma-deg'] = 0
                fdm['ic/phi-deg'] = config[0]

                # Initialize the aircraft with initial conditions
                fdm.run_ic() 

                fdm.run()

                # Trim
                try:
                    fdm['simulation/do_simple_trim'] = 1
                    # Store trim result (speed, aoa)
                    config[2].append((fdm['velocities/vc-kts'], fdm['aero/alpha-deg']))       
                except RuntimeError as e:
                    # The trim cannot succeed. Just make sure that the raised 
                    # exception is due to the trim failure otherwise rethrow.
                    if e.args[0] != 'Trim Failed':
                        raise

            speed, alpha = zip(*config[2])
            plt.plot(speed, alpha, label=config[1])

        # Calculate abs diff between inverted and upright aoa for trim speed
        abs_diffs = []
        for i, speed_alpha in enumerate(configs[0][2]):
            _, alpha = configs[1][2][i]
            diff = abs(alpha) - speed_alpha[1]
            abs_diffs.append(diff)

        plt.plot(speed, abs_diffs, label='Abs Diff')

        plt.xlabel('IAS (kt)')
        plt.ylabel('AoA (deg)')
        plt.title('AoA vs IAS')
        plt.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (trim_inverted_upright,)


@app.cell(hide_code=True)
def _(mo, trim_inverted_upright):
    mo.md(
        rf"""
    Sure enough JSBSim didn’t have any issues calculating trim solutions for the inverted case.

    {trim_inverted_upright()}

    The difference of ~2.7°, i.e. the slightly larger AoA required for the inverted case pretty much matches the negative AoA required to achieve the same absolute $C_L$ achieved at 0° AoA, i.e. where the $C_L$ vs AoA line crosses the y-axis.

    This difference will vary depending on the airfoil in terms of the slope of the $C_L$ vs AoA line and where it crosses the y-axis. In the case of a symmetrical, i.e. non-cambered airfoil the $C_L$ vs AoA will pass through the origin so there won’t be a difference in the absolute AoA required for upright versus inverted flight.
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    import jsbsim
    import matplotlib.pyplot as plt
    import math
    return jsbsim, math, mo, plt


if __name__ == "__main__":
    app.run()
