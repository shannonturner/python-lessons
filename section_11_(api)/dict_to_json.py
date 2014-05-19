# Converting Dictionaries (and lists and strings, etc) to JSON

# First, use the built-in library json.  You don't need to pip install this, it comes with python.
import json

# Next, create your dictionary.
# Using some based on https://github.com/shannonturner/python-lessons/tree/master/section_10_(dictionaries)

contacts = [
    {'friends': [
    {'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner'} },
    {'Amy': {'phone': '410-515-3000', 'fax': '410-555-3001', 'email': 'amy@amy.org'} },
    {'Jen': {'phone': '301-600-5555', 'email': 'jen@jen.biz'} },
    {'Julie': {'phone': '202-333-9876'} },
    ],
    'enemies': []}
]

# contacts is a list that holds a dictionary with two keys: friends and enemies
#       friends is a list that holds four dictionaries
#           Shannon is one dictionary, and she has a dictionary for all of the ways to contact her
#           Amy is another dictionary, and she has a dictionary for all of the ways to contact her
#           Jen is another dictionary, and she has a dictionary for all of the ways to contact her
#           Julie is another dictionary, and she has a dictionary for all of the ways to contact her
#       enemies is an empty list

# json.dumps() is used to dump your information stored as dictionaries, lists, and strings into the JSON format
print json.dumps(contacts, indent=4, sort_keys=True)
# indent=4 will indent each level as this many spaces (4), which looks way nicer than not doing this.
# sort_keys=True will sort the keys within the dictionary based on their name

# You might not see the indentation if you print to the terminal; you may need to write the output to a file to see it.
with open('contacts.json', 'w') as json_contacts:
    json_contacts.write(json.dumps(contacts, indent=4, sort_keys=True))