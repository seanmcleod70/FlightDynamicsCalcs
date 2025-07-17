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

#### [Optimal Climb Time](ClimbPerformance.html)

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
