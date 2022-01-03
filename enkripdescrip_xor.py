import os
from hashlib import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Enkripsi sembarang berkas dengan algoritma XOR sederhana
print("Pilih file")
Tk().withdraw()
files = askopenfilename()
print(files)
Fin = files
Fout = str(input("\nMasukkan nama file hasil : "))

K = str(input("Kata Kunci : "))
KunciSha = sha256(K.encode('utf-8')).digest()

with open(Fin, 'rb') as Fin:
    with open(Fout, 'wb') as Fout:
        print("\nMengubah ", Fin, " menjadi ", Fout)
        i = 0
        while Fin.peek():
            p = ord(Fin.read(1))
            j = i % len(KunciSha)
            c = bytes([p ^ KunciSha[j]])
            Fout.write(c)
            i = i + 1
print("Enkripsi  Berhasil!")


# Deskripsi sembarang berkas dengan algoritma XOR sederhana
# print("Pilih file yang telah dienkripsi sebelumnya")
# Tk().withdraw()
# files = askopenfilename()
# print(files)
# Fin = files
# Fout = str(input("\nMasukkan nama file hasil deskripsi : "))

# K = str(input("Masukkan Kata Kunci yang sama saat mengenkripsi file : "))
# KunciSha = sha256(K.encode('utf-8')).digest()

# with open(Fin, 'rb') as Fin:
#     with open(Fout, 'wb') as Fout:
#         print("\nMengubah ", Fin, " menjadi ", Fout)
#         i = 0
#         while Fin.peek():
#             c = ord(Fin.read(1))
#             j = i % len(KunciSha)
#             p = bytes([c ^ KunciSha[j]])
#             Fout.write(p)
#             i = i + 1
# print("Deskripsi Berhasil")
