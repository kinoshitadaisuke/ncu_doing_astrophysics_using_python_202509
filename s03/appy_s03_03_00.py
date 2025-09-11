#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:39:04 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with 10 elements all equal to zeros
array_k = numpy.zeros ( (10,) )

# printing Numpy array
print (f'array_k:\n{array_k}')

# printing information
print (f'information:')
print (f'  ndim     = {array_k.ndim}')
print (f'  size     = {array_k.size}')
print (f'  shape    = {array_k.shape}')
print (f'  dtype    = {array_k.dtype}')
print (f'  itemsize = {array_k.itemsize} byte')
