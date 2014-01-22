# String methods: string.replace()

# string.replace() is similar to the find -> replace feature in Word, Excel, or other office-y type programs

song = "eat, eat, eat, apples and bananas"

# Let's start here:
print "I like to ... {0}".format(song)


# string.replace() lets us replace all instances of one string with another.
print "I like to ... {0}".format(song.replace("a","o")) # We're replacing all of the lowercase *a*s in song with *o*s

# Let's take a look at the syntax.
# We've seen the {0} syntax; that's the placeholder that string.format() uses to insert a variable into the string that comes before the dot in .format()
# The 0 corresponds to the first variable in the list inside the parentheses (remember that Python starts counting at zero)
# What's the variable we're going to insert at {0}? It's song.replace("a", "o")
# Python will evaluate song.replace("a", "o") and place the result inside of the {0}
# How song.replace("a", "o") works is: .replace() will replace every "a" it finds in song with an "o"
# The way I remember it is .replace() will perform its action on what comes before the dot (which in song.replace("a", "o"), is song)

print "But note that the original song itself is unchanged: {0}".format(song)

print "string.replace() is case-sensitive."
print song.replace("Eat", "chop") # This won't replace anything!

print song
print song.replace("eat", "chop")
print song # the original is unchanged

# If you want your changes to stick, you'll need to assign your variable song a new value
song = song.replace("eat", "chop")
# What we're saying here is essentially:
# song is now equal to the new value of song.replace("eat", "chop")

# If you have lots of replaces to do on a string, you *could* do it like this:
song = song.replace("apples", "mangos")
song = song.replace(" and", ", pears, and")
song = song.replace("bananas", "kiwis")

print song

# Or, you could chain lots of replaces together -- remember that what gets replaced is what comes before the dot!
# In other words, replaces will occur in left-to-right order
song = "eat, eat, eat, apples and bananas" # setting it back to the original
song = song.replace("eat", "chop").replace("apples", "mangos").replace(" and", ", pears, and").replace("bananas", "kiwis")

print song