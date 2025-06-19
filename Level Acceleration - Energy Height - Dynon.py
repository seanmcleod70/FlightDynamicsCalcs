import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Level Acceleration

    This notebook demonstrates the calculation of climb performance from a level acceleration test using the energy height calculation.

    Load in the data recorded by a Dynon glass cockpit system.
    """
    )
    return


@app.cell
def _(np):
    data = np.genfromtxt('data/LevelAcceleration/TestPoint1-Dynon.csv', delimiter=',', names=True)
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Generate 0 based time values.""")
    return


@app.cell
def _(data):
    time = data['GPSSecondsToday'] - data[0]['GPSSecondsToday']
    return (time,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Take a look at the IAS and altitude during the test point.""")
    return


@app.cell
def _(data, plt, time):
    plt.figure()
    plt.title("KIAS vs Time")
    plt.plot(time, data['Indicated_Airspeed_knots'])
    plt.ylabel('KIAS')

    plt.figure()
    plt.title("Altitude vs Time")
    plt.plot(time, data['Pressure_Altitude_ft']);
    plt.ylabel('Altitude (ft)')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Calculate TAS from IAS, assuming ISA standard day and pressure altitude of 8000ft.""")
    return


@app.cell
def _(data):
    TASData = data["Indicated_Airspeed_knots"] * 1.127
    return (TASData,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's create a 4th order polynomial in order to smooth out the noise in the TAS data.""")
    return


@app.cell
def _(TASData, np, time):
    TASPoly = np.polyfit(time, TASData, 4)
    TASPoly
    return (TASPoly,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Generate smoothed TAS data from the polynomial coefficients.""")
    return


@app.cell
def _(TASPoly, time):
    TASSmoothedData = TASPoly[0] * time**4 + TASPoly[1] * time**3 + TASPoly[2] * time**2 + TASPoly[3] * time + TASPoly[4]
    return (TASSmoothedData,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Plot of the TAS data including the smoothed polynomial fit.""")
    return


@app.cell
def _(TASData, TASSmoothedData, plt, time):
    plt.figure()
    plt.title("KTAS vs Time")
    plt.plot(time, TASData)
    plt.plot(time, TASSmoothedData);
    plt.ylabel('KTAS')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now calculate energy height:

    $\Large h_e = h + \dfrac{V_t^2}{2g}$
    """
    )
    return


@app.cell
def _(TASSmoothedData, data):
    g = 32.2           # ft/s^2
    ktTofps = 1.68     # conversion from kt to ft/s

    heData = data['Pressure_Altitude_ft'] + ((TASSmoothedData * ktTofps)**2) / (2 * g)
    return (heData,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Calculate a 3rd order polynomial fit for the energy height data.""")
    return


@app.cell
def _(heData, np, time):
    hePoly = np.polyfit(time, heData, 3)
    hePoly
    return (hePoly,)


@app.cell
def _(hePoly, time):
    heSmoothedData = hePoly[0] * time**3 + hePoly[1] * time**2 + hePoly[2] * time + hePoly[3]
    return (heSmoothedData,)


@app.cell
def _(heData, heSmoothedData, plt, time):
    plt.figure()
    plt.title("Height Energy vs Time")
    plt.plot(time, heData)
    plt.plot(time, heSmoothedData);
    plt.ylabel('$h_e$')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now calculate excess power in ft/sec:

    $\Large P_s = \dfrac{\mathrm{d} h_e}{\mathrm{d}t}$
    """
    )
    return


@app.cell
def _(hePoly):
    dhedtPoly = [ 3*hePoly[0], 2*hePoly[1], 1*hePoly[2] ]
    dhedtPoly
    return (dhedtPoly,)


@app.cell
def _(dhedtPoly, time):
    PsData = (dhedtPoly[0] * time**2 + dhedtPoly[1] * time + dhedtPoly[2]) * 60  # fps to fpm
    return (PsData,)


@app.cell
def _(PsData, plt, time):
    plt.figure()
    plt.title("$P_s$ vs Time")
    plt.plot(time, PsData)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Generate smoothed IAS data from the smoothed TAS data. Again assuming ISA standard day at 8000ft.""")
    return


@app.cell
def _(TASSmoothedData):
    IASSmoothedData = TASSmoothedData / 1.127
    return (IASSmoothedData,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Finally plot $P_s$ vs KIAS""")
    return


@app.cell
def _(IASSmoothedData, PsData, plt):
    plt.figure()
    plt.title("$P_s$ vs KIAS")
    plt.plot(IASSmoothedData, PsData);
    plt.show()
    return


@app.cell
def _(PsData, data, plt):
    plt.figure()
    plt.title("$P_s$ vs Unsmoothed KIAS")
    plt.plot(data["Indicated_Airspeed_knots"], PsData);
    plt.show()
    return


@app.cell
def _():
    import marimo as mo

    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


if __name__ == "__main__":
    app.run()
