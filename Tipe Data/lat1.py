from os import system
from unicodedata import name

#system("cls")
nama = input("Masukkan nama\t\t: ")
tgl  = input("Masukkan tanggal lahir\t: ")
job  = input("Masukkan pekerjaan\t: ")

system("cls")
print("DATA INPUTAN USER")
print("Nama\t\t: ",nama)
print("Tanggal lahir\t: ",tgl)
print("Pekerjaan\t: ",job)