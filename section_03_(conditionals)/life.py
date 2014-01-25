# What you can do in life
# Change the age and gender to change the behavior of this program

# Note the indentation levels and the nesting of different if and elif statements.

age = 10
gender = 'f'

if age < 2:
	print "You can eat and poo all day and people will fall all over themselves over how adorable you are"

elif age == 2:
	print "You can throw tantrums and it's pretty much expected"

elif age == 3:
	print "By this point, you are the master of object permanence."

elif 4 <= age <= 6: # is age between 4 and 6?
	print "This seems like a good time to learn how to read."

	if age == 4:
		print "How about some preschool?"
	elif age == 5:
		print "Kindergarten is cool -- nap time rocks.  Don't forget to share."
	elif age == 6:
		print "First grade.  Naptime is a thing of the past. You're probably too stubborn to be upset much by this."

elif 7 <= age <= 9: # is age between 7 and 9?
	print "Grade school goes by so quickly"

elif 10 <= age <= 11: # is age between 10 and 11?
	print "Middle school is kind of neat."

	if age == 10:
		print "Health class for the first time ..."

		if gender.lower() == 'f':
			print "... Well, that explains a lot, really."
		elif gender.lower() == 'm':
			print "Wonder what the girls are all talking about?"

	elif age == 11:
		print "The periodic table is SO COOL"

elif 12 <= age <= 13: # is age between 12 and 13?
	print "Junior high, aka welcome to hormone land"
	print "PS: sucks to be you"

elif 14 <= age <= 17: # is age between 14 and 17?
	print "High school was probably the worst"
	print "Why on earth did everyone say it was the best time of their life?"

	if age >= 16:
		print "But you can drive, so you've got that going for you"

elif age == 18:
	print "So you're technically an adult now. But not really."
	print "But you can vote, so you've got that going for you."
	print "PS: you have responsibilities now. sucks to be you"

	if gender.lower() == 'm':
		print "Better register for the draft."

elif 19 <= age <= 20:
	print "Now's a good time to be in college."

elif age == 21:
	print "Well, you can drink now."

elif 22 <= age <= 24:
	print "Graduating college and spoiling your liver, mostly."

elif age == 25:
	print "You can rent a car now.  You know, that's never actually come up for me, but apparently it's a thing ..."

else: # In all other cases not covered by the ifs and elifs above

	print "You're an adult.  Do what you want."

	if age > 30 and gender.lower() == 'f': # Note that both of these conditions must be true
		print "Meddling folks are going to start hectoring you about your love life.  Yawn."

	# Notice how the if statements below are all evaluated independently

	if age > 40:
		print "You're over the hill"

	if age > 50:
		print "Everything hurts and your children never call."

	if age > 70:
		print "You're old enough not to care about anything.  You can now do what you like with total impunity."