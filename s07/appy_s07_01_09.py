#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:23:03 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_AA       = astropy.units.AA
u_eV       = astropy.units.eV
u_keV      = astropy.units.keV
u_spectral = astropy.units.spectral ()

# wavelength
wl = 1.0 * u_AA

# energy of a photon corresponding to wavelength of 10 AA
energy_eV  = wl.to (u_eV, equivalencies=u_spectral)
energy_keV = wl.to (u_keV, equivalencies=u_spectral)

# printing result
print (f'wavelength = {wl:g}  ==>  energy = {energy_eV:g} = {energy_keV:g}')
