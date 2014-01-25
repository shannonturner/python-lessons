# Volunteer recruitment
# Change these variables to change the behavior of your program
volunteers_goal = 20
current_volunteers = 100

# Is current_volunteers less than, equal to, or greater than volunteers_goal?

if current_volunteers < volunteers_goal:
	print "You still have {0} volunteers to recruit!".format(volunteers_goal - current_volunteers)
elif current_volunteers == volunteers_goal:
	print "You met your goal exactly! Way to go!"
elif current_volunteers > volunteers_goal:
	print "You exceeded your recruitment goals by {0}! Way to go!".format(current_volunteers - volunteers_goal)