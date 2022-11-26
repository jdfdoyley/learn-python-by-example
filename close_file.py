# use the close() function to close an open file.
# f = open('my_file.txt')
# f.close()

# check closed status
# print(f.closed)
# Prints: True

# There are two approaches to ensure that a file is closed properly, even in
# cases of error.

# The first approach is to use the with keyword, which Python recommends, as
# it automatically takes care of closing the file once it leaves the with
# block (even in cases of error).

# with open('my_file.txt') as f:
#     print(f.read())

# The second approach is to use the try-finally block:
# f = open('my_file.txt')
# try:
#     # File operations goes here
#     print(f.read())
# finally:
#     f.close()