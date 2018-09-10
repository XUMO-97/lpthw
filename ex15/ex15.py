# use argv to get a filename
from sys import argv

# defines script and filename to argv
script, filename = argv

# get the contents of the txt file
txt = open(filename)

# print a string with format characters
print "Here's your file %r:" % filename
# print the contents of the txt file
print txt.read()
txt.close()

# print a sentence
print "Type the filename again:"
# assigns the variable file_again with user's input 
file_again = raw_input("> ")

# assigns the variable txt_again with the contents of the txt file
txt_again = open(file_again)

# print the contents of txt_again
print txt_again.read()
txt_again.close()

# study drills 1:Above each line, write out in English what that line does.

# study drills 4:Get rid of the part from lines 10- 15 where you use raw_input and try the script then.
# just print the txt once

# study drills 5:Use only raw_input and try the script that way. Think of why one way of getting the filename would be better than another.
# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# if don't use raw_input I needn't to print the filename in python just in command line.

# study drills 7:Start python again and use open from the prompt. Notice how you can open fi les and run read on them right there? 
# read=open("C:/Users/18402/lpthw/ex15/ex15_sample.txt")
# read.read()
# read.close()

# study drills 8:Have your script also do a close() on the txt and txt_again variables. It’s important to close fi les when you are done with them.
# ok