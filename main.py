import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import astropy.units as u
from astropy.utils.data import download_file
from astropy.io import fits # We use fits to open the actual data file

from astroquery.esasky import ESASky
from astroquery.utils import TableList
from astropy.wcs import WCS
from reproject import reproject_interp


a = ["/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_356.00+34.35_N.fits"]

count=0
while(count<224):
    a.append("/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_116.00+26.35_N.fits")
    count=count+1
count=0
i=0
ra = 356.00
dec=34.35
while(i<5):
    count=0
    ra=356.00
    while(count<45):
        a[count]="/home/aman/Downloads/Summer_2k18_Cosmology_RHT/Data/narrow/GALFA_HI_RA+DEC_"+str(ra)+"+"+str(dec)+"_N.fits"
        count=count+1
        ra=ra-8
    i=i+1
    dec=dec-8
i=0
while(i<224):
    cube=SpectralCube.read(a[i])
    
