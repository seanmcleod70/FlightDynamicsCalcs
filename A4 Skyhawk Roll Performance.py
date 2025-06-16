import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # A-4 - Skyhawk Roll Performance

    From a Linkedin post by Elliot Seguin - https://www.linkedin.com/posts/elliot-seguin-ba2a6434_testpilot-fly-aviation-ugcPost-6887428405525139457-o5co/

    > The legendary roll rate of the A-4, is it really that fast? I was told in engineering school an A-4 rolled at 700 degrees per second, roughly twice the roll rate of an F-16. When the opportunity came up to evaluate the A-4 I became pretty focused on this data point.

    >Talking to the owner, the manual says 720 deg/sec and limits the pilot to one full deflection roll due to roll yaw coupling. Reading online there was speculation that the 720 number had been a misprint in an old A-4 manual and in fact the number was 270 deg per sec. Every A-4 pilot I talked to was quick to compliment the roll rate but no one seemed to have real data. Then we went flying.

    >The flight was about demonstrating flatline speed so the maneuvering was extra, but we did some rolls. I don’t know that we ever did full deflection rolls but in the videos show you can see a lot of deflection. The video shows a “fast” roll in each direction (speed ~400 KIAS).

    >We topped out on this flight at 500 Knots, ~100 knots faster than this roll. The airplane is capable of but more speed and likely more deflection, based on that I think 700 deg/s is a real number. What do you think?

    From Gordon McClymont's comment on the post.

    >So I dug out the final report…The rapid roll test we performed was at 15K/350KIAS/1G/Full stick in 1/4 sec for 360 deg of roll (with empty drop tanks). For Left roll it was 1.68 secs and Right was 1.56 secs. These numbers are similar to your clip. Without taking into account the roll rate acceleration that equates to 230 deg/s. Being generous we could maybe assume a 270 deg/s steady state roll rate.

    >I agree that at a higher speed and with the drop tanks removed the steady state roll rate may well be increased-but no where near 700 deg/s. I agree 100% with Murcat that these roll rates are most impractical-if not impossible. As with all legendary jet fighters around the world-the tales get taller with the years! The Scooter rolled pretty fast-but not that fast!

    15,000ft 350KIAS Mach 0.69 u0 = 221.604 m/s
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        rf"""
    ## A-4D Aerodynamic Data

    Aerodynamic data for the A-4D Skyhawk from [AIRCRAFT STABILITY AND CONTROL DATA By Gary L. Teper April 1969 NASA report](https://www.robertheffley.com/docs/Data/Teper--NASA_CR-96008.pdf]).

    {mo.image("public/A4Data1.png")}

    {mo.image("public/A4Data2.png")}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Steady State Roll Rate Calculation

    ### Pure Rolling Motion

    $$
    \begin{align}
    \large L_p &= C_{lp} \frac{b}{2u_0} \frac{QSb}{I_x} \\ \nonumber
    \\
    \large L_{\delta a} &= C_{l \delta a} \frac{QSb}{I_x} \\ \nonumber
    \\
    \large \tau &= -\frac{1}{L_p} \\ \nonumber
    \\
    \large p(t) &= -\frac{L_{\delta a}}{L_p} (1 - e^{-t/\tau}) \Delta \delta_a \\ \nonumber
    \\
    \large p_{ss} &= -\frac{L_{\delta a}}{L_p} \Delta \delta_a \\ \nonumber
    \\
    \large p_{ss} &= -\frac{2u_0}{b} \frac{C_{l \delta a}}{C_{lp}} \Delta \delta_a \\ \nonumber
    \\
    \end{align}
    $$

    $b$ - Wingspan.

    $S$ - Reference area, wing area.

    $u_0$ - True airspeed.

    $Q$ - Dynamic pressure = $\frac{1}{2}\rho{u_0}^2$.

    $I_x$ - Moment of inertia around the x-axis.

    $\Delta \delta_a$ - Aileron deflection angle.

    $L_p$ - Roll moment due to roll rate $p$. Roll damping.

    $L_{\delta a}$ - Roll moment due to aileron deflection. Aileron control power.

    $\tau$ - Time constant, roll constant.

    $p(t)$ - Roll rate as a function of time.

    $p_{ss}$ - Steady state roll rate.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Geometry and Moment of Inertia""")
    return


@app.cell
def _():
    S = 24.2       # m^2
    b = 8.4        # m
    Ix = 10659     # kgm^2

    # Max aileron deflection 
    # TODO Need to determine what the max is for the A-4
    # For now, 22.5 degrees matches Gordon's data of 360 deg roll in 1.56s 
    da = 22.5 * 0.017453  # rad
    return Ix, S, b, da


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Calculation Functions""")
    return


@app.cell
def _(Ix, S, b):
    def rollTimeConstant(rho, u0, clp):
        Q = 0.5 * rho * u0**2
        L_p = clp * (b/(2*u0)) * ((Q*S*b)/Ix)
        return -1/L_p
    return (rollTimeConstant,)


@app.cell
def _(b):
    def pss(u0, clda, clp, da):
        return -((2*u0)/b) * (clda/clp) * da
    return (pss,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Function to plot roll rate and roll angle versus time""")
    return


