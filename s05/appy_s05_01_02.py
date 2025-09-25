#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:12:04 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'generating random numbers of uniform distribution between 0 and 1'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n = args.number

# generating a set of random numbers of uniform distribution between 0.0 and 1.0
ru = scipy.stats.uniform.rvs (size=n)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{ru}')

# finding data type of object "ru"
type_ru = type (ru)

# printing type of object "ru"
print (f'type of object "ru" = {type_ru}')

# getting number of elements
n_elements = ru.size

# printing number of elements
print (f'number of elements in the array = {n_elements}')
