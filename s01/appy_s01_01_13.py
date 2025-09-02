#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/09/02 21:15:40 (UT+08:00) daisuke>
#

# importing math module
import math

# (x, y) coordinate
x, y = +1.0, -1.0

# calculation of arctangent
a_rad = math.atan2 (y, x)

# conversion from radian into degree
a_deg = math.degrees (a_rad)

# printing result of calculation
print (f'x            = {x}')
print (f'y            = {y}')
print (f'atan2 (y, x) = {a_rad} rad = {a_deg} deg')
