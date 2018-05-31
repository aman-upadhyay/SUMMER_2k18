#check how many of these imports i actually need
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits # We use fits to open the actual data file

import aplpy
from spectral_cube import SpectralCube

from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp

def integrate(cube):
    x=cube.shape[0] #channels
    y=cube.shape[1] #Ra
    z=cube.shape[2] #dec
    arr=np.zeroes((y,z),dtype=np.float)
    for p in range(z):
        for q in range(y):
            for r in range(x):
                arr[q,p]=arr[q,p]+cube.unmasked_data[r,q,p]
    return (arr)

a = ["/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_356.00+34.35_N.fits"]    #add a input function for custom file address

for count in range(224):
    a.append("/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_116.00+26.35_N.fits")
count=0
i=0
ra = 356.00
dec=34.35
r=0
for i in range(5):    #add zeroes before and after decimal!
    count=0
    ra=356.00
    for count in range(45):
        a[r]="/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_"+str(ra)+"0+"+str(dec)+"_N.fits"
        r=r+1
        ra=ra-8
    dec=dec-8
an=[None]*34       #add a input function to mark the part of sky needed to analyze
i=0
for i in range(17):
    an[i]=a[14+i]    #you dont need this whole new list
i=0
for i in range(17):
    an[17+i]=a[59+i]
    i=i+1
i=0              #add a input function for velocity range
for i in range(34):
    cube=SpectralCube.read(an[i])
    cube=cube.spectral_slab(-7 *u.km/u.s,-1.1 *u.km/u.s)
    arr=integrate(cube)
    cube=None
