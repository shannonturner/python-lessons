# Basic bingo using zip()

words = ['apple', 'banana', 'carrot', 'danke', 'elephant', 'fruit', 'gorilla', 'horse, michael', 'ice cream', 'jack, one eye', 'kazoo', 'lollerskates', 'mango', 'noodles', 'oboe', 'porcupine', 'quill', 'rowboat', 'sailboat', 'trolley', 'umbrella', 'voltage', 'watermelon', 'xylophobe', 'yarn', 'zebra-clops']

print "words has {0} words in the list.".format(len(words))

output = ''

# Normal for loops allow you to loop over a list and do something for each item in that list.
# A for loop using zip() allows you to loop over multiple lists and do something with each item in those lists at the same time.
# Normally, you'll want to do that with lists that are the same size.  But it still works if one list is shorter; it just behaves a little differently.

# In this case, words is 26 items long and range(25) is 25 items long
# So the for loop will only run 25 times in this case.

# No matter how many more items you add to words, your bingo board should only have 25 squares.

# If you uncomment lines #19 and #20, you'll get a random bingo board every time you run!
# import random
# random.shuffle(words)

for word, position in zip(words, range(25)):

	if position == 12:
		output += 'Free space,'
	else:
		output += "{0},".format(word)

	if position in (4,9,14,19,24):
		output += "\n"

print output

# apple,banana,carrot,danke,elephant,
# fruit,gorilla,horse, michael,ice cream,jack, one eye,
# kazoo,lollerskates,Free space,noodles,oboe,
# porcupine,quill,rowboat,sailboat,trolley,
# umbrella,voltage,watermelon,xylophobe,yarn,