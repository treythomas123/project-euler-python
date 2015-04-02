# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(num):
    collatz = [num]
    
    while (num > 1):
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        
        collatz.append(num)
    
    return collatz

max = 0
longest = 0

for i in range(1,1000000):
    collatzLen = len(collatz(i))

    if collatzLen > longest:
        longest = collatzLen
        max = i

print max
