# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt, a 15K text file
# containing a triangle with one-hundred rows.

rows = 100

file = open('triangle.txt')

numbers = [[]] * 100

for i in range(100):
    numbers[i] = [int(x) for x in file.readline().split()]

for row in range(rows-2,-1,-1):
    for col in range( len(numbers[row]) ):
        numbers[row][col] += max( numbers[row+1][col:col+2] )
    
print (numbers[0][0])
