# If you're new to file handling, be sure to check out with_open.py first!
# You'll also want to check out read_text.py before this example.  This one is a bit more advanced.

with open('read_csv.csv', 'r') as states_file:
    
    # Instead of leaving the file contents as a string, we're splitting the file into a list at every new line, and we save that list into the variable states
    states = states_file.read().split("\n")
    
    # Since this is a spreadsheet in comma separated values (CSV) format, we can think of states as a list of rows.
    # But we'll need to split the columns into a list as well!

    for index, state in enumerate(states):
        states[index] = state.split(",")

# Now we have a nested list with all of the information!

# Our file looks like this:
# State, Population Estimate, Percent of Total population
# California, 38332521, 11.91%
# Texas, 26448193, 8.04%
# ...

# Our header row is at state[0], so we can use that to display the information in a prettier way.
for state in states[1:]: # We use [1:] so we skip the header row.

    # state[0] is the first column in the row, which contains the name of the state.
    print "\n---{0}---".format(state[0])

    for index, info in enumerate(state[1:]): # We use [1:] so we don't repeat the state name.
        print "{0}:\t{1}".format(states[0][index+1], info)

    # states is the full list of all of the states.  It's a nested list.  The outer list contains the rows, each inner list contains the columns in that row.
    # states[0] refers to the header row of the list
    # So states[0][0] would refer to "State", states[0][1] would refer to "Population Estimate", and states[0][2] would refer to "Percent of total population"

    # state is one state within states. state is also a list, containing the name, population, and percentage of that particular state.
    # So the first time through the loop, state[0] would refer to "California", state[1] would refer to 38332521, and state[2] would refer to 11.91%
    # Since state is being create by the for loop in line 24, it gets a new value each time through.

    # We're using enumerate to get the index (slicing number) of the column we're on, along with the information.
    # That way we can pair the column name with the information, as shown in line 30.
    # NOTE: Since we're slicing from [1:] in line 29, we need to increase the index by + 1, otherwise our headers will be off by one.

# Sample output:

# ---"California"---
# "Population Estimate":  38332521
# "Percent of Total population":  "11.91%"

# ---"Texas"---
# "Population Estimate":  26448193
# "Percent of Total population":  "8.04%"

# ---"New York"---
# "Population Estimate":  19651127
# "Percent of Total population":  "6.19%"