import pytest

from src.models import DaftarMahasiswa, Mahasiswa


def test_mahasiswa_valid():
    mahasiswa = Mahasiswa(
        nim="20241320023",
        nama="Naufal Fauzan Azmii",
        program_studi="Sistem Informasi",
        angkatan=2024,
        ipk=4.00,
    )

    assert mahasiswa.nim == "20241320023"
    assert mahasiswa.nama == "Naufal Fauzan Azmii"
    assert mahasiswa.program_studi == "Sistem Informasi"
    assert mahasiswa.angkatan == 2024
    assert mahasiswa.ipk == 4.00


def test_nim_terlalu_pendek():
    with pytest.raises(ValueError):
        Mahasiswa(
            nim="20241",
            nama="Rafi Haikal Akram",
            program_studi="Sistem Informasi",
            angkatan=2024,
            ipk=3.50,
        )


def test_ipk_tidak_valid():
    with pytest.raises(ValueError):
        Mahasiswa(
            nim="20241320021",
            nama="Rafi Haikal Akram",
            program_studi="Sistem Informasi",
            angkatan=2024,
            ipk=4.50,
        )


def test_tambah_dan_cari_mahasiswa():
    daftar = DaftarMahasiswa()

    mahasiswa = Mahasiswa(
        nim="20241320021",
        nama="Rafi Haikal Akram",
        program_studi="Sistem Informasi",
        angkatan=2024,
        ipk=3.50,
    )

    daftar.tambah(mahasiswa)

    hasil = daftar.cari("20241320021")

    assert hasil is not None
    assert hasil.nama == "Rafi Haikal Akram"


def test_nim_duplikat():
    daftar = DaftarMahasiswa()

    mahasiswa1 = Mahasiswa(
        nim="20241320049",
        nama="Athallah Naufal Ghali",
        program_studi="Teknik Komputer",
        angkatan=2024,
        ipk=3.33,
    )

    mahasiswa2 = Mahasiswa(
        nim="20241320049",
        nama="Muhammad Khoirul Amad",
        program_studi="Teknik Komputer",
        angkatan=2024,
        ipk=3.90,
    )

    daftar.tambah(mahasiswa1)

    with pytest.raises(ValueError):
        daftar.tambah(mahasiswa2)


def test_nim_kosong():
    with pytest.raises(ValueError):
        Mahasiswa(
            nim="",
            nama="Rafi Haikal Akram",
            program_studi="Sistem Informasi",
            angkatan=2024,
            ipk=3.50,
        )


def test_nama_kosong():
    with pytest.raises(ValueError):
        Mahasiswa(
            nim="20241320021",
            nama="   ",
            program_studi="Sistem Informasi",
            angkatan=2024,
            ipk=3.50,
        )


def test_ipk_batas_bawah():
    mahasiswa = Mahasiswa(
        nim="20241320042",
        nama="Muhammad Khoirul Amad",
        program_studi="Teknik Komputer",
        angkatan=2024,
        ipk=0.00,
    )

    assert mahasiswa.ipk == 0.00


def test_ipk_batas_atas():
    mahasiswa = Mahasiswa(
        nim="20241320042",
        nama="Muhammad Khoirul Amad",
        program_studi="Teknik Komputer",
        angkatan=2024,
        ipk=4.00,
    )

    assert mahasiswa.ipk == 4.00


def test_hapus_nim_tidak_ditemukan():
    daftar = DaftarMahasiswa()

    hasil = daftar.hapus("20241320999")

    assert hasil is False


def test_cari_nim_tidak_ditemukan():
    daftar = DaftarMahasiswa()

    hasil = daftar.cari("20241320999")

    assert hasil is None