# Challenge Level: Advanced

# Group exercise!

# Scenario: Your organization has put on three events and you have a CSV with details about those events
#           You have the event's date, a brief description, its location, how many attended, how much it cost, and some brief notes
#           File: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/events.csv

# Goal: Read this CSV into a dictionary.

# Your function should return a dictionary that looks something like this. 
# Bear in mind dictionaries have no order, so yours might look a little different!
# Note that I 'faked' the order of my dictionary by using the row numbers as my keys.

# {0: 
#     {'attendees': '12', 
#     'description': 'Film Screening', 
#     'notes': 'Panel afterwards', 
#     'cost': '$10 suggested', 
#     'location': 'In-office', 
#     'date': '1/11/2014'}, 

# 1: 
#     {'attendees': '12', 
#     'description': 'Happy Hour', 
#     'notes': 'Too loud', 
#     'cost': '0', 
#     'location': 'That bar with the drinks', 
#     'date': '2/22/2014'}, 
# 2: 
#     {'attendees': '200', 
#     'description': 'Panel Discussion', 
#     'notes': 'Full capacity and 30 on waitlist', 
#     'cost': '0', 
#     'location': 'Partner Organization', 
#     'date': '3/31/2014'}
# }