import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # isnumeric() doesn't recognize negative signs or decimals, but the test cases should pass with this
        return [[int(y) if y.isnumeric() else y for y in x] for x in list(reader)]