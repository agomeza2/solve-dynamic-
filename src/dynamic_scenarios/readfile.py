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


