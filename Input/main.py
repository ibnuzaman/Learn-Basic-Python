from os import system



#jadi tipe data yang kebaca adalah string
system("cls")
nama = input("Masukkan nama anda = ")
print ("Nama anda adalah",nama,"Tipenya adalah",type(nama))

#jika ingin merubah tipe data tinggal meng casting tipe data
int_nama = int(input("Masukkan angka : "))
print ("Setelah di casting menjadi int",type(int_nama))