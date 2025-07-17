import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Climb Performance""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## TECS Trigger

    A [Facebook post](https://www.facebook.com/share/p/1VcBovxhNS/) by Agostino De Marco regarding an optimal time to 
    climb profile making use of an autopilot based on the Total Energy Control System (TECS) triggered my interest in 
    the topic of climb performance.

    {mo.image('public/ClimbPerformance/TECSROC.jpg')}

    I asked how the contour plot of rate of climb (ROC) against altitude and airspeed was generated:

    > You trim the model for those "operating points" in level flight. For each point you calculate the maximum excess thrust and maximum excess power w.r.t. the level-flight required values. Those quantities divided by A/C weight give you the maximum attainable flight path angle and RoC.

    Lastly Agostino mentioned that:

    > another interesting fact emerging from this max-RoC tracking simulation is that, while climbing, the max performance condition is perfectly pursued; yet this optimal climb is achieved by an energy-based MIMO control known as TECS, with **no need to push the throttle setting to its max**. A nice combination of elevator and throttle laws does the job nicely.

    Let's take a look at the basic climb performance theory and use JSBSim to test and compare the results with the theory and then look
    at the TECS based max-ROC autopilot performance.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## Theory

    For a steady/non-accelerating climb.

    {mo.image('public/ClimbPerformance/AnglesForces.png', width=400)}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    \begin{align}
    T - D - W \sin \theta &= 0  \tag{1} \\
    \nonumber \\
    L - W \cos \theta &= 0  \tag{2}
    \end{align}
    $$

    The vertical component of the velocity is the **rate of climb** ($R/C$) of the aircraft.

    $$
    \begin{align}
    R/C &= V_{\infty} \sin \theta  \tag{3} \\
    \nonumber \\
    V_{\infty} \sin \theta = R/C &= \frac{T V_{\infty} - D V_{\infty}}{W}  \tag{4} \\
    \nonumber \\
    Excess\ Power &= T V_{\infty} - D V_{\infty}  \tag{5}
    \end{align}
    $$

    **Question:** Assumption appears to be that $\alpha$ is very small so $\theta \approx \gamma$?

    The power required, $P_R$, which is equal to $DV_\infty$, for level flight at a particular 
    altitude is calculated for and plotted against a range of true airspeeds $V_\infty$. 
    The maximum power available, $P_A$, which is equal to $TV_\infty$ at the particular altitude 
    is also plotted against $V_\infty$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""{mo.image('public/ClimbPerformance/ExcessPowerPropellor.png', width=400)}""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$R/C = \frac{Excess\ Power}{W}  \tag{6}$$

    The true airspeed at which the maximum rate of climb occurs for a particular altitude, $V_{{(R/C)_{max}}}$, 
    occurs at the airspeed where excess power is a maximum.

    For a jet engine the thrust is essentially constant with velocity, therefore the power available, $P_A$ has a linear
    relationship to $V_\infty$ resulting in the following graph.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""{mo.image('public/ClimbPerformance/ExcessPowerJet.png', width=400)}""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ### Hodograph Diagram

    Is a plot of the aircraft's vertical velocity $V_V$ versus its horizontal velocity $V_H$. Consider an
    arbitary point on the hodograph curve, denoted by point 1. Draw a line from the origin to point 1.
    Geometrically, the length of the line is $V$, and the angle it makes with the horizontal axis is the
    corresponding climb angle at that velocity.

    Point 2 denotes the maximum $R/C$; the length of the line from the origin to point 2 is the aircraft's
    velocity at maxmum $R/C$ and the angle it makes with the horizontal axis is the climb angle for maximum $R/C$.

    A line drawn from the origin and tangent to the hodograph curve locates point 3. The angle of this line relative
    to the horizontal axis defines the maximum possible climb angle.

    {mo.image('public/ClimbPerformance/Hodograph.png', width=400)}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In aircraft flight manuals $V_{\theta_{max}}$ is typically denoted as $V_x$ and $V_{{(R/C)}_{max}}$ as $V_y$ after 
    being converted to IAS.

    So climbing at an airspeed of $V_x$ will give you the steepest climb possible, useful for clearing obstacles
    whereas climbing at an airspeed of $V_y$ will give you the fastest climb rate possible, both for a particular
    altitude, i.e. $V_x$ and $V_y$ will vary with altitude. Note $V_x$ and $V_y$ will be specified as CAS and not TAS.

    Another way of calulating the airspeed for the steepest climb is to plot thrust available $T_A$ versus true airspeed and
    drag/thrust required $T_R$ versus true airspeed for level flight. The airspeed at which $T_A - T_R$ is a maximum will
    determine the airspeed for the steepest climb. In other words using thrust as opposed to power.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Using JSBSim to Test and Compare

    We'll use the Boeing 737 model from the JSBSim repo.

    The thrust factor table for the 737's CFM56 jet engine based on density altitude and Mach shows
    that there is only a small variation in thrust based on velocity, so matching the assumption that
    thrust for a jet engine is essentialy constant with velocity.

    ```xml
      <function name="MilThrust">
       <table>
        <independentVar lookup="row">velocities/mach</independentVar>
        <independentVar lookup="column">atmosphere/density-altitude</independentVar>
        <tableData>
              -10000       0   10000   20000   30000   40000   50000   60000
         0.0   1.2600  1.0000  0.7400  0.5340  0.3720  0.2410  0.1490  0.0
         0.2   1.1710  0.9340  0.6970  0.5060  0.3550  0.2310  0.1430  0.0
         0.4   1.1500  0.9210  0.6920  0.5060  0.3570  0.2330  0.1450  0.0
         0.6   1.1810  0.9510  0.7210  0.5320  0.3780  0.2480  0.1540  0.0
         0.8   1.2580  1.0200  0.7820  0.5820  0.4170  0.2750  0.1700  0.0
         1.0   1.3690  1.1200  0.8710  0.6510  0.4750  0.3150  0.1950  0.0
         1.2   0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0
        </tableData>
       </table>
      </function>

    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_thrust_carpet):
    plot_thrust_carpet()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Thrust Data Setup and Calculation""")
    return


@app.cell
def _(np):
    # Setup thrust data for CFM56

    # Create a grid of mach and alt values
    mach = np.linspace(0, 1, 6)
    alt = np.linspace(0, 40000, 5)
    mach, alt = np.meshgrid(mach, alt)

    # Thrust values
    thrust = np.zeros(mach.shape)

    static_thrust = 40000  # lbf

    # From JSBSim's engine\CFM56.xml
    data = [
        [1.0,   0.934, 0.921, 0.951, 1.02,  1.12],   # 0ft
        [0.74,  0.697, 0.692, 0.721, 0.782, 0.871],  # 10,000ft
        [0.534, 0.506, 0.506, 0.532, 0.582, 0.651],  # 20,000ft
        [0.372, 0.355, 0.357, 0.378, 0.417, 0.475],  # 30,000ft
        [0.241, 0.231, 0.233, 0.248, 0.275, 0.315]   # 40,000ft
    ]

    # Populate thrust mesh
    for alt_index in range(len(data)):
        for mach_index in range(len(data[alt_index])):
            thrust[alt_index, mach_index] = data[alt_index][mach_index] * static_thrust
    return alt, mach, thrust


@app.cell
def _(RegularGridInterpolator, np, thrust):
    # Thrust lookup

    mach_grid = np.linspace(0, 1, 6)
    alt_grid = np.linspace(0, 40000, 5)

    # Create 2D interpolator
    thrust_interpolator = RegularGridInterpolator((alt_grid, mach_grid), thrust)

    def max_thrust(alt, mach):
        return thrust_interpolator([[alt, mach]])[0]
    return (max_thrust,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Climb Performance Routine

    Using the 737 JSBSim model, for a given altitude and a range of airspeeds we'll use JSBSim to trim the aircraft
    for level flight at the given altitude. Then query JSBSim for the drag at the trim point. Using the Mach
    value returned by JSBSim and the `max_thrust(alt, mach)` routine the thrust available can be calculated.

    Using the TAS for the trim point, the drag and thrust available, the power required and power available can
    then be calculated.

    Lastly using equation $(6)$ the ROC can then be calculated:


    $$R/C = \frac{Excess\ Power}{W}  \tag{6}$$

    |Return Parameters per airspeed trim point|
    |------------------------------|
    |TAS (kt)|
    |Mach|
    |CAS (kt)|
    |Drag (lbf)|
    |Thrust Available (lbf)|
    |Power Required ($\mathrm {ft} \, \mathrm {lbf} / \mathrm s$)|
    |Power Available ($\mathrm {ft} \, \mathrm {lbf} / \mathrm s$)|
    |ROC (fps)|
    """
    )
    return


@app.cell
def _(jsbsim, math, max_thrust, np):
    # For a given altitude and TAS range
    # Return np array of tuples - (tas, mach, cas, drag, thrust_avail, power_required, power_avail, roc)

    kt2fps = 1.687664

    def sim_climb(minTAS, maxTAS, altitude):

        AIRCRAFT_NAME="737"
        # Path to JSBSim files, location of the folders "aircraft", "engines" and "systems"
        PATH_TO_JSBSIM_FILES="data/jsbsim"

        # Avoid flooding the console with log messages
        jsbsim.FGJSBBase().debug_lvl = 0

        fdm = jsbsim.FGFDMExec(PATH_TO_JSBSIM_FILES)

        # Load the aircraft model
        fdm.load_model(AIRCRAFT_NAME)

        # Set engines running
        fdm['propulsion/set-running'] = -1

        # Set alpha range for trim solutions
        fdm['aero/alpha-max-rad'] = math.radians(12)
        fdm['aero/alpha-min-rad'] = math.radians(-8.0)

        # Range of airspeeds (TAS)
        airspeeds = np.linspace(minTAS, maxTAS, 50)

        result = []

        for airspeed in airspeeds:
            fdm['ic/h-sl-ft'] = altitude
            fdm['ic/gamma-deg'] = 0       # Level trim
            fdm['ic/vt-kts'] = airspeed   # TAS
            fdm.run_ic()

            try:
                fdm['simulation/do_simple_trim'] = 1

                mach = fdm['velocities/mach']
                cas = fdm['velocities/vc-kts']
                weight = fdm['inertia/weight-lbs']
                drag = fdm['forces/fwx-aero-lbs']
                thrust_avail = max_thrust(altitude, mach)

                power_avail = thrust_avail * airspeed * kt2fps
                power_required = drag * airspeed * kt2fps
                roc = (power_avail - power_required) / weight

                result.append((airspeed, mach, cas, drag, thrust_avail, power_required, power_avail, roc))

            except jsbsim.TrimFailureError:
                pass  # Ignore trim failures        

        return np.array(result)
    return kt2fps, sim_climb


@app.cell
def _(mo, sim_climb):
    # Calculate climb performance data using JSBSim for various altitudes.
    # JSBSim used to trim for level flight for thrust required and power required.

    # Supress stdout messages about expected trim failures
    with mo.redirect_stdout():

        minTAS = 150
        maxTAS = 550

        sim_results = {
            0     : sim_climb(minTAS, maxTAS, 150),  # 150ft out of ground effect
            10000 : sim_climb(minTAS, maxTAS, 10000),  
            20000 : sim_climb(minTAS, maxTAS, 20000),
            30000 : sim_climb(minTAS, maxTAS, 30000)
        }
    return maxTAS, minTAS, sim_results


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Thrust Available vs Thrust Required Results""")
    return


@app.cell(hide_code=True)
def _(plot_thrust_difference):
    plot_thrust_difference()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Power Available vs Power Required Results

    Unlike in the example power graph from the theory section these don't have the $P_R$ and $P_A$ curves intersecting
    on the low speed side.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_power_difference):
    plot_power_difference()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Question:** Should JSBSim's trim routines be able to generate more level trim solutions on the high
    speed and particularly low speed portions of the envelope in order for $P_R$ and $P_A$ to intersect? Looks
    like on the low speed end the trim routine is running into a limit with the maximum AoA available at $C_{L_{max}}$.
    A flaps down configuration would probably result in an intersection.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ### ROC Results

    Rate of climb for 4 different altitudes with the airspeed (TAS) for maximum ROC displayed as a dashed line.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_roc):
    plot_roc()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""ROC for different altitudes displayed on a combined graph.""")
    return


@app.cell(hide_code=True)
def _(plot_roc_combined):
    plot_roc_combined()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Hodograph Results

    In the **ROC Results** section above the plot of ROC is against $V_\infty$, whereas for a Hodograph it is ROC ($V_V$)
    against $V_H$.

    **Question:** Hmm, given the need for the x and y axes to have the same scale in order for the vector lengths to work and angles,
    these Hodographs are not as easy to read compared to the example in the theory section.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_hodograph):
    plot_hodograph()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ### Trimmed for Maximum ROC

    Previously I'd used JSBSim in order to generate a [Trim Envelope](https://seanmcleod70.github.io/FlightDynamicsCalcs/TrimEnvelope.html) for the 737 model at 15,000ft.

    {mo.image('public/ClimbPerformance/TrimEnvelope.svg')}

    It used a brute force approach of trying to calculate a trim solution at each airspeed across a range of 
    flight path angles $\gamma$ from +10 to -10 degrees. The graphs included information on the required amount
    of thrust as well as the AoA for the trim point.

    The maximum ROC for each airspeed can be calculated from these graphs by converting the airspeed into TAS from IAS
    and then using:

    $ROC = V_{{TAS}} \sin \gamma$

    So for comparison to the graphs generated above showing ROC versus TAS using excess power and weight to calculate the
    ROC we'll now use JSBSim's trim routine to work out a maximum ROC for each airspeed. Doing so by determining the maximum
    flight path angle $\gamma$ with a feasible trim solution, for each given airspeed. Making use of a bisection style
    loop.
    """
    )
    return


@app.cell
def _(maxTAS, minTAS, mo, trim_max_gamma_range):
    # Calculate climb performance data using JSBSim to find maximum gamma for feasible trim
    # for each airspeed at specified altitude.

    # Supress stdout messages about expected trim failures
    with mo.redirect_stdout():

        sim_climb_results = {
            0     : trim_max_gamma_range(minTAS, maxTAS, 150)  # 150ft out of ground effect
        }
    return (sim_climb_results,)


@app.cell(hide_code=True)
def _(plot_jsbsim_climb_trim_roc):
    plot_jsbsim_climb_trim_roc(0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There is a fairly close match between the graphs showing ROC vs TAS at sea level between the approach using
    excess power and the approach using JSBSim to calculate a trim climb solution for a maximum $\gamma$. With a 
    peak ROC from the JSBSim trimb climb solution of 97fps versus 104fps for the excess power calculation, i.e. 6.8% less.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_roc_excess_power_climb_trim_comparison):
    plot_roc_excess_power_climb_trim_comparison(0)  # Sea level
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        rf"""
    ## TECS

    Summary of TECS from Agostino's slide presentation at NODYCON 2025.

    {mo.image('public/ClimbPerformance/TECSSummary.png')}

    So the throttle controls the total energy available and the elevator conrtols how the energy available is split
    between an increase in kinetic energy and an increase in potential energy.

    So it seems counterintuitive that you could climb at max ROC with the throttle at less than 100%. Since if the aircraft
    was at the optimal climb speed, i.e. no need for an increase in kinetic energy surely any excess energy over and above
    what the throttle was supplying at less than 100% could be turned into an increase in potential energy, i.e. to increase the
    ROC?

    Also in terms of the climb theory above less than 100% thrust will result in lower excess power and therefore a lower
    ROC.

    I've digitized the following plots to compare the ROC from the TECS based autopilot with the ROC values calculated for
    the contour plot of ROC versus airspeed and altitude, which is based on excess power divided by weight.

    {mo.image('public/ClimbPerformance/TECSROCDigitized.png')}

    |Altitude|Throttle|ROC      |Contour Plot ROC|ROC Factor|
    |--------|--------|---------|----------------|----------|
    |0 ish   | 78%    | 18.9m/s | > 22m/s | < 86% |
    |2000m   | 78%    | 17.5m/s | 20m/s   | 86% |
    |4000m   | 75%    | 14.0m/s | 16m/s   | 88% |
    |6000m   | 78%    | 10.8m/s | 12.5m/s | 86% |
    |8000m   | 60%    | 8.0m/s  | 9.5m/s  | 84% |
    |10,000m | 64%    | 5.5m/s  | 6.5m/s  | 85% |

    So for each of the data points the ROC achieved by the TECS based autopilot is ~15% less than the ROC
    indicated on the contour plot.

    The TECS based autopilot followed the velocity setpoint fairly accurately to climb at the optimal airspeed
    to maximize the ROC as defined by the coontour plots for the specific altitude.

    {mo.image('public/ClimbPerformance/TECSVelocityTracking.png')}

    However, even though the aircraft was flying at the optimal speed given the reduced thrust below 100% of the
    available thrust it would appear that the aircraft didn't attain the maximum ROC at each point along it's climb, 
    as defined by the contour plots. Presumumably climbing at a shallower flight path angle than the flight path angle required to achieve the maximum ROC.

    So was this climb by the TECS based autopilot really achieving an optimal climb, in terms of minimum time to the
    set-point altitude? If the throttle had been fixed at 100% during the climb wouldn't it have achieved a quicker time
    to altitude?

    In terms of an optimal climb to altitude how achievable is it to exactly match the optimal climb profile based on 
    the contour plot generated using the excess power calculation?

    Firstly in terms of the difference in ROC performance between the excess power calculation and the trim climb 
    approach, even with the trim climb approach always using pretty much 100% throttle.

    **Question-** Explanation for the difference in performance?

    Secondly even if the aircraft could be trimmed at each altitude at the airspeed for maximum ROC with 100% throttle
    there is often a need for the aircraft to increase it's kinetic energy in order to achieve the airspeed required for
    maximum ROC at a higher altitude. So based on the TECS reservoir analogy in order to increase the kinetic energy
    that means some of the total energy available will then be diverted from achieving the maximum ROC during this transition.

    For example these were the required TAS at increasing altitude in order to achieve the maximum ROC possible at
    each altitude based on the excess power calculation.

    |Altitude|TAS|
    |--------|---|
    |0ft     |330kt|
    |10,000ft|338kt|
    |20,000ft|346kt|
    |30,000ft|379kt|
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Plotting Functions""")
    return


@app.cell
def _(alt, mach, np, plt, thrust):
    def plot_thrust_carpet():
        # Create a 3D plot
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface
        surface = ax.plot_surface(mach, alt, thrust/1000, cmap='viridis', edgecolor='red')

        # Flip axes
        ax.set_ylim([45000, 0])
        ax.set_xlim([1.05, -0.05])

        ax.yaxis.set_ticks(np.arange(0, 40001, 10000))

        # Set labels
        ax.set_xlabel('Mach')
        ax.set_ylabel('Altitude (ft)')
        ax.set_zlabel('Thrust (k lbf)')

        # Show the plot
        #mo.mpl.interactive(plt.gca())
        return plt.gca()
    return (plot_thrust_carpet,)


@app.cell
def _(np, plt, sim_results):
    def plot_roc():
        fig = plt.figure(figsize=(16,4))
        axes = fig.subplots(1, 4)

        for i in range(4):
            altitude = i*10000
            sim_data = sim_results[altitude]
            axes[i].plot(sim_data[:,0], sim_data[:,7])
            roc_max_index = np.argmax(sim_data[:,7])
            v_roc_max = sim_data[:,0][roc_max_index]
            max_roc = sim_data[:,7][roc_max_index]
            axes[i].axvline(x=v_roc_max, color='red', linestyle='--', linewidth=2)
            axes[i].set_xlabel('TAS (kt)')
            axes[i].set_ylabel('ROC (fps)')
            axes[i].set_title(f'ROC - {altitude}ft')

        return plt.gca()
    return (plot_roc,)


@app.cell
def _(np, plt, sim_results):
    def plot_roc_combined():
        plt.figure(figsize=(12, 8))

        for i in range(4):
            altitude = i*10000
            sim_data = sim_results[altitude]
            plt.plot(sim_data[:,0], sim_data[:,7], label=f'{altitude}ft')
            roc_max_index = np.argmax(sim_data[:,7])
            v_roc_max = sim_data[:,0][roc_max_index]
            max_roc = sim_data[:,7][roc_max_index]
            plt.vlines(v_roc_max, 0, max_roc, color='red', linestyle='--', linewidth=2)
            plt.scatter(v_roc_max, max_roc, label=f'{max_roc:.0f}fps - {v_roc_max:.0f}kt')

        plt.title('ROC')
        plt.xlabel('TAS (kt)')
        plt.ylabel('ROC (fps)')
        plt.legend()

        return plt.gca()
    return (plot_roc_combined,)


@app.cell
def _(kt2fps, math, np, plt, sim_results):
    def plot_hodograph():
        figure, axes = plt.subplots(1, 4, figsize=(16, 4))

        for i in range(4):
            altitude = i*10000
            sim_data = sim_results[altitude]
            v_h = np.sqrt(sim_data[:,0]**2 - sim_data[:,7]**2) * kt2fps
            axes[i].plot(v_h, sim_data[:,7])

            roc_max_index = np.argmax(sim_data[:,7])
            v_roc_max = sim_data[:,0][roc_max_index] * kt2fps
            max_roc = sim_data[:,7][roc_max_index]
            v_h_roc_max = np.sqrt(v_roc_max**2 - max_roc**2)
            gamma = math.degrees(math.atan2(max_roc, v_h_roc_max))
            axes[i].scatter(v_h_roc_max, max_roc, label=f'R/C = {max_roc:.0f} $\gamma$ = {gamma:.1f}$^{{\circ}}$')

            axes[i].plot([0, v_h_roc_max], [0, max_roc])

            axes[i].set_xlim([0, 550*kt2fps])
            axes[i].set_ylim([0, 550*kt2fps])

            axes[i].set_xlabel('$V_H$ (fps)')
            axes[i].set_ylabel('ROC $V_V$ (fps)')
            axes[i].set_title(f'Hodograph - {altitude}ft')
            axes[i].legend()

        return plt.gca()
    return (plot_hodograph,)


@app.cell
def _(np, plt, sim_results):
    def plot_power_difference():
        figure, axes = plt.subplots(1, 4, figsize=(16, 4))

        for i in range(4):
            altitude = i*10000
            sim_data = sim_results[altitude]
            axes[i].plot(sim_data[:,0], sim_data[:,5], label='$P_R$')
            axes[i].plot(sim_data[:,0], sim_data[:,6], label='$P_A$')

            # Calculate max excess
            max_excess_index = np.argmax(sim_data[:,6] - sim_data[:,5])
            max_excess_v  = sim_data[:,0][max_excess_index]
            max_excess_pr = sim_data[:,5][max_excess_index]
            max_excess_pa = sim_data[:,6][max_excess_index]

            axes[i].vlines(max_excess_v, max_excess_pr, max_excess_pa, color='red', linestyle='--', linewidth=2)

            axes[i].set_xlabel('TAS (kt)')
            axes[i].set_ylabel('Power')
            axes[i].set_title(f'Power - {altitude}ft')
            axes[i].legend()

        return plt.gca()
    return (plot_power_difference,)


@app.cell
def _(np, plt, sim_results):
    def plot_thrust_difference():
        figure, axes = plt.subplots(1, 4, figsize=(16, 4))

        for i in range(4):
            altitude = i*10000
            sim_data = sim_results[altitude]
            axes[i].plot(sim_data[:,0], sim_data[:,3]/1000, label='$T_R$')
            axes[i].plot(sim_data[:,0], sim_data[:,4]/1000, label='$T_A$')

            # Calculate max excess
            max_excess_index = np.argmax(sim_data[:,4] - sim_data[:,3])
            max_excess_v  = sim_data[:,0][max_excess_index]
            max_excess_tr = sim_data[:,3][max_excess_index]/1000
            max_excess_ta = sim_data[:,4][max_excess_index]/1000

            axes[i].vlines(max_excess_v, max_excess_tr, max_excess_ta, color='red', linestyle='--', linewidth=2)

            axes[i].set_xlabel('TAS (kt)')
            axes[i].set_ylabel('Thrust (k lbf)')
            axes[i].set_title(f'Thrust - {altitude}ft')
            axes[i].legend()

        return plt.gca()
    return (plot_thrust_difference,)


@app.cell
def _(jsbsim, kt2fps, math, np):
    # Use JSBSim trim routine using a bisection style loop to determine the maximum flight path
    # angle for a valid trim solution

    def trim(fdm, alt, TAS, gamma):
        fdm['ic/h-sl-ft'] = alt
        fdm['ic/vt-kts'] = TAS
        fdm['ic/gamma-deg'] = gamma

        # Initialize the aircraft with initial conditions
        fdm.run_ic()

        # Trim
        try:
            fdm['simulation/do_simple_trim'] = 1
            return (gamma, fdm['fcs/throttle-cmd-norm[0]'], fdm['aero/alpha-deg'])
        except jsbsim.TrimFailureError:
            return None

    def trim_max_gamma(fdm, alt, TAS):
        # Assume absolute max gamma is 20
        max_gamma = 20
        min_gamma = 0
        last_trim = trim(fdm, alt, TAS, min_gamma)
        if last_trim is None:
            return None

        level_alpha = last_trim[2]
        level_throttle = last_trim[1]
        last_gamma = min_gamma
        next_gamma = 20

        # Bisection loop
        for i in range(15):
            current_trim = trim(fdm, alt, TAS, next_gamma)
            if current_trim is None:
                next_gamma = (next_gamma + last_gamma)/2
            else:
                last_trim = current_trim
                last_gamma = next_gamma
                next_gamma = (next_gamma + max_gamma)/2

        return last_trim + (level_alpha, level_throttle,)

    def trim_max_gamma_range(min_TAS, max_TAS, alt):
        AIRCRAFT_NAME="737"
        # Path to JSBSim files, location of the folders "aircraft", "engines" and "systems"
        PATH_TO_JSBSIM_FILES="data/jsbsim"

        # Avoid flooding the console with log messages
        jsbsim.FGJSBBase().debug_lvl = 0

        fdm = jsbsim.FGFDMExec(PATH_TO_JSBSIM_FILES)

        # Load the aircraft model
        fdm.load_model(AIRCRAFT_NAME)

        # Set engines running
        fdm['propulsion/set-running'] = -1

        # Set alpha range for trim solutions
        fdm['aero/alpha-max-rad'] = math.radians(12)
        fdm['aero/alpha-min-rad'] = math.radians(-4.0)

        results = []

        for tas in np.linspace(min_TAS, max_TAS, 50):
            trim_data = trim_max_gamma(fdm, alt, tas)
            if trim_data is not None:
                gamma, throttle, alpha, level_alpha, level_throttle = trim_data
                roc = (tas*kt2fps)*math.sin(math.radians(gamma))
                results.append((tas, gamma, roc, throttle, level_throttle, alpha, level_alpha))

        return np.array(results)

    return (trim_max_gamma_range,)


@app.cell
def _(np, plt, sim_climb_results):
    def plot_jsbsim_climb_trim_roc(alt):
        figure, axes = plt.subplots(1, 4, figsize=(16, 4))

        results = sim_climb_results[alt]
    
        axes[0].plot(results[:,0], results[:,2])
        axes[1].plot(results[:,0], results[:,1])
        axes[2].plot(results[:,0], results[:,3], label='Climb')
        axes[2].plot(results[:,0], results[:,4], label='Level', linestyle='--')
        axes[3].plot(results[:,0], results[:,5], label='Climb')
        axes[3].plot(results[:,0], results[:,6], label='Level', linestyle='--')

        roc_max_index = np.argmax(results[:,2])
        v_roc_max = results[:,0][roc_max_index]
        max_roc = results[:,2][roc_max_index]
        max_gamma = results[:,1][roc_max_index]

        for i in range(4):
            axes[i].axvline(x=v_roc_max, color='red', linestyle='--', linewidth=2)

        axes[0].scatter(v_roc_max, max_roc, label=f'R/C = {max_roc:.0f}')
        axes[1].scatter(v_roc_max, max_gamma, label=f'$\\gamma$ = {max_gamma:.0f}')
    
        yaxes_info = [ 'ROC (fps)', 'Gamma $\\gamma$', 'Throttle', 'AoA $\\alpha$' ]

        for i in range(len(axes)):
            axes[i].set_xlabel('TAS (kt)')
            axes[i].set_ylabel(yaxes_info[i])
            axes[i].set_title('Altitude 0ft')
            axes[i].legend()
    
        return plt.gca()
    return (plot_jsbsim_climb_trim_roc,)


@app.cell
def _(plt, sim_climb_results, sim_results):
    # Plot comparison of ROC from excess power calculation versus from max climb trim solution

    def plot_roc_excess_power_climb_trim_comparison(alt):
        figure, axes = plt.subplots(1, 2, figsize=(16, 8))

        climb_trim_tas = sim_climb_results[alt][:,0]
        climb_trim_roc = sim_climb_results[alt][:,2]

        power_tas = sim_results[alt][:,0]
        power_roc = sim_results[alt][:,7]
    
        axes[0].plot(climb_trim_tas, climb_trim_roc, label='Climb Trim')
        axes[0].plot(power_tas, power_roc, label='Excess Power')

        axes[1].plot(climb_trim_tas, climb_trim_roc/power_roc)

        for axis in axes:
            axis.set_xlabel('TAS (kt)')
            axis.set_title(f'Altitude {alt}ft')

        axes[0].set_ylabel('ROC (fps)')
        axes[0].legend()
        axes[1].set_ylabel('Climb Trim ROC / Excess Power ROC')
    
        return plt.gca()
    return (plot_roc_excess_power_climb_trim_comparison,)


@app.cell
def _(max_thrust):
    # 2D interpolation thrust lookup test
    max_thrust(15000, 0.3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## References

    Most of the theory section in this notebook comes from the SRM class notes reference.

    [SRM Institute of Science and Technology - Class Notes](https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/downloads/class12-2012.pdf)

    [MSc thesis - Aircraft Flight Control: Advancing Towards Human-Like Behavior (Leonardo Molino)]()

    [Energy-based Multiple-Input-Multiple-Output nonlinear control of fixed-wing aircraft (Leonardo Molino, Agostino De Marco, Sabato Manfredi)](https://www.linkedin.com/posts/agostino-de-marco-08398a7_presentation-by-de-marco-et-al-nodycon-2025-activity-7343309822525607937-opP5?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAbR04BVZw2ZGYntq-M24BwQiSJ1KHuRiQ)

    #### TECS

    [Integrated Autopilot/Autothrottle Based on a Total Energy Control Concept: Design and Evaluation 
    of Additional Autopilot Modes](https://ntrs.nasa.gov/api/citations/19880010924/downloads/19880010924.pdf)

    [NASA B737 Flight Test Results of the Total Energy Control System](https://ntrs.nasa.gov/api/citations/19870017485/downloads/19870017485.pdf)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Imports""")
    return


@app.cell
def _():
    import marimo as mo

    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from scipy.interpolate import RegularGridInterpolator
    import jsbsim
    return RegularGridInterpolator, jsbsim, math, mo, np, plt


if __name__ == "__main__":
    app.run()
