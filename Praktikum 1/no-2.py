n = int(input("Jumlah siswa: "))
inputan = {}

for i in range(n):
    nama = str(input(f"Nama siswa ke-{i + 1}: "))
    nilai = int(input(f"Masukkan nilai {nama}: "))
    inputan[nama] = nilai

print(inputan)
