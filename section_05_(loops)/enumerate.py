# enumerate() example

# enumerate() is used to loop through a list, and for each item in that list, to also give the index where that item can be found

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# This is how we're used to looping -- for each item in this list, print this item
for day in days:
	print day


# Now we add a layer of complexity.  Notice how two variables (index, day) are being created by the for loop.
for index, day in enumerate(days):
	print "days[{0}] contains {1}".format(index, day)
	print "day contains {0}".format(day)


# Since we humans aren't counting days by zero, we do a little addition inside the .format()
for index, day in enumerate(days):
	print "{0} is day # {1}".format(day, index+1)