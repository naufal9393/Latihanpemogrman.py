
from sistem_informasi.service.mahasiswa_service import (
    tambah_mahasiswa,
    tampilkan_semua,
    cari_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)

from sistem_informasi.utils.format_data import (
    tampilkan_mahasiswa,
    tampilkan_daftar
)


print("=== SISTEM INFORMASI MAHASISWA ===")

# 1. Create: menambahkan data
print("\n1. TAMBAH MAHASISWA")
print(tambah_mahasiswa("23001", "Naufal", "Sistem Informasi"))
print(tambah_mahasiswa("23002", "Adi", "Informatika"))

# 2. Read: menampilkan semua data
print("\n2. TAMPILKAN SEMUA MAHASISWA")
tampilkan_daftar(tampilkan_semua())

# 3. Search: mencari mahasiswa
print("\n3. CARI MAHASISWA")
tampilkan_mahasiswa(cari_mahasiswa("23001"))

# 4. Update: mengubah data mahasiswa
print("\n4. UBAH DATA MAHASISWA")
print(ubah_mahasiswa("23001", "Naufal Fauzan", "Sistem Informasi"))
tampilkan_mahasiswa(cari_mahasiswa("23001"))

# 5. Delete: menghapus mahasiswa
print("\n5. HAPUS MAHASISWA")
print(hapus_mahasiswa("23002"))

# 6. Menampilkan data terakhir
print("\n6. DATA AKHIR")
tampilkan_daftar(tampilkan_semua())
