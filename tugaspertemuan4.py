 # 1 – Penjumlahan Sederhana
angka1 = int(input("Angka pertama = "))
angka2 = int(input("Angka kedua = "))
hasil = angka1 + angka2
print(f"Hasil dari {angka1} + {angka2} adalah {hasil}")


# 2 – Luas Persegi Panjang
panjang_x = float(input("panjang: "))
lebar_y = float(input("lebar: "))
luas_z = panjang_x * lebar_y
print(f"Luas persegi panjang dengan panjang {panjang_x} dan lebar {lebar_y} adalah luas {luas_z}")

# 3 – Rata-rata 3 Nilai
nilaiA = float(input("Masukkan nilainya: "))
nilaiB = float(input("Masukkan nilainya: "))
nilaiC = float(input("Masukkan nilainya: "))
rata_rata = (nilaiA + nilaiB + nilaiC) / 3
print(f"Rata-rata dari {nilaiA}, {nilaiB}, dan {nilaiC} adalah {rata_rata}")

# 4 – Hitung Usia 
nama = input("Masukkan nama: ")
Tahun_lahir = int(input("Tahun lahir: "))
usia = 2025 - Tahun_lahir
print(f"Halo {nama}, usia kamu sekarang adalah {usia} tahun.")

# 5 – Konversi Suhu
SuhuC = float(input("Suhu Celcius: "))
RumusF = (SuhuC * 9/5) + 32
print(f"Konversi dari suhu Celcius {SuhuC} ke suhu Fahrenheit adalah {RumusF}")