# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

import sys

def hundredsWords(num):
    underTwenties = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    
    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    
    if num == 0:
        return ""
    
    if num > 0 and num < 20:
        return underTwenties[num]
    
    ret = ""
    
    if num > 99:
        ret += underTwenties[num / 100] + " hundred"
        num %= 100
        
        if num > 0:
            ret += " and "
    
    if num > 19:
        ret += tens[ num / 10 ]
        num %= 10
        if num > 0:
            ret += " "
    
    if num > 0:
        ret += underTwenties[ num ]
    
    return ret

def wordsFor(num):
    powersOfTen = {
        3: "thousand",
        6: "million",
        9: "billion",
        12: "trillion"
    }
    
    numberString = ""
    
    remainder = num
    
    powerList = list(powersOfTen.iterkeys())
    powerList.sort()
    
    for power in powerList[::-1]:
        
        if remainder >= 10**power:
            numberString += hundredsWords( remainder / 10**power ) + " " + powersOfTen[power]
            remainder %= 10**power
            
            if remainder > 99:
                numberString += ", "
            elif remainder > 0:
                numberString += " and "
    
    hundredsString = hundredsWords(remainder)
    
    if len(hundredsString) > 0:
        numberString += hundredsString
    
    return numberString

def lettersIn(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = 0
    
    for character in list(string):
        if character in alphabet:
            letters += 1
    return letters

total = 0

for x in range(1,1001):
    string = wordsFor(x)
    letters = lettersIn(string)
    total += letters

print total
