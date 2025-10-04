import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(jsbsim737_kCDge_data, jsbsim737_kCLge_data, mo, plot_generic_xy):
    mo.md(
        rf"""
    # Ground Effect Models

    In the [Landing - Ground Effect, Flare - JSBSim](https://seanmcleod70.github.io/2018/02/landing-ground-effect-flare-jsbsim/)
    writeup the influence of ground effect was analyzed using the 737 aircraft model from the JSBSim repo during landing.

    The JSBSim 737 model includes a scale factor for lift and drag based on $h/b$ (height/wingspan) to model ground 
    effect. There is no ground effect modelling for the change in the pitch moment. The $C_L$ and $C_D$ ground effect scale factor is independent of flap configuration and also independent of angle of attack ($\alpha$). 

    {plot_generic_xy(jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1], 'JSBSim 737 $kC_{L_{ge}}$', '$h/b$', '$kC_{L_{ge}}$')}

    {plot_generic_xy(jsbsim737_kCDge_data[:,0], jsbsim737_kCDge_data[:,1], 'JSBSim 737 $kC_{D_{ge}}$', '$h/b$', '$kC_{D_{ge}}$')}

    In this write up we'll take a look at how the ground effect is modelled by Boeing for a B747-100 simulator and 
    also by Airbus for a generic civil transport aircraft and then compare the three ground effect models.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## NASA/Boeing 747-100 Simulator Model

    Boeing were contracted by NASA in 1970 to provide NASA-Ames Research Center with mathematical models and data to simulate the flying qualities and characteristics of the Boeing 747 on the NASA Flight Simulator for Advanced Aircraft (FSAA).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Lift

    $\Delta C_{L_{Ground \space Effect}} = K^B_{GE} \space \Delta C_{L_{GE}}$

    The change in lift due to ground effect is modelled as an increment in the lift coefficient based on a scaling
    factor $K^B_{GE}$ which varies between 0 and 1 depending on the height of the gear above ground. The $\Delta C_{L_{GE}}$
    factor is defined as an increment in $C_L$ based on a particular flap configuration and versus $\alpha$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    The basic $C_L$ versus $\alpha$ for low speed for different flap configurations, to which the $\Delta C_L$ due to 
    ground effect will be added.

    {mo.image("public/GroundEffect/CLBasic.png", width=600)}

    Ground effect height factor, $K^B_{{GE}}$ based on gear height above ground.

    {mo.image("public/GroundEffect/KBGE.png", width=600)}

    The $\Delta C_{{L_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCLGE.png", width=600)}
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_CL_groundeffect,
    plot_CL_groundeffect_AOA,
    plot_K_B_GE,
    plot_basic_CL,
    plot_delta_CL,
):
    mo.md(
        rf"""
    [Engauge Digitizer](https://engauge-digitizer.software.informer.com/) was used to digitize the plots from the NASA report.

    The take-off flap settings for the 747 are flaps 10 or flaps 20 and the landing flap options are flaps 25 or flaps 30.

    {plot_basic_CL()}

    {plot_K_B_GE()}

    {plot_delta_CL()}

    So combining $K^B_{{GE}}$ and $\Delta C_{{L_{{GE}}}}$ for the flaps 30 landing configuration we can see the increase in 
    the $C_L$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ vs AoA', '$C_L$', scaled_version=False)}

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ vs AoA', '$C_L$', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ scaling vs AoA for flaps 30', 'Scale Factor', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_L$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CL_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_L$ Scaling vs $h/b$ for flaps 30')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Drag

    $\Delta C_{D_{Ground \space Effect}} = K^A_{GE} \space \Delta C_{D_{GE}}$

    The change in drag due to ground effect takes the same form as the change in lift due to ground effect, i.e. 
    a change in the drag coefficient based on a scaling factor $K^A_{GE}$ which varies between 0 and 1 depending
    on the height of the gear above ground. The $\Delta C_{D_{GE}}$ factor is defined as a decrement in $C_D$ based
    on a particular flap configuration and versus $\alpha$. Note that the scaling factor $K^A_{GE}$ for drag is different
    to the one used for lift, $K^B_{GE}$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    The basic $C_D$ versus $\alpha$ for low speed for different flap configurations, to which the $\Delta C_D$ due to 
    ground effect will be added.

    {mo.image("public/GroundEffect/CDBasic.png", width=600)}

    Ground effect height factor, $K^A_{{GE}}$ based on gear height above ground.

    {mo.image("public/GroundEffect/KAGE.png", width=600)}

    The $\Delta C_{{D_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCDGE.png", width=600)}
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_CD_groundeffect,
    plot_CD_groundeffect_AOA,
    plot_K_A_GE,
    plot_basic_CD,
    plot_delta_CD,
):
    mo.md(
        rf"""
    Digitized plots.

    {plot_basic_CD()}

    {plot_K_A_GE()}

    {plot_delta_CD()}

    So combining $K^A_{{GE}}$ and $\Delta C_{{D_{{GE}}}}$ for the flaps 30 landing configuration we can see the decrease in 
    the $C_D$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ vs AoA', '$C_D$', scaled_version=False)}

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ vs AoA', '$C_D$', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ scaling vs AoA for flaps 30', 'Scale Factor', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_D$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CD_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_D$ Scaling vs $h/b$ for flaps 30')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Pitching Moment

    $\Delta C_{m_{Ground \space Effect}} = K^B_{GE} \space \Delta C_{m_{GE}}$

    The change in pitching moment due to ground effect takes the same form as the change in lift and drag due to 
    ground effect, i.e. a change in the pitching moment coefficient based on a scaling factor $K^B_{GE}$ which varies 
    between 0 and 1 depending on the height of the gear above ground. The $\Delta C_{m_{GE}}$ factor is defined as a 
    delta in $C_m$ based on a particular flap configuration and versus $\alpha$. Note that the scaling factor $K^B_{GE}$ 
    used for the pitching moment is the same one as used for lift.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    The basic $C_m$ versus $\alpha$ for low speed for different flap configurations, to which the $\Delta C_m$ due to 
    ground effect will be added.

    {mo.image("public/GroundEffect/CMBasic1.png", width=600)}

    {mo.image("public/GroundEffect/CMBasic2.png", width=600)}

    Ground effect height factor, $K^B_{{GE}}$ based on gear height above ground. Same one used for lift.

    {mo.image("public/GroundEffect/KBGE.png", width=600)}

    The $\Delta C_{{m_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCMGE.png", width=600)}
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_CM_groundeffect,
    plot_CM_groundeffect_AOA,
    plot_K_B_GE,
    plot_basic_CM,
    plot_delta_CM,
):
    mo.md(
        rf"""
    Digitized plots.

    {plot_basic_CM()}

    {plot_K_B_GE()}

    {plot_delta_CM()}

    So combining $K^B_{{GE}}$ and $\Delta C_{{m_{{GE}}}}$ for the flaps 30 landing configuration we can see the change in 
    the $C_m$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ vs AoA', '$C_m$', scaled_version=False)}

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ vs AoA', '$C_m$', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ scaling vs AoA for flaps 30', 'Scale Factor', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_m$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CM_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_m$ Scaling vs $h/b$ for flaps 30')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Airbus Generic Civil Transport

    In 2016 ONERA and Airbus proposed [A Civilian Aircraft Landing Challenge](https://w3.onera.fr/smac/sites/default/files/2024-01/CALC_v2.pdf):

    > the final approach and landing phases still remain critical in poor visibility and strong wind conditions. Based on a realistic nonlinear model of a civil transport aircraft in full configuration, the objective of the proposed challenge is to design an autopilot system to enable a correct landing despite parametric variations and **maximized cross wind** conditions.

    Included in the model is a ground effect model, modelling the change in $C_L$ and $C_m$, but no modelling of the change
    in $C_D$.

    The model is for a single 'full configuration' for landing, so unlike the 747 model there isn't data for different
    flap configurations.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Lift

    $\Delta C_{L_{Ground \space Effect}} = C_{L_{H}} e^{- \lambda_L H_{LG}}$

    $C_{L_{H}} = 0.20$ 

    $\lambda_L = 0.12$

    $H_{LG}$ - Landing gear height
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, plot_airbus_delta_CL):
    mo.md(
        rf"""
    Assuming a wingspan of $b = 60.3m$ based on an A330.

    {plot_airbus_delta_CL()}

    The lift is modelled only over the linear portion of the $C_L$ versus $\alpha$ curve with:

    $C_{{L_{{0}}}} = 0.90$

    $C_{{L_{{\alpha}}}} = 5.5$
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_airbus_lift_plus_delta_ge,
    plot_airbus_lift_scaling,
    plot_airbus_lift_scaling_vs_hb,
):
    mo.md(
        rf"""
    {plot_airbus_lift_plus_delta_ge()}

    {plot_airbus_lift_scaling()}

    {plot_airbus_lift_scaling_vs_hb()}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Pitching Moment

    $\Delta C_{m_{GroundEffect}} = (C_{m_{H_{0}}} + C_{m_{H_{\alpha}}} \alpha) e^{- \lambda_m H_{LG}}$

    $C_{m_{H_{0}}} = -0.09$

    $C_{m_{H_{\alpha}}} = -0.9$

    $\lambda_m = 0.15$

    $H_{LG}$ - Landing gear height

    The basic pitch moment is modelled by:

    $C_m = C_{m_{0}} + C_{m_{\alpha}} \alpha$

    $C_{m_{0}} = -0.3$

    $C_{m_{\alpha}} = -1.5$
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_airbus_basic_cm,
    plot_airbus_delta_Cm,
    plot_airbus_delta_Cm_alpha,
    plot_airbus_net_Cm,
    plot_airbus_net_Cm_scaling,
):
    mo.md(
        rf"""
    {plot_airbus_basic_cm()}

    {plot_airbus_delta_Cm()}

    {plot_airbus_delta_Cm_alpha()}

    {plot_airbus_net_Cm()}

    {plot_airbus_net_Cm_scaling()}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## References

    - [The Simulation of a Jumbo Jet Transport Aircraft - Volume II - Modeling Data](https://ntrs.nasa.gov/api/citations/19730001300/downloads/19730001300.pdf)

    - [A Civilian Aircraft Landing Challenge](https://w3.onera.fr/smac/sites/default/files/2024-01/CALC_v2.pdf)

    - [Dynamic Ground Effects Flight Test of an F-15 Aircraft](https://ntrs.nasa.gov/api/citations/19950005778/downloads/19950005778.pdf)

    - [Flight Measurements of Ground Effect on the Lift and Pitching Moment of a Large Transport Aircraft (Comet 3B) and Comparison with Wind Tunnel and Other Data ](https://aerade.cranfield.ac.uk/bitstream/handle/1826.2/2880/arc-rm-3611.pdf?sequence=1)

    - [Ground-Effect Analysis of a Jet  Transport Airplane](https://ntrs.nasa.gov/api/citations/19850007378/downloads/19850007378.pdf)

    - [Lifting-Line Predictions for Induced Drag and Lift in Ground Effect](https://www.researchgate.net/publication/269047238_Lifting-Line_Predictions_for_Induced_Drag_and_Lift_in_Ground_Effect)

    - [Crash During Experimental Test Flight 
    Gulfstream Aerospace Corporation GVI (G650)](https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR1202.pdf)
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
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    return math, mo, np, plt


@app.cell
def _():
    # Wingspan 
    b = 195.68

    def flaps_data_index(flap_setting):
        flap_indices = { 0: 1, 1: 2, 5: 3, 10: 4, 20: 5, 25: 6, 30: 7 }    
        return flap_indices[flap_setting] 

    def flaps_label(flap_setting):
        return f"Flaps {flap_setting}"
    return b, flaps_data_index, flaps_label


@app.cell
def _(np):
    # Data

    jsbsim737_kCLge_data = np.loadtxt('data/GroundEffect/737kCLge.csv', delimiter=',', skiprows=1)
    jsbsim737_kCDge_data = np.loadtxt('data/GroundEffect/737kCDge.csv', delimiter=',', skiprows=1)

    basic_cl_data = np.loadtxt('data/GroundEffect/CL-Curves.csv', delimiter=',', skiprows=1)
    K_B_GE_data = np.loadtxt('data/GroundEffect/KBGE.csv', delimiter=',', skiprows=1)
    delta_cl_data = np.loadtxt('data/GroundEffect/Delta-CLGE.csv', delimiter=',', skiprows=1)

    basic_cd_data = np.loadtxt('data/GroundEffect/CD-Curves.csv', delimiter=',', skiprows=1)
    K_A_GE_data = np.loadtxt('data/GroundEffect/KAGE.csv', delimiter=',', skiprows=1)
    delta_cd_data = np.loadtxt('data/GroundEffect/Delta-CDGE.csv', delimiter=',', skiprows=1)

    basic_cm_data = np.loadtxt('data/GroundEffect/CM-Curves.csv', delimiter=',', skiprows=1)
    delta_cm_data = np.loadtxt('data/GroundEffect/Delta-CMGE.csv', delimiter=',', skiprows=1)
    return (
        K_A_GE_data,
        K_B_GE_data,
        basic_cd_data,
        basic_cl_data,
        basic_cm_data,
        delta_cd_data,
        delta_cl_data,
        delta_cm_data,
        jsbsim737_kCDge_data,
        jsbsim737_kCLge_data,
    )


@app.cell
def _(K_A_GE_data, K_B_GE_data, plot_K_GE):
    def plot_K_B_GE():
        return plot_K_GE(K_B_GE_data, "$K^B_{GE}$")

    def plot_K_A_GE():
        return plot_K_GE(K_A_GE_data, "$K^A_{GE}$")
    return plot_K_A_GE, plot_K_B_GE


@app.cell
def _(b, mo, plt):
    def plot_K_GE(data, ylabel):
        fig, ax = plt.subplots()

        ax.plot(data[:,1], data[:,0])
        ax.set_xlabel("Gear height above ground (ft)")
        secax = ax.secondary_xaxis('top', functions=(lambda x: x/b, lambda x: b*x))
        secax.set_xlabel("h/b")

        ax.set_ylabel(ylabel)
        ax.set_title("Ground Effect Height Factor")

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_K_GE,)


@app.cell
def _(basic_cl_data, plot_CL_versus_alpha):
    def plot_basic_CL():
        return plot_CL_versus_alpha(basic_cl_data, [10, 20, 25, 30], 'Basic $C_L$ versus $\\alpha$', '$C_L$')
    return (plot_basic_CL,)


@app.cell
def _(delta_cl_data, plot_CL_versus_alpha):
    def plot_delta_CL():
        return plot_CL_versus_alpha(delta_cl_data, [10, 20, 25, 30], '$\\Delta C_{L_{GE}}$ versus $\\alpha$', '$\\Delta C_{L_{GE}}$')
    return (plot_delta_CL,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CL_versus_alpha(data, flaps, title, ylabel):

        fig, ax = plt.subplots()

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CL_versus_alpha,)


@app.cell
def _(
    K_B_GE_data,
    b,
    basic_cl_data,
    delta_cl_data,
    flaps_data_index,
    flaps_label,
    mo,
    np,
    plt,
):
    def plot_CL_groundeffect(flap, h_bs, title, ylabel, scaled_version, xlim=None):

        fig, ax = plt.subplots()

        # Plot basic CL for flap argument
        if scaled_version is False:
            ax.plot(basic_cl_data[:,0], basic_cl_data[:,flaps_data_index(flap)], label=flaps_label(flap), color='b')

        # Calculate and plot using K_GE and delta-CL
        for h_b in h_bs:
            k_ge = np.interp(h_b * b, np.flip(K_B_GE_data[:,1]), np.flip(K_B_GE_data[:,0]))
            scaled_delta_cl = delta_cl_data[:,flaps_data_index(flap)] * k_ge

            CL = []
            for index in range(len(delta_cl_data[:,0])):
                alpha = delta_cl_data[index,0]
                cl_basic = np.interp(alpha, basic_cl_data[:,0], basic_cl_data[:,flaps_data_index(flap)])
                if scaled_version:
                    CL.append((scaled_delta_cl[index] + cl_basic)/cl_basic)
                else:
                    CL.append(scaled_delta_cl[index] + cl_basic)         

            ax.plot(delta_cl_data[:,0], CL, label=f'h/b {h_b}')

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()

        if xlim is not None:
            ax.set_xlim(xlim[0], xlim[1])

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CL_groundeffect,)


@app.cell
def _(
    K_B_GE_data,
    b,
    basic_cl_data,
    delta_cl_data,
    flaps_data_index,
    mo,
    np,
    plt,
):
    def plot_CL_groundeffect_AOA(flap, alphas, title):

        fig, ax = plt.subplots()

        for alpha in alphas:
            cl_basic = np.interp(alpha, basic_cl_data[:,0], basic_cl_data[:,flaps_data_index(flap)])
            cl_delta = np.interp(alpha, delta_cl_data[:,0], delta_cl_data[:,flaps_data_index(flap)])
            alpha_scale = []
            hbs = np.linspace(0, 0.4)
            for hb in hbs:
                kge = np.interp(hb * b, np.flip(K_B_GE_data[:,1]), np.flip(K_B_GE_data[:,0]))
                scale = (cl_basic + kge * cl_delta) / cl_basic
                alpha_scale.append(scale)
            ax.plot(hbs, alpha_scale, label=f'$\\alpha = {alpha}$')

        ax.set_title(title)
        ax.set_ylabel('Scale Factor')
        ax.set_xlabel('$h/b$')
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CL_groundeffect_AOA,)


@app.cell
def _(basic_cd_data, plot_CD_versus_alpha):
    def plot_basic_CD():
        return plot_CD_versus_alpha(basic_cd_data, [10, 20, 25, 30], 'Basic $C_D$ versus $\\alpha$', '$C_D$')
    return (plot_basic_CD,)


@app.cell
def _(delta_cd_data, plot_CD_versus_alpha):
    def plot_delta_CD():
        return plot_CD_versus_alpha(delta_cd_data, [10, 20, 25, 30], '$\\Delta C_{D_{GE}}$ versus $\\alpha$', '$\\Delta C_{D_{GE}}$')
    return (plot_delta_CD,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CD_versus_alpha(data, flaps, title, ylabel):

        fig, ax = plt.subplots()

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CD_versus_alpha,)


@app.cell
def _(
    K_A_GE_data,
    b,
    basic_cd_data,
    delta_cd_data,
    flaps_data_index,
    flaps_label,
    mo,
    np,
    plt,
):
    def plot_CD_groundeffect(flap, h_bs, title, ylabel, scaled_version, xlim=None):

        fig, ax = plt.subplots()

        # Plot basic CD for flap argument
        if scaled_version is False:
            ax.plot(basic_cd_data[:,0], basic_cd_data[:,flaps_data_index(flap)], label=flaps_label(flap), color='b')

        # Calculate and plot using K_GE and delta-CD
        for h_b in h_bs:
            k_ge = np.interp(h_b * b, np.flip(K_A_GE_data[:,1]), np.flip(K_A_GE_data[:,0]))
            scaled_delta_cd = delta_cd_data[:,flaps_data_index(flap)] * k_ge

            CD = []
            for index in range(len(delta_cd_data[:,0])):
                alpha = delta_cd_data[index,0]
                cd_basic = np.interp(alpha, basic_cd_data[:,0], basic_cd_data[:,flaps_data_index(flap)])
                if scaled_version:
                    CD.append((scaled_delta_cd[index] + cd_basic)/cd_basic)
                else:
                    CD.append(scaled_delta_cd[index] + cd_basic)         

            ax.plot(delta_cd_data[:,0], CD, label=f'h/b {h_b}')

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()

        if xlim is not None:
            ax.set_xlim(xlim[0], xlim[1])

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CD_groundeffect,)


@app.cell
def _(
    K_A_GE_data,
    b,
    basic_cd_data,
    delta_cd_data,
    flaps_data_index,
    mo,
    np,
    plt,
):
    def plot_CD_groundeffect_AOA(flap, alphas, title):

        fig, ax = plt.subplots()

        for alpha in alphas:
            cd_basic = np.interp(alpha, basic_cd_data[:,0], basic_cd_data[:,flaps_data_index(flap)])
            cd_delta = np.interp(alpha, delta_cd_data[:,0], delta_cd_data[:,flaps_data_index(flap)])
            alpha_scale = []
            hbs = np.linspace(0, 0.4)
            for hb in hbs:
                kge = np.interp(hb * b, np.flip(K_A_GE_data[:,1]), np.flip(K_A_GE_data[:,0]))
                scale = (cd_basic + kge * cd_delta) / cd_basic
                alpha_scale.append(scale)
            ax.plot(hbs, alpha_scale, label=f'$\\alpha = {alpha}$')

        ax.set_title(title)
        ax.set_ylabel('Scale Factor')
        ax.set_xlabel('$h/b$')
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CD_groundeffect_AOA,)


@app.cell
def _(basic_cm_data, plot_CM_versus_alpha):
    def plot_basic_CM():
        return plot_CM_versus_alpha(basic_cm_data, [10, 20, 25, 30], 'Basic $C_m$ versus $\\alpha$', '$C_m$')
    return (plot_basic_CM,)


@app.cell
def _(delta_cm_data, plot_CM_versus_alpha):
    def plot_delta_CM():
        return plot_CM_versus_alpha(delta_cm_data, [10, 20, 25, 30], '$\\Delta C_{m_{GE}}$ versus $\\alpha$', '$\\Delta C_{m_{GE}}$')
    return (plot_delta_CM,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CM_versus_alpha(data, flaps, title, ylabel):

        fig, ax = plt.subplots()

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CM_versus_alpha,)


@app.cell
def _(
    K_B_GE_data,
    b,
    basic_cm_data,
    delta_cm_data,
    flaps_data_index,
    flaps_label,
    mo,
    np,
    plt,
):
    def plot_CM_groundeffect(flap, h_bs, title, ylabel, scaled_version, xlim=None):

        fig, ax = plt.subplots()

        # Plot basic CM for flap argument
        if scaled_version is False:
            ax.plot(basic_cm_data[:,0], basic_cm_data[:,flaps_data_index(flap)], label=flaps_label(flap), color='b')

        # Calculate and plot using K_GE and delta-CM
        for h_b in h_bs:
            k_ge = np.interp(h_b * b, np.flip(K_B_GE_data[:,1]), np.flip(K_B_GE_data[:,0]))
            scaled_delta_cm = delta_cm_data[:,flaps_data_index(flap)] * k_ge

            CM = []
            for index in range(len(delta_cm_data[:,0])):
                alpha = delta_cm_data[index,0]
                cm_basic = np.interp(alpha, basic_cm_data[:,0], basic_cm_data[:,flaps_data_index(flap)])
                if scaled_version:
                    CM.append((scaled_delta_cm[index] + cm_basic)/cm_basic)
                else:
                    CM.append(scaled_delta_cm[index] + cm_basic)         

            ax.plot(delta_cm_data[:,0], CM, label=f'h/b {h_b}')

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()

        if xlim is not None:
            ax.set_xlim(xlim[0], xlim[1])

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CM_groundeffect,)


@app.cell
def _(
    K_B_GE_data,
    b,
    basic_cm_data,
    delta_cm_data,
    flaps_data_index,
    mo,
    np,
    plt,
):
    def plot_CM_groundeffect_AOA(flap, alphas, title):

        fig, ax = plt.subplots()

        for alpha in alphas:
            cm_basic = np.interp(alpha, basic_cm_data[:,0], basic_cm_data[:,flaps_data_index(flap)])
            cm_delta = np.interp(alpha, delta_cm_data[:,0], delta_cm_data[:,flaps_data_index(flap)])
            alpha_scale = []
            hbs = np.linspace(0, 0.4)
            for hb in hbs:
                kge = np.interp(hb * b, np.flip(K_B_GE_data[:,1]), np.flip(K_B_GE_data[:,0]))
                scale = (cm_basic + kge * cm_delta) / cm_basic
                alpha_scale.append(scale)
            ax.plot(hbs, alpha_scale, label=f'$\\alpha = {alpha}$')

        ax.set_title(title)
        ax.set_ylabel('Scale Factor')
        ax.set_xlabel('$h/b$')
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CM_groundeffect_AOA,)


@app.cell
def _(mo, np, plt):
    def plot_airbus_delta_CL():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        clh = 0.2
        lambdal = 0.12

        hlg = np.linspace(0, 60.3, 100)
        hb = hlg/b

        delta_cl = clh * np.exp(-lambdal * hlg)

        ax.plot(hb, delta_cl)
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('$\\Delta C_{L_{GE}}$')
        plt.title('$\\Delta C_{L_{GE}}$ versus $h/b$')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_delta_CL,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_plus_delta_ge():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        clh = 0.2
        lambdal = 0.12    

        cl0 = 0.9
        clalpha = 5.5 / math.degrees(1)

        min_alpha = 0
        max_alpha = 14
        alphas = [min_alpha, max_alpha]
    
        ax.plot(alphas, [cl0 + clalpha*min_alpha, cl0 + clalpha*max_alpha], label='Landing Flaps', color='b')
    
        for hb in [0, 0.1, 0.2, 0.3]:
        
            hlg = b * hb
            delta_cl = clh * np.exp(-lambdal * hlg)
            cls = [cl0 + clalpha*min_alpha + delta_cl, cl0 + clalpha*max_alpha + delta_cl]
            ax.plot(alphas, cls, label=f'h/b {hb:.1f}')    

        ax.legend()
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('$C_L$')
        plt.title('$C_L$ vs AoA')
    
        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_lift_plus_delta_ge,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_scaling():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        clh = 0.2
        lambdal = 0.12    

        cl0 = 0.9
        clalpha = 5.5 / math.degrees(1)

        min_alpha = 0
        max_alpha = 14
        alphas = [min_alpha, max_alpha]
           
        for hb in [0, 0.1, 0.2, 0.3]:
            hlg = b * hb
            delta_cl = clh * np.exp(-lambdal * hlg)
            cls = [(cl0 + clalpha*min_alpha + delta_cl)/(cl0 + clalpha*min_alpha), (cl0 + clalpha*max_alpha + delta_cl)/(cl0 + clalpha*max_alpha)]
            ax.plot(alphas, cls, label=f'h/b {hb:.1f}')    

        ax.legend()
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_L$ scaling vs AoA')
    
        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_lift_scaling,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_scaling_vs_hb():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        clh = 0.2
        lambdal = 0.12 

        cl0 = 0.9
        clalpha = 5.5 / math.degrees(1)    

        for alpha in [0, 5, 10, 14.5]:
            hbs = np.linspace(0, 0.4, 50)
            hlg = b * hbs
            delta_cl = clh * np.exp(-lambdal * hlg)      
            cl_base = cl0 + clalpha*alpha
            cl_scaling = (delta_cl + cl_base) / cl_base
            ax.plot(hbs, cl_scaling, label=f'$\\alpha = $ {alpha}')

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_L$ scaling vs $h/b$')
    
        return mo.md(f"{mo.as_html(fig)}")     
    return (plot_airbus_lift_scaling_vs_hb,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_basic_cm():

        fig, ax = plt.subplots()

        cm_0 = -0.3
        cm_alpha = -1.5 / math.degrees(1)

        alphas = np.linspace(0, 14, 3)
        cms = cm_0 + cm_alpha*alphas
    
        ax.plot(alphas, cms)
    
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('$C_m$')
        plt.title('Basic $C_m$ versus $\\alpha$')    

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_basic_cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_delta_Cm():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        cm_h0 = -0.09
        cm_halpha = -0.9
        lambda_m = 0.15

        hlg = np.linspace(0, 60.3/2, 100)
        hb = hlg/b

        for alpha in [0, 5, 10, 15]:
            alpha_rad = math.radians(alpha)
            delta_cm = (cm_h0 + cm_halpha * alpha_rad) * np.exp(-lambda_m * hlg)
            ax.plot(hb, delta_cm, label=f'$\\alpha$ = {alpha}')

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('$\\Delta C_{m_{GE}}$')
        plt.title('$\\Delta C_{m_{GE}}$ versus $h/b$')

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_delta_Cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_delta_Cm_alpha():

        fig, ax = plt.subplots()

        b = 60.3  # A-330 wingspan
        cm_h0 = -0.09
        cm_halpha = -0.9 / math.degrees(1)
        lambda_m = 0.15
    
        alphas = np.linspace(0, 14, 28)

        for hb in [0, 0.1, 0.2, 0.3]:
            hlg = b * hb 
            delta_cms = (cm_h0 + cm_halpha * alphas) * np.exp(-lambda_m * hlg)
            ax.plot(alphas, delta_cms, label=f'$h/b$ {hb:.1f}')
    
        ax.legend()
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('$\\Delta C_{m_{GE}}$')
        plt.title('$\\Delta C_{m_{GE}}$ versus AoA')

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_delta_Cm_alpha,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_net_Cm():

        fig, ax = plt.subplots()
    
        b = 60.3  # A-330 wingspan
        cm_0 = -0.3
        cm_alpha = -1.5 / math.degrees(1)
        cm_h0 = -0.09
        cm_halpha = -0.9 / math.degrees(1)
        lambda_m = 0.15    

        alphas = np.linspace(0, 14, 3)
        cms = cm_0 + cm_alpha*alphas
    
        ax.plot(alphas, cms, label='Landing flaps')

        for hb in [0, 0.1, 0.2, 0.3]:
            hlg = b * hb
            alphas = np.linspace(0, 14, 20)
            cm_nets = (cm_h0 + cm_halpha * alphas) * np.exp(-lambda_m * hlg) + cm_0 + cm_alpha * alphas
            ax.plot(alphas, cm_nets, label=f'$h/b$ {hb:.1f}')
    
        ax.legend()
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('$C_m$')
        plt.title('$C_m$ versus AoA')

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_net_Cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_net_Cm_scaling():

        fig, ax = plt.subplots()
    
        b = 60.3  # A-330 wingspan
        cm_0 = -0.3
        cm_alpha = -1.5 / math.degrees(1)
        cm_h0 = -0.09
        cm_halpha = -0.9 / math.degrees(1)
        lambda_m = 0.15    

        alphas = np.linspace(0, 14, 3)
        cms = cm_0 + cm_alpha*alphas

        for hb in [0, 0.1, 0.2, 0.3]:
            hlg = b * hb
            alphas = np.linspace(0, 14, 20)
            cm_nets = (cm_h0 + cm_halpha * alphas) * np.exp(-lambda_m * hlg) + cm_0 + cm_alpha * alphas
            cm_basic = cm_0 + cm_alpha * alphas
            cm_net_scaling = cm_nets / cm_basic
            ax.plot(alphas, cm_net_scaling, label=f'$h/b$ {hb:.1f}')
    
        ax.legend()
        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_m$ scaling versus AoA')

        return mo.md(f"{mo.as_html(fig)}") 
    return (plot_airbus_net_Cm_scaling,)


@app.cell
def _(mo, plt):
    def plot_generic_xy(x, y, title, xlabel, ylabel):

        fig, ax = plt.subplots()

        ax.plot(x, y)

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_generic_xy,)


if __name__ == "__main__":
    app.run()
