# Flight Dynamics Calcs
Calculations, simulations with JSBSim and write up with [marimo](https://marimo.io/) notebooks.

Static html snapshots of each marimo notebook can be found in the `docs` directory and via Github
Pages at [Flight Dynamics Calcs](https://seanmcleod70.github.io/FlightDynamicsCalcs/).

## Roll Performance

#### [A4 Skyhawk Roll Performance](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/A4%20Skyhawk%20Roll%20Performance.py)
Can the A4 really roll at 720 deg/s or is it a tall tale? Using some aerodynamic data published by NASA let’s take a look.

#### [Fighter Roll Rates](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Fighter%20Roll%20Rates.py)
Comparing fighter roll rates based on published aerodynamic data.

## Aircraft Carrier

#### [Aircraft Carrier Flight Path Angles](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Aircraft%20Carrier%20Flight%20Path%20Angles.py)

Flight path angle for carrier approaches based on wind over deck, approach speed and meatball angle.

## Climb Performance

### Level Acceleration Test Technique

Examples of processing flight test data collected during a level acceleration test to determine climb performance.

#### [Level Acceleration - Energy Height - iLevil](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Level%20Acceleration%20-%20Energy%20Height%20-%20iLevil.py)

#### [Level Acceleration - Energy Height - Dynon](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Level%20Acceleration%20-%20Energy%20Height%20-%20Dynon.py)

#### [Level Acceleration - Nigel Speedy](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Level%20Acceleration%20-%20Nigel%20Speedy.py)

### Trim Envelope

#### [Trim Envelope](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Trim%20Envelope.py)

Calculate the set of trim points for an aircraft over a range of airspeeds and range of flight path angles. The required thrust and AoA is indicated for each trim point.

### Theory vs Simulation Trim Results

#### [Theory vs Simulation Trim Results](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Climb%20Performance.py)

Review the theory of climb performance and then use JSBSim to compare the results to the theory using the excess power calculation and using JSBSim
to calculate the maximum rate of climb (ROC) using it's trim routine. Lastly compare the results to those from a paper presenting climb performance
from a TECS based autopilot.

## VTOL

#### [VTOL Take-off Failure Options](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/VTOL%20Take-off%20Failure%20Options.py)

Looking at some of the options in terms of engine failure(s) during a vertical take-off of an aircraft like the Pegasus Vertical Business Jet (VBJ).

## Thrust Vectoring

#### [Thrust Vectoring Analysis](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Thrust%20Vectoring%20Analysis.py)

Use JSBSim to compare how varying the thrust vector angle can minimize fuel burn for a given flight condition and compare the results to the 
NASA report - [Optimal Pitch Thrust-Vector Angle and Benefits for all Flight Regimes](https://ntrs.nasa.gov/api/citations/20000034897/downloads/20000034897.pdf).

## Flight Test Techniques

#### [Rudder Kick](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Rudder%20Kick.py)

Simulate a pilot performing a rudder kick test by inputing a rudder input based on a ramp input. Aileron input is also included to maintain a steady heading sideslip (SHSS). The time histories of the control inputs and beta (sideslip angle) are plotted.

## Atmosphere

#### [International Standard Atmosphere](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/International%20Standard%20Atmosphere.py)

Calculate the International Standard Atmosphere (ISA) temperature, pressure, density and speed of sound at a given altitude.

#### [CAS TAS Mach](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/CAS%20TAS%20Mach.py)

Plot routine to calculate and plot the relationship between CAS, TAS and Mach number as altitude varies using the ISA.

#### [EAS - Equivalent Airspeed](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/EAS.py)

Explanation of Equivalent Airspeed (EAS) and how it relates to IAS, CAS and TAS. The relationship is plotted as altitude varies and airspeed varies.

## Ground Effect

#### [Ground Effect Models](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Ground%20Effect%20Models.py)

Comparison of different ground effect models to model the change in lift, drag and pitching moment as a function of height above ground.
A 747 simulator model provided by Boeing, a generic airliner model provided by Airbus  for an autoland challenge and a common JSBSim model
are detailed and compared.

## Dynamic Pressure

#### [Max Q - Maximum Dynamic Pressure](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/MaxQ.py)

Maximum dynamic pressure experienced by a SpaceX rocket, the Space Shuttle and an airliner.

#### [X-15 Max Q](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/X-15%20MaxQ.py)

Maximum dynamic pressure experienced by the X-15 rocket plane during its test flights for altitude missions and speed missions.

## Total Air Temperature (TAT)

#### [X-15 TAT](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/X-15%20TAT.py)

Total Air Temperature (TAT) experienced during X-15 test flights for altitude missions and speed missions.


## Work In Progress

Notebooks that are still being worked on and not yet ready for prime time.

#### [Generic Global Aerodynamic Model](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Generic%20Global%20Aerodynamic%20Model.py)

#### [JSBSim Aerodynamics](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/JSBSim%20Aerodynamics.py)

#### [Takeoff Speeds Vmu Vr Vlof](https://github.com/seanmcleod70/FlightDynamicsCalcs/blob/main/Takeoff%20Speeds%20Vmu%20Vr%20Vlof.py)

