import re 
def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into individual data points
            line_data = line.split()
            # Convert data points to appropriate data types if needed
            # For example, if you expect integers: line_data = [int(x) for x in line_data]
            data.extend(line_data)  # Add data points to the array
    return data


def filter_numbers(array):
    number_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    return [x for x in array if number_pattern.match(x)]
    
def float_array(array):
    num_array =  [float(x) for x in array]
    return num_array
