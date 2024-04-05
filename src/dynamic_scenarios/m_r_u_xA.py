from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURAXA(movimiento rectilineo uniforme acelerado en el eje x).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
print(data)