# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import itertools
from operator import mul, add
    
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
            composits.append( reduce(mul, i) )
    
    ret = list(set(composits))
    ret.sort()
    
    return ret
    
def d(num):
    return reduce(add, properDivisors(num) )


sum = 0

for i in range(1,10000):
    di = d(i)
    if d(di)==i and di!=i:
        sum += i

print sum
