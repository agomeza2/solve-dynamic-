from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURA3(movimiento rectilineo uniforme acelerado en los 3 ejes).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)