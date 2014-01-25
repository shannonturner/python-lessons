# String methods: string.lower()

# string.lower() is used for turning all characters in your string lowercase.
# There are some related string methods too, like string.upper()

name = "SHANNON!!"

print name.lower() # shannon!!
print name # it's back to the original of SHANNON!!

# To make the changes stick:
name = name.lower()

print name # shannon!!


# string.upper() will turn all characters in your string uppercase but otherwise works in the same manner as string.lower()

greeting = "hello, hi" # not very exuberant ...

print greeting.upper() # MUCH BETTER!

# Making the changes stick:
greeting = greeting.upper()

print greeting # HELLO, hi


# string.lower() and .upper() are primarily used for testing strings in a case-insensitive manner

gender = 'F'

if gender.lower() == 'f':
	print "Hi lady!"

# To accomplish the same thing without string.lower(), you would have to do:
if gender == 'F' or gender == 'f':
	print "Hi lady!"