#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 14:03:53 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.linspace (0.0, 10.0, 11)

# printing values of "a", "b", and "c"
print (f'a = {a}')

# trying b = a
print (f'making array "b" by "b = a"...')
b = a

# trying a.copy ()
print (f'making array "c" by "c = a.copy ()"...')
c = a.copy ()

# printing values of "a", "b", and "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = {c}')

# IDs of "a", "b", and "c"
print (f'id (a) = {id (a)}')
print (f'id (b) = {id (b)}')
print (f'id (c) = {id (c)}')

# modifying array "a"
print (f'carrying out "a[3] += 5.0"...')
a[3] += 5.0

# printing values of "a", "b", and "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = {c}')

# modifying array "c"
print (f'carrying out "c[7] -= 10.0"...')
c[7] -= 10.0

# printing values of "a", "b", and "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = {c}')
