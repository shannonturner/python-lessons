# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' }, 
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey


# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# ...

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).