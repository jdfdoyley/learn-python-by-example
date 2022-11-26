# Read entire file
# f = open('my_file.txt')
# print(f.read())

# Prints
# First line of the file.
# Second line of the file.
# Third line of the file.

# By default, the read() method reads the entire file. However, you can
# specify the maximum number of characters to read.
f = open('my_file.txt')

print(f.read(3))
# Prints: Fir

# print(f.read(5))
# Prints: First
