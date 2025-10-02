#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/21 09:06:43 (UT+08:00) daisuke>
#

# importing sys module
import sys

# catalogue file name
file_catalogue = 'ngc2000.data'

# output file name
file_output = 'ngc2000_extracted.data'

# opening output file for writing
with open (file_output, 'w') as fh_w:
    # opening catalogue file
    with open (file_catalogue, 'r') as fh_r:
        # reading catalogue line-by-line
        for line in fh_r:
            # catalogue
            if (line[0:1] == 'I'):
                catalogue = 'IC'
            else:
                catalogue = 'NGC'
            # number
            try:
                number = int (line[1:5])
            except:
                # printing message
                print (f'ERROR: Something is wrong with following line...')
                print (f'ERROR:   {line[:75]}')
                print (f'ERROR: Cannot extract object ID number!')
                # exit
                sys.exit (1)
            # object ID
            object_id = f'{catalogue}{number:04d}'
            # object type
            obj_type = line[6:9].strip ()
            if (obj_type == 'Gx'):
                object_type = 'galaxy'
            elif (obj_type == 'OC'):
                object_type = 'open cluster'
            elif (obj_type == 'Gb'):
                object_type = 'globular cluster'
            elif (obj_type == 'Nb'):
                object_type = 'emission or reflection nebula'
            elif (obj_type == 'Pl'):
                object_type = 'planetary nebula'
            elif (obj_type == 'C+N'):
                object_type = 'star cluster with nebulosity'
            elif (obj_type == 'Ast'):
                object_type = 'asterism'
            elif (obj_type == 'Kt'):
                object_type = 'knot or nebulous region in a galaxy'
            elif (obj_type == '***'):
                object_type = 'triple star'
            elif (obj_type == 'D*'):
                object_type = 'double star'
            elif (obj_type == 'D*?'):
                object_type = 'double star ???'
            elif (obj_type == '*'):
                object_type = 'single star'
            elif (obj_type == '*?'):
                object_type = 'single star ???'
            elif (obj_type == '?'):
                object_type = 'uncertain'
            elif (obj_type == ''):
                object_type = 'unidentified'
            elif (obj_type == '-'):
                object_type = 'non-existent'
            elif (obj_type == 'PD'):
                object_type = 'photographic plate defect'
            else:
                # printing message
                print (f'ERROR: Something is wrong with following line...')
                print (f'ERROR:   {line[:75]}')
                print (f'ERROR: Cannot extract object type!')
                # exit
                sys.exit (1)
            # RA
            ra = line[10:17]
            # Dec
            dec = line[19:25]
            # constellation
            constellation = line[29:32].strip ()
            # size
            try:
                size_arcmin = float (line[33:38])
            except:
                size_arcmin = -999.9
            # magnitude
            try:
                mag = float (line[40:44])
            except:
                mag = +999.9

            # writing extracted data to output file
            fh_w.write (f'{object_id}\n')
            fh_w.write (f'  Type          = {object_type}\n')
            fh_w.write (f'  RA            = {ra}\n')
            fh_w.write (f'  Dec           = {dec}\n')
            fh_w.write (f'  Constellation = {constellation}\n')
            fh_w.write (f'  Size          = {size_arcmin} arcmin\n')
            fh_w.write (f'  Magnitude     = {mag:4.1f} mag\n')
