# tipe data = cara / bentuk dari data yang di simpan 

angka = 10 # tipe data angka bulat > ini (interger)
kalimat = 'Reynhard' # tipe data kalimat > str (string)
angka_koma = 10.5 # tipe adata angka koma > float 
flag = True # tipe data boolean > bool
print(type(angka)) # cek untuk tipe datanya 
print(type(kalimat))
print(type(angka_koma))
print(type(flag))
angka =int("b") # typecast -> serubah tipe data
kalimat = str(300) # dari angka ke kalimat / string
cek = bool("Bitch") # bentuknya jadi true 
print(type(angka))

# operator 
# +, -, +, /, %
penjumlahan = 2 + 4
penjumlahan = angka + 5
print(penjumlahan) # angka berapa??
concat = f" ini adalah hasilnya {penjumlahan}" #menggabungkan kelimat dengan angka   
print(concat) 
concat2 = "Text" + "halo"
print(concat2)

pengurangan = 2 - 4
print(pengurangan)

perkalian = 2 * 8
print(perkalian)

pembagian = 2 / 4
print(pembagian)

modulo = 5 % 3
print(modulo)