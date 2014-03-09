# This is probably the best place to start with dictionaries.

# First, let's create a string, a list, and a dictionary.

name = "Shannon"

attendees = ['Shannon', 'Amy', 'Jen', 'Julie']

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# We can access part of a string using slicing:
print name[0] # S

# We can access part of a list using slicing:
print attendees[0:2] # Shannon, Amy

# We can access part of a dictionary if we know its key.
print contacts['Jen'] # 301-600-5555

# In lines 9-14, we created a dictionary.
# Dictionaries are another way of storing information in Python.
# Dictionaries are made up of key+value pairs.

# In the dictionary contacts, the keys are Shannon, Amy, Jen, and Julie.
# A dictionary's keys are strings that you can use to see the contents.
# A dictionary's values can be any type of information - a string, a list, a number, even a dictionary!
# That value is tied to the key - it belongs to a key.

# The best way to think about a dictionary is a phone book or a contact list.
# How difficult would it be if we had to store contacts like this?

contacts_as_list = [
    ['Shannon', '202-555-1234'],
    ['Amy', '410-515-3000'],
    ['Jen', '301-600-5555'],
    ['Julie', '202-333-9876']
]

# What if we wanted to get Jen's phone number? It would be a pain to retrieve it!
# We'd have to loop through each item in the list and check the name, like this:

phone_we_want = 'Jen'

for contact in contacts_as_list:
    if contact[0] == phone_we_want:
        print contact[1] # The phone number

# Kind of a pain.  Luckily, dictionaries mean we don't have to do this!

print contacts['Jen']