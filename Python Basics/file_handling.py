# Doing CRUD in files
# open(r'loops.py')
# r=> read mode, default mode
# w=>Create file or overwrites
# a=> append add to end of the file
# x=> create new fails if exists
# fl=open("sample.txt",'w')
# fl.write("This is the file we just created")
# fl.write('This will be overwritten and previous will be removed')
# fl.write("change w to append before executing so that contents doesn't geet overwritten")
# fl=open("sample.txt",'r')
# print(fl.read())  # reading entire file
# print(fl.readline()) # reading only one line
# print(fl.readlines()) # reading all lines in a list
# fl.close() #To close file(mandatory to do it)