#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:45:53 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of 3x3x3 shape
# with all the elements initialised by one.
array_p = numpy.ones ( (3, 3, 3) )

# printing Numpy array
print (f'array_p:\n{array_p}')

# printing information
print (f'information:')
print (f'  ndim     = {array_p.ndim}')
print (f'  size     = {array_p.size}')
print (f'  shape    = {array_p.shape}')
print (f'  dtype    = {array_p.dtype}')
print (f'  itemsize = {array_p.itemsize} byte')
