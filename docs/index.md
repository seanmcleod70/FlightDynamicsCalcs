Calculations, simulations with JSBSim and write up with Marimo notebooks

Marimo notebooks available in the [Flight Dynamics Calcs repo](https://github.com/seanmcleod70/FlightDynamicsCalcs).

## Roll Performance

#### [A4 Skyhawk Roll Performance](A4SkyhawkRollPerformance.html)

Can the A4 really roll at 720 deg/s or is it a tall tale? Using some aerodynamic data published by NASA let's take a look.

#### [Fighter Roll Rates](FighterRollRates.html)

Comparing fighter roll rates based on published aerodynamic data.
 
## Aircraft Carrier

#### [Aircraft Carrier Flight Path Angles](AircraftCarrierFlightPathAngles.html)

Flight path angle for carrier approaches based on wind over deck, approach speed and meatball angle.

## Climb Performance 

### Level Acceleration Test Technique

Examples of processing flight test data collected during a level acceleration test to determine climb performance.

#### [Level Acceleration - Energy Height - iLevil](LevelAccelerationEnergyHeightiLevil.html)

#### [Level Acceleration - Energy Height - Dynon](LevelAccelerationEnergyHeightDynon.html)

#### [Level Acceleration - Nigel Speedy](LevelAccelerationNigelSpeedy.html)

### Trim Envelope

#### [Trim Envelope](TrimEnvelope.html)

Calculate the set of trim points for an aircraft over a range of airspeeds and range of flight path angles. The required thrust and AoA is indicated for each trim point.

### Theory vs Simulation Trim Results

#### [Theory vs Simulation Trim Results](ClimbPerformance.html)

Review the theory of climb performance and then use JSBSim to compare the results to the theory using the excess power calculation and using JSBSim
to calculate the maximum rate of climb (ROC) using it's trim routine. Lastly compare the results to those from a paper presenting climb performance
from a TECS based autopilot.

## VTOL

#### [VTOL Take-off Failure Options](VTOLTake-offFailureOptions.html)

Looking at some of the options in terms of engine failure(s) during a vertical take-off of an aircraft like the Pegasus Vertical Business Jet (VBJ).

## Thrust Vectoring

#### [Thrust Vectoring Analysis](ThrustVectoringAnalysis.html)

Use JSBSim to compare how varying the thrust vector angle can minimize fuel burn for a given flight condition and compare the results to the 
NASA report - [Optimal Pitch Thrust-Vector Angle and Benefits for all Flight Regimes](https://ntrs.nasa.gov/api/citations/20000034897/downloads/20000034897.pdf).

## Flight Test Techniques

#### [Rudder Kick](RudderKick.html)

Simulate a pilot performing a rudder kick test by inputing a rudder input based on a ramp input. Aileron input is also included to maintain a steady heading sideslip (SHSS). The time histories of the control inputs and beta (sideslip angle) are plotted.

## Atmosphere

#### [International Standard Atmosphere](InternationalStandardAtmosphere.html)

Calculate the International Standard Atmosphere (ISA) temperature, pressure, density and speed of sound at a given altitude.

#### [CAS TAS Mach](CASTASMach.html)

Plot routine to calculate and plot the relationship between CAS, TAS and Mach number as altitude varies using the ISA.

#### [EAS - Equivalent Airspeed](EAS.html)

Explanation of Equivalent Airspeed (EAS) and how it relates to IAS, CAS and TAS. The relationship is plotted as altitude varies and airspeed varies.

## Ground Effect

#### [Ground Effect Models](GroundEffectModels.html)

Comparison of different ground effect models to model the change in lift, drag and pitching moment as a function of height above ground.
A 747 simulator model provided by Boeing, a generic airliner model provided by Airbus  for an autoland challenge and a common JSBSim model
are detailed and compared.

## Dynamic Pressure

#### [Max Q - Maximum Dynamic Pressure](MaxQ.html)

Maximum dynamic pressure experienced by a SpaceX rocket, the Space Shuttle and an airliner.

#### [X-15 Max Q](X15MaxQ.html)

Maximum dynamic pressure experienced by the X-15 rocket plane during its test flights for altitude missions and speed missions.

## Total Air Temperature (TAT)

#### [X-15 TAT](X15TAT.html)

Total Air Temperature (TAT) experienced during X-15 test flights for altitude missions and speed missions.

## Trim

#### [Inverted Trim](InvertedTrim.html)

Trim calculation using JSBSim for inverted flight.

#### [Trim Envelope](TrimEnvelope.html)

Calculate the set of trim points for an aircraft over a range of airspeeds and range of flight path angles. The required thrust and AoA is indicated for each trim point.

## Work In Progress

Notebooks that are still being worked on and not yet ready for prime time.

#### [Generic Global Aerodynamic Model](GenericGlobalAerodynamicModel.html)

#### [JSBSim Aerodynamics](JSBSimAerodynamics.html)

#### [Takeoff Speeds Vmu Vr Vlof](TakeoffSpeedsVmuVrVlof.html)


