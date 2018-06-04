#check how many of these imports i actually need
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits # We use fits to open the actual data file

#import aplpy
from spectral_cube import SpectralCube
import pyfits
#from astroquery.esasky import ESASky
#from astroquery.utils import TableList
#from astropy.wcs import WCS
#from reproject import reproject_interp

def integrate(cube):
    x=cube.shape[0] #channels
    y=cube.shape[1] #Ra
    z=cube.shape[2] #dec
    arr=np.zeros((y,z),dtype=np.float)
    for p in range(z):
        for q in range(y):
            for r in range(x):
                arr[q,p]=arr[q,p]+cube.unmasked_data[r,q,p]
    return (arr)
def writematrixtofits(arr,string):
    hdu = pyfits.PrimaryHDU(arr)
    hdulist = pyfits.HDUList([hdu])
    hdulist.writeto(string, clobber=True)
    hdulist.close()

a = [None]*225
b = [None]*225
count=0
i=0
ra = 356.00
dec=34.35
r=0
for i in range(5):    #add zeroes before and after decimal!
    count=0
    ra=356.00
    for count in range(45):
        a[r]="/home/aman/RHT/data/narrow/GALFA_HI_RA+DEC_"+str(ra)+"0+"+str(dec)+"_N.fits"    #add a function for custom file address
        b[r]="/home/aman/RHT/data/narrow/pro_data/processed_RA+DEC_"+str(ra)+"0+"+str(dec)+"_N.fits"
        r=r+1
        ra=ra-8
    dec=dec-8
an=[None]*34       #add a input function to mark the part of sky needed to analyze
bn=[None]*34
i=0
for i in range(17):
    an[i]=a[14+i]    #you dont need this whole new list
    bn[i]=b[14+i]
i=0
for i in range(17):
    an[17+i]=a[59+i]
    bn[17+i]=b[59+i]
    i=i+1
i=0       
d=1.00       #add a input function for velocity range
for i in range(34):
    cube=SpectralCube.read(an[i])
    cube=cube.spectral_slab(-7 *u.km/u.s,-1.1 *u.km/u.s)
    arr=integrate(cube)
    f=(d/34)*100
    print("                   "+str(f) + "% integration completed")
    d=d+1
    writematrixtofits(arr,bn[i])
    arr=None
    cube=None
