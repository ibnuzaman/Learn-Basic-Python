from ctypes import c_double
from operator import truediv


x_integer = 10
print("Nilai x adalah",x_integer)
print("Bertipe",type(x_integer))

x_float = 10.22
print("Ini tipe data", type(x_float))
print("Dengan nilai",x_float)

x_string = "Sayang"
print("Ini adalah tipe data", type(x_string))
print("Isinnya adalah", x_string)

x_binner = True
print("ini adalah tipe data", type(x_binner))
print("Bernilai", x_binner)

x_binner = False
print("ini adalah tipe data", type(x_binner))
print("Bernilai", x_binner)

#Tipe data khusus

#tipe data kompleks
x_complex = complex(5,9)
print("Ini adalah tipe data", x_complex)
print("Bernilai", x_complex)

#Tipe data dari bahasa C
x_c_double = c_double(10.77)
print("Bernilai", x_c_double)
print("Ini adalah tipe data dari bahasa C ",type(x_c_double))