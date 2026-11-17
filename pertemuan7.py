# while -> looping 
# pengulangan -> waktu kita membuka aplikasi maka program berjalan (mengulang)
# perulangan berdasarkan kondisi

masukan = True
while ( not masukan == False) :
    break
    print("=== Menu ===")
    print("1. Lanjutkan menu")
    print("2. Skip menu")
    print("3. Keluar")
    print("4. segitiga")
    pilihan = input("pilih menu: ")
    if (pilihan == "3"):
        break # keluar dari looping langsung
        pilihan = False

    if (pilihan =="2") : 
    continue # skip baris kode di bawah dan lanjutin looping
    if (pilihan =="4") :
        ctr = 0
        while (ctr<5) :
            print("#" * ctr) # looping print ke kanan
            ctr = ctr + 1
    print("Menu berhasil dilanjutkan")
else : 
    print('anda memilih exit')









