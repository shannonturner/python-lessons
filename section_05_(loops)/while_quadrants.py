
nw_addresses = []
ne_addresses = []
sw_addresses = []
se_addresses = []
no_quadrant = []

address = raw_input("Enter an address: ")

while address.strip() != "": # every time it reaches the end of the loop it will ask: once you've stripped away all of the extra whitespace, is address an empty string?
    
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

    address = raw_input("Enter an address: ") # It's very important that we include this line to give it a chance to change the value the while loop checks.


print "NW addresses include: {0}".format(nw_addresses)
print "NE addresses include: {0}".format(ne_addresses)
print "SW addresses include: {0}".format(sw_addresses)
print "SE addresses include: {0}".format(se_addresses)
print "Addresses without a quadrant include: {0}".format(no_quadrant)

# This is pretty similar to the for_quadrants.py example, but there are some key differences.

# Most notably, in for_quadrants.py, you need to specify how many addresses to accept.
# This program will allow you to continue to enter addresses until you enter a blank line
# On older computers, this is somewhat similar to how they made the "Press any key to continue" work