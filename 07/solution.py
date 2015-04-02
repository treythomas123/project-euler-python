# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

def primeGen():
    primes = [2]
    yield 2
    x = 3
    
    while True:
        for prime in primes:
            if x % prime == 0:
                break
        else:
            primes.append(x)
            yield x
        
        x += 1


countDown = 10001

for x in primeGen():
    countDown -= 1
    
    if countDown == 0:
        print x
        exit()
