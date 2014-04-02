with open("states.csv", "r") as states_file:        
    states = states_file.read().split("\n")

for index, state in enumerate(states):
    states[index] = states[index].split(",")

    print "{0}'s abbreviation is {1}".format(states[index][1], states[index][0])    

# print states
