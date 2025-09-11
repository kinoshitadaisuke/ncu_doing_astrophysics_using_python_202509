#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 11:27:17 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of a specified data type
# numpy.dtype ('i1') : 8-bit integer
array_f = numpy.array ([0, 1, 2, 3, 4, 5, -1, -2, -3, -4, 128], \
                       dtype=numpy.dtype ('i1') )

# printing Numpy array
print (f'array_f:\n{array_f}')

# printing information
print (f'information:')
print (f'  ndim     = {array_f.ndim}')
print (f'  size     = {array_f.size}')
print (f'  shape    = {array_f.shape}')
print (f'  dtype    = {array_f.dtype}')
print (f'  itemsize = {array_f.itemsize} byte')
