# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001
# Topic: Keyword Arguments

# Keyword arguments can be put in any order
def message(name, text):
    print(f"{name}: {text}")

message(text="Hi, how are you doing?", name="Elena")
message(name="Elena", text="Hi, how are you doing?")
# Prints:
# Elena: Hi, how are you doing?
# Elena: Hi, how are you doing?

# NOTE: It is possible to combine positional and keyword arguments in a single
# call. If you do so, specify the positional arguments before keyword arguments
