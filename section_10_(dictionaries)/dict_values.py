# If you're new to dictionaries, you might want to start with dict_access.py

# We create a dictionary.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# We can use the dictionary method .values() to give us a list of all of the values in contacts.

print contacts.values()

for phone in contacts.values():
    print "{0}".format(phone)

# .values() is used less frequently than .keys() since you can't get the key from the value (but you can get the value if you know the key)

# Use .values() when you don't care what the key is, you just want a list of all of the values.  It's less common, but still good to know.