# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001
# Topic: Default Arguments

# Default allow you to make selected arguments optional.

# Set default value 'developer' to a 'job' parameter
def profile(name, job='student'):
    print(name, 'is a', job)


profile('Selena', 'CEO')
# Prints: Selena is a CEO

profile('Selena')
# Prints: Selena is a student
