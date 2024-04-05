from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURAXAZA(movimiento rectilineo uniforme acelerado en ejes x,z).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)