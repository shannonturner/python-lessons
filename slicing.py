# Slicing examples
# Slicing allows us to see one piece or 'slice' of an item, like a single character (or set of characters) within a string


# Let's start by creating a variable called github_handle; it will hold a string with my GitHub handle in it
github_handle = '@shannonturner'


# You can use a comma to separate different items that you want to print as shown below
print "My github handle is ", github_handle


# This is our first slicing example.  Notice the square brackets attached directly to the variable name with no spaces in between.
# The two numbers in the middle, separated by a colon, are called the slicing indexes
print "My first name is ", github_handle[1:8]


# Here's how you can visualize the print statement above.

#       @shannonturner
#       0123456789....

# A note about the above: Python starts counting at zero, and the last few letters (r, n, e, r) are tied to 10, 11, 12, 13

# Or, shown vertically, it looks like this:

##      0		@
##      1		s
##      2		h
##      3		a
##      4		n
##      5		n
##      6		o
##      7		n
##      8		t
##      9		u
##      10		r
##      11		n
##      12		e
##      13		r

# So in the example of github_handle[1:8], notice that the t (at slice #8) is not included, but the s (at slice #1), is.
# That's because the first slice value is inclusive, but the second slice value is exclusive.
# I think of it as: Python starts at 1 and walks UNTIL it gets to 8 and then stops, gathering up everything in between.


print "My last name is ", github_handle[8:14]

# Notice that there is no index 14.  If the second index is higher than what exists, Python will assume you mean "until the very end"

# You can omit the second index; Python understands this as "go to the end"
print "My last name is ", github_handle[8:]

# And if you omit the first index, Python understands this as "start from the beginning"
print "My twitter handle is NOT ", github_handle[:8]

# What happens if you use a negative slicing index?

# You can use negative slicing indexes to count backwards from the end, like this:

##      -14		@
##      -13		s
##      -12		h
##      -11		a
##      -10		n
##      -9		n
##      -8		o
##      -7		n
##      -6		t
##      -5		u
##      -4		r
##      -3		n
##      -2		e
##      -1		r

print "My last name is ", github_handle[-6:]

# You can also mix and match positive and negative slicing indexes as needed

print "My first name is ", github_handle[1:-6]

# In these examples, we're relying on knowing the exact slicing indexes.  But what if our string changes in size or content?
# With short strings, it's fairly easy (especially if you write it out as above) to figure out which slices you need.

# But a more common and practical way to slice, rather than using numbers directly, is to create a variable that holds the number you need (but can change as needed)

# If this part is confusing, you may want to revisit this section when you're comfortable with string methods like str.find()

print "### Part Two ###"

text = "My GitHub handle is @shannonturner and my Twitter handle is @svt827"

# Let's extract the GitHub handle using str.find() and slicing.

snail_index = text.find('@')

print text[snail_index:snail_index + 14] # So the first slicing index is given by the variable, but we're still relying on knowing the exact number of characters (14).  We can improve this.

space_after_first_snail_index = text[snail_index:].find(' ') # Note that we're using slicing here to say start the .find() after the first snail is found.

print text[snail_index:snail_index + space_after_first_snail_index] # Why do we need to add snail_index to the second slicing index? Take a look:

print "snail_index is: ", snail_index
print "space_after_first_snail_index is: ", space_after_first_snail_index

print "So this is essentially saying text[20:34], see? --> ", text[20:34]

# Instead of creating a separate variable, you can just add the str.find() that gives the number you want right into the slice, like this:

print text[text.find('@'):text.find('@')+text[text.find('@'):].find(' ')] # But as you can see, it's not the most readable, especially compared to above.

# Still, it's a fairly common syntax / notation, so it's worth being familiar with it and knowing what it looks like in case you run into it.

print "Can you use slicing and string methods like str.find() to extract the Twitter handle from text?"



