print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# study drills 1:Go online and find out what Python's raw_input does.
# raw_input treat all inputs as strings and return the string type.

# study drills 2:Can you find other ways to use it? Try some of the samples you find.
a = raw_input("input:")
print a

# study drills 3:Write another "form" like this to ask some other questions.
print "What's your name?",
name = raw_input()
print "What's your hobby?",
hobby = raw_input()
print "Who's your father?",
father = raw_input()

print "So, you're %r, like %r and %r is your father." % (
	name, hobby, father)
	
# study drills 4:Related to escape sequences, try to find out why the last line has '6\'2"' with that \'sequence. See how the single- quote needs to be escaped because otherwise it would end the string?
# Because the formatter character used was %r, is for debugging, the single-quote be escaped, if it's %s then just display the string.