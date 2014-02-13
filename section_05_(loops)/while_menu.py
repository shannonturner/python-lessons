

instructions = """Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show the names in your list
Q to quit 
>"""

allowed_commands = ['a', 'r', 's', 'q']
names = []

command = raw_input(instructions)

while command.lower() in allowed_commands:
    
    if command.lower() == 'a':
        name = raw_input("Enter a name to add to your list: ")
        names.append(name)
    elif command.lower() == 'r':
        name = raw_input("Enter a name to remove from your list: ")
        names.pop(names.index(name)) # this will remove the first instance of this name that appears; if there are duplicates, only the first one will be removed
    elif command.lower() == 's':
        print '\n'.join(names)
    elif command.lower() == 'q':
        break # this will break out of the while loop

    command = raw_input(instructions)