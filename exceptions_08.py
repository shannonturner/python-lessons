# Example #8: try-finally

# Use an finally block attached to a try block to execute code no matter what happens

user_input = raw_input("Please enter a number: ")

try:
    user_input = int(float(user_input))

except ValueError:
    print "You didn't enter a number, did you?"
    
else: # no errors occurred
    print "Hooray! We didn't encounter any errors!"

finally: # no matter what
    print "Here was your input: {0}".format(user_input)

print "'finally' isn't that common though, and you could really just put your code outside of the block entirely."
print "Here was your input: {0}".format(user_input) # Like this!
