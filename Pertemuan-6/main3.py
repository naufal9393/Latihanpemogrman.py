
from utilitas_akademik import (
    hitung_ipk,
    konversi_nilai_huruf,
    generate_transkrip
)

mahasiswa = {
    "nama": "Naufal Fauzan Azmi",
    "nim": "123456789"
}

nilai_mata_kuliah = {
    "Struktur Data": 85,
    "Basis Data": 78,
    "Pemrograman Web": 90,
    "Sistem Informasi": 70
}

total_bobot = 10.0
total_sks = 3

ipk = hitung_ipk(total_bobot, total_sks)

print("IPK:", round(ipk, 2))
print("Nilai huruf untuk 85:", konversi_nilai_huruf(85))

print()
generate_transkrip(mahasiswa, nilai_mata_kuliah)
