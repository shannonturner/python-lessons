import requests

title = raw_input("Enter your movie: ")

url = 'http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}'.format(title).replace(" ","+").replace("'","&#39;")

print url

response = requests.get(url).json()

print response

# Search for 'matrix' gives the following JSON response (this is printed at line 11):

# [
#     {
#         u'rating': u'3', 
#         u'submitterid': u'1', 
#         u'imdbid': u'0234215', 
#         u'title': u'Matrix Reloaded, The', 
#         u'dubious': u'0', 
#         u'visible': u'1', 
#         u'year': u'2003', 
#         u'date': u'2008-07-21 00:00:00', 
#         u'id': u'58'
#     },

#     {
#         u'rating': u'3', 
#         u'submitterid': u'1', 
#         u'imdbid': u'0242653', 
#         u'title': u'Matrix Revolutions, The', 
#         u'dubious': u'0', 
#         u'visible': u'1', 
#         u'year': u'2003', 
#         u'date': u'2008-07-21 00:00:00', 
#         u'id': u'59'
#     }, 

#     {
#         u'rating': u'1', 
#         u'submitterid': u'7916', 
#         u'imdbid': u'0303678', 
#         u'title': u'Armitage: Dual Matrix', 
#         u'dubious': u'1', 
#         u'visible': u'1', 
#         u'year': u'2002', 
#         u'date': u'2013-08-01 15:26:03', 
#         u'id': u'4429'
#     }, 

#     {
#         u'rating': u'3', 
#         u'submitterid': u'1', 
#         u'imdbid': u'0133093', 
#         u'title': u'Matrix, The', 
#         u'dubious': u'0', 
#         u'visible': u'1', 
#         u'year': u'1999', 
#         u'date': u'2008-07-20 00:00:00', 
#         u'id': u'36'
#     }
# ]

# Which is then looped through
for movie in response:
    print movie['title'], movie['rating']

# And printed:
# Matrix Reloaded, The 3
# Matrix Revolutions, The 3
# Armitage: Dual Matrix 1
# Matrix, The 3