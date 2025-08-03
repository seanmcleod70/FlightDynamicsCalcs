import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Takeoff Speeds $V_{LOF}$, $V_{MU}$, $V_R$, 

    $V_{LOF}$ - Airspeed at which the aircraft first becomes airborne. 

    $V_{MU}$ - Minimum airspeed at which an aircraft can lift off the ground.

    $V_R$ - Airspeed at which the pilot starts a longitudinal input to start a pitch up of the aircraft.

    ## $V_{LOF}$

    Occurs when the lift starts to exceed the current weight of the aircraft. 

    $L = C_L \frac{1}{2} \rho V^2 S$

    There are only two variables in the lift equation that the pilot has control over, the coefficient of 
    lift $C_L$ and the velocity $V$. 

    The pilot controls the $C_L$ by first selecting a flap setting for takeoff and then by varying the 
    angle of attack $\alpha$ by increasing the aircraft's pitch attitude $\theta$ via an elevator input. 
    While the main gear are still in contact with the ground $\alpha = \theta$.

    $V$ is controlled via a throttle input and time, with the net force from the difference in thrust, 
    given by the throttle input, and the sum of the drag force and friction force. The net force divided
    by the mass of the aircraft results in an acceleration increasing $V$ over time.

    $D = C_D \frac{1}{2} \rho V^2 S$

    Like $C_L$, the coefficient of drag $C_D$ also depends on the flap setting selected and the current $\alpha$. 
    The drag, like lift is also proportional to $V^2$ and since the thrust is constant during takeoff this means that the net
    force decreases and therefore the acceleration decreases as $V$ increases during the takeoff. Although the friction
    force decreases as $V$ increases given the increasing lift which results in a lower reaction force, the drag force
    dominates.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## References

    ### PFD Videos During Takeoff

    |Video|$V_1$|$V_R$|$V_{LOF}$|Comments|
    |-----|-----|-----|---------|--------|
    |[Airbus A320 TOGA takeoff](https://www.youtube.com/watch?v=ECV3IBkzZLc)|112kt|115kt|132kt|Light weight, max thrust|
    |[UAL A320 Takeoff profiles](https://www.youtube.com/watch?v=uB-9vPj29gY)|122kt|132kt|152kt|Derated thrust, flex 69|
    |[Cockpit Cam - PFD Closeup](https://www.youtube.com/watch?v=CsGEmDnMZH0)|140kt|155kt|162kt|Derated thrust, flex 59|

    **TODO** - video analysis frame by frame to calculate acceleration, pitch rate, pitch attitude at lift off, alpha etc.

    ### Certification

    [Part 25 - Section 25.107 Takeoff speeds](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-B/subject-group-ECFR14f0e2fcc647a42/section-25.107)

    - (d) $V_{MU}$ is the calibrated airspeed at and above which the airplane can safely lift off the ground, and continue the takeoff. $V_{MU}$ speeds must be selected by the applicant throughout the range of thrust-to-weight ratios to be certificated. These speeds may be established from free air data if these data are verified by ground takeoff tests.

    - (e) $V_R$, in terms of calibrated airspeed, must be selected in accordance with the conditions of paragraph (e)(1) through (4) of this section:

        - (1) $V_R$ may not be less than -

            - (i) $V_1$
            - (ii) 105 percent of $V_{MC}$
            - (iii) The speed that allows reaching $V_2$ before reaching a height of 35 feet above the takeoff surface; or
            - (iv) A speed that, if the airplane is rotated at its maximum practicable rate, will result in a $V_{LOF}$ of not less than -
                - (A) 110 percent of $V_{MU}$ in the all-engines-operating condition, and 105 percent of $V_{MU}$ determined at the thrust-to-weight ratio corresponding to the one-engine-inoperative condition; or
                - (B) If the $V_{MU}$ attitude is limted by the geometry of the airplane (i.e. tail contact with the runway), 108 percent of $V_{MU}$ in the all-engines-operating condition, and 104 percent of $V_{MU}$ determined at the thrust-to-weight ratio corresponding to the one-engine-inoperative condition.

    - (f) $V_{LOF}$ is the calibrated airspeed at which the airplane first becomes airborne.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
