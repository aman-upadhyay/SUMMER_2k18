import numpy as np
import pyfits
from astropy.io import fits
import multiprocessing as mp

a = [None]*225
a = np.array(a)
b = [None]*225
b = np.array(b)
count=0
i=0
ra =356
dec=34
r=0
for i in range(5):
	count=0
	ra=356
	for count in range(45):
		a[r]="/home/aman/RHT/data/narrow/pro_data/processed_RA+DEC_"+str(ra).zfill(3)+".00+"+str(dec).zfill(2)+".35_N.fits"
		b[r]="/home/aman/RHT/data/narrow/croped_data/croped_RA+DEC_"+str(ra).zfill(3)+".00+"+str(dec).zfill(2)+".35_N.fits"
		r=r+1
		ra=ra-8
	dec=dec-8
a=np.reshape(a,(5,45))
b=np.reshape(b,(5,45))
a=a.transpose()
b=b.transpose()
a1 = np.delete(a,44,axis=0)
b1 = np.delete(b,44,axis=0)
a1 = np.delete(a1,4,axis=1)
b1 = np.delete(b1,4,axis=1)
a1 = a1.flatten
b1 = b1.flatten
a2 = np.delete(a,np.s_[0:4:1],axis=1)
b2 = np.delete(b,np.s_[0:4:1],axis=1)
a3 = np.delete(a,np.s_[0:44:1],axis=0)
b3 = np.delete(b,np.s_[0:44:1],axis=0)
a3 = a3.flatten
b3 = b3.flatten
def crop1(f):
	matrix = fits.open(a1[f])
	image = matrix[0].data
	image = np.delete(image,np.s_[481:513:1],axis=1)
	image = np.delete(image,np.s_[481:513:1],axis=0)
	hdu = pyfits.PrimaryHDU(image)
	hdulist = pyfits.HDUList([hdu])
	hdulist.writeto(b1[f], clobber=True)
	hdulist.close()
	matrix=None
	image=None
def crop2(g):
	matrix = fits.open(a2[g])
	image = matrix[0].data
	image = np.delete(image,np.s_[481:513:1],axis=1)
	hdu = pyfits.PrimaryHDU(image)
	hdulist = pyfits.HDUList([hdu])
	hdulist.writeto(b2[g], clobber=True)
	hdulist.close()
	matrix=None
	image=None
def crop3(h):
        matrix = fits.open(a3[g])
        image = matrix[0].data
        image = np.delete(image,np.s_[481:513:1],axis=0)
        hdu = pyfits.PrimaryHDU(image)
        hdulist = pyfits.HDUList([hdu])
        hdulist.writeto(b3[g], clobber=True)
        hdulist.close()
        matrix=None
        image=None
pool1 = mp.Pool(processes=64)
pool1.map(crop1, range(0,176))
pool2 = mp.Pool(processes=64)
pool2.map(crop2,range(0,44))
pool3 =mp.Pool(processes=64)
pool3.map(crop3,range(0,4))
matrix = fits.open(a[44,4])
image = matrix[0].data
hdu = pyfits.PrimaryHDU(image)
hdulist = pyfits.HDUList([hdu])
hdulist.writeto(b[44,4], clobber=True)
hdulist.close()
matrix=None
image=None

