# To read a single line from the file, use readline() method.

# f = open('my_file.txt')
# print(f.readline())
# Prints: First line of the file.

# Call it again to read next line
# print(f.readline())
# Prints: Second line of the file.

# Loop through an entire file, line by line
# f = open('my_file.txt')

# for line in f:
#     print(line)

# Prints:
# First line of the file.
# Second line of the file.
# Third line of the file.

# If you want to read all the lines in a file into a list of strings, use
# readlines() method.
# f = open('my_file.txt')
# print(f.readlines())

# Prints:
# [
    # 'First line of the file.\n',
    # 'Second line of the file.\n',
    # 'Third line of the file.'
# ]
# Note that list(f) gives the same result as readlines()

tecno_file = open('tecno_file.txt')
text = tecno_file.read()
text = text.replace(', ', '\n')
text = text.replace('. ', '\n')
text = text.replace('?', '?\n')
text_list = text.split('\n')

while ("" in text_list):
    text_list.remove("")

for index, item in enumerate(text_list, start=1):
    print(f"{index} {item}")