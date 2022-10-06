import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits as pf

import glob
# importing this as pf is a convention that dates back to when the fits handling module 
# was in pyfits rather than astropy and allows the code to be used more-or-less 
# interchangeably with old code using pyfits
# You will want all of the exposure time information in one file, so define it up top
# Using a context manager (the ‘with…’ statement) helps you make sure your file
# is saved if the code crashes unexpectedly. 
# The ‘a’ mode makes it so you’re appending to a file if it already exists or writing
# to a new file if it doesn’t exist. You may need to change this to ‘w’ if you want to 
# overwrite an old file from a previous run. You can also just do that with rm from the terminal.

with output as open(‘/rotse/base/dir/ExposureTimes.csv’, ‘a’):

	#replace this with the location of the directory

	directory = 'the/directory/you/want/to/use/' 

	# the second * is in case the file ends in “.fits” rather than “.fit”

	fileList = glob.glob(directory + ‘*_c.fit*') 
	for fn in fileList:
		hdulist = pf.open(fn)
		hdu = hdulist[0]
		headername=hdu.header['EXPTIME'] #to just extract 'EXPTIME' header
		#data = fits.getdata('*_c.fit', extname='EXPTIME') #to obtain data from the EXPTIME column
		output.write(‘{0},{1:.03f}\n’.format(fn, headername)) # Never forget to add the ‘\n’ when writing to files like this. 
	     



