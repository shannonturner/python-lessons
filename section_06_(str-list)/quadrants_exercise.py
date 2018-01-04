# Exercise that you'll do in front of the group during the group exercise.
# This is a rough approximation of the code that you'll end up with in the end.
# This isn't how you'll start it off.
# The first version of your code will be incomplete and a bit wrong.
# You'll talk through the exercise, soliciting feedback from the class.
# Be sure to ask lots of questions, especially "what do we expect is going to happen here?"
# Each of the problem addresses is specifically designed to cause unexpected behavior if the program isn't written carefully.
# It's a good thing to trip over these problem addresses. Students won't learn anything from seeing you do it perfectly in one go. But they'll learn a lot from the process of iterating, finding the problem, and improving.

NW = []
NE = []
SE = []
SW = []
Other = []

address = "" # Enter your addresses here.
# Problem 1: 123 SEA LANE SW
# Problem 2: 456 fake st se
# Problem 3: 678 lincoln ave

print address

address_as_list = address.upper().split(' ')

if 'NW' in address_as_list:
    NW.append(address)
elif 'NE' in address_as_list:
    NE.append(address)
elif 'SE' in address_as_list:
    SE.append(address)
elif 'SW' in address_as_list:
    SW.append(address)
else:
    Other.append(address)

print "NW is {0}".format(NW)
print "NE is {0}".format(NE)
print "SE is {0}".format(SE)
print "SW is {0}".format(SW)
print "Other is {0}".format(Other)
