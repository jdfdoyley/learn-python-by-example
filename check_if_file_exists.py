# Check if File Exists
# If you try to open or delete that does not exist, an error occors. To avoid
# this, you can precheck if the file already exists by using the isfile()
# method from the OS module.
import os

if os.path.isfile('newfile_1.txt'):
    f = open('newfile_1.txt')
else:
    print('The file does not exists.')