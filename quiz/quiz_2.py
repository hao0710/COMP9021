# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# Replace this comment with your code
has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''
integral_part = numerator // denominator
if numerator % denominator == 0:
   	has_finite_expansion = True
if numerator % denominator != 0:
    remains = [numerator % denominator]
    while not has_finite_expansion:
        new = remains[-1] * 10
        sigma += str(new // denominator)
        if new % denominator == 0:
            has_finite_expansion = True
            tau = ''
            break
        if new % denominator not in remains:
            remains.append(new % denominator)
        else:
            tau = sigma[remains.index(new % denominator):]
            sigma = sigma[:remains.index(new % denominator)]
            break
if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')
