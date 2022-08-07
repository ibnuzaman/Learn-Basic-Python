# Belajar Casting
# Merubah dari satu tipe ke tipe lain

from os import system


data_int = 0
system("cls")
print("Data ini adalah ", type(data_int),"Yang bernilai",data_int)

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data = ",data_float,",type =",type(data_float))
print("Data = ",data_str,",type =",type(data_str))
print("Data = ",data_bool,",type =",type(data_bool))

print("---STRING---")
data_str = "";
print ("Data = ",data_str,"type = ",type(data_str))

data_int = int(data_str) # Harus angka
data_float = float(data_str) #harus angka
data_bool = bool(data_str) #false jika string kosong
print ("Data = ",data_int,"type = ",type(data_int))
print ("Data = ",data_float,"type = ",type(data_float))
print ("Data = ",data_bool,"type = ",type(data_bool))
