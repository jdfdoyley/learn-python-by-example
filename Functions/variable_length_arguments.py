# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001
# Topic: Variable Length Arguments (*args and **kwargs)

# *args- collects all the unmatched positional arguments into a tuple and you
# can perform any operation that a tuple supports, like indexing, iteration etc
def print_arguments(*args):
    print(args)

print_arguments(3, 2, 6, 9)                 # Prints: (3, 2, 6, 9)
print_arguments(1, 5, 8, 6, 3, 2, 6, 9)     # Prints: (1, 5, 8, 6, 3, 2, 6, 9)

# NOTE: You don't need to call this keyword parameter args, but it is standard
# practice