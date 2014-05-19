# Converting Dictionaries (and lists and strings, etc) to JSON

# First, use the built-in library json.  You don't need to pip install this, it comes with python.
import json

# Now, load the file (contacts.json) that you created in https://github.com/shannonturner/python-lessons/blob/master/section_11_(api)/dict_to_json.py
with open('contacts.json', 'r') as contacts_file:
    contacts = contacts_file.read()

print contacts

print "\n\n contacts above is a string"

# Now we have loaded the contents of the file as a string that looks like JSON.
# json.loads() will allow us to load it back into a form Python can use (and loop over)
contacts = json.loads(contacts)

print contacts

print "\n\n now you can loop over contacts, since it is a list (with dictionaries and other goodies nested within)"