# String Formatting

# String formatting is how we can use variables (which store information including numbers, strings, and other types of data) inside of strings
# We can do this by using the .format() string method.

# Here's how it works:

# First, we'll need a variable:
name = "Shannon"

# Now, let's insert it into the print statement:
print "My name is {0}".format(name) # This will print "My name is Shannon"

# We'll analyze each part of the syntax in a moment.  For now, why is this preferable to doing a print "My name is Shannon"?

# Using .format() is more flexible and allows your strings to change as your variables change.

# So let's give the name variable a new value.
name = "Pumpkin"

# Now, let's print it again
print "My name is {0}".format(name) # This will print "My name is Pumpkin"

# Remember that Python runs commands from top to bottom, left to right.

# The two new parts of this print statement are the {0} and the .format(name)

# The {0} is a placeholder for the 0th variable in the list that appears inside the parentheses of .format() -- remember Python starts counting at 0, not 1
# So it really just keeps the spot warm.

# To see why it's {0}, let's define a few more variables.

age = 100
location = "The Pumpkin Patch"

# Now if we want to include those variables, we'll need to put placeholders in the string as well.
print "My name is {0} and my age is {1} and I live in {2}".format(name, age, location)

# Note how we put the placeholders exactly in the string where we want them; and the variables go inside the parentheses of the .format()

# Remember how Python counts.
# So {0} is a placeholder for name;
# {1} is a placeholder for age;
# and {2} is a placeholder for location

# If we had more variables to include, we'd continue in the same way.

# But there's more than one way to do this:
print "My name is {name} and my age is {age} and I live in {location}".format(name=name, age=age, location=location) # This way feels more explicit

# Only some of the ways string formatting is used are covered here. If you'd like to continue to learn all of the ways to use it:
# This is a great guide for lots of different string formatting options: http://ebeab.com/2012/10/10/python-string-format/
#	NOTE: Their examples using the print statement use Python version 3; since we're using 2.7, any time you see print("something") in their examples, using print "something" instead
