# Program ke 1 
try:
    angka = int(input("Masukkan angka: "))
    total = 0
    deret = ""

    for i in range(1, angka+1):
        total += i
        if i != angka:
            deret += str(i) + " + "
        else:
            deret += str(i)

    print(deret, "=", total)

except:
    print("Input bukan angka!")


print(total)

# Program ke 2
try:
    angka = int(input("Masukkan angka: "))
    faktorial = 1
    deret = ""

    if angka == 0:
        faktorial = 1
        deret = "0! = 1"
    else:
        for i in range(angka, 0, -1):
            faktorial *= i
            if i != 1:
                deret += str(i) + " * "
            else:
                deret += str(i)

    print(f"{angka}! = {deret} = {faktorial}")

except:
    print("Input bukan angka!")


# Program ke 3 
try:
    rahasia = 999
    while True:
        tebakan = int(input("Masukkan tebakan angka: "))

        if tebakan == rahasia:
            print("Tebakan benar!")
            break
        else:
            print("Tebakan salah")
            
except:
    print("Input bukan angka!")