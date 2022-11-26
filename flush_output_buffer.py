# Flush output buffer to disk without closing
f = open('my_file.txt', 'a')
f.write('Append this text')
f.flush()