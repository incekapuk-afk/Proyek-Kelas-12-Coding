# while -> Looping yang berdasarkan kondisi
# for -> Looping yang berdasarkan step / banyak nya berapa 

# nested looping 

# buat sebuah cetak bangun datar sederhana :D 
'''
for y in range(4):
    for x in range (4):
        print('x',end='')
    print('')
''' 
'''
for y in range(4):
    for x in range(y + 1):
        print('*', end='')
    print('')
'''
'''
for y in range(4):
    for x in range(4 - y, 0, -1):
        print(y + 1, end='')
    print('')
'''

for y in range (4,0, -1):
    for x in range(y):
        print(y, end='')
    print('')