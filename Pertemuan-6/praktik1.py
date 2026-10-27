
import statistics
import math


def hitung_statistik(angka):
    if not angka:
        raise ValueError("List angka tidak boleh kosong")

    mean = statistics.mean(angka)
    median = statistics.median(angka)
    modus = statistics.multimode(angka)
    rentang = max(angka) - min(angka)
    standar_deviasi = math.sqrt(statistics.pvariance(angka))

    return {
        "mean": mean,
        "median": median,
        "modus": modus,
        "range": rentang,
        "standard_deviation": standar_deviasi
    }


if __name__ == "__main__":
    data = [70, 80, 80, 90, 100]
    hasil = hitung_statistik(data)

    for nama, nilai in hasil.items():
        print(f"{nama}: {nilai}")
