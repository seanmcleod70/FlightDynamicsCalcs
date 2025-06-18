import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Fighter Roll Rates

    For pure rolling motion the steady state roll rate is: 

    $$ p_{ss} = -\frac{2u_0}{b}\frac{C_{l \delta a}}{C_{lp}} \Delta \delta_a $$
    """
    )
    return


@app.cell(hide_code=True)
def _(math, mo, pss):
    mo.md(
        rf"""
    ## F-15

    Aerodynamic data from - [Automatic Control of Aircraft and Missiles 2nd Edition](https://www.amazon.com/Automatic-Control-Aircraft-Missiles-Blakelock/dp/0471506516) in appendix F. Original source being: 

    *F / TF-15 Stability Derivatives, Mass and Inertia Characteristics, Flight Test Basis, Parts I and
    II, MDCA4172, McDonnell Aircraft Company, Saint Louis, Missouri, August 1976, revised October 1977.*

    $b = 42.8ft$

    Aileron maximum deflection of 20 deg.

    Ignoring differential horizontal stabilizers.

    |Lateral Data|1|2|3|4|
    |-----------------|-|-|-|-|
    |h (ft)             |20,000|5,000 |20,000|40,000|
    |$V_T$ (fps)        |622.14|877.68|829.52|774.8|
    |Mach               |0.6   |0.8   |0.8   |0.8|
    |$C_{{l \delta a}}$ |0.048 |0.027 |0.035 |0.045|
    |$C_{{lp}}$         |-0.27 |-0.19 |-0.24 |-0.27|
    |**$p_{{ss}}$ (deg/s)**|{pss(622.14, 42.8, 0.048, -0.27, math.radians(20)):.0f}|{pss(877.68, 42.8, 0.027, -0.19, math.radians(20)):.0f}|{pss(829.52, 42.8, 0.035, -0.24, math.radians(20)):.0f}|{pss(774.8, 42.8, 0.045, -0.27, math.radians(20)):.0f}|

    The F-15 mixes in differential horizontal stabilizer inputs to aid in roll control. The following sources provide the aerodynamic coefficient data for the roll moment due to differential horizontal stabilizers.

    [Investigation of the High Angle of Attack Dynamics of the F-15B using Bifurcation Analysis](https://apps.dtic.mil/sti/tr/pdf/ADA230462.pdf) [1]

    [JSBSim F-15 FDM](https://github.com/Zaretto/F-15/blob/ae99d562321f2bf2e32a134c5ca1af962658befd/f15a.xml) based on data from [1].

    The maximum differential horizontal stabilizer appears to be 6.667 deg. With $C_{{l \delta ds}} = 0.039$ per radian.

    |Lateral Data|1|2|3|4|
    |-----------------|-|-|-|-|
    |**$p_{{ss}}$ (deg/s)** aileron only|{pss(622.14, 42.8, 0.048, -0.27, math.radians(20)):.0f}|{pss(877.68, 42.8, 0.027, -0.19, math.radians(20)):.0f}|{pss(829.52, 42.8, 0.035, -0.24, math.radians(20)):.0f}|{pss(774.8, 42.8, 0.045, -0.27, math.radians(20)):.0f}|
    |**$p_{{ss}}$ (deg/s)** aileron and stabilizer|{pss(622.14, 42.8, 0.048, -0.27, math.radians(20), 0.039, math.radians(6.667)):.0f}|{pss(877.68, 42.8, 0.027, -0.19, math.radians(20), 0.039, math.radians(6.667)):.0f}|{pss(829.52, 42.8, 0.035, -0.24, math.radians(20), 0.039, math.radians(6.667)):.0f}|{pss(774.8, 42.8, 0.045, -0.27, math.radians(20), 0.039, math.radians(6.667)):.0f}|

    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## F-16""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Steady State Roll Rate Calculation""")
    return


@app.cell
def _(math):
    # u0     - TAS
    # b      - wingspan
    # cl_da  - roll moment coefficient for aileron deflection
    # da     - aileron deflection
    # cl_dds - roll moment coefficient for differential horizontal stabilizer deflection
    # dds    - differential horizontal stabilizer deflection

    def pss(u0, b, cl_da, cl_p, da, cl_dds=0, dds=0):
        return math.degrees((-2*u0*(cl_da*da + cl_dds*dds))/(b*cl_p))
    return (pss,)


@app.cell
def _():
    import marimo as mo
    import math
    return math, mo


if __name__ == "__main__":
    app.run()
