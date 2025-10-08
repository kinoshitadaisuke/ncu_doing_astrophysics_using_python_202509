#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:21:41 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants
import astropy.units

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# units of "km" and "sec"
unit_km         = astropy.units.km
unit_sec        = astropy.units.s

# creating a unit "km/sec"
unit_km_per_sec = unit_km / unit_sec

# conversion of unit
v2 = v.to (unit_km_per_sec)

# printing c, v, and v2
print (f'c = {c}')
print (f'v = 0.01 * {c}')
print (f'  = {v}')
print (f'  = {v2}')
