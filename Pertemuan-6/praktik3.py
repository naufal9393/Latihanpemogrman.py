
def hitung_ipk(total_bobot, total_sks):
    if total_sks <= 0:
        raise ValueError("Total SKS harus lebih dari 0")

    return total_bobot / total_sks


def konversi_nilai_huruf(nilai):
    if nilai < 0 or nilai > 100:
        return "Nilai tidak valid"
    elif nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def generate_transkrip(mahasiswa, nilai_mata_kuliah):
    print("=== TRANSKRIP AKADEMIK ===")
    print(f"Nama: {mahasiswa['nama']}")
    print(f"NIM: {mahasiswa['nim']}")
    print("\nDaftar Nilai:")

    for mata_kuliah, nilai in nilai_mata_kuliah.items():
        huruf = konversi_nilai_huruf(nilai)
        print(f"{mata_kuliah}: {nilai} ({huruf})")
