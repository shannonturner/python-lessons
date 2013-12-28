
# Variable assignment

# In Python (or any programming language), variables hold information that you can access, use, and change
# In Python, there are lots of different types of information that you can hold

# Some languages make you decide early on what type of information you want to store, or even what the name of a variable is, before you even get started.
# I like Python because it's flexible and forgiving.


# Rules of variable names
# -----------------------
# Variables must begin with a letter or underscore
# Variables may contain letters and numbers and underscores, but not spaces
# Variables can't be named the same thing as built-in Python commands

# If you see a word on its own that isn't reserved to Python, chances are it's a variable.

lesson_section = 1 # General Programming Basics
lesson_subsection = 2 # Variable Assignment

# In line 19, I'm telling Python I want to create a variable called 'section' and set it equal to 1

# Shannon's Rules of variable names
# ---------------------------------
# Variables should be descriptive, even if it means their names are long
# You should be able to show your code to anyone and they'll know exactly information what a given variable holds
# Use underscores to break up words!

# We've stored values inside of lesson_section and lesson_subsection, so now let's use them!

print "We are on Section #", lesson_section
print "And this is unit #", lesson_subsection, ", which covers Variable Assignment"

print "Take another look at the code for the basic math unit."
print "Anywhere you see a number in that code, you can replace it with a variable that holds a number instead."

# Let's see that in practice:
days_in_a_year = 365 # Beautifully descriptive variable names are their own comments
my_age = 21 # yeah, right!

print "My age is ", my_age, ", and I've been alive for ", days_in_a_year * my_age, " days, give or take."

# Now let's change the value stored in days_in_a_year to account for leap years and try it again.

days_in_a_year = days_in_a_year + .25 # Equivalent to days_in_a_year = 365 + .25

print "My age is ", my_age, ", and I've been alive for ", days_in_a_year * my_age, " days, give or take, now that I'm including leap years."





















