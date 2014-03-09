# If you're new to file handling, be sure to check out with_open.py first!
# You'll also want to check out read_text.py before this example.  
# You'll also want to check out read_csv.py before this example.  This one is a bit more advanced, and builds off read_csv.py.

with open('read_csv.csv', 'r') as states_file:
    
    # Instead of leaving the file contents as a string, we're splitting the file into a list at every new line, and we save that list into the variable states
    states = states_file.read().split("\n")
    
    # Since this is a spreadsheet in comma separated values (CSV) format, we can think of states as a list of rows.
    # But we'll need to split the columns into a list as well!

    for index, state in enumerate(states):
        states[index] = state.split(",")

# Now we have a nested list with all of the information!

# Instead of printing out the information as in read_csv.py, let's save it to a new file instead.

with open('states_pop.txt', 'w') as population_file:

    # In line 20, we create the file in a similar way to opening the file -- the only difference being the write flag (second parameter)
    # Line 20 creates a new variable called population_file, which is a file object.

    # .read() is a file method that we're pretty familiar with by now, but there's also .write()

    # .write() is a file method that allows us to write a string to a file.

    # Our header row is at state[0], so we can use that to display the information in a prettier way.
    for state in states[1:]: # We use [1:] so we skip the header row.

        # state[0] is the first column in the row, which contains the name of the state.
        population_file.write("\n---{0}---\n".format(state[0])) # Instead of printing the string, we're now writing the string to the file.

        for index, info in enumerate(state[1:]): # We use [1:] so we don't repeat the state name.
            population_file.write("{0}:\t{1}\n".format(states[0][index+1], info)) # Instead of printing the string, we're now writing the string to the file.

# Note that we had to add in some extra newlines compared to in read_csv.py; when printing, Python is generous with newlines.
# But when you're writing to a file, Python doesn't assume you want those newlines in, and you'll have to add them in yourself.