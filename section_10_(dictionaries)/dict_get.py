# If you're new to dictionaries, you might want to start with dict_access.py

# We create a dictionary.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

name = raw_input("Enter the name of the person whose phone number you want: ")

print "We will get a KeyError if you entered a name that wasn't in the dictionary."
print "{0}'s number is: {1}".format(name, contacts[name])

print "But there's a way we don't need to worry about KeyErrors."

name = raw_input("Enter the name of the person whose phone number you want ... might I suggest Frankenstein? ")

# .get() is a dictionary method that lets us safely access a dictionary even if that key doesn't exist.

print "{0}'s number is ... {1}".format(name, contacts.get(name, " ... I couldn't find it!"))