
# Twelve Days of Christmas, Python style

gifts = ["A partridge in a pear tree",
         "Two turtle doves",
         "Three french hens",
         "Four colly birds",
         "Five golden rings",
         "Six geese-a-laying",
         "Seven swans-a-swimming",
         "Eight maids-a-milking",
         "Nine ladies dancing",
         "Ten lords-a-leaping",
         "Eleven pipers piping",
         "Twelve drummers drumming"
         ]

gifts_given = []

for day in range(1,13): # identical to the statement   for day in [1,2,3,4,5,6,7,8,9,10,11,12]:

    gifts_given.extend(gifts[:day]) # use list.extend() when adding one or more items to the end of a list; use append to add a single item to a list.
    # If you were to use .append() instead of .extend() here, you would get a list of lists -- not exactly what we want in this case.

    if day == 1:
        suffix = "st"
    elif day == 2:
        suffix = "nd"
    elif day == 3:
        suffix = "rd"
    elif day >= 4:
        suffix = "th"

    print "---------------------------------------------------------"
    print "On the {0}{1} day of Christmas, my true love gave to me: ".format(day, suffix)
    print "---------------------------------------------------------"

    print "\t" + "\n\t".join(reversed(gifts[:day]))

print "---------------------------------------------------------"
print "The gifts I have received in total are: "
print "---------------------------------------------------------"

print "\t" + "\n\t".join(sorted(gifts_given))

print "---------------------------------------------------------"
print "Over all twelve days I received: "
print "---------------------------------------------------------"

total_gifts = 0

for repetitions, day in zip(reversed(range(1,13)), range(1,13)):
    print "{0} of {1}".format(repetitions * day, gifts[day-1][gifts[day-1].index(' ')+1:]) # Complex slicing going on here!
    total_gifts += repetitions * day

print "I received {0} gifts in total".format(total_gifts)

# Complex Slicing Note:

# The first word in each gift is how many was received on that day.
# So I can access the gift itself (and not the number received) by
# slicing past the index of the first space in each string.

# gifts[day-1] is the current gift, which is a string containing the name of the gift (including the number)
# Slicing on that string (beginning at the index of where the first space occurs) lets us take out the number and just get the gift itself.

# So in other words:

# gifts = ["A partridge in a pear tree", ... ]
# Since gifts is a list, we can access the gift items by slicing.

# gifts[2] is a string, "Three french hens"
# gifts[2][0] is a string, "T"

# But we don't want to start at gifts[2][0].
# We want to start at gifts[2][5] - but it won't be 5 each time; it will be different for each gift.

# If we did a "Three french hens".index(' ')+1, we would get the index just past the first space that appears.

# So we insert that into the second slice index, and add the : to ensure that it continues through until the end.

# So: gifts[day-1][gifts[day-1].index(' ')+1:]
