from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# study drills 1:Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
# yes there's an error, it tell you to type more than 3 values to unpack.

# study frills 2:Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.

# from sys import argv

# script, first, second = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second

# from sys import argv

# script, first, second, third, fourth = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third
# print "Your fourth variable is:", fourth