address = "1600 Pennsylvania Ave NW Washington, DC"

# .split() is a string method (a function that works only on strings) that splits a string into a list based on some delimiter.
# In this example, we're splitting address into a list at every space.
address = address.split(" ")

# Address is now a list equal to:
# ['1600', 'Pennsylvania', 'Ave', 'NW', 'Washington,', 'DC']
# Note that the list created is a list of strings.

# And since it's a list, you can loop over it!

# .split() is commonly used to split text files into a list (at each newline)
# .split() is also commonly used to split spreadsheet files in comma separated value (CSV) format into a list (at each comma)

# Any time you need to split a string into multiple parts, you can use .split()