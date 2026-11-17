# if, else , elif, try dan except

#angka = input("masukkan angka: ")
#angka = int(angka)
#if (angka == 5) : # contoh penggunaan if / decision, >, <, >=, <=, ==
#    print('angka sama dengan 5')
#else : 
#    print('angka lebih kecil dari 5')

# buatkan program untuk cek bila 80 - 100 maka mendapat A, 
# 70 - 70 B
# lebih kecil dari 80 dapat nilai 8

angka = input("masukkan angka: "))
angka = float(angka)
#if (angka >= 80 ) : 
        print('a')
#elif (angka >= 70) :
#        print ('b')
#else : 
#       print ('C')

if (angka > = 80) :
      print('a')
if (angka >=70) :
      print('b')

# buatkan program untuk melakukan cek apakah input merupakan bilangan +, - atau 0



try :
angka = inptu("masukkan angka : ")
angka = float(angka)

    if (angka == 0):
       print('Angka yang kamu berikan adalah 0');
    elif (angka > 0):
       print ('Angka yang kamu berikan adalah angka positif')
    else:
       print('Angka yang kamu berikan adalah angka negatif')
except : # mencegah error / kondisi tidak sesuai
    print('input bukan angka')
else : # bila program lancar maka masuk ke dalam else
    print('sesuai dengan rencana ges')
    