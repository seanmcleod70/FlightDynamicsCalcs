import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(jsbsim737_kCDge_data, jsbsim737_kCLge_data, mo, plot_generic_xy):
    mo.md(
        rf"""
    # Ground Effect

    In the [Landing - Ground Effect, Flare - JSBSim](https://seanmcleod70.github.io/2018/02/landing-ground-effect-flare-jsbsim/)
    writeup the influence of ground effect was analyzed using the 737 aircraft model in the JSBSim repo during landing.

    The JSBSim 737 model includes a scale factor for lift and drag based on $h/b$ (height/wingspan) to model ground 
    effect. There is no ground effect modelling for the change in the pitch moment. The $C_L$ and $C_D$ ground effect scale factor is independent of flap configuration and also independent of angle of attack ($\alpha$). 

    {plot_generic_xy(jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1], 'JSBSim 737 $kC_{L_{ge}}$', '$h/b$', '$kC_{L_{ge}}$')}

    {plot_generic_xy(jsbsim737_kCDge_data[:,0], jsbsim737_kCDge_data[:,1], 'JSBSim 737 $kC_{D_{ge}}$', '$h/b$', '$kC_{D_{ge}}$')}

    In this write up we'll take a look at how the ground effect is modelled by Boeing for a B747-100 simulator.
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

    **TODO**
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## References

    - [The Simulation of a Jumbo Jet Transport Aircraft - Volume II - Modeling Data](https://ntrs.nasa.gov/api/citations/19730001300/downloads/19730001300.pdf)

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
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


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
    return (
        K_A_GE_data,
        K_B_GE_data,
        basic_cd_data,
        basic_cl_data,
        delta_cd_data,
        delta_cl_data,
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
    def plot_CL_groundeffect(flap, h_bs, title, ylabel, scaled_version):

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
    def plot_CD_groundeffect(flap, h_bs, title, ylabel, scaled_version):

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
