from readfile import * 

filename ='data_Péndulo resorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)