from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Colisión lineal inelástica.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m1=data[0]
m2=data[1]
d=data[2]
v01=data[3]
v02=data[4]