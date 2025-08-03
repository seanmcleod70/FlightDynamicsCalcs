import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # JSBSim Aerodynamics

    The main purpose of this guide is to provide useful information for JSBSim FDM modellers who don't necessarily have a formal background in flight dynamics. To make them aware of the typical aerodynamic forces and moments they need to provide to model the flight characteristics of an aircraft, without turning into a full-fledged textbook on flight dynamics.

    In creating an FDM for a particular aircraft type the FDM modeller needs to decide what level of fidelity they want to aim for. This will partly be based on the FDM modeller's aim for the project but will also often be dictated by the level of source data available for the aircraft type. 

    JSBSim is a 6 degrees of freedom simulator but doesn't come with any pre-defined forces and moments. The FDM developer needs to supply definitions for each of the forces and moments acting on the aircraft. During each time step JSBSim will then sum the individual forces and moments for each of the 3 axes and then use them to calculate translational and angular accelerations based on the aircraft's current mass and moments of inertia. These accelerations will then be integrated via the equations of motion to calculate an updated pose (3D position and attitude) for the aircraft.

    ## Frames of Reference

    The FDM modeller 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The force coefficients are made non-dimensional by dividing the force by the dynamic pressure and a reference area.

    $$ C_L = \frac{L}{QS} \quad C_D = \frac{D}{QS} \quad C_Y = \frac{Y}{QS} $$

    The moment coefficients are made non-dimensional by dividing the moment by the dynamic pressure, a reference area and a reference length.

    $$ C_m = \frac{M}{QS \bar{c}} \quad C_l = \frac{L}{QSb} \quad C_n = \frac{N}{QSb} $$

    | Coefficient                           | Description                    |
    | ------------------------------------- | ------------------------------ |
    | **Lift Forces**                       |                                |
    | $C_{L_{0}}$ $C_{L_{\alpha}}$          | Lift due to alpha              |
    | $C_{L_{\dot \alpha}}$                 | Lift due to alpha rate         |
    | $C_{L_{q}}$                           | Lift due to pitch rate         |
    | $C_{L_{\delta_e}}$                    | Lift due to elevator           |
    | **Drag Forces**                       |                                |
    | $C_{D_{0}}$ $C_{D_{\alpha}}$          | Drag due to alpha              |
    | $C_{D_{\delta_e}}$                    | Drag due to elevator           |
    | **Side Forces**                       |                                |
    | $C_{Y_{\beta}}$                       | Side force due to beta         |
    | $C_{Y_{\delta_r}}$                    | Side force due to rudder       |
    | **Pitch Moments**                     |                                |
    | $C_{m_{\alpha}}$                      | Pitch moment due to alpha      |
    | $C_{m_{\dot \alpha}}$                 | Pitch moment due to alpha dot  |
    | $C_{m_{q}}$                           | Pitch moment due to pitch rate |
    | $C_{m_{\delta_e}}$                   | Pitch moment due to elevator   |
    | **Yaw Moments**                       |                                |
    | $C_{n_{\beta}}$                       | Yaw moment due to beta         |
    | $C_{n_{p}}$                           | Yaw moment due to roll rate    |
    | $C_{n_{r}}$                           | Yaw moment due to yaw rate     |
    | $C_{n_{\delta_r}}$                    | Yaw moment due to rudder       |
    | $C_{n_{\delta_a}}$                    | Yaw moment due to aileron      |
    | **Roll Moments**                      |                                |
    | $C_{l_{\beta}}$                       | Roll moment due to beta        |
    | $C_{l_{p}}$                           | Roll moment due to roll rate   |
    | $C_{l_{r}}$                           | Roll moment due to yaw rate    |
    | $C_{l_{\delta_a}}$                    | Roll moment due to aileron     |
    | $C_{l_{\delta_r}}$                    | Roll moment due to rudder      |
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Nondimensional Angular Rates

    Coefficients that are based on angular rates like $C_{m_{q}}$ are based on nondimensional body-axis angular rates.

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

    $S$ - Wing planform area

    $b$ - Wing span

    $\bar{c}$ - Mean chord

    $V$ - True airspeed

    $\rho$ - Air density

    $Q = \frac{1}{2} \rho V^2$ - Dynamic pressure

    $C_{m_{q}} = \dfrac{\partial C_m}{\partial\left(\dfrac{q \bar{c}}{2V}\right)}$

    ```xml
                <function name="aero/coefficient/Cmq">
                    <description>Pitch_moment_due_to_pitch_rate</description>
                    <product>
                        <property>aero/qbar-psf</property>
                        <property>metrics/Sw-sqft</property>
                        <property>metrics/cbarw-ft</property>
                        <property>aero/ci2vel</property>
                        <property>velocities/q-aero-rad_sec</property>
                        <value>-27.0</value>
                    </product>
                </function>
    ```

    $C_{m_{\dot \alpha}} = \dfrac{\partial C_m}{\partial\left(\dfrac{\dot \alpha \bar{c}}{2V}\right)}$
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
