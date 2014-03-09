# If you're new to dictionaries, you might want to start with dict_access.py

# We create a dictionary.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# We can use the dictionary method .items() to give us a list of all of the items in contacts.

print contacts.items()

# Strictly speaking, .items() doesn't give us a list, it gives us a *tuple*, which is another way of storing information in Python.
# Tuples are almost identical to lists, except they're read-only.  You can't add to/remove from a tuple.
# But they're accessed and used in pretty much the same way, so we're going to treat it as if Python's giving us a list, and it will behave as we expect.

# .items() gives us a key and value pair together - so we can use that directly when we're looping.

for contact, phone in contacts.items():
    print "{0}'s number is {1}".format(contact, phone)

# .items() is probably most commonly used out of .keys(), .values(), and .items() because it gives you both the key and the value together.