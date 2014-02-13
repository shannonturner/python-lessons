# start by creating four lists of your quadrants.  we'll learn a better way to do this next lesson.

nw_addresses = []
ne_addresses = []
sw_addresses = []
se_addresses = []
no_quadrant = []

for entry in range(3): # do this three times:
    address = raw_input("What is your address? ") # get the address from the user

    address = address.split(" ") # split address into a list based on the spaces

    if 'NW' in address:
        nw_addresses.append(' '.join(address)) # if 'NW' appears in address, add the address (joined back as a string) to the proper list

    elif 'NE' in address:
        ne_addresses.append(' '.join(address))

    elif 'SW' in address:
        sw_addresses.append(' '.join(address))

    elif 'SE' in address:
        se_addresses.append(' '.join(address))

    else:
        # In all other instances

        no_quadrant.append(' '.join(address))


print "NW addresses include: {0}".format(nw_addresses)
print "NE addresses include: {0}".format(ne_addresses)
print "SW addresses include: {0}".format(sw_addresses)
print "SE addresses include: {0}".format(se_addresses)
print "Addresses without a quadrant include: {0}".format(no_quadrant)

# Things to think about:

# 1) Which list would 1500 CORNWALL ST be added to? Why is that?

# 2) In other words, how does the 'in' operator work when you use it on a string versus on a list?

# 3) Thinking about it another way, if you commented out line 12 and ran that address through, you'd get a different result.