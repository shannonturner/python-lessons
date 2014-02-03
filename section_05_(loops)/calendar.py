months_in_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Note how in line 6 we slice on the list we are looping over instead of looping over the entire list of months.
for month in months_in_year[0:6]: # For each month in the first six months ...
		print "\n"
		print month
		print "\n"

		for week in range(1, 5):
				print "Week {0}".format(week)

				# Notice that we're slicing again in line 15 instead of looping over the entire week.
				for day in days_of_week[-2:]: # For the last two days of the week (Saturday and Sunday)
						print day

# By removing the slicing from lines 6 and 15, we get the full year (or at least 12 months with 4 weeks of 7 days)