tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape Sequences
# Escape     	What it does.
# \\   			Backslash (\)
# \' 			Single- quote (')
# \" 			Double- quote (")
# \a 			ASCII bell (BEL)
# \b 			ASCII backspace (BS)
# \f 			ASCII formfeed (FF)
# \n 			ASCII linefeed (LF)
# \N{name} 		Character named name in the Unicode database (Unicode only)
# \r 			ASCII carriage return (CR)
# \t 			ASCII horizontal tab (TAB)
# \uxxxx 		Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx 	Charac with 32- bit hex value xxxxxxxx (Unicode only)
# \v 			ASCII vertical tab (VT)
# \ooo 			Character with octal value oo
# \xhh 			Character with hex value hh

# study drills 1:Memorize all the escape sequences by putting them on fl ash cards.

# study drills 2:Use ''' (triple- single- quote) instead. Can you see why you might use that instead of """?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
# In the function three single-quotes is same to three double-quotes, but three single-quotes is easy to type.

# study drills 3:Combine escape sequences and format strings to create a more complex format.
print "\"How are you?\"\n\"I\'m fine thanks.\""

# study drills 4:Remember the %r format? Combine %r with double- quote and single- quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your fi le, but %s prints it the way you'd like to see it?
A = "I/'m fine too."
print "\"And you?\"\n%r" % A