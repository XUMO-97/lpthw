from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# study drills 1:Find out what Zork and Adventure were. Try to fi nd a copy and play it.
# It's a game.

# study drills 2:Change the prompt variable to something else entirely.
# from sys import argv

# script, user_name = argv
# go = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(go)

# print "Where do you live %s?" % user_name
# lives = raw_input(go)

# print "What kind of computer do you have?"
# computer = raw_input(go)

# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)

# study drills 3:Add another argument and use it in your script.

# from sys import argv

# script, age, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script and I'm %s years old." % (user_name, script, age)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)

# study drills 4:Make sure you understand how I combined a """ style multiline string with the % format activator as the last print.
# Yes I undersand it.