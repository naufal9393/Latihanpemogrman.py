
from sistem_informasi.model.mahasiswa import Mahasiswa

_data_mahasiswa = {}


def tambah_mahasiswa(nim, nama, jurusan):
    if nim in _data_mahasiswa:
        return False, "NIM sudah terdaftar"

    mahasiswa = Mahasiswa(nim, nama, jurusan)
    _data_mahasiswa[nim] = mahasiswa

    return True, "Mahasiswa berhasil ditambahkan"


def tampilkan_semua():
    return [
        mahasiswa.to_dict()
        for mahasiswa in _data_mahasiswa.values()
    ]


def cari_mahasiswa(nim):
    mahasiswa = _data_mahasiswa.get(nim)

    if mahasiswa is None:
        return None

    return mahasiswa.to_dict()


def ubah_mahasiswa(nim, nama, jurusan):
    mahasiswa = _data_mahasiswa.get(nim)

    if mahasiswa is None:
        return False, "Mahasiswa tidak ditemukan"

    mahasiswa.nama = nama
    mahasiswa.jurusan = jurusan

    return True, "Data mahasiswa berhasil diubah"


def hapus_mahasiswa(nim):
    if nim not in _data_mahasiswa:
        return False, "Mahasiswa tidak ditemukan"

    del _data_mahasiswa[nim]

    return True, "Mahasiswa berhasil dihapus"
