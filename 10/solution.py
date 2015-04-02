# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

a = [True] * 2000000
sum = 0

for x in range(2,2000000):
    if a[x]:
        a[::x] = [False] * len(a[::x])
        sum += x

print sum
