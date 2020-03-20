#!usr/bin/python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as pl
import string, re, struct, sys, math, os, time
import numpy as np
from sys import argv
from matplotlib import rc
from pylab import *

#############################################################################
r01, Gr01, n01 = np.genfromtxt('DFT_C1-C2.csv', comments = '#', unpack=True)
r11, Gr11, n11 = np.genfromtxt('15-1_C1-C2.csv', comments = '#', unpack=True)
r21, Gr21, n21 = np.genfromtxt('MD_C1-C2.csv', comments = '#', unpack=True)

r02, Gr02, n02 = np.genfromtxt('DFT_C2-H.csv', comments = '#', unpack=True)
r12, Gr12, n12 = np.genfromtxt('15-1_C2-H.csv', comments = '#', unpack=True)
r22, Gr22, n22 = np.genfromtxt('MD_C2-H.csv', comments = '#', unpack=True)

r03, Gr03, n03 = np.genfromtxt('DFT_N1-C1.csv', comments = '#', unpack=True)
r13, Gr13, n13 = np.genfromtxt('15-1_N1-C1.csv', comments = '#', unpack=True)
r23, Gr23, n23 = np.genfromtxt('MD_N1-C1.csv', comments = '#', unpack=True)
#############################################################################

fig=pl.figure(figsize=(9,5))
name_file_save=r'rdf_intra'
name_file_save+='.pdf'

ax = fig.add_subplot(1,3,1)

pl.title(r'RDF C1 - C2',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(1.3,1.6)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1))

ax.plot(r11*0.01, Gr11, color='gold', label='FIT 15.1', linewidth=0.5)
ax.plot(r21*0.01, Gr21, color='darkturquoise', label='Initial', linewidth=0.5)
ax.plot(r01*0.01, Gr01, color='dimgray', label='Ab initio', linewidth=0.75)


pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)
pl.legend(loc='best', prop=dict(size=8))

###########################################################################
ax = fig.add_subplot(1,3,2)

pl.title(r'RDF C2 - H',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(0.95,1.26)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1))

ax.plot(r12*0.01, Gr12, color='gold', linewidth=0.5)
ax.plot(r22*0.01, Gr22, color='darkturquoise', linewidth=0.5)
ax.plot(r02*0.01, Gr02, color='dimgray', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)

###########################################################################
ax = fig.add_subplot(1,3,3)

pl.title(r'RDF N1 - C1',fontsize=12)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='both', width=2.0)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(1.05,1.26)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 0.1)) 

ax.plot(r13*0.01, Gr13, color='gold', linewidth=0.5)
ax.plot(r23*0.01, Gr23, color='darkturquoise', linewidth=0.5)
ax.plot(r03*0.01, Gr03, color='dimgray', linewidth=0.75)

pl.xlabel(r'Distance r ($\mathrm{\AA}$)', fontsize = 12)
pl.tick_params(axis = 'both', labelsize = 10)


fig.savefig(name_file_save, bbox_inches='tight')
