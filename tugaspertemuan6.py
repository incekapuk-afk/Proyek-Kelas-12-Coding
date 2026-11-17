# TUGAS CODING
# NO 1

try:
    angka = int(input("Masukkan angka tebakan: "))
    if angka == 7:
        print("Tebakan benar")
    elif angka > 7:
        print("Terlalu besar")
    else: 
        print("Terlalu kecil")
except:
    print("Input bukan angka!")

print("-" * 40) 

# NO 2
try:
    nilai = float(input("Masukkan nilai ujian: "))
    if nilai >= 90:
        print("Lulus dengan predikat istimewa")
    elif nilai >= 75:
        print("Lulus")
    else:
        print("Tidak lulus")
except:
    print("Input bukan angka!")

# NO 3
try:
    umur = int(input("Masukkan umur: "))
    if umur < 13:
        print("Anak-anak")
    elif umur < 18:
        print("Remaja")
    elif umur < 60:
        print("Dewasa")
    else:
        print("Lansia")
except:
    print("Input bukan angka!")

print("-" * 40)

# NO 4
try:
    umur = int(input("Masukkan umur penonton: "))
    if umur < 5:
        print("Tiket gratis")
    elif umur < 13:
        print("Harga tiket Rp25.000")
    elif umur < 60:
        print("Harga tiket Rp50.000")
    else:
        print("Harga tiket Rp30.000")
except:
    print("Input bukan angka!")

print("-" * 40)

# NO 5
try:
    angka = int(input("Masukkan angka (1-5): "))
    if angka == 1:
        print("A")
    elif angka == 2:
        print("B")
    elif angka == 3:
        print("C")
    elif angka == 4:
        print("D")
    elif angka == 5:
        print("E")
    else:
        print("Tidak valid")
except:
    print("Input bukan angka!")

print("-" * 40)