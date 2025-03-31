
# Task
# Given an integer, , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
#
# Input Format
# A single line containing a positive integer, n.
#
# Constraints
# 1 < n < 100

n = int(input('Введите число из промежутка от 1 до 100 включительно: '))
if n < 1 or n > 100:
  if  n % 2 == 0 and 2 >= n <= 5:
    print('Not Weird')
  elif n % 2 == 0 and 6 >= n <= 20:
    print('Weird')
  elif n % 2 == 0 and n > 20:
    print('Not Weird')
  else:
    print('Weird')

else:
  print('Not Weird')
