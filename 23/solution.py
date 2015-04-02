# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

import itertools
from operator import mul, add
import functools

def primeFactors(product):
    factors = []
    possibleFactor = 2
    
    while product > 1:
        if product % possibleFactor == 0:
            product = product / possibleFactor
            factors.append( possibleFactor )
        else:
            possibleFactor = possibleFactor + 1
    
    return factors

def properDivisors(num):
    factors = primeFactors(num)
    composits = [1]
    
    for j in range( 1, len(factors) ):
        for i in itertools.combinations(factors, j):
            composits.append( functools.reduce(mul, i) )
    
    ret = list(set(composits))
    ret.sort()
    
    return ret

def isAbundant(num):
    return sum(properDivisors(num)) > num

abundantNumbers = []

for i in range(1,28123):
    if isAbundant(i):
        abundantNumbers.append(i)

sums = [False]*28123

for num1 in abundantNumbers:
    for num2 in abundantNumbers:
        sum = num1 + num2
        if sum < len(sums):
            sums[sum] = True

total = 0

for i in range(len(sums)):
    if sums[i]==False:
        total += i

print(total)
