# Example #7: try-else

# Use an else block attached to a try block when you want to execute code only when no errors occured.

user_input = raw_input("Please enter a number: ")

try:
    user_input = int(float(user_input))
except ValueError:
    print "You didn't enter a number, did you?"
    
else: # no errors occurred
    print "Hooray! We didn't encounter any errors!"
    print "Oh, by the way, your number was: {0}".format(user_input)
