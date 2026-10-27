
import requests
import json


def ambil_data_pengguna():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    return response.json()


def olah_data_pengguna(data):
    # Mengambil data tertentu menggunakan map()
    pengguna = list(map(
        lambda user: {
            "id": user["id"],
            "nama": user["name"],
            "email": user["email"],
            "kota": user["address"]["city"]
        },
        data
    ))

    # Menyaring data menggunakan filter()
    pengguna_valid = list(filter(
        lambda user: "." in user["email"],
        pengguna
    ))

    # Mengurutkan data berdasarkan nama
    pengguna_urut = sorted(
        pengguna_valid,
        key=lambda user: user["nama"]
    )

    return pengguna_urut


def simpan_data(data, nama_file):
    with open(nama_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    try:
        data = ambil_data_pengguna()
        hasil = olah_data_pengguna(data)

        simpan_data(hasil, "hasil_pengguna.json")

        print("Data berhasil diambil dan diolah!")
        print(f"Jumlah pengguna: {len(hasil)}")
        print("Hasil disimpan ke hasil_pengguna.json")

        print("\nDaftar pengguna:")
        for user in hasil:
            print(
                f"{user['nama']} | "
                f"{user['email']} | "
                f"{user['kota']}"
            )

    except requests.RequestException as error:
        print("Gagal mengambil data dari API:", error)

    except (ValueError, KeyError, TypeError) as error:
        print("Terjadi kesalahan saat mengolah data:", error)


if __name__ == "__main__":
    main()
