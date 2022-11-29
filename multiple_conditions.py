# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001

# Multiple Conditions
# To join two or more conditions into a single if statement, use logical
# operators viz. and, or and not.

# and expression is True, if all the conditions are true.
# x, y, z = 7, 4, 2
# if x > y and x > z:
#     print('x is greater')

# Prints: x is greater

# or expression is True, if at least one of the conditions is True.
x, y, z = 7, 4, 9
if x > y or x > z:
    print('x is greater than y or z')

# Prints: x is greater than y or z