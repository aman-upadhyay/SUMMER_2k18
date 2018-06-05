import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.io import fits


from spectral_cube import SpectralCube
import pyfits
import multiprocessing as mp

pool =mp.Pool(processes=64)
pool.map(process, range(0,224))
def process(f):
	a = [None]*225
	b = [None]*225
	count=0
	i=0
	ra = 356.00
	dec=34.35
	r=0
	for i in range(5):
		count=0
		ra=356.00
		for count in range(45):
			a[r]="/home/aman/RHT/data/narrow/GALFA_HI_RA+DEC_"+str(ra).zfill(3)+".00+"+str(dec).zfill(5)+"_N.fits"    
			b[r]="/home/aman/RHT/data/narrow/pro_data/processed_RA+DEC_"+str(ra).zfill(3)+".00+"+str(dec).zfill(5)+"_N.fits"
			r=r+1
			ra=ra-8
		dec=dec-8
	cube=SpectralCube.read(a[f])
	cube=cube.spectral_slab(-7 *u.km/u.s,-1.1 *u.km/u.s)
	arr=integrate(cube)
	writematrixtofits(arr,b[f])
	arr=None
	cube=None
def integrate(cube):
        x=cube.shape[0] #channels
        y=cube.shape[1] #Ra
        z=cube.shape[2] #dec
        arr=np.zeros((y,z),dtype=np.float)
        for r in range(x):
		arr=arr+cube[x,:,:].quicklook
        return (arr)
def writematrixtofits(arr,string):
        hdu = pyfits.PrimaryHDU(arr)
        hdulist = pyfits.HDUList([hdu])
        hdulist.writeto(string, clobber=True)
        hdulist.close()
