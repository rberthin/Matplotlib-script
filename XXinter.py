#!usr/bin/python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pl
import string, re, struct, sys, math, os, time
import numpy as np
from sys import argv
from matplotlib import rc
from pylab import *

##############################################################################
r01, Gr01, n01 = np.genfromtxt('DFT_CY-CY.csv', comments = '#', unpack=True)
r11, Gr11, n11 = np.genfromtxt('15-1_CY-CY.csv', comments = '#', unpack=True)
r21, Gr21, n21 = np.genfromtxt('MD_CY-CY.csv', comments = '#', unpack=True)

r02, Gr02, n02 = np.genfromtxt('DFT_N-N.csv', comments = '#', unpack=True)
r12, Gr12, n12 = np.genfromtxt('15-1_N-N.csv', comments = '#', unpack=True)
r22, Gr22, n22 = np.genfromtxt('MD_N-N.csv', comments = '#', unpack=True)

r03, Gr03, n03 = np.genfromtxt('DFT_CT-CT.csv', comments = '#', unpack=True)
r13, Gr13, n13 = np.genfromtxt('15-1_CT-CT.csv', comments = '#', unpack=True)
r23, Gr23, n23 = np.genfromtxt('MD_CT-CT.csv', comments = '#', unpack=True)

r04, Gr04, n04 = np.genfromtxt('DFT_H-H.csv', comments = '#', unpack=True)
r14, Gr14, n14 = np.genfromtxt('15-1_H-H.csv', comments = '#', unpack=True)
r24, Gr24, n24 = np.genfromtxt('MD_H-H.csv', comments = '#', unpack=True)
##############################################################################

fig=pl.figure(figsize=(17,7))
name_file_save=r'XX_rdf'
name_file_save+='.pdf'

##############################################################################
ax = fig.add_subplot(1,4,1)

pl.title(r'RDF C2 - C2',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(2.5,7.1)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 1))

ax.plot(r21*0.01, Gr21, color='deepskyblue', label='Initial', linewidth=0.75)
ax.plot(r11*0.01, Gr11, color='mediumvioletred', label='Classical', linewidth=0.75)
ax.plot(r01*0.01, Gr01, color='dimgrey', label='Ab Initio', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)
pl.legend(loc='upper left', prop=dict(size=8))

##############################################################################
ax = fig.add_subplot(1,4,2)

pl.title(r'RDF N1 - N1',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(2.5,7.1)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 1))

ax.plot(r22*0.01, Gr22, color='deepskyblue', linewidth=0.75)
ax.plot(r12*0.01, Gr12, color='mediumvioletred', linewidth=0.75)
ax.plot(r02*0.01, Gr02, color='dimgrey', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

##############################################################################
ax = fig.add_subplot(1,4,3)

pl.title(r'RDF C2 - C2',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(3,7.1)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 1)) 

ax.plot(r23*0.01, Gr23, color='deepskyblue', linewidth=0.75)
ax.plot(r13*0.01, Gr13, color='mediumvioletred', linewidth=0.75)
ax.plot(r03*0.01, Gr03, color='dimgrey', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

##############################################################################
ax = fig.add_subplot(1,4,4)

pl.title(r'RDF H - H',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(1.5,7.1)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 1))

ax.plot(r24*0.01, Gr24, color='deepskyblue', linewidth=0.75)
ax.plot(r14*0.01, Gr14, color='mediumvioletred', linewidth=0.75)
ax.plot(r04*0.01, Gr04, color='dimgrey', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

fig.savefig(name_file_save, bbox_inches='tight')
