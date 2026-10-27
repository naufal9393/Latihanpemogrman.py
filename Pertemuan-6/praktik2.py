
def validasi_data(data, schema, *args, **kwargs):
    errors = []

    for field, aturan in schema.items():
        if field not in data:
            errors.append(f"{field} wajib diisi")
            continue

        nilai = data[field]
        tipe = aturan.get("type")

        if tipe == int and not isinstance(nilai, int):
            errors.append(f"{field} harus berupa integer")

        elif tipe == float and not isinstance(nilai, (int, float)):
            errors.append(f"{field} harus berupa angka")

        elif tipe == str and not isinstance(nilai, str):
            errors.append(f"{field} harus berupa teks")

        if "min" in aturan and isinstance(nilai, (int, float)):
            if nilai < aturan["min"]:
                errors.append(
                    f"{field} minimal {aturan['min']}"
                )

        if "max" in aturan and isinstance(nilai, (int, float)):
            if nilai > aturan["max"]:
                errors.append(
                    f"{field} maksimal {aturan['max']}"
                )

    return len(errors) == 0, errors


# Data yang akan diperiksa
data_mahasiswa = {
    "nama": "Naufal",
    "umur": 20,
    "nilai": 85
}

# Aturan validasi
schema_mahasiswa = {
    "nama": {"type": str},
    "umur": {"type": int, "min": 17, "max": 100},
    "nilai": {"type": int, "min": 0, "max": 100}
}

# Menjalankan fungsi
valid, errors = validasi_data(
    data_mahasiswa,
    schema_mahasiswa,
    "data mahasiswa",
    sumber="praktik"
)

if valid:
    print("Data mahasiswa valid!")
else:
    print("Data mahasiswa tidak valid:")
    for error in errors:
        print("-", error)
