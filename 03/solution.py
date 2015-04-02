# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
d = 2

while x > 1:
    if x % d == 0:
        x = x / d
    else:
        d = d+1

print d
