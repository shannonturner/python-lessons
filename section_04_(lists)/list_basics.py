# list basics: adding items, removing items, inserting items, slicing

names = [] # an empty list
print names

names.append('Shannon') # add one item to the end of the list
print names

# Accessing names by slicing:
print names[0] # Shannon

# Inserting an item (not just adding it to the end):
names.insert(0, 'Finn')
print names

# 0 is the slicing number for where you'd like to insert the item BEFORE
# In other words, this will insert 'Finn' just *before* index 0

many_more = ['Jake', 'Princess Bubblegum', 'Marceline the Vampire Queen', 'Peppermint Butler']

# Now we can add all of the names in many_more the end of the list
names.extend(many_more)
print names

# Now we're going to go sugar-free, so everyone from the candy kingdom needs to go.
# Let's remove Peppermint Butler and Princess Bubblegum from our list.

names.pop() # this will remove the last item from the list, which happens to be Peppermint Butler
print names

names.pop(3) # this will remove the item at slicing number / index 3, which is Princess Bubblegum
print names

# Now we're going to search for an item and remove it.
remove_this = names.index('Jake')
print "I found Jake at slicing number / index #{0}".format(remove_this)
print "Now I can use .pop() to remove that item."
names.pop(remove_this)
print names

# We can also use .remove() to shortcut that.
names.remove('Finn')
print names