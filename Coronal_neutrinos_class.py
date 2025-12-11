import numpy as np 
import pandas as pd


class coronal_nu:
    beta_rec, eta_p, eta_ph= [0.1, 0.1, 0.5]
    c_light, m_p, m_e, sigma_T=[3*10**(10), 1.67*10**(-24), 9.1*10**(-28), 6.65*10**(-25)]
    erg_2_eV=5.11*10**5/(m_e*c_light**2)
    band_cor=3.*np.log(10)/np.log(10/2)
    
    file=pd.read_csv('./templates_sigmap_LX_R.txt', usecols=range(0, 123), header=None)
    templates=np.log10(np.array(file[1:], dtype=float)[:, 3:])
    energ_range=np.array(np.array(file)[0, 3:], dtype=float)
    sigma_ps, LX, R_eff=np.array(np.unique(np.array(file)[1:, 0]), dtype=int), np.array(np.unique(np.array(file)[1:, 1]), dtype=float), np.array(np.unique(np.array(file)[1:, 2]), dtype=float)
    templates=templates.reshape(len(sigma_ps), len(LX), len(R_eff), templates.shape[-1])

    def __init__(self, sigma_p, L_X, R):
        self.sigma_p=min(max(sigma_p, min(coronal_nu.sigma_ps)), max(coronal_nu.sigma_ps)) #proton magnetization value in log10
        self.L_X=min(max(L_X+np.log10(coronal_nu.band_cor), min(coronal_nu.LX)), max(coronal_nu.LX)) #X ray coronal luminosity in the 2-10 keV band in log10
        self.R=min(max(R, min(coronal_nu.R_eff)), max(coronal_nu.R_eff)) #R_eff in log10

    def neutrino_spectrum(self):
        ii, jj, kk=np.where(self.L_X>=coronal_nu.LX)[-1][-1], np.where(self.R>=coronal_nu.R_eff)[-1][-1], np.where(self.sigma_p>=coronal_nu.sigma_ps)[-1][-1]

        if self.L_X==min(coronal_nu.LX):
            t=0
        elif ii==len(coronal_nu.LX)-1:
            ii-=1
            t=1
        else:
            t=(self.L_X-coronal_nu.LX[ii])/(coronal_nu.LX[ii+1]-coronal_nu.LX[ii])
        
        if self.R==min(coronal_nu.R_eff):
            u=0
        elif jj==len(coronal_nu.R_eff)-1:
            jj=-1
            u=1
        else:
            u=(self.R-coronal_nu.R_eff[jj])/(coronal_nu.R_eff[jj+1]-coronal_nu.R_eff[jj])
        
        if self.sigma_p==min(coronal_nu.sigma_ps):
            f=0
        elif kk==len(coronal_nu.sigma_ps)-1:
            kk-=1
            f=1
        else:
            f=(self.sigma_p-coronal_nu.sigma_ps[kk])/(coronal_nu.sigma_ps[kk+1]-coronal_nu.sigma_ps[kk])
              
        inds=[np.arange(0, min(2, len(coronal_nu.LX)-ii), dtype=int), np.arange(0, min(2, len(coronal_nu.R_eff)-jj), dtype=int), np.arange(0, min(2, len(coronal_nu.sigma_ps)-kk), dtype=int)]
        corners=[(i,j,k) for i in inds[0] for j in inds[1] for k in inds[2]]

        weights = np.array([((1 - t)**(1 - i) * t**i)*((1 - u)**(1 - j) * u**j)*((1 - f)**(1 - k) * f**k) for i,j,k in corners])
        spectra_stack=np.array([coronal_nu.templates[kk+k, ii+i, jj+j] for i,j,k in corners])
        inter_spec=np.sum(weights[:, np.newaxis]*spectra_stack, axis=0)  
        
        return inter_spec
                