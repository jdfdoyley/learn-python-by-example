# Create a New File
# If you try to open a file for writing that does not exist, Python will
# automatically create the file for you.

# Create a file and open it for writing

# write mode
# f = open('newfile_1.txt', 'w')

# append mode
# f = open('newfile_2.txt', 'a')

# read + write mode
# f = open('newfile_3.txt', 'w+')

# There is another way to create a file. You can use open() method and specify
# exclusive creation mode ‘x’.

# Create a file exclusively
f = open('newfile_4.txt', 'x')

# Note that when you use this mode, make sure that the file is not already
# present, if it is, Python will raise the error.
