# You can also handle multiple types of exceptions in the same block

# In the example below, changing age at line five will change the behavior of the program.
# If age can be converted to an int, line 13 will run.
# If age is a string, but cannot be converted to an int, a ValueError will occur
# If age is a different type of thing (a dictionary, list, etc), 
#       a TypeError will occur since those cannot be converted into a list

age = '' # try with 100 or with 'x100' or with ['100'] or with None or with False or with {'age': 100}

try:
    age = int(age)
except (TypeError, ValueError) as err:
    print "Invalid entry: {0}; error: {1}".format(age, err)
else:
    print "Your age is: {0}".format(age)