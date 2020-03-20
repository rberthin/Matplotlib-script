#!usr/bin/python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np
from sys import argv
from matplotlib import rc
from pylab import *

#############################################################################
r01, Gr01 = np.genfromtxt('acetonitrile_exp.dat', comments = '#', unpack=True)
r11, Gr11 = np.genfromtxt('data_fit.dat', comments = '#', unpack=True)
r21, Gr21 = np.genfromtxt('data_MD.dat', comments = '#', unpack=True)
#############################################################################

fig=pl.figure(figsize=(9,5))
name_file_save=r'infrared_spectrum'
name_file_save+='.pdf'

ax = fig.add_subplot(1,1,1)

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_linewidth(1.5)
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_linewidth(1.5)
ax.tick_params(axis='both', width=2.0)
pl.tick_params(axis = 'both', labelsize = 10)
pl.xlabel(r'$cm^{-1}$)', fontsize = 12)

ax.set_xlim(3300,500)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(end, start, 500))

ax.plot(r01, Gr01, color='dimgray', label='Experimental', linewidth=0.5)
ax.plot(r11, Gr11, color='crimson', label='Classical', linewidth=0.5)
ax.plot(r21, Gr21, color='c', label='Initial', linewidth=0.5)

pl.legend(loc='best', prop=dict(size=8))

fig.savefig(name_file_save, bbox_inches='tight')
