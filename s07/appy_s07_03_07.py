#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/01 14:09:54 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units

# hour
u_hr = astropy.units.hr

# time t1
t1 = astropy.time.Time ('2025-12-31 20:00:00', format='iso', scale='utc')

# calculation of t1 + 12-hr
t2 = t1 + 16.0 * u_hr

# printing date/time
print (f't1              = {t1}')
print (f't2 = t1 + 12-hr = {t2}')
