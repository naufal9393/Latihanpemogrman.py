from dataclasses import dataclass


@dataclass
class Mahasiswa:
    nim: str
    nama: str
    program_studi: str
    angkatan: int
    ipk: float

    def __post_init__(self):
        if len(self.nim) < 6:
            raise ValueError("NIM minimal 6 karakter")

        if not self.nama.strip():
            raise ValueError("Nama tidak boleh kosong")

        if not 0 <= self.ipk <= 4:
            raise ValueError("IPK harus antara 0 dan 4")


class DaftarMahasiswa:
    def __init__(self):
        self.mahasiswa = []

    def tambah(self, mahasiswa: Mahasiswa):
        if self.cari(mahasiswa.nim):
            raise ValueError("NIM sudah terdaftar")
        self.mahasiswa.append(mahasiswa)

    def cari(self, nim: str):
        for mahasiswa in self.mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def hapus(self, nim: str):
        mahasiswa = self.cari(nim)

        if mahasiswa:
            self.mahasiswa.remove(mahasiswa)
            return True

        return False

    def jumlah(self):
        return len(self.mahasiswa)