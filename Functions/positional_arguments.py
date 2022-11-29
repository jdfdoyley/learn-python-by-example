# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001
# Topic: Positional Arguments

# The most common are positional arguments, whose values are copied to their
# corresponding parameters in order.
# def character(name, job):
#     print(name, "is the", job)

# character("Wrath", "King of the vampire Race")
# Prints: Wrath is the King of the vampire race

# The only downside is that you have to pass arguments in the order in which
# it was defined.
def character(name, job):
    print(name, "is the", job)

character("King of the vampire Race", "Wrath")
# Prints: King of the vampire race is the Wrath