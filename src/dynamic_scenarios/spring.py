from readfile import * 
from vpython import * 
filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Resorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
k=data[1]
x0=data[2]
