# If you're new to file handling, be sure to check out with_open.py first!

with open('states.txt', 'r') as states_file:
    states = states_file.read().split("\n")

print states

# .read() is a file method that reads the file (which file? the one in the file object just before the dot) and returns the whole contents as a string.

# Instead of leaving it as a string, we're splitting the file into a list at every new line, and we save that list into the variable states

# Now we can loop over that list!

for state in states:
    print state