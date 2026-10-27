
def tampilkan_mahasiswa(mahasiswa):
    if mahasiswa is None:
        print("Data mahasiswa tidak ditemukan")
        return

    print(f"NIM     : {mahasiswa['nim']}")
    print(f"Nama    : {mahasiswa['nama']}")
    print(f"Jurusan : {mahasiswa['jurusan']}")


def tampilkan_daftar(daftar):
    if not daftar:
        print("Belum ada data mahasiswa")
        return

    for nomor, mahasiswa in enumerate(daftar, start=1):
        print(f"\nMahasiswa ke-{nomor}")
        tampilkan_mahasiswa(mahasiswa)
