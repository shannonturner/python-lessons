# Example #5: Nesting exception handling

# Exception handling works the same as any other indentation level in Python

user_input = raw_input(" Example #5: enter a number: ")

try:
    user_input = int(user_input)
except ValueError:
    try:
        print "User input was either a float or a string."
        user_input = int(float(user_input))
        print "Turns out it was a float! {0}".format(user_input)
    except ValueError:
        print "Guess {0} was a string and not a number at all.".format(user_input)

print "Now the code block above works pretty much the same as the following: "

user_input = raw_input(" Example #5: enter a number: ")

try:
    user_input = int(float(user_input))
except ValueError:
    print "Guess {0} was a string and not a number at all.".format(user_input)
