
# Soal 4: Inventaris Toko

# Data inventaris awal (data contoh)
inventaris = {
    "Buku": (15000, 20),
    "Pensil": (3000, 50),
    "Tas": (120000, 10)
}


# (a) Menambah barang baru
def tambah_barang(nama, harga, stok):
    if nama in inventaris:
        print("Barang sudah tersedia.")
    else:
        inventaris[nama] = (harga, stok)
        print("Barang berhasil ditambahkan.")


# (b) Memperbarui stok
def update_stok(nama, stok_baru):
    if nama in inventaris:
        harga, stok_lama = inventaris[nama]
        inventaris[nama] = (harga, stok_baru)
        print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")


# (c) Mencari barang dalam rentang harga
def cari_barang(harga_min, harga_maks):
    for nama, (harga, stok) in inventaris.items():
        if harga_min <= harga <= harga_maks:
            print(nama, "- Harga:", harga, "- Stok:", stok)


# (d) Menghitung total nilai inventaris
def total_nilai_inventaris():
    total = 0

    for harga, stok in inventaris.values():
        total += harga * stok

    return total


# Menampilkan inventaris
print("Daftar inventaris:")
for nama, (harga, stok) in inventaris.items():
    print(nama, "- Harga:", harga, "- Stok:", stok)

print("\nPencarian barang harga Rp3.000 sampai Rp20.000:")
cari_barang(3000, 20000)

print("\nTotal nilai inventaris:", total_nilai_inventaris())