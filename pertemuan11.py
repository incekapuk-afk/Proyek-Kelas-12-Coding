# tuple
# array yang dimiliki oleh pyhton
# tidak bisa dirubah datanya

contoh_tuple = ('satu', 'dua', 'tiga')
print(type(contoh_tuple))
print(contoh_tuple)
print(contoh_tuple[2]) # penting angka dua di dalam itu 
'''
for data in contoh_tuple:
    print(data)
'''
print(contoh_tuplet[-3]) # index ke tiga dari belakang, kalau negat0if berarti index ke berapa dari belakang
print(contoh_tuple[1:3]) # ambil index satu sampai index dua

thistuple = ("apple", "banana", "cherry","mango", "orange", "durian", "pineapple")
# cetak dari mango sampai durian
print(thistuple[3:6])
# cetak pineapple tapi menggunakan index negatif
print(thistuple[-1])
# cetak cherry tapi menggunakan index negatif
print(thistuple[-5])

# unpack
hewans= ('kucing', 'sapi', 'komodo')
hewan_1, hewan_2, hewan_3 = hewans
print(hewan_1)
print(hewan_2)
print(hewan_3)

'''
Tuple Berisi Angka

Buat tuple berisi angka berikut:

(10, 20, 30, 40, 50)

Tulislah program untuk menghitung:

Jumlah seluruh elemen 

Nilai terbesar dan terkecil dalam tuple

Rata rata dari total nilai tuple

'''

angka = (10, 20, 30, 40, 50)
print("Jumlah seluruh elemen:", sum(angka))
print("Nilai terbesar:", max(angka))
print("Nilai terkecil:", min(angka))
print("Rata-rata:", sum(angka)/5)


