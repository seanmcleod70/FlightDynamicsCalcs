import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # CAS TAS Mach

    The relationship between calibrated airspeed (CAS), true airspeed (TAS) and Mach versus altitude can be plotted using the
    `plotCASTASMach()` function provided below.

    Using the [International Standard Atmosphere](InternationalStandardAtmosphere.html) class and the utility airspeed
    functions it provides we can plot lines of constant CAS and Mach based on TAS and altitude.

    The `plotCASTASMach()` allows you to specify custom plot ranges for altitude, TAS, CAS and Mach and to specify the step 
    interval for CAS and Mach.
    """
    )
    return


@app.cell
def _(plotCASTASMach):
    plotCASTASMach(minAlt=0, maxAlt=60000, minTAS=0, maxTAS=1000, minCAS=50, maxCAS=700, casStep=50, minMach=0.2, maxMach=1.6, machStep=0.1)
    return


@app.cell
def _(plotCASTASMach):
    plotCASTASMach(minAlt=0, maxAlt=40000, minTAS=100, maxTAS=500, minCAS=125, maxCAS=450, casStep=25, minMach=0.3, maxMach=0.8, machStep=0.1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Plot Routine""")
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    from ISA import ISAtmosphere, CAStoTAS, TAStoCAS
    #from labellines import labelLines

    max_altitude = 60000

    ISA = ISAtmosphere()

    def SpeedOfSound(altitude):
        _, _, _, speed_of_sound = ISA.state(ftTom(altitude))
        return msTokt(speed_of_sound)

    def tas2mach(tas, alt=max_altitude):
        return tas / SpeedOfSound(alt)

    def mach2tas(mach, alt=max_altitude):
        return SpeedOfSound(alt) * mach

    def ftTom(ft):
        return ft / 3.28084

    def mToft(m):
        return m * 3.28084

    def msTokt(ms):
        return ms * 1.944012

    def ktToms(kt):
        return kt / 1.944012 


    def plotCASTASMach(minAlt, maxAlt, minTAS, maxTAS, minCAS, maxCAS, casStep, minMach, maxMach, machStep):

        max_altitude = maxAlt
    
        fig, ax = plt.subplots(layout='constrained', figsize=(10, 5))
    
        ax.margins(y=0)
    
        # Plot Mach lines
        alt = []
        for altitude in range(int(ftTom(minAlt)), int(ftTom(maxAlt))+1, 1000):
            alt.append(mToft(altitude))
        alt.append(maxAlt)
    
        for mach in np.arange(minMach, maxMach+0.01, machStep):
            tas = []
            for altitude in alt:
                _, _, _, speed_of_sound = ISA.state(ISA.geometric_altitude(ftTom(altitude)))
                tas.append(msTokt(speed_of_sound * mach))
            ax.plot(tas, alt, color='gray')
    
        # Plot CAS lines
        for cas in range(minCAS, maxCAS+1, casStep):    
            tas = []
            alt = []
            for altitude in range(0, max_altitude+1, 1000):
                tas.append(msTokt(CAStoTAS(ktToms(cas), ftTom(altitude))))
                alt.append(altitude)
            ax.plot(tas, alt, label=f'{cas}KCAS')
    
        ax.set_xlabel('TAS (kts)')
        ax.set_ylabel('Altitude (ft)')
        ax.set_title('CAS TAS Mach')
        ax.set_xlim(minTAS, maxTAS)
    
        secax = ax.secondary_xaxis('top', functions=(tas2mach, mach2tas))
        secax.set_xlabel('Mach')
        plt.legend()
        plt.grid(True, linestyle='--')
    
        return plt.gca()

    return (plotCASTASMach,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
