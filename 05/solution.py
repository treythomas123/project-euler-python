# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from operator import mul

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

x = 1

requiredPrimeFactors = []

for d in xrange(1,20):
    factorList = primeFactors(d)
    
    for e in set(factorList):
        while requiredPrimeFactors.count(e) < factorList.count(e):
            requiredPrimeFactors.append(e)

print reduce(mul, requiredPrimeFactors)
