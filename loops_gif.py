days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
foods_of_day = ['Manicotti', 'Tacos', 'Waffles', 'Raspberries', 'Franks', 'Salad', 'Soup']

# Example #1
for day in days_of_week:
    print "Today is {0}".format(day)
print "\n"


# Example #2: Enumerate (gives the index of the list item)
for (index, day) in enumerate(days_of_week):

    print "Today is the {0}th day of the week, which is {1}".format(index, day) # Please pardon/ignore 0th day and the grammar for "1th", "2th", "3th"

    # In this loop using enumerate, we can access the values of list items in two ways: directly using the looping variable day (which is preferred), or using the index.

    print "So day_of_week[{0}] is: {1}, which is the same as day, which is: {2}".format(index, days_of_week[index], day)
print "\n"

# Example #3: Zip
for (day, food) in zip(days_of_week, foods_of_day):
    print "Today is {0} so obviously I'm having {1} for dinner.".format(day, food)

# NOTE: zip relies on each list being the same length! If the lists are not the same length, zip will only loop through as many items as are in the shorter list!
