# De-duplicating a list

# De-duplicating list is one of the most commonly used actions in computer programming

# Here, we have a list of state abbreviations ... but our list has lots of duplicates!
list_with_duplicates = ['CT', 'DE', 'MN', 'OH', 'CT', 'OK', 'MT', 'FL', 'TX', 'CT', 'OK', 'TX', 'PA', 'OK']

# First we convert our list with duplicates to the set type, which will eliminate the duplicates
# Next we convert that set back to a list so we can use it as intended.
list_without_duplicates = list(set(list_with_duplicates))

print "List with duplicates: {0}".format(list_with_duplicates)

print "List without duplicates: {0}".format(list_without_duplicates)