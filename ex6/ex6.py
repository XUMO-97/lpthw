# defines the variable x includes the string and format character %d, 10 is formatted into the string with %d
x = "There are %d types of people." % 10
# defines the variable binary ,the content of binary is binary.
binary = "binary"
# just like above.
do_not = "don't"
# defines the variable y includes the string and format character %s, bind binary and do_not to the string with %s format
y = "Those who know %s and those who %s." % (binary, do_not)

# print the content of x
print x
# print the content of y
print y 

# print the string and variable x is formatted into the string with %r
print "I said: %r." % x
# print the string and variable y is formatted into the string with %s
print "I also said: '%s'." % y

# defines the variable hilarious, the content of hilarious is False
hilarious = False
# defines the variable joke_evaluation,the content of joke_evaluation is a string with a format %r
joke_evaluation = "Isn't that joke so funny?! %r"

# print the various joke_evaluation ,the variable hilarious is formatted into the string of joke_evaluation with %r
print joke_evaluation % hilarious

# defines the variable w with a string
w = "This is the left side of..."
# defines the variable e with a string
e = "a string with a right side."

# print w plus e
print w + e

# study drills 1
# the above

# study drills 2
# 1.y = "Those who know %s and those who %s." % (binary, do_not)   There is two.
# 2. print "I said: %r." % x
# 3.print "I also said: '%s'." % y

# study drills 3
# There is two in y, then print "I also said: '%s'." % y transfer y so there is also two string in the string.

# study drills 4
# Use + is a kind of way to stitch strings