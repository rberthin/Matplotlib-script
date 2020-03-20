#!usr/bin/python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pl
import string, re, struct, sys, math, os, time
import numpy as np
from sys import argv
from matplotlib import rc
from pylab import *

#############################################################################
r01, Gr01 = np.genfromtxt('DFT_N-C1-C2.csv', comments = '#', unpack=True)
r11, Gr11 = np.genfromtxt('15-1_N-C1-C2.csv', comments = '#', unpack=True)
r21, Gr21 = np.genfromtxt('MD_N-C1-C2.csv', comments = '#', unpack=True)

r02, Gr02 = np.genfromtxt('DFT_H-C2-H.csv', comments = '#', unpack=True)
r12, Gr12 = np.genfromtxt('15-1_H-C2-H.csv', comments = '#', unpack=True)
r22, Gr22 = np.genfromtxt('MD_H-C2-H.csv', comments = '#', unpack=True)

r03, Gr03 = np.genfromtxt('DFT_H-C2-C1.csv', comments = '#', unpack=True)
r13, Gr13 = np.genfromtxt('15-1_H-C2-C1.csv', comments = '#', unpack=True)
r23, Gr23 = np.genfromtxt('MD_H-C2-C1.csv', comments = '#', unpack=True)
#############################################################################

fig=pl.figure(figsize=(9,5))
name_file_save=r'adf_intra'
name_file_save+='.pdf'

ax = fig.add_subplot(1,3,1)

pl.title(r'N1 - C1 - C2', fontsize=12)

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
pl.xlabel(r'Angle)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

ax.set_xlim(1.3,1.6)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1))

ax.plot(r01*0.01, Gr01, color='dimgray', label='Ab initio', linewidth=0.5)
ax.plot(r11*0.01, Gr11, color='crimson', label='Classical', linewidth=0.5)
ax.plot(r21*0.01, Gr21, color='c', label='Initial', linewidth=0.5)

pl.legend(loc='best', prop=dict(size=8))

###########################################################################
ax = fig.add_subplot(1,3,2)

pl.title(r'H - C2 - H', fontsize=12)

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
pl.xlabel(r'Angle)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

ax.set_xlim(0.9,1.31)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1))

ax.plot(r02*0.01, Gr02, color='dimgray', linewidth=0.5)
ax.plot(r12*0.01, Gr12, color='crimson', linewidth=0.5)
ax.plot(r22*0.01, Gr22, color='c', linewidth=0.5)

###########################################################################
ax = fig.add_subplot(1,3,3)

pl.title(r'H - C2 - C1', fontsize=12)

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
pl.xlabel(r'Angle)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

ax.set_xlim(1.05,1.26)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1)) 

ax.plot(r03*0.01, Gr03, color='dimgray', linewidth=0.5)
ax.plot(r13*0.01, Gr13, color='crimson', linewidth=0.5)
ax.plot(r23*0.01, Gr23, color='c', linewidth=0.5)


fig.savefig(name_file_save, bbox_inches='tight')
