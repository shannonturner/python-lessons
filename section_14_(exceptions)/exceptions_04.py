# Example #4: The catch-all handler: Exception

print "Now we'll just repeat the try ... except block from Example #3 but with a catch-all for any exception."

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
except Exception, e:
    print "With any exception type (not just Exception), you can find out the detailed message specific to the error by using ', e' afterward."
    print "In this case, the detailed message was: {0}".format(e)
    print "Exception is best used in addition to other specific exceptions first."
    print "For best results, think of each except as being similar to an 'elif' statement targeting something specific; except Exception is similar to an 'else' statement being the catch-all."
