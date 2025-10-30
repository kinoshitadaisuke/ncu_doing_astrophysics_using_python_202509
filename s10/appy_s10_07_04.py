#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/05 19:46:13 (UT+08:00) daisuke>
#

# import astropy module
import astropy.cosmology

# use preloaded cosmology model
cosmo_planck2018 = astropy.cosmology.Planck18

# Hubble constant and density parameters
H0      = cosmo_planck2018.H0
Ode0    = cosmo_planck2018.Ode0
Om0     = cosmo_planck2018.Om0
Odm0    = cosmo_planck2018.Odm0
Ob0     = cosmo_planck2018.Ob0
Onu0    = cosmo_planck2018.Onu0
Ogamma0 = cosmo_planck2018.Ogamma0
Ok0     = cosmo_planck2018.Ok0
Ot0     = Ode0 + Odm0 + Ob0 + Ogamma0 + Onu0 + Ok0

# Hubble time
hubble_time = cosmo_planck2018.hubble_time

# printing parameters
print (f'Parameters from Planck 2018 model')
print (f'  H0          = {H0:20s} # Hubble constant at z=0')
print (f'  Ode0        = {Ode0:8.6f}             # dark energy density at z=0')
print (f'  Om0         = {Om0:8.6f}             # matter density at z=0')
print (f'  Odm0        = {Odm0:8.6f}             # dark matter density at z=0')
print (f'  Ob0         = {Ob0:8.6f}             # baryonic matter density at z=0')
print (f'  Onu0        = {Onu0:8.6f}             # neutrino density at z=0')
print (f'  Ogamma0     = {Ogamma0:8.6f}             # photon density at z=0')
print (f'  Ok0         = {Ok0:8.6f}             # curvature density at z=0')
print (f'  Ot0         = {Ot0:8.6f}             # Ode0+Odm0+Ob0+Ogamma0+Onu0+Ok0 at z=0')
print (f'  Hubble time = {hubble_time}')