@app.cell
def _(da, np, plt, pss, rollTimeConstant):
    def plotRollRateRollAngleVsTime(rho, u0, Cl_p, Cl_da):
        timeConstant = rollTimeConstant(rho, u0, Cl_p)
        steadyStateRollRate = pss(u0, Cl_da, Cl_p, da)

        rollRate = []
        rollAngle = []
        time = []

        currentRollAngle = 0

        dt = 0.01

        for t in np.arange(0, 5, dt):
            p = steadyStateRollRate * (1 - np.e**(-t/timeConstant))
            rollRate.append(p * 57.29578)
            currentRollAngle += p * 57.29578 * dt
            rollAngle.append(currentRollAngle)
            time.append(t)

        plt.figure()
        plt.plot(time, rollRate)
        plt.axvline(timeConstant, color='r')
        plt.xlabel("Time (s)", fontsize=15)
        plt.ylabel("Roll Rate (deg/s)", fontsize=15)
        plt.title("Roll Rate vs Time", fontsize=15)
        plt.show()

        plt.figure()
        plt.plot(time, rollAngle)
        plt.axhline(360, color='r')
        plt.xlabel("Time (s)", fontsize=15)
        plt.ylabel("Roll Angle (deg)", fontsize=15)
        plt.title("Roll Angle vs Time", fontsize=15)
        plt.show()
    return (plotRollRateRollAngleVsTime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Test 1 - 350KIAS 15kft""")
    return


@app.cell
def _(NamedTuple):
    class Data350KIAS15kft(NamedTuple):
        # Coefficients for Mach 0.69 (350KIAS @ 15kft)
        Cl_p = -0.27   # per rad
        Cl_da = 0.077  # per rad

        # Air data for Mach 0.69 (350KIAS @ 15kft)
        rho = 0.77109  # kg/m^3
        u0 = 221.604   # m/s

    t1 = Data350KIAS15kft()
    return (t1,)


@app.cell
def _(rollTimeConstant, t1):
    print(f'Roll time constant: {rollTimeConstant(t1.rho, t1.u0, t1.Cl_p):.2f}s')
    return


@app.cell
def _(da, pss, t1):
    print(f'Steady state roll rate: {pss(t1.u0, t1.Cl_da, t1.Cl_p, da) * 57.29578:.2f} deg/s')
    return


@app.cell
def _(plotRollRateRollAngleVsTime, t1):
    plotRollRateRollAngleVsTime(t1.rho, t1.u0, t1.Cl_p, t1.Cl_da)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Test 2 - 450KIAS 15kft

    Note the changes in $C_{l_p}$ and $C_{l \delta_a}$ at Mach 0.87.
    """
    )
    return


@app.cell
def _(NamedTuple):
    class Data450KIAS15kft(NamedTuple):
        # Coefficients for Mach 0.87 (450KIAS @ 15kft)
        Cl_p = -0.28   # per rad
        Cl_da = 0.065  # per rad

        # Air data for Mach 0.87 (450KIAS @ 15kft)
        rho = 0.77109  # kg/m^3
        u0 = 281.402   # m/s

    t2 = Data450KIAS15kft()
    return (t2,)


@app.cell
def _(rollTimeConstant, t2):
    print(f'Roll time constant: {rollTimeConstant(t2.rho, t2.u0, t2.Cl_p):.2f}s')
    return


@app.cell
def _(da, pss, t2):
    print(f'Steady state roll rate: {pss(t2.u0, t2.Cl_da, t2.Cl_p, da) * 57.29578:.2f} deg/s')
    return


@app.cell
def _(plotRollRateRollAngleVsTime, t2):
    plotRollRateRollAngleVsTime(t2.rho, t2.u0, t2.Cl_p, t2.Cl_da)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Integrating Roll Rate

    $\Large p(t) = -\frac{L_{\delta a}}{L_p} (1 - e^{-t/\tau}) \Delta \delta_a$

    $\Large \int_{0}^{t}-\frac{L_{\delta a}}{L_p} (1 - e^{-t/\tau}) \Delta \delta_a dt$

    Antiderivate $F(t)$

    $\Large F(t) = -\frac{L_{\delta a}}{L_p}\left(\tau e^{-t/\tau}+t\right) \Delta \delta_a$

    $\Large F(t) = p_{ss}\left(\tau e^{-t/\tau}+t\right)$

    Definite integral from $a$ to $b$ is antiderivatives $F(b) - F(a)$
    """
    )
    return


@app.cell
def _(np):
    # Figures for Gordon's 350KIAS 15kft, 1.56s to roll through 360 deg
    _t = 1.56
    _tau = 0.5411978780018623
    _pss = 338.55599519673757 / 57.29578  # rad

    # Anti-derivative F(t)
    def F(t):
        return _pss * (_tau * np.e**(-t/_tau) + t)

    # Calculate definite integral from 0 to 1.56
    rollAngle = (F(1.56) - F(0)) * 57.29578  # deg

    print(f'Roll angle after 1.56s = {rollAngle:.2f} deg')
    return


@app.cell
def _():
    import marimo as mo
    from typing import NamedTuple
    import numpy as np
    import matplotlib.pyplot as plt
    return NamedTuple, mo, np, plt


if __name__ == "__main__":
    app.run()
