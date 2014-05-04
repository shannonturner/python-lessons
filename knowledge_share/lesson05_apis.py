# Knowledge Sharing from Lesson 5: APIs

print len(response)

if response == []:
    print "Sorry not found"

if title[0:3] == 'The':
    title = title.replace("The", "")

if title.isdigits():
    print "It's all digits!"

# Getting KeyErrors? use .get()

if response.get('title'):
    print "There's a title here"

# Don't do too much at once!
# Break it down step by step.

# Be sure to use the right endpoint and parameters

# Getting user input to attach as a parameter
title = raw_input("What movie do you want? ")

url = 'http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}'.format(title).replace(" ","+").replace("'","&#39;")

print url

response = requests.get(url).json()

# Formatting of an IMDB ID vs. a title

# Having lots of users makes testing great

# Use multiple raw_inputs if it didn't find the movie!

# Sometimes the endpoints return different responses!

# Removing spaces from the user input
title = title.strip()

# Removing 'The' from the user input ... any of these characters
title = title.strip('The')

if title[0:4] == 'The ':
    title = title[4:]

# ASCII replaces: www.asciitables.com
import urllib
url = urllib.quote(url)

response = requests.get(url)

# Using .get() to avoid KeyErrors
# Using .get('key', 'ifnotfound')

# Converting the responses to the format we needed

# Using multiple APIs: sometimes the parameters need adjustment

# Thelma and Louise? Don't remove the 'The'

# Loop through and test -- you can't fix every user error

# Mash on your keyboard for user testing

title = 'lsdfasdjflksjflksd'

# Don't forget .json()
