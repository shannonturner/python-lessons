
def csvtodict(filename):
    
    with open(filename, 'r') as csv_file:
        text = csv_file.read().strip().split('\n')

    header_row = text[0].split(',')

    dictionary = {}

    for row, line in enumerate(text[1:]):

        dictionary[row] = {}

        for col, cell in enumerate(line.split(',')):

            dictionary[row][header_row[col]] = cell


    return dictionary


print csvtodict('events.csv')
