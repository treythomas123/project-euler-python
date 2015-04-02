# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome( possiblePalindrome ):
    return possiblePalindrome[::-1] == possiblePalindrome

palindromes = []

for x in xrange(100,999):
    for y in xrange(x,999):
        if isPalindrome( str(x*y) ):
            palindromes.append( x*y )

palindromes.sort()

print palindromes[-1]
