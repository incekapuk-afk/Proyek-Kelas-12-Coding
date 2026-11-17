from gtts import GTTS
import os

# 1. Teks yang ingin diucapkan
kalimat = "Hail fuhrer! Saya adalah entitas absolute 100% manusia yang memiliki identitas sebagai siswa."

# 2. Mengubah teks jadi suara  (Pilih bhasa 'id' untuk Indonesia)
suara = gTTS(text=kalimat, lang='d', slow=False)

# 3. Menyimpan suara ke dalam file mp3
suara.save("robot.mp3")

# 4. Memainkan file mp3 tersebut
os.system("start robot.mp3") #(Gunakan afplay untuk Mac)