# String methods: string.find()

# string.find() tells you where you can find a part of one string in a larger string.
# string.find() will return a number:
# 		if string.find() returns -1, it could not find the string inside the larger string.
#		otherwise, string.find() will return the slicing number/index of where it found that string

email_address = "hoorayforpython@notarealwebsite.com"

print "I found the snail at: {0}".format(email_address.find("@")) # the slicing number/index of where the at symbol appears

# string.find() + slicing = awesome!

# Everything before the @ is part of the email_handle; everything after the @ is part of the domain where they have their email registered.
# Let's use string.find() and slicing together to split those apart.

at_symbol_index = email_address.find("@")

print "I found the snail at: {0}".format(at_symbol_index) # Notice how line 10 and 19 each give the same result, but take a different approach

email_handle = email_address[0:at_symbol_index]

print "The email_handle is: {0}".format(email_handle)

email_domain = email_address[at_symbol_index + 1:] # without the +1, the at symbol would be included. Notice that there is no number after the colon, so Python assumes you want everything to the end.

print "The email_domain is: {0}".format(email_domain)

print "When string.find() can't find a string, it'll give a -1.  So since there's no 'QQQ' in email_address, this will return a -1: {0}".format(email_address.find("QQQ"))