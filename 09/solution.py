# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1,999):
    for b in range(a,1000-a):
        if a**2 + (b-a)**2 == (1000-b)**2:
            print a * (b-a) * (1000-b)
            exit()
