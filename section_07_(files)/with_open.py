with open('states.txt', 'r') as states_file:
    states = states_file.read()

print states

# *with* is a special Python keyword that's used to create a "container" that will automatically close your file when the indentation level is broken.
#   So in line 1, the file 'states.txt' is opened, and the variable states_file is created.
#   states_file is a *file object*, which shouldn't be too scary.  We've worked with string objects and list objects without even realizing it!
#   String objects and list objects are different ways of storing information in Python, and each has its own set of functions that only work with that type of thing.
#   So string objects have string methods like .find() and .replace() -- functions that only work on strings.
#   List objects have list methods like .append() and .pop() -- functions that only work on lists.
#   We use with open('states.txt') as states_file to create a *file object*, and file objects have file methods -- functions that only work on files.

# open() is a special built-in Python function that tells Python to open a file.
#   open() can take up to two arguments/parameters.
#   The first parameter is the file you want to open.
#       If the file you want to open and the script that you're running are in the same folder, you can just say the filename, as we did in line 1.
#       Otherwise, you'll need to give Python more details on where it can find the file -- either using the full pathname of the file,
#       Or just the path from where it's looking right now. (section_07_(files))

#   The second parameter tells Python how to open the file.  This parameter is a string.
#       There are three common ways to open the file, and we'll discuss those first.
#           r: read-only mode.  Python won't make any changes to this file, but you can read from it.
#           w: write mode. If the file doesn't exist, Python will create a new file with that name.  Otherwise, Python will overwrite the existing file.
#           a: append mode. If the file doesn't exist, Python will create a new file with that name. Otherwise, Python will append to the end of the existing file.
#       And still important, but less common:
#           b: binary mode.  Use this when reading from a non-text file, like an image.

# .read() is a file method that reads the file (which file? the one in the file object just before the dot) and returns the whole contents as a string.
# In line 2 we save the entire file contents as a string, states