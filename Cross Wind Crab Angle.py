import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    # Cross Wind Crab Angle

    Agostino's [Facebook post](https://www.facebook.com/share/p/19Qgwaqz2j/) included a [video reel](https://www.facebook.com/reel/1031870132599539) of an airliner landing in a cross wind, and he asked:

    > A great shot showing a cross-wind landing. Guess the sideslip angle (and sign) right before touch down.

    So doing some pixel angle measurements before the crab angle is reduced towards zero during the flare and 
    touchdown it looks like it's roughly 11 deg. The sign convention for sideslip angle is positive when the 
    relative wind comes from the right side of the aircraft's nose, so positive in this example.

    {mo.image("public/CrossWindCrabAngle/CrossWindLandingVideoFrame.png", width=600)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Crab Method

    - The crab method is executed by establishing a heading (crab) toward the wind with the wings level
    so that the airplane's ground track remains aligned with the centerline of the runway.

    - This crab angle is maintained until just prior to touchdown, during the flare rudder is applied to
    align the aircraft with the runway heading.

    The crab angle required during the approach is based on a combination of the aircraft's true airspeed (TAS)
    and the crosswind component.

    $$\mathrm{Crab \, Angle} = \arctan \left( \frac{\mathrm{Cross \, Wind}}{\mathrm{TAS}} \right)$$

    Assuming an approach speed of 130KIAS as being fairly typical for airliners, and assuming a sea level standard
    day that means 130KTAS, and given the measured crab angle of 11 deg that equates to a crosswind component of
    roughly 25kt.

    The [Airbus Crosswind Landing Techniques]([yy](https://skybrary.aero/sites/default/files/bookshelf/179.pdf))
    document mentions that on most Airbus models at touchdown the maximum crab angle allowed is 5 deg based on
    the side load forces on the gear.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    The following sliders allow you to set the TAS and the headwind and crosswind components which are then used
    to calculate the required crab angle during the landing approach in order to achieve a sidelsip angle of
    zero, i.e. to keep center vane centered.

    {mo.image("public/CrossWindCrabAngle/HunterVanes.jpg")}

    In addition to the crab angle being calculated, the groundspeed is also calculated and lastly a diagram showing
    the vector components of the relative wind etc. is dynamically updated as the sliders are moved.
    """)
    return


@app.cell(hide_code=True)
def _(hw_slider, mo, tas_slider, xw_slider):
    mo.vstack([tas_slider, hw_slider, xw_slider])
    return


@app.cell(hide_code=True)
def _(display_parameters, hw_slider, tas_slider, xw_slider):
    display_parameters(tas_slider.value, hw_slider.value, xw_slider.value)
    return


@app.cell(hide_code=True)
def _(hw_slider, plot_aircraft_wind_vectors, tas_slider, xw_slider):
    plot_aircraft_wind_vectors(tas_slider.value, xw_slider.value, hw_slider.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Code
    """)
    return


@app.cell
def _(math, plt):
    def plot_aircraft_wind_vectors(tas, xwind, hwind):

        crab_angle = math.asin(xwind/tas)
        gs_hw = tas * math.cos(crab_angle)
        gs = gs_hw - hwind

        # Aircraft body
        aircraft_len = tas/2
        aircraft_x = 0
        aircraft_y = 0
        aircraft_dx = aircraft_len * math.cos(math.pi/2 - crab_angle)
        aircraft_dy = aircraft_len * math.sin(math.pi/2 - crab_angle)

        # TAS
        tas_x = tas * math.cos(math.pi/2 - crab_angle) + aircraft_dx
        tas_y = tas * math.sin(math.pi/2 - crab_angle) + aircraft_dy
        tas_dx = -tas * math.cos(math.pi/2 - crab_angle)
        tas_dy = -tas * math.sin(math.pi/2 - crab_angle)

        # Ground speed
        gs_x = aircraft_dx
        gs_y = aircraft_dy + gs
        gs_dx = 0
        gs_dy = -gs

        # Head wind
        hw_x = gs_x
        hw_y = gs_y + hwind
        hw_dx = 0
        hw_dy = - hwind

        # Cross wind
        xwind_x = aircraft_dx + xwind
        xwind_y = aircraft_dy
        xwind_dx = -xwind
        xwind_dy = 0

        # Cross wind longitudinal
        xwind_lon_x = xwind_x
        xwind_lon_y = xwind_y
        xwind_lon_mag = xwind * math.sin(crab_angle)
        xwind_lon_dx = xwind_lon_mag * math.cos(-math.pi/2 - crab_angle)
        xwind_lon_dy = xwind_lon_mag * math.sin(-math.pi/2 - crab_angle)

        # Cross wind lateral
        xwind_lat_x = xwind_lon_x + xwind_lon_dx
        xwind_lat_y = xwind_lon_y + xwind_lon_dy
        xwind_lat_dx = aircraft_dx - xwind_lat_x
        xwind_lat_dy = aircraft_dy - xwind_lat_y

        # Ground speed plus headwind - lateral
        gs_hw_lat_mag = gs_hw * math.sin(crab_angle)
        gs_hw_lat_x = gs_hw_lat_mag * math.cos(math.pi/2 + math.pi/2 - crab_angle) + aircraft_dx
        gs_hw_lat_y = gs_hw_lat_mag * math.sin(math.pi/2 + math.pi/2 - crab_angle) + aircraft_dy
        gs_hw_lat_dx = aircraft_dx - gs_hw_lat_x
        gs_hw_lat_dy = aircraft_dy - gs_hw_lat_y

        # Ground speed plus headwind - longitudinal
        gs_hw_lon_x = hw_x
        gs_hw_lon_y = hw_y
        gs_hw_lon_dx = gs_hw_lat_x - hw_x
        gs_hw_lon_dy = gs_hw_lat_y - hw_y

        fig, ax = plt.subplots(figsize=(6, 6))

        # Plot aircraft body
        ax.quiver(aircraft_x, aircraft_y, aircraft_dx, aircraft_dy, angles='xy', scale_units='xy', scale=1, 
                  label='Aircraft x-axis', color='black')

        # Plot TAS
        ax.quiver(tas_x, tas_y, tas_dx, tas_dy, angles='xy', scale_units='xy', scale=1, 
                  label='TAS', color='red')

        # Plot Ground Speed
        ax.quiver(gs_x, gs_y, gs_dx, gs_dy, angles='xy', scale_units='xy', scale=1, 
                  label='Ground Speed', color='green')

        # Plot Head Wind
        ax.quiver(hw_x, hw_y, hw_dx, hw_dy, angles='xy', scale_units='xy', scale=1, 
                  label='Head Wind', color='brown')    

        # Plot cross-wind
        ax.quiver(xwind_x, xwind_y, xwind_dx, xwind_dy, angles='xy', scale_units='xy', scale=1, 
                  label='Cross Wind', color='brown')

        # Plot cross-wind aircraft longitudinal
        ax.quiver(xwind_lon_x, xwind_lon_y, xwind_lon_dx, xwind_lon_dy, angles='xy', scale_units='xy', scale=1,
                  label='Cross Wind Lon', color='cyan')

        # Plot cross-wind aircraft lateral
        ax.quiver(xwind_lat_x, xwind_lat_y, xwind_lat_dx, xwind_lat_dy, angles='xy', scale_units='xy', scale=1,
                  label='Cross Wind Lat', color='cyan')

        # Plot ground speed + head wind lateral
        ax.quiver(gs_hw_lat_x, gs_hw_lat_y, gs_hw_lat_dx, gs_hw_lat_dy, angles='xy', scale_units='xy', scale=1,
                  label='GS+HW Lat', color='blue')

        # Plot ground speed + head wind lateral
        ax.quiver(gs_hw_lon_x, gs_hw_lon_y, gs_hw_lon_dx, gs_hw_lon_dy, angles='xy', scale_units='xy', scale=1,
                  label='GS+HW Lon', color='blue')    

        ax.set_xlim(-50, tas*1.8)
        ax.set_ylim(-0.5, tas*1.8)
        plt.tick_params(axis='both', which='both', labelbottom=False, labelleft=False)
        plt.tight_layout()

        fig.legend(bbox_to_anchor=(1.05, 0.95), loc='upper left', borderaxespad=0.)

        return fig

    return (plot_aircraft_wind_vectors,)


@app.cell
def _(math, tableprint):
    def display_parameters(tas, headwind, crosswind):

        crab_angle = round(math.degrees(math.atan2(crosswind, tas)), 1)
        wind_mag = round(math.sqrt(headwind**2 + crosswind**2))
        ground_speed = tas - headwind
        wind_dir = 90 - round(math.degrees(math.atan2(headwind, crosswind)))

        data = { 
            'Wind': f'{wind_dir:03d}/{wind_mag}',
            'Crab Angle': crab_angle,
            'Ground Speed': ground_speed
        }

        return tableprint(data)

    return (display_parameters,)


@app.cell
def _(mo):
    def tableprint(dictdata):
        table = "|Parameter|Value|\n"
        table += "|---|---|\n"
        for key in dictdata.keys():
            table += "|" + key + "|" + str(dictdata[key]) + "|\n"
        return mo.md(table)

    return (tableprint,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## UI Controls
    """)
    return


@app.cell
def _(mo):
    tas_slider = mo.ui.slider(start=30,stop=200, value=130, show_value=True, label='TAS')
    hw_slider = mo.ui.slider(start=0, stop=100, value=20, show_value=True, label='Head Wind Component')
    xw_slider = mo.ui.slider(start=0, stop=100, value=40, show_value=True, label='Cross Wind Component')
    return hw_slider, tas_slider, xw_slider


@app.cell
def _():
    import marimo as mo
    import math
    import matplotlib.pyplot as plt
    import numpy as np

    return math, mo, plt


if __name__ == "__main__":
    app.run()
