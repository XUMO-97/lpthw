formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# study drills 1:Do your checks of your work, write down your mistakes, and try not to make them on the next exercise.
# Sorry I spell formatter to formateer at the first line.

# study drills 2:Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
# the single-quotes and double-quotes is for separate each string, single-quotes is normal, if there's a string have single-quotes in it, then use double-quotes.