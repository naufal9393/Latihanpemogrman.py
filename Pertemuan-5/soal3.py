
# Soal 3: Operasi Set Penerima Beasiswa

# Dua list ID mahasiswa (data contoh)
beasiswa_a = [
    "20241320023",
    "20241320024",
    "20241320025",
    "20241320026"
]

beasiswa_b = [
    "20241320025",
    "20241320026",
    "20241320027",
    "20241320028"
]

# Mengubah list menjadi set
set_a = set(beasiswa_a)
set_b = set(beasiswa_b)

# (a) Menerima kedua beasiswa
kedua_beasiswa = set_a & set_b

# (b) Hanya menerima beasiswa A
hanya_a = set_a - set_b

# (c) Menerima B tetapi tidak A
bukan_a = set_b - set_a

# (d) Semua penerima unik
semua_penerima = set_a | set_b

print("Penerima kedua beasiswa:", sorted(kedua_beasiswa))
print("Hanya beasiswa A:", sorted(hanya_a))
print("Beasiswa B tetapi tidak A:", sorted(bukan_a))
print("Semua penerima unik:", sorted(semua_penerima))
