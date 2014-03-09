# If you're new to dictionaries, you might want to start with dict_access.py

# We create a dictionary.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# We can use the dictionary method .keys() to give us a list of all of the keys in contacts.

print contacts.keys()

for contact in contacts.keys():
    print "{0}'s number is {1}".format(contact, contacts[contact])

# Dictionaries are unordered, so the keys (and their values) might be in a different order each time.  Or they might not.  Either way, that's normal.

# In other words, you can't rely on the ordering of anything in a dictionary.  But you could apply ordering to the keys.

# The built-in function sorted() will sort a list in ascending order.

for contact in sorted(contacts.keys()):
    print "{0}'s number is {1}".format(contact, contacts[contact])