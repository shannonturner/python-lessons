def is_alphaspace(string):

    """
    Returns True if all characters in the string are spaces or letters; otherwise returns False.

    using str.isalpha() returns a bool on whether ALL of the characters in a string are letters
    using str.isspace() returns a bool on whether ALL of the characters in a string are whitespace;

    Although it's not a string method, this function combines the functionality of the string methods above        
    """
    
    return all([any([char.isspace(), char.isalpha()]) for char in string])

# This custom function will behave similarly to the str.isalpha() and str.isspace() combined together.

test_string = "This string will return false for each of isalpha and isspace but it will return true for the custom function"

print "test_string.isalpha() gives us: ", test_string.isalpha()
print "test_string.isspace() gives us: ", test_string.isspace()

# Note how the syntax differs.  That's because is_alphaspace() isn't a string method, it's a custom function.
print "But is_alphaspace(test_string) gives us: ", is_alphaspace(test_string)

