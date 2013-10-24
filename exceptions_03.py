# Example #3: Different types of exceptions can be caught.

print "Example #3: Phonebook!"

phonebook = {}

while True: # this will loop forever until we issue a break!

    key = raw_input(" (Ex #3, Phonebook) Please enter a person's name, or leave blank to quit: ")

    if key == '':
        break
    
    value = raw_input(" (Ex #3, Phonebook) Please enter {0}'s phone number with no punctuation: ")

    phonebook[key] = value


user_input = raw_input(" Okay, now we're done entering names. Please enter the name of the person whose number you would like: ")

try:
    print int(phonebook[user_input])
except KeyError:
    print "You don't have {0}'s phone number!".format(user_input)
except ValueError:
    print "You typed in punctuation, didn't you?"
    print "Here's the number anyway ... {0}".format(phonebook[user_input])
