# If you're new to dictionaries, you might want to start with dict_access.py

# We create a dictionary.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# If we want to add a new item to a dictionary, we can use direct access to change it.
contacts['Rachel'] = '202-888-1234'

# We can do the same thing to change an existing dictionary item, too.
contacts['Amy'] = '703-444-8888'

# That's great for changing a dictionary one key at a time, but let's say we have a lot of updates.  We have two options.

new_contacts = {
    'Kristin': '703-333-1234',
    'Katie': '301-555-9876',
    'Grace': '202-777-2222',
    'Charlotte': '410-555-9999'
}

# Option 1: Loop through the changes one at a time.

for name, phone in new_contacts.items():
    contacts[name] = phone

# Now contacts has everything in new_contacts.
print contacts, "\n"


# Let's set contacts back to the value it had before we added new_contacts.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876',
    'Rachel': '202-888-1234'
}

# Option 2: Use the dictionary method .update()

contacts.update(new_contacts)

print contacts