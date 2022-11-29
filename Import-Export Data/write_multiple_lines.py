# Write Multiple Lines
# To write multiple lines to a file at once, use writelines() method. This
# method accepts list of strings as an input.

f = open('my_file.txt', 'w')
lines = ['New line 1\n', 'New line 2\n', 'New line 3']
f.writelines(lines)