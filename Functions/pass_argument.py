# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001
# Topic: Pass Argument

# Pass single argument to a function
def hello(name: str):
    print("Hello,", name)


hello("Rhage")
# Prints: Hello, Rhage

hello("Wrath")
# Prints: Hello, Wrath

# Pass two arguments
def person_info(name, job):
    print(name, "is a", job)


person_info("Rhage", "Member of the Black Dagger Brotherhood")
# Prints: Rhage is a Member of the Black Dagger Brotherhood