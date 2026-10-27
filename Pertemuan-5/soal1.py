
# Soal 1: Mengolah Kalimat

kalimat = input("Masukkan sebuah kalimat: ")

kata = kalimat.split()

jumlah_kata = len(kata)
jumlah_karakter = len(kalimat)

if kata:
    kata_terpanjang = max(kata, key=len)
else:
    kata_terpanjang = ""

kalimat_title = kalimat.title()

print("Jumlah kata:", jumlah_kata)
print("Jumlah karakter:", jumlah_karakter)
print("Kata terpanjang:", kata_terpanjang)
print("Kalimat title case:", kalimat_title)
