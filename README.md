# Coronal_neutrinos
Python class that calculates the neutrino spectrum of a magnetically powered coronal environment, as presented in Fiorillo et al.(2024, ApJL 961 L14) and Karavola et al. (2025, JCAP).

## The coronal model

In the aforementioned model, the corona is described as a cuboid with dimensions $LxLx\beta_{rec}L$ with $\beta_{rec} \sim 0.1$ being the reconnection rate of the magnetic reconnection site. We model the corona as a sphere with colume $\beta_{rec}L^3$ and thus the effective radius of the source is $R \sim 0.29 L$.

In such environments both leptons and proton are accelerated to high energies. In particular protons, which are of main interest for neutrino production, can reach Lorentz factors of $\gamma_{\rm p} \sim σ_{\rm p}$ with $σ_{\rm p}=B^2/(4π n_p m_p c^2)$ being the proton magnetization value that quantifies the magnetic dominance of the source, with B being the coronal magnetic field and $n_p$ being the non-relativistic proton density.

We assume that the lepton and proton populations are in rough equipartition with the magnetic field and moreover that the X rays of the corona originate by leptonic emission and, thus:

$\bullet$ the bolometric X-ray luminosity in the 0.1-100keV band is written as $L_X \sim η_x L_B~(1)$ 

$\bullet$ the bolometric proton luminosity is written as $L_p \sim η_p L_B~(2)$

$\bullet η_x+η_p \sim 1~(3)$

with $L_B= \frac{c}{4π} \beta_{rec}  B^2 S$ being the Poynting luminosity and S being the coronal surface.

We fixate $\eta_X=0.5$ and $\eta_p=0.3$. Since for individual sources $L_X$ is an observational quantity, fron eqs.(1) and (2) we can derive $B$ and $L_{p}$ respectively.

Note: The neutrino luminosity scales linearly with $\eta_p$ (see eq. 3.6 in Karavola et al. (2025)) so the results of this study can be re-rnormalize in respect to different $\eta_p$ values.

## Python class 
The python class takes as inputs three parameters:

$\bullet$ the proton magnetization $\sigma_p$ in $log_{10}$

$\bullet$ the bolometric X-ray luminosity in the 2-10keV band $L_{X, 2-10}$ in $log_{10}$, which is internally extrapolated to the 0.1-100keV bolometric luminosity $L_X$  

$\bullet$ the effective radius of the (spherical) corona R in $log_{10}$

We have performed 72 runs with the leptohadronic code $ATHE \nu A$ (Dimitrakoudis et al. (2012)) in the parameter space of 

**($log_{10}L_X$, $log_{10}R$, $log_{10}\sigma_{\rm p}$)=([42, 47], [12.4, 14.4], [3, 6])**


all in integer steps and cgs units. You can find a visualization of the aforementioned templates under the name "templates.png".
For any given set of parameter by the user we perform a trilinear interpolation between the templates. If any value is outside of the limits mentioned above, the closest value available in the parameter space is used instead.

## Outputs
$\bullet$ The energy bins of the neutrino spectrum are stored in the class as an array named **energ_range** which is in eV (not in logarithm). 
$\bullet$ The class returns the luminosity of the neutrino spectrum in the coronal rest frame in $erg/s$ in logarithm of a base of 10.
