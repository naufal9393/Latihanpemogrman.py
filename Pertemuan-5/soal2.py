
# Soal 2: Mengolah Nilai Mahasiswa

nilai_mahasiswa = [
    float(nilai)
    for nilai in input(
        "Masukkan nilai mahasiswa dipisahkan koma: "
    ).split(",")
]

if nilai_mahasiswa:
    rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)

    print("Daftar nilai:", nilai_mahasiswa)
    print("Rata-rata:", round(rata_rata, 2))
    print("Nilai tertinggi:", max(nilai_mahasiswa))
    print("Nilai terendah:", min(nilai_mahasiswa))

    # Batas kategori sementara, bukan ketentuan eksplisit modul.
    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    for nilai in nilai_mahasiswa:
        if nilai >= 85:
            kategori = "A"
        elif nilai >= 75:
            kategori = "B"
        elif nilai >= 65:
            kategori = "C"
        elif nilai >= 50:
            kategori = "D"
        else:
            kategori = "E"

        frekuensi[kategori] += 1

        print(f"Nilai {nilai}: kategori {kategori}")

    print("Frekuensi setiap kategori:")
    for kategori, jumlah in frekuensi.items():
        print(f"{kategori}: {jumlah}")
