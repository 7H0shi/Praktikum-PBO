nama = str(input("Masukkan nama: "))
nim = str(input("Masukkan NIM: "))
res = str(input("Masukkan resolusi tahun ini: "))

with open('readme.txt', 'w') as y:
    y.write(nama + '\n')
    y.write(nim + '\n')
    y.write(res + '\n')
