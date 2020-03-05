#!usr/bin/python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np
from scipy.stats import linregress
from math import pi

x = np.array([0.0243, 0.0377, 0.0635])    # 1/AA
y = np.array([3.5895, 3.4153, 3.0332])    # 10-9 m2/s

fig=pl.figure(figsize=(5,5))
name_file_save=r'diffusion'
name_file_save+='.pdf'
ax = fig.add_subplot(1,1,1)
(slope, intercept, r_value, p_value, std_err) = linregress(x, y)
pl.suptitle(r'Diffusion coefficient', fontsize = 14) 
pl.title( r'D$_{PBC}$ = '+str(round(slope,5))+r'$\times$L$^{-1}$ + '+str(round(intercept,5))+', R$^{2}$ = '+str(round(r_value**2,3)),fontsize = 10)
visco = -(2.837*1.38064852e-23*298)/(6*pi*slope*1e-19*1e-03)
ax.set_xlim(0.02,0.071)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.01))
pl.plot(x, y, '+', color='indianred')
pl.plot(x, intercept + slope*x, 'dimgray', linewidth = 0.5)
pl.text(0.05, 3.55, r'D$_{0}$ = '+str(round(intercept,2)*1e-09)+r' m$^{2}$.s$^{-1}$'+'\n'+r'$\eta$ = '+str(round(visco,3))+' mPa.s')
pl.xlabel(r'L$^{-1}$ ($\mathrm{\AA}$)', fontsize = 10)
pl.ylabel(r'D$_{PBC}$ ($\times$ 10$^{-9} $m$^{2}$.s$^{-1}$)', fontsize = 10)
fig.savefig(name_file_save, bbox_inches='tight')
