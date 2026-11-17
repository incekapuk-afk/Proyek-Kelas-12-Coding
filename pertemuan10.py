# array 
# sekumpulan data yang di simpan pada satu tempat / variabel yang dapat menampung
# banyak data
# untuk mengakses data dibutuhkan index

# list, tuple, set dictionary

#list 
# -> array yang dapat diubah datanya
# -> datanya dapat diurutkan, dan dapat menampung data kembar
# -> index/kuncinya berupa angka, selalu dimulai dari angka nol
nama_murid = ['Fendy','Yongki', 'Yobel', 'Danu']
print(nama_murid)
print(nama_murid[2])
nama_murid[2] = 'Daud'
print(nama_murid[2]) #akses salah satu data
print(type(nama_murid)) #mendapatkan jenis / type 
print(len(nama_murid)) #mendapatkan panjang
print(nama_murid[1:3]) #menampilkan data dengan index 1 sampai 2(karena 3 batas atas)

nama_murid.append('Budi') #menambahkan data pada bagian akhir
print(nama_murid)

nama_terhapus = nama_murid.pop(1) #menghapus data, kalau tidak di tuliksan maka index terhakhir yang diambil
print(nama_murid)
print(nama_terhapus)

nama_hewan = ['Kucing', 'Anjing', 'Kuda', 'Burung', 'Ikan', 'Kelinci', 'Gajah', 'Singa', 'Panda', 'Ular']
print(nama_hewan)

nama_hewan[2] = 'Nautilus'
print(nama_hewan)

nama_hewan.pop()
print(nama_hewan)


