def open_csvfile(filename, delimiter=','):

    with open(filename, "r") as csv_file:        
        rows = csv_file.read().split("\n")

    for index, row in enumerate(rows):
        rows[index] = row.split(delimiter)

    return rows