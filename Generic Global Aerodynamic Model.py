import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # A Generic Global Aerodynamic Model for Aircraft

    [Grauer and Morelli](https://ntrs.nasa.gov/api/citations/20140011902/downloads/20140011902.pdf) from NASA took detailed wind tunnel databases for eight different aircraft to identify a generic global aerodynamic model structure that could be used for any of the aircraft. The structure they came up with includes 45 scalar model parameters $\theta_1$ through $\theta_{45}$, used in conjunction with the following:

    | Category | Variables |
    | -------- | --------- |
    | Aerodynamic angles | $\alpha$, $\beta$ |
    | Angular rates | $\tilde{p}$, $\tilde{q}$, $\tilde{r}$ |
    | Control surfaces | $\delta_e$, $\delta_a$, $\delta_r$ |

    The angular rates are the standard nondimensional body-axis angular rates.

    $$
    \begin{bmatrix}
    \tilde{p} \\
    \tilde{q} \\
    \tilde{r}
    \end{bmatrix}
    =
    \frac{1}{2V}
    \begin{bmatrix}
    b & 0 & 0 \\
    0 & \bar{c} & 0 \\
    0 & 0 & b
    \end{bmatrix}
    \begin{bmatrix}
    p \\
    q \\
    r
    \end{bmatrix}
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## GGA Model


    $C_D =       \theta_1 + 
                \theta_2 \alpha + 
                \theta_3 \alpha \tilde{q} + 
                \theta_4 \alpha \delta_e +
                \theta_5 \alpha^2 +
                \theta_6 \alpha^2 \tilde{q} +
                \theta_7 \alpha^2 \delta_e +
                \theta_8 \alpha^3 +
                \theta_9 \alpha^3 \tilde{q} +
                \theta_{10} \alpha^4$
 
    $C_Y =       \theta_{11} \beta +
                \theta_{12} \tilde{p} +
                \theta_{13} \tilde{r} +
                \theta_{14} \delta_a +
                \theta_{15} \delta_r$

    $C_L =       \theta_{16} +
                \theta_{17} \alpha +
                \theta_{18} \tilde{q} +
                \theta_{19} \delta_e +
                \theta_{20} \alpha \tilde{q} +
                \theta_{21} \alpha^2 +
                \theta_{22} \alpha^3 +
                \theta_{23} \alpha^4$

    $\space$

    $C_l =       \theta_{24} \beta +
                \theta_{25} \tilde{p} +
                \theta_{26} \tilde{r} +
                \theta_{27} \delta_a +
                \theta_{28} \delta_r$

    $C_m =       \theta_{29} +
                \theta_{30} \alpha +
                \theta_{31} \tilde{q} +
                \theta_{32} \delta_e +
                \theta_{33} \alpha \tilde{q} +
                \theta_{34} \alpha^2 \tilde{q} +
                \theta_{35} \alpha^2 \delta_e +
                \theta_{36} \alpha^3 \tilde{q} +
                \theta_{37} \alpha^3 \delta_e +
                \theta_{38} \alpha^4$

    $C_n =       \theta_{39} \beta +
                \theta_{40} \tilde{p} +
                \theta_{41} \tilde{r} +
                \theta_{42} \delta_a +
                \theta_{43} \delta_r +
                \theta_{44} \beta^2 +
                \theta_{45} \beta^3$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Forces are in the stability frame and the moments are in the body frame.

    Mach effects are not modelled and only a single configuration is modelled, i.e. changes with respect to flaps, gear etc. are not modelled.

    Nonlinear flight simulations were used to demonstrate that the GGA model accurately reproduces trim solutions, local dynamic behavior, and global dynamic behavior under large-amplitude excitation.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Drag

    #### Drag vs Alpha

    | Model Parameter | Standard Equivalent |
    | --------------- | ------------------- |
    | $\theta_1$      | $C_{D_0}$           |
    | $\theta_2$      | $C_{D_{\alpha}}$    |
    | $\theta_5$      | $C_{D_{\alpha^2}}$  |

    $\theta_1$, $\theta_2$, $\theta_5$, $\theta_8$ and $\theta_{10}$ are used to model $C_D$ versus $\alpha$, making use of $\alpha$ from 0th to 4th order.  

    #### Drag vs Elevator
    $\theta_4$ and $\theta_7$ are used to model $C_D$ versus elevator deflection, in conjunction with 1st and 2nd order $\alpha$. Often drag versus elevator deflection, $C_{D_{\delta_e}}$ is modelled independently of $\alpha$.

    #### Drag vs Pitch Rate
    $\theta_3$, $\theta_6$ and $\theta_9$ are used to model $C_D$ versus normalized pitch rate.

    TODO - Is drag vs pitch rate a common term?

    #### Summary

    | Effect     | Model Parameters | Model Terms |
    | ---------- | ---------------- | ----------- |
    | Alpha      | $\theta_1$, $\theta_2$, $\theta_5$, $\theta_8$, $\theta_{10}$ | $\theta_1 + \theta_2 \alpha + \theta_5 \alpha^2 + \theta_8 \alpha^3 + \theta_{10} \alpha^4$ |
    | Elevator   | $\theta_4$, $\theta_7$ | $\theta_4 \alpha \delta_e + \theta_7 \alpha^2 \delta_e$ |
    | Pitch Rate | $\theta_3$, $\theta_6$, $\theta_9$ | $\theta_3 \alpha \tilde{q} + \theta_6 \alpha^2 \tilde{q} + \theta_9 \alpha^3 \tilde{q}$ |

    TODO - Any standard drag terms missing?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Side Force

    #### Side Force v Beta

    | Model Parameter | Standard Equivalent |
    | --------------- | ------------------- |
    | $\theta_{11}$   | $C_{Y_\beta}$       |
    """
    )
    return


@app.cell
def _():
    t_f16 = [ 
        0.034, -0.005, 20.77, 0.177, 1.285, -19.97, 0.756, 5.887, 55.59, -5.155,
        -1.146, -0.188, 0.876, 0.060, 0.164,
        0.074, 4.458, 29.90, 0.412, -5.538, -2.477, -1.101, 1.906, 
        -0.071, -0.445, 0.058, -0.143, 0.023,
        -0.024, -0.288, -8267, -0.563, -5.513, 9.793, -1.057, -2.018, 1.897, -0.094,
        0.234, 0.056, -0.418, 0.034, -0.085, 0.372, -0.725
    ]
    return (t_f16,)


@app.cell
def _(math, np, t_f16):
    alpha_rad = np.linspace(math.radians(-4), math.radians(30), 100)
    CL = t_f16[15] + t_f16[16]*alpha_rad + t_f16[20]*(alpha_rad**2) + t_f16[21]*(alpha_rad**3) + t_f16[22]*(alpha_rad**4)
    CD = t_f16[0] + t_f16[1]*alpha_rad + t_f16[4]*(alpha_rad**2) + t_f16[7]*(alpha_rad**3) + t_f16[9]*(alpha_rad**4)
    Cm = t_f16[28] + t_f16[29]*alpha_rad + t_f16[39]*(alpha_rad**4)
    return CD, CL, Cm, alpha_rad


@app.cell
def _(CD, CL, Cm, alpha_rad, plt):
    plt.figure()
    plt.plot(alpha_rad * 57.29578, CL, label='$C_L$')
    plt.plot(alpha_rad * 57.29578, CD, label='$C_D$')
    plt.plot(alpha_rad * 57.29578, Cm, label='$C_m$')
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## References

    [A Generic Nonlinear Aerodynamic Model for Aircraft](https://ntrs.nasa.gov/api/citations/20140011902/downloads/20140011902.pdf) - J. Grauer, E. Morelli
    """
    )
    return


@app.cell
def _():
    import marimo as mo

    import numpy as np
    from matplotlib import pyplot as plt
    import math
    return math, mo, np, plt


if __name__ == "__main__":
    app.run()
