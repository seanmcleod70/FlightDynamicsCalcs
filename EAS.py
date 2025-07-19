import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # EAS - Equivalent AirSpeed

    Aerodynamic forces like lift, drag etc. are proportional to the dynamic pressure.

    $Q = \frac{1}{2} \rho V^2$

    $Q$ - dynamic pressure 
    $\rho$ - air density
    $V$ - airspeed of the aircraft relative to the air mass

    The air density $\rho$ varies based on pressure altitude and temperature, see [International Standard Atmosphere](https://seanmcleod70.github.io/FlightDynamicsCalcs/InternationalStandardAtmosphere.html).

    - **TAS** - True Airspeed, the velocity of the aircraft relative to the air mass.

    - **IAS** - Indicated Airspeed, airspeed measured by the pitot-static system.

    - **CAS** - Calibrated Airspeed, IAS corrected for instrument and position errors.

    - **EAS** - Equivalent Airspeed, CAS corrected for compressibility effects.

    The pitot static system of the aircraft measures the difference between the total/stagnation pressure $p_t$
    and the static pressure $p_s$, and is calibrated for standard sea-level ISA conditions via $\rho_0$, the air
    density for standard sea-level ISA conditions, $1.225 kg/m^3$.

    $IAS = \sqrt{\dfrac{2(p_t - p_s)}{\rho_0}}$

    Assuming standard day ISA sea-level conditions and assuming no instrument or position error and low enough
    airspeed that compressibility isn't a factor, then $TAS = IAS = CAS = EAS$.

    ## Compressibility

    When the aircraft is flying at high airspeeds the total/stagnation pressure in the pitot tube is not representative
    of the airstream dynamic pressure due to a magnification by compressibility. The compressibility of the airflow in
    the pitot tube produces a pressure which is greater than if the flow was incompressible. Therefore the airspeed 
    indicator reports an erroneous airspeed based on this magnification.

    The following plot shows the ratio of the dynamic pressure $Q$ for a specific CAS as the altitude varies compared
    to the sea-level dynamic pressure $Q_0$ for the same CAS.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_dynamic_pressure_scaling):
    plot_dynamic_pressure_scaling([100, 200, 300, 400], 30000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    EAS is defined as producing the same dynamic pressure when coupled with standard sea level density as the TAS
    coupled with the actual air density.

    $(EAS)^2 \rho_0 = (TAS)^2 \rho$

    $EAS = TAS \sqrt{\dfrac{\rho}{\rho_0}}$

    $\rho$ - actual air density $\rho_0$ - standard sea level density
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In terms of when compressibility needs to be taken into account, it depends on the degree of accuracy required, 
    with regards to whether you treat $\rho$ as a constant or as a variable. The following equation calculates
    the density $\rho$ as a function of Mach.

    $\dfrac{\rho_0}{\rho} = \left( 1 + \dfrac{\gamma - 1}{2} M^2 \right)^{1/(\gamma - 1)}$

    Looking at the plot of this function below for $M < 0.32$ the variation in $\rho$ is smaller then 5%. As a result
    a general rule of thumb the density variation should be accounted for at Mach numbers > 0.3.
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_density_versus_mach):
    plot_density_versus_mach()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Airspeed Corrections

    $EAS = CAS + \Delta V_C$
    """
    )
    return


@app.cell(hide_code=True)
def _(plot_compressibility_correction):
    plot_compressibility_correction([5000, 10000, 15000, 20000, 25000, 30000], 100, 400)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Plot Routines""")
    return


@app.cell
def _(dynamic_pressure, np, plt):
    def plot_dynamic_pressure_scaling(cas_speeds, max_alt):
        fig, ax = plt.subplots(figsize=(10, 5))

        alts = np.linspace(0, max_alt, 50)
        for cas in cas_speeds:
            cas_0_pressure = dynamic_pressure(cas, 0)
            dynamic_pressure_ratio = []
            for alt in alts:
                dynamic_pressure_ratio.append(dynamic_pressure(cas, alt) / cas_0_pressure)
            ax.plot(alts, dynamic_pressure_ratio, label=f'{cas} KCAS')

        ax.set_ylabel('Dynamic pressure ratio  $\\dfrac{Q}{Q_0}$')
        ax.set_xlabel('Altitude (ft)')
        ax.set_title('Dynamic Pressure Ratio vs Altitude')
        ax.legend()

        return plt.gca()
    return (plot_dynamic_pressure_scaling,)


@app.cell
def _(math, np, plt, ticker):
    def plot_density_versus_mach():
        fig, ax = plt.subplots(figsize=(10, 5))

        gamma = 1.4
        exponent = 1/(gamma - 1)

        density_ratios = []
        machs = np.linspace(0, 1, 50)
        for mach in machs:
            density_ratio = math.pow(1 + ((gamma -1)/2)*mach**2, exponent)
            density_ratios.append(1/density_ratio)
        ax.plot(machs, density_ratios)

        ax.axhline(y=0.95, linestyle='--')
        ax.axvline(x=0.32, linestyle='--')

        ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))

        ax.set_ylabel('$\\dfrac{\\rho}{\\rho_0}$')
        ax.set_xlabel('M')
        ax.set_title('Density Variation versus Mach')

        return plt.gca()
    return (plot_density_versus_mach,)


@app.cell
def _(CAStoEAS, ftTom, ktToms, msTokt, np, plt):
    def plot_compressibility_correction(altitudes, min_cas, max_cas):
        fig, ax = plt.subplots(figsize=(10, 5))
    
        for alt in altitudes:
            corrections = []
            cass = np.linspace(min_cas, max_cas, 50)
            for cas in cass:
                eas = CAStoEAS(ktToms(cas), ftTom(alt))
                corrections.append(msTokt(eas) - cas)
            ax.plot(cass, corrections, label=f'{alt}ft')
    
        ax.set_ylabel('Compressibility Correction $\\Delta V_C$ (kt)')
        ax.set_xlabel('CAS (kt)')
        ax.set_title('Compressibility Correction')
        ax.legend()
    
        return plt.gca()
    return (plot_compressibility_correction,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Utility Functions""")
    return


@app.cell
def _(CAStoTAS, ISA, ftTom, ktToms):
    def dynamic_pressure(cas, alt):
        # cas - kt, alt - ft
        _, density, _, _ = ISA.state(ftTom(alt))
        tas = CAStoTAS(ktToms(cas), ftTom(alt))

        return 0.5 * density * tas**2
    return (dynamic_pressure,)


@app.cell
def _():
    def ftTom(ft):
        return ft / 3.28084

    def mToft(m):
        return m * 3.28084

    def msTokt(ms):
        return ms * 1.944012

    def ktToms(kt):
        return kt / 1.944012 
    return ftTom, ktToms, msTokt


@app.cell
def _():
    import marimo as mo
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from ISA import ISAtmosphere, CAStoTAS, TAStoCAS, CAStoEAS, EAStoTAS, MachtoCAS, CAStoMach

    ISA = ISAtmosphere()
    return CAStoEAS, CAStoTAS, ISA, math, mo, np, plt, ticker


if __name__ == "__main__":
    app.run()
