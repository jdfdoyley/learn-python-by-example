# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001

# The elif (else if) Statement
# Use elif statement to specify a new condition to test, if the first
# condition is false.
# x, y = 5, 5
# if x > y:
#     print('x is greater')
# elif x < y:
#     print('y is greater')
# else:
#     print('x and y are equal')

# Prints
# x and y are equal

# Substitute for Switch Case
# Unlike other programming languages, Python does not have a ‘switch‘
# statement. You can use if…elif…elif sequence as a substitute.
choice = 6

if choice == 1:
    print('case 1')
elif choice == 2:
    print('case 2')
elif choice == 3:
    print('case 3')
elif choice == 4:
    print('case 4')
else:
    print('default case')

# Prints: default case