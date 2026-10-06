from rich.console import Console
from rich.table import Table

from .models import DaftarMahasiswa, Mahasiswa


console = Console()
daftar = DaftarMahasiswa()


def tambah_mahasiswa():
    console.print("\n[bold cyan]Tambah Mahasiswa Baru[/bold cyan]")

    try:
        nim = input("NIM: ")
        nama = input("Nama: ")
        program_studi = input("Program Studi: ")
        angkatan = int(input("Angkatan: "))
        ipk = float(input("IPK: "))

        mahasiswa = Mahasiswa(
            nim=nim,
            nama=nama,
            program_studi=program_studi,
            angkatan=angkatan,
            ipk=ipk,
        )

        daftar.tambah(mahasiswa)

        console.print(
            f"[green]Berhasil: {nama} ditambahkan[/green]"
        )

    except ValueError as error:
        console.print(f"[red]Gagal: {error}[/red]")


def tampilkan_semua():
    console.print("\n[bold cyan]Daftar Semua Mahasiswa[/bold cyan]")

    if daftar.jumlah() == 0:
        console.print("[yellow]Belum ada data mahasiswa.[/yellow]")
        return

    table = Table()

    table.add_column("NIM")
    table.add_column("Nama")
    table.add_column("Program Studi")
    table.add_column("Angkatan")
    table.add_column("IPK")

    for mahasiswa in daftar.mahasiswa:
        table.add_row(
            mahasiswa.nim,
            mahasiswa.nama,
            mahasiswa.program_studi,
            str(mahasiswa.angkatan),
            f"{mahasiswa.ipk:.2f}",
        )

    console.print(table)


def cari_mahasiswa():
    console.print("\n[bold cyan]Cari Mahasiswa[/bold cyan]")

    nim = input("Masukkan NIM: ")

    mahasiswa = daftar.cari(nim)

    if mahasiswa:
        console.print(f"NIM: {mahasiswa.nim}")
        console.print(f"Nama: {mahasiswa.nama}")
        console.print(f"Program Studi: {mahasiswa.program_studi}")
        console.print(f"Angkatan: {mahasiswa.angkatan}")
        console.print(f"IPK: {mahasiswa.ipk:.2f}")
    else:
        console.print("[yellow]Mahasiswa tidak ditemukan.[/yellow]")


def hapus_mahasiswa():
    console.print("\n[bold cyan]Hapus Mahasiswa[/bold cyan]")

    nim = input("Masukkan NIM: ")

    mahasiswa = daftar.cari(nim)

    if mahasiswa:
        nama = mahasiswa.nama
        daftar.hapus(nim)
        console.print(
            f"[green]Berhasil: {nama} dihapus[/green]"
        )
    else:
        console.print("[yellow]Mahasiswa tidak ditemukan.[/yellow]")


def edit_ipk():
    console.print("\n[bold cyan]Edit IPK Mahasiswa[/bold cyan]")

    nim = input("Masukkan NIM: ")

    mahasiswa = daftar.cari(nim)

    if not mahasiswa:
        console.print("[yellow]Mahasiswa tidak ditemukan.[/yellow]")
        return

    try:
        ipk_baru = float(input("IPK Baru: "))

        if not 0 <= ipk_baru <= 4:
            raise ValueError("IPK harus antara 0 dan 4")

        mahasiswa.ipk = ipk_baru

        console.print(
            f"[green]Berhasil: IPK {mahasiswa.nama} "
            f"diperbarui menjadi {mahasiswa.ipk:.2f}[/green]"
        )

    except ValueError as error:
        console.print(f"[red]Gagal: {error}[/red]")


def tampilkan_menu():
    console.print()
    console.print("[bold cyan]╭────────────── Menu ──────────────╮[/bold cyan]")
    console.print("[bold cyan]│[/bold cyan] 1. Tambah Mahasiswa")
    console.print("[bold cyan]│[/bold cyan] 2. Tampilkan Semua Mahasiswa")
    console.print("[bold cyan]│[/bold cyan] 3. Cari Mahasiswa (NIM)")
    console.print("[bold cyan]│[/bold cyan] 4. Hapus Mahasiswa")
    console.print("[bold cyan]│[/bold cyan] 5. Edit IPK Mahasiswa")
    console.print("[bold cyan]│[/bold cyan] 0. Keluar")
    console.print("[bold cyan]╰─────────────────────────────────╯[/bold cyan]")


def main():
    while True:
        console.print("\n[bold cyan]Sistem Informasi Mahasiswa[/bold cyan]")

        tampilkan_menu()

        pilihan = input("Pilih [0-5]: ")

        if pilihan == "1":
            tambah_mahasiswa()

        elif pilihan == "2":
            tampilkan_semua()

        elif pilihan == "3":
            cari_mahasiswa()

        elif pilihan == "4":
            hapus_mahasiswa()

        elif pilihan == "5":
            edit_ipk()

        elif pilihan == "0":
            console.print("[blue]Program selesai.[/blue]")
            break

        else:
            console.print("[red]Pilihan tidak valid.[/red]")


if __name__ == "__main__":
    main()  