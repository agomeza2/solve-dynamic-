from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURAYAZA(movimiento rectilineo uniforme en ejes y,z).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)