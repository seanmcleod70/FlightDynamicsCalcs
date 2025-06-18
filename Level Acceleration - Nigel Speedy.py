import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Level Acceleration

    This notebook demonstrates the calculation of climb performance from a level acceleration test using the procedure as described by Nigel Speedy at - [Using Level Accelerations to Determine Climb Performance](https://www.kitplanes.com/using-level-accelerations-to-determine-climb-performance/).

    Load in the data recorded by iLevil based FTI system.
    """
    )
    return


@app.cell
def _(np):
    data = np.genfromtxt('data/TestPoint1-iLevil.csv', delimiter=',', names=True)
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
    plt.plot(time, data['IASkt'])

    plt.figure()
    plt.title("Altitude vs Time")
    plt.plot(time, data['Altitude'])
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Calculate TAS from IAS, assuming ISA standard day and pressure altitude of 8000ft.""")
    return


@app.cell
def _(data):
    TASData = data["IASkt"] * 1.127
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
    plt.plot(time, TASSmoothedData)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's calculate $dv/dt$ derivative from the TAS polynomial.""")
    return


@app.cell
def _(TASPoly):
    dvdtPolyCoefs = [ 4*TASPoly[0], 3*TASPoly[1], 2*TASPoly[2], 1*TASPoly[3] ]
    dvdtPolyCoefs
    return (dvdtPolyCoefs,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Generate $dv/dt$ data and plot it.""")
    return


@app.cell
def _(dvdtPolyCoefs, time):
    dvdtData = dvdtPolyCoefs[0] * time**3 + dvdtPolyCoefs[1] * time**2 + dvdtPolyCoefs[2] * time + dvdtPolyCoefs[3]
    return (dvdtData,)


@app.cell
def _(dvdtData, plt, time):
    plt.figure()
    plt.title("dv/dt KTAS vs Time")
    plt.plot(time, dvdtData)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now calculate:

    $\dfrac{dH}{dt} = \dfrac{V_t}{g} \dfrac{dV}{dt}$
    """
    )
    return


@app.cell
def _(TASSmoothedData, dvdtData):
    g = 32.2           # ft/s^2
    ktTofps = 1.68     # conversion from kt to ft/s
    fpsTofpm = 60      # conversion from ft/s to ft/min

    dHdtData = (((TASSmoothedData * ktTofps) / g) * dvdtData * ktTofps) * fpsTofpm
    return (dHdtData,)


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
    mo.md(r"""Finally let's plot $dH/dt$ versus KIAS.""")
    return


@app.cell
def _(IASSmoothedData, dHdtData, plt):
    plt.figure()
    plt.title("ROC (fpm) vs KIAS")
    plt.plot(IASSmoothedData, dHdtData)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now plot against unsmoothed KIAS.""")
    return


@app.cell
def _(dHdtData, data, plt):
    plt.figure()
    plt.title("ROC (fpm) vs Unsmoothed KIAS")
    plt.plot(data['IASkt'], dHdtData)
    plt.show()
    return


@app.cell
def _():
    import marimo as mo

    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
