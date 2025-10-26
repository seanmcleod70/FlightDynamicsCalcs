import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    # Ground Effect Models

    In the [Landing - Ground Effect, Flare - JSBSim](https://seanmcleod70.github.io/2018/02/landing-ground-effect-flare-jsbsim/)
    writeup the influence of ground effect was analyzed using the 737 aircraft model from the JSBSim repo during landing.

    In this write up we'll take a look at how the ground effect is modelled by JSBSim's 737 model, by Boeing for a 
    B747-100 simulator and also by Airbus for a generic civil transport aircraft and then compare the three ground effect models.

    ## Background

    > Ground effects may be explained by the interaction  of the aircraft wingtip vortices with the ground.
    > This interaction reduces the strength of these vortices. The  weakened wingtip vortices reduce the wing
    > downwash which increases the lift and decreases the induced drag, or drag caused by lift.
    > In addition, the reduced downwash at the wing trailing edge increases the angle of attack  of the relative
    > wind at the elevator, resulting in a nose down pitching moment. In a fundamental sense, the  change in
    > downwash near the ground results in a different pressure distribution over the wing, tail, and fuselage.
    > This distribution alters the aircraft aerodynamic forces and moments.
    """
    )
    return


@app.cell(hide_code=True)
def _(
    jsbsim737_kCDge_data,
    jsbsim737_kCLge_data,
    mo,
    plot_generic_xy,
    plot_jsbsim_CD_scaling,
):
    mo.md(
        rf"""
    ## JSBSim Model

    The JSBSim 737 model includes a scale factor for lift and drag based on $h/b$ (height/wingspan) to model ground 
    effect. There is no ground effect modelling for the change in the pitch moment.

    ### Lift

    The $kC_{{L_{{ge}}}}$ ground efect scale factor is independent of flap configuration and also independent of angle of attack ($\alpha$).

    {plot_generic_xy(jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1], 'JSBSim 737 $kC_{L_{ge}}$', '$h/b$', '$kC_{L_{ge}}$', 'Figure 1')}

    ### Drag

    The $kC_{{D_{{ge}}}}$ ground effect scale factor is applied to the induced drag component of the 737's drag model 
    where the induced drag is proportional to ${{C_L}}^2$. The $kC_{{D_{{ge}}}}$ ground efect scale factor is 
    independent of flap configuration and also independent of angle of attack ($\alpha$).

    {plot_generic_xy(jsbsim737_kCDge_data[:,0], jsbsim737_kCDge_data[:,1], 'JSBSim 737 $kC_{D_{ge}}$', '$h/b$', '$kC_{D_{ge}}$', 'Figure 2')}

    The extra complication is that in ground effect the lift is increased via the $kC_{{L_{{ge}}}}$ scale factor, which 
    means ${{C_L}}^2$ increases which then increases the induced drag. However the net drag needs to be reduced in ground
    effect which means the $kC_{{D_{{ge}}}}$ scale factor needs to undo the increase in induced drag due to the increase in
    lift in ground effect, and then reduce it further in order to have a net reduction in drag in ground effect.

    {plot_jsbsim_CD_scaling('Figure 3')}
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

    {mo.image("public/GroundEffect/CLBasic.png", width=600, caption='Figure 4')}

    Ground effect height factor, $K^B_{{GE}}$ based on gear height above ground.

    {mo.image("public/GroundEffect/KBGE.png", width=600, caption='Figure 5')}

    The $\Delta C_{{L_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCLGE.png", width=600, caption='Figure 6')}
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

    {plot_basic_CL('Figure 7')}

    {plot_K_B_GE('Figure 8')}

    {plot_delta_CL('Figure 9')}

    So combining $K^B_{{GE}}$ and $\Delta C_{{L_{{GE}}}}$ for the flaps 30 landing configuration we can see the increase in 
    the $C_L$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ vs AoA', '$C_L$', 'Figure 10', scaled_version=False)}

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ vs AoA', '$C_L$', 'Figure 11', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ scaling vs AoA for flaps 30', 'Scale Factor', 'Figure 12', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_L$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CL_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_L$ Scaling vs $h/b$ for flaps 30', 'Figure 13')}
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

    {mo.image("public/GroundEffect/CDBasic.png", width=600, caption='Figure 14')}

    Ground effect height factor, $K^A_{{GE}}$ based on gear height above ground.

    {mo.image("public/GroundEffect/KAGE.png", width=600, caption='Figure 15')}

    The $\Delta C_{{D_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCDGE.png", width=600, caption='Figure 16')}
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

    {plot_basic_CD('Figure 17')}

    {plot_K_A_GE('Figure 18')}

    {plot_delta_CD('Figure 19')}

    So combining $K^A_{{GE}}$ and $\Delta C_{{D_{{GE}}}}$ for the flaps 30 landing configuration we can see the decrease in 
    the $C_D$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ vs AoA', '$C_D$', 'Figure 20', scaled_version=False)}

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ vs AoA', '$C_D$', 'Figure 21', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CD_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_D$ scaling vs AoA for flaps 30', 'Scale Factor', 'Figure 22', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_D$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CD_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_D$ Scaling vs $h/b$ for flaps 30', 'Figure 23')}
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

    {mo.image("public/GroundEffect/CMBasic1.png", width=600, caption='Figure 24')}

    {mo.image("public/GroundEffect/CMBasic2.png", width=600, caption='Figure 25')}

    Ground effect height factor, $K^B_{{GE}}$ based on gear height above ground. Same one used for lift.

    {mo.image("public/GroundEffect/KBGE.png", width=600, caption='Figure 26')}

    The $\Delta C_{{m_{{GE}}}}$ versus $\alpha$ for different flap configurations.

    {mo.image("public/GroundEffect/DeltaCMGE.png", width=600, caption='Figure 27')}
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

    {plot_basic_CM('Figure 28')}

    {plot_K_B_GE('Figure 29')}

    {plot_delta_CM('Figure 30')}

    So combining $K^B_{{GE}}$ and $\Delta C_{{m_{{GE}}}}$ for the flaps 30 landing configuration we can see the change in 
    the $C_m$ versus $\alpha$ curves for varying values of $h/b$.

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ vs AoA', '$C_m$', 'Figure 31', scaled_version=False)}

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ vs AoA', '$C_m$', 'Figure 32', scaled_version=False, xlim=(-1, 16))}

    Plotting the results as a scale factor. 

    {plot_CM_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_m$ scaling vs AoA for flaps 30', 'Scale Factor', 'Figure 33', scaled_version=True)}

    Lastly for a set of fixed $\alpha$ values a plot of the $C_m$ scaling factor versus $h/b$ for a flaps 30 configuration.

    {plot_CM_groundeffect_AOA(30, [0, 5, 10, 14.5], '$C_m$ Scaling vs $h/b$ for flaps 30', 'Figure 34')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Airbus Generic Civil Transport Model

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

    {plot_airbus_delta_CL('Figure 35')}

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
    {plot_airbus_lift_plus_delta_ge('Figure 36')}

    {plot_airbus_lift_scaling('Figure 37')}

    {plot_airbus_lift_scaling_vs_hb('Figure 38')}
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
    plot_airbus_Cm_scaling_vs_hb,
    plot_airbus_basic_cm,
    plot_airbus_delta_Cm,
    plot_airbus_delta_Cm_alpha,
    plot_airbus_net_Cm,
    plot_airbus_net_Cm_scaling,
):
    mo.md(
        rf"""
    {plot_airbus_basic_cm('Figure 39')}

    {plot_airbus_delta_Cm('Figure 40')}

    {plot_airbus_delta_Cm_alpha('Figure 41')}

    {plot_airbus_net_Cm('Figure 42')}

    {plot_airbus_net_Cm_scaling('Figure 43')}

    {plot_airbus_Cm_scaling_vs_hb('Figure 44')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Summary

    Ground effect models need to model the change in lift, drag and pitching moment as the aircraft transitions through
    the ground effect zone, typically when the aircraft's AGL is within a wingspan of the aircraft.
    """
    )
    return


@app.cell(hide_code=True)
def _(
    mo,
    plot_CL_groundeffect,
    plot_cl_comparison,
    plot_cl_comparison_jsbsim_airbus,
):
    mo.md(
        rf"""
    ### Lift

    At moderate angles of attack the lift is increased when in ground effect for the same angle of attack.

    However the critical/stall AoA is reduced in ground effect, and for **some** aircraft the maximum lift coefficient
    is also reduced.

    > The NTSB found that contradictory information existed in technical literature about the 
    maximum lift coefficient for airplanes in ground effect. Some sources indicated that the 
    maximum lift coefficient in ground effect was similar to that in free air (as apparently assumed 
    by FTE1),106 whereas other sources indicated that the maximum lift coefficient would be reduced 
    in ground effect. The NTSB determined, through conversations with Gulfstream, other 
    manufacturers, and the FAA, that the potential for the maximum lift coefficient in ground effect 
    to be reduced might not be recognized industry-wide. Given the results of Gulfstream‟s CFD 
    analysis and the findings of this accident investigation, it is clear that the maximum lift 
    coefficient for at least some airplanes could be reduced in ground effect and that assumptions to 
    the contrary could result in an overestimation of the stall AOA in ground effect and could 
    increase the risk of a stall in ground effect with little or no stall warning.

    > 106 -  For example, a peer-reviewed 2007 technical paper by an aerospace engineer (who was employed by a 
    different airplane manufacturer than Gulfstream) stated, “the aircraft in ground effect possesses a similar [maximum 
    lift coefficient] as in-flight, but the absolute AOA for stall has reduced.” 

    {mo.image("public/GroundEffect/GroundEffectLift.png", width=600, caption='Figure 45')}

    Note that as shown in figures 9 and 10 above for the Boeing model the Boeing lift curves in ground effect
    don't really match these generic lift curves in terms of the gradient of the $C_L$ vs alpha curve. The Boeing curves
    start out with a positive delta at 0 alpha, but have a lower gradient compared to the free air case, and therefore
    end up intersecting the free air curve round an alpha of ~12 deg. The ground effect curves do appear to lead to a 
    lower critical/stall AoA and lower maximum $C_L$, although unfortunately the Boeing data for the delta $C_L$ in 
    ground effect ends at 14 deg AoA.

    {plot_CL_groundeffect(30, [0.0, 0.1, 0.2, 0.3], '$C_L$ vs AoA', '$C_L$', 'Figure 10', scaled_version=False)}

    All three models, JSBSim's 737, Boeing's 747-100 and Airbus's generic airliner model the change in lift due to
    ground effect, however with varying levels of fidelity.

    |Model|$h/b$|AoA|Flap Configuration|
    |:--|:--|:--|:--|
    |JSBSim|Yes|No|No|
    |Airbus|Yes|No|No|
    |Boeing|Yes|Yes|Yes|

    JSBSim and Airbus don't make use of AoA to vary the amount of delta lift in ground effect. JSBSim also doesn't
    vary the amount of delta lift based on the flap configuration, nor does the Airbus model, although the Airbus model
    was specifically only designed for a single flap configuration.

    Whereas the Boeing model's delta lift in ground effect is a function of all 3, i.e. $\Delta C_L = f(h/b, AoA, Flaps)$.

    One parameter not taken into account by any of the three models is the vertical rate of the aircraft through the
    ground effect region.

    > Ground effects data can be obtained in the wind tunnel or in flight. In conventional wind-tunnel
    > ground effects testing, measurements are taken for a stationary
    > aircraft model at various fixed ground heights. The results are called static ground effects data.
    > Unfortunately, this static data simulates the aircraft flying near the ground at a constant altitude
    > rather than simulating the transient or dynamic effects of the aircraft descending through a given
    > altitude, termed "dynamic" ground effects.
    >
    > Ground-based techniques have proved successful in more closely duplicating dynamic effects by using
    > a model that moves toward a stationary or moving ground board in the wind tunnel, thereby simulating
    > the rate of descent. 

    The [Dynamic Ground Effects Flight Test of an F-15 Aircraft](https://ntrs.nasa.gov/api/citations/19950005778/downloads/19950005778.pdf) measured the change in ground effect
    based on the sink rate. Higher sink rates lower the increase in $C_L$ due to ground effect.

    In terms of comparing all three models on a single graph, the scaling effect on $C_L$ is compared for a single flap 
    configuration of flaps 30 for the Boeing 747 and at a particular AoA of 5 deg for the Boeing 747. A figure of 5 deg for
    the AoA for the Boeing model is chosen based on a typical AoA for the landing approach.

    {plot_cl_comparison('Figure 46')}

    The $C_L$ scale factor curves for the JSBSim and Airbus models are very similiar, particularly in terms of their shape,
    with the JSBSim model being more 'aggressive' in terms of the scale of the effect.

    Using the Airbus formula - $C_{{L_{{H}}}} e^{{- \lambda_L H_{{LG}}}}$ and the following parameters for JSBSim we can 
    match JSBSim's discretized scale factor curve:

    |Parameter|Airbus|JSBSim|
    |---------|------|------|
    |$C_{{L_{{H}}}}$|0.20|0.28|
    |$\lambda_L$|0.12|0.08|

    {plot_cl_comparison_jsbsim_airbus('Figure 47')}

    However the Boeing curve is quite a bit different, it's not a pure exponential curve over the full range.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, plot_jsbsim_boeing_CD_scaling_comparison):
    mo.md(
        rf"""
    ### Drag

    Only the JSBSim and Boeing models model the change in drag due to ground effect. I asked one of the authors of
    the Airbus model why they hadn't included the change in drag in their ground effect model:

    > indeed the longitudinal ground effects have not been considered here since their influence on the control design process remains negligible

    Their aim was to have a representative model for designing an autoland control system for handling large cross winds.

    The JSBSim model appears to use an exponential curve over it's full range, whereas the Boeing model 
    appears to be exponential from larger $h/b$ values down towards lower $h/b$ values but then has an 
    inflection point around about $h/b = 0.1$.

    {plot_jsbsim_boeing_CD_scaling_comparison('Figure 48')}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, plot_boeing_airbus_Cm_scaling_comparison):
    mo.md(
        rf"""
    ### Pitching Moment

    Only the Boeing and Airbus models model the change in pitching moment due to ground effect. The Airbus model
    uses an exponential curve over the full range, whereas the Boeing model starts off with an exponential curve
    at it's maximum $h/b$, but then has an inflection point as $h/b$ decreases.

    {plot_boeing_airbus_Cm_scaling_comparison('Figure 49')}
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
    import copy
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
def _():
    # Saved data for model comparisons
    jsbsim737_hbs = []
    jsbsim737_CD_scaling = []
    boeing747_hbs = []
    boeing747_CD_scaling = []

    airbus_Cm_hbs = []
    airbus_Cm_scaling = []
    boeing747_Cm_hbs = []
    boeing747_Cm_scaling = []
    return (
        airbus_Cm_hbs,
        airbus_Cm_scaling,
        boeing747_CD_scaling,
        boeing747_Cm_hbs,
        boeing747_Cm_scaling,
        boeing747_hbs,
        jsbsim737_CD_scaling,
        jsbsim737_hbs,
    )


@app.cell
def _(mo, plt):
    def plot_generic_xy(x, y, title, xlabel, ylabel, figure_no=None):

        fig, ax = plt.subplots(layout='constrained')

        ax.plot(x, y)

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if figure_no is not None:
            fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_generic_xy,)


@app.cell
def _(K_A_GE_data, K_B_GE_data, plot_K_GE):
    def plot_K_B_GE(figure_no):
        return plot_K_GE(K_B_GE_data, "$K^B_{GE}$", figure_no)

    def plot_K_A_GE(figure_no):
        return plot_K_GE(K_A_GE_data, "$K^A_{GE}$", figure_no)
    return plot_K_A_GE, plot_K_B_GE


@app.cell
def _(b, mo, plt):
    def plot_K_GE(data, ylabel, figure_no):
        fig, ax = plt.subplots(layout='constrained')

        ax.plot(data[:,1], data[:,0])
        ax.set_xlabel("Gear height above ground (ft)")
        secax = ax.secondary_xaxis('top', functions=(lambda x: x/b, lambda x: b*x))
        secax.set_xlabel("h/b")

        ax.set_ylabel(ylabel)
        ax.set_title("Ground Effect Height Factor")
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_K_GE,)


@app.cell
def _(basic_cl_data, plot_CL_versus_alpha):
    def plot_basic_CL(figure_no):
        return plot_CL_versus_alpha(basic_cl_data, [10, 20, 25, 30], 'Basic $C_L$ versus $\\alpha$', '$C_L$', figure_no)
    return (plot_basic_CL,)


@app.cell
def _(delta_cl_data, plot_CL_versus_alpha):
    def plot_delta_CL(figure_no):
        return plot_CL_versus_alpha(delta_cl_data, [10, 20, 25, 30], '$\\Delta C_{L_{GE}}$ versus $\\alpha$', '$\\Delta C_{L_{GE}}$', figure_no)
    return (plot_delta_CL,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CL_versus_alpha(data, flaps, title, ylabel, figure_no):

        fig, ax = plt.subplots(layout='constrained')

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        fig.supxlabel(figure_no)

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
    def plot_CL_groundeffect(flap, h_bs, title, ylabel, figure_no, scaled_version, xlim=None):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)
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
    def plot_CL_groundeffect_AOA(flap, alphas, title, figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CL_groundeffect_AOA,)


@app.cell
def _(basic_cd_data, plot_CD_versus_alpha):
    def plot_basic_CD(figure_no):
        return plot_CD_versus_alpha(basic_cd_data, [10, 20, 25, 30], 'Basic $C_D$ versus $\\alpha$', '$C_D$', figure_no)
    return (plot_basic_CD,)


@app.cell
def _(delta_cd_data, plot_CD_versus_alpha):
    def plot_delta_CD(figure_no):
        return plot_CD_versus_alpha(delta_cd_data, [10, 20, 25, 30], '$\\Delta C_{D_{GE}}$ versus $\\alpha$', '$\\Delta C_{D_{GE}}$', figure_no)
    return (plot_delta_CD,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CD_versus_alpha(data, flaps, title, ylabel, figure_no):

        fig, ax = plt.subplots(layout='constrained')

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        fig.supxlabel(figure_no)

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
    def plot_CD_groundeffect(flap, h_bs, title, ylabel, figure_no, scaled_version, xlim=None):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)
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
    boeing747_CD_scaling,
    boeing747_hbs,
    delta_cd_data,
    flaps_data_index,
    mo,
    np,
    plt,
):
    def plot_CD_groundeffect_AOA(flap, alphas, title, figure_no):

        fig, ax = plt.subplots(layout='constrained')

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

            # Record for comparison with other models
            if alpha == 5:
                boeing747_hbs.clear()
                boeing747_CD_scaling.clear()
                for hb in hbs:
                    boeing747_hbs.append(hb)
                for scale in alpha_scale:
                    boeing747_CD_scaling.append(scale)

        ax.set_title(title)
        ax.set_ylabel('Scale Factor')
        ax.set_xlabel('$h/b$')
        fig.supxlabel(figure_no)
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CD_groundeffect_AOA,)


@app.cell
def _(basic_cm_data, plot_CM_versus_alpha):
    def plot_basic_CM(figure_no):
        return plot_CM_versus_alpha(basic_cm_data, [10, 20, 25, 30], 'Basic $C_m$ versus $\\alpha$', '$C_m$', figure_no)
    return (plot_basic_CM,)


@app.cell
def _(delta_cm_data, plot_CM_versus_alpha):
    def plot_delta_CM(figure_no):
        return plot_CM_versus_alpha(delta_cm_data, [10, 20, 25, 30], '$\\Delta C_{m_{GE}}$ versus $\\alpha$', '$\\Delta C_{m_{GE}}$', figure_no)
    return (plot_delta_CM,)


@app.cell
def _(flaps_data_index, flaps_label, mo, plt):
    def plot_CM_versus_alpha(data, flaps, title, ylabel, figure_no):

        fig, ax = plt.subplots(layout='constrained')

        for flap_setting in flaps:
            ax.plot(data[:,0], data[:,flaps_data_index(flap_setting)], label=flaps_label(flap_setting))

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        fig.supxlabel(figure_no)

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
    def plot_CM_groundeffect(flap, h_bs, title, ylabel, figure_no, scaled_version, xlim=None):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)
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
    boeing747_Cm_hbs,
    boeing747_Cm_scaling,
    delta_cm_data,
    flaps_data_index,
    mo,
    np,
    plt,
):
    def plot_CM_groundeffect_AOA(flap, alphas, title, figure_no):

        fig, ax = plt.subplots(layout='constrained')

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

            # Record for comparison with other models
            if alpha == 5:
                boeing747_Cm_hbs.clear()
                boeing747_Cm_scaling.clear()
                for hb in hbs:
                    boeing747_Cm_hbs.append(hb)
                for scale in alpha_scale:
                    boeing747_Cm_scaling.append(scale)

        ax.set_title(title)
        ax.set_ylabel('Scale Factor')
        ax.set_xlabel('$h/b$')
        fig.supxlabel(figure_no)
        ax.legend()

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_CM_groundeffect_AOA,)


@app.cell
def _(mo, np, plt):
    def plot_airbus_delta_CL(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_delta_CL,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_plus_delta_ge(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_lift_plus_delta_ge,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_scaling(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_lift_scaling,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_lift_scaling_vs_hb(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")     
    return (plot_airbus_lift_scaling_vs_hb,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_basic_cm(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        cm_0 = -0.3
        cm_alpha = -1.5 / math.degrees(1)

        alphas = np.linspace(0, 14, 3)
        cms = cm_0 + cm_alpha*alphas

        ax.plot(alphas, cms)

        ax.set_xlabel('Alpha $\\alpha$ (deg)')
        ax.set_ylabel('$C_m$')
        plt.title('Basic $C_m$ versus $\\alpha$')
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_basic_cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_delta_Cm(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_airbus_delta_Cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_delta_Cm_alpha(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_delta_Cm_alpha,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_net_Cm(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")    
    return (plot_airbus_net_Cm,)


@app.cell
def _(math, mo, np, plt):
    def plot_airbus_net_Cm_scaling(figure_no):

        fig, ax = plt.subplots(layout='constrained')

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
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}") 
    return (plot_airbus_net_Cm_scaling,)


@app.cell
def _(airbus_Cm_hbs, airbus_Cm_scaling, math, mo, np, plt):
    def plot_airbus_Cm_scaling_vs_hb(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        b = 60.3  # A-330 wingspan
        cm_0 = -0.3
        cm_alpha = -1.5 / math.degrees(1)
        cm_h0 = -0.09
        cm_halpha = -0.9 / math.degrees(1)
        lambda_m = 0.15    

        hbs = np.linspace(0, 0.4, 20)

        for alpha in [0, 5, 10, 14.5]:
            cm_scale_factor = []
            cm_free = cm_0 + cm_alpha * alpha
            for hb in hbs:
                hlg = b * hb          
                cm_ge = cm_free + (cm_h0 + cm_halpha * alpha) * np.exp(-lambda_m * hlg)
                cm_scaling = cm_ge / cm_free
                cm_scale_factor.append(cm_scaling)
            ax.plot(hbs, cm_scale_factor, label=f'$\\alpha$ = {alpha}')

            # Record for comparison with other models
            airbus_Cm_hbs.clear()
            airbus_Cm_scaling.clear()
            for hb in hbs:
                airbus_Cm_hbs.append(hb)
            for scale in cm_scale_factor:
                airbus_Cm_scaling.append(scale)

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_m$ scaling vs $h/b$')
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}") 
    return (plot_airbus_Cm_scaling_vs_hb,)


@app.cell
def _(
    K_B_GE_data,
    basic_cl_data,
    delta_cl_data,
    flaps_data_index,
    jsbsim737_kCLge_data,
    math,
    mo,
    np,
    plt,
):
    def plot_cl_comparison(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        # JSBSim
        ax.plot(jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1], label='JSBSim')

        # Airbus
        b = 60.3  # A-330 wingspan
        clh = 0.2
        lambdal = 0.12 
        cl0 = 0.9
        clalpha = 5.5 / math.degrees(1)    
        alpha = 5
        hbs = np.linspace(0, 1, 50)
        hlg = b * hbs
        delta_cl = clh * np.exp(-lambdal * hlg)      
        cl_base = cl0 + clalpha*alpha
        cl_scaling = (delta_cl + cl_base) / cl_base
        ax.plot(hbs, cl_scaling, label='Airbus')    

        # Boeing
        alpha = 5
        flap = 30
        cl_basic = np.interp(alpha, basic_cl_data[:,0], basic_cl_data[:,flaps_data_index(flap)])
        cl_delta = np.interp(alpha, delta_cl_data[:,0], delta_cl_data[:,flaps_data_index(flap)])
        alpha_scale = []
        hbs = np.linspace(0, 1.0, 50)
        for hb in hbs:
            kge = np.interp(hb * b, np.flip(K_B_GE_data[:,1]), np.flip(K_B_GE_data[:,0]))
            scale = (cl_basic + kge * cl_delta) / cl_basic
            alpha_scale.append(scale)
        ax.plot(hbs, alpha_scale, label='Boeing')    

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_L$ Scaling Comparison')
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")         
    return (plot_cl_comparison,)


@app.cell
def _(jsbsim737_kCLge_data, math, mo, np, plt):
    def plot_cl_comparison_jsbsim_airbus(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        # JSBSim
        ax.plot(jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1], label='JSBSim', linestyle='--')

        # Airbus
        b = 60.3  # A-330 wingspan
        #clh = 0.2
        #lambdal = 0.12 
        clh = 0.28
        lambdal = 0.08
        cl0 = 0.9
        clalpha = 5.5 / math.degrees(1)    
        alpha = 5
        hbs = np.linspace(0, 1, 50)
        hlg = b * hbs
        delta_cl = clh * np.exp(-lambdal * hlg)      
        cl_base = cl0 + clalpha*alpha
        cl_scaling = (delta_cl + cl_base) / cl_base
        ax.plot(hbs, cl_scaling, label='Airbus Formula')      

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_L$ Scaling Comparison')
        fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")  
    return (plot_cl_comparison_jsbsim_airbus,)


@app.cell
def _(
    jsbsim737_CD_scaling,
    jsbsim737_hbs,
    jsbsim737_kCDge_data,
    jsbsim737_kCLge_data,
    math,
    mo,
    np,
    plt,
):
    def plot_jsbsim_CD_scaling(figure_no=None):

        fig, ax = plt.subplots(layout='constrained')

        for alpha in [0, 5, 10, 13]:
            hbs = np.linspace(0, 0.8, 30)
            cl_clear = np.interp(alpha, [0, math.degrees(0.23)], [0.2, 1.2])
            cd_basic = np.interp(alpha, [0, math.degrees(0.26)], [0.021, 0.042])
            cdi_clear = cl_clear**2 * 0.043
            cd_flap = 0.059
            cd_total_clear = cd_basic + cdi_clear + cd_flap

            scale_factors = []
            for hb in hbs:
                kCLge = np.interp(hb, jsbsim737_kCLge_data[:,0], jsbsim737_kCLge_data[:,1])
                cl_ge = np.interp(alpha, [0, math.degrees(0.23)], [0.2, 1.2]) * kCLge
                kCDge = np.interp(hb, jsbsim737_kCDge_data[:,0], jsbsim737_kCDge_data[:,1])
                cdi_ge = cl_ge**2 * 0.043 * kCDge
                cd_total_ge = cd_basic + cdi_ge + cd_flap
                scale_factors.append(cd_total_ge/cd_total_clear)

            # Record alpha == 5 case for comparison with other models
            if alpha == 5:
                jsbsim737_hbs.clear()
                jsbsim737_CD_scaling.clear()
                for hb in hbs:
                    jsbsim737_hbs.append(hb)
                for scale in scale_factors:
                    jsbsim737_CD_scaling.append(scale)
                    #jsbsim737_CD_scaling = copy.deepcopy(scale_factors)

            ax.plot(hbs, scale_factors, label=f'$\\alpha$ = {alpha}')

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('JSBSim $C_D$ Scaling versus $h/b$')    

        if figure_no is not None:
            fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_jsbsim_CD_scaling,)


@app.cell
def _(
    boeing747_CD_scaling,
    boeing747_hbs,
    jsbsim737_CD_scaling,
    jsbsim737_hbs,
    mo,
    plt,
):
    def plot_jsbsim_boeing_CD_scaling_comparison(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        ax.plot(jsbsim737_hbs, jsbsim737_CD_scaling, label='JSBSim')
        ax.plot(boeing747_hbs, boeing747_CD_scaling, label='Boeing')

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_D$ Scaling Comparison at $\\alpha$ = 5')    

        if figure_no is not None:
            fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_jsbsim_boeing_CD_scaling_comparison,)


@app.cell
def _(
    airbus_Cm_hbs,
    airbus_Cm_scaling,
    boeing747_Cm_hbs,
    boeing747_Cm_scaling,
    mo,
    plt,
):
    def plot_boeing_airbus_Cm_scaling_comparison(figure_no):

        fig, ax = plt.subplots(layout='constrained')

        ax.plot(airbus_Cm_hbs, airbus_Cm_scaling, label='Airbus')
        ax.plot(boeing747_Cm_hbs, boeing747_Cm_scaling, label='Boeing')

        ax.legend()
        ax.set_xlabel('$h/b$')
        ax.set_ylabel('Scale Factor')
        plt.title('$C_m$ Scaling Comparison at $\\alpha$ = 5')    

        if figure_no is not None:
            fig.supxlabel(figure_no)

        return mo.md(f"{mo.as_html(fig)}")
    return (plot_boeing_airbus_Cm_scaling_comparison,)


if __name__ == "__main__":
    app.run()
