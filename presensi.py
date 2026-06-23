import csv
import os
import pandas as pd
from collections import deque

FILE_CSV = "presensi.csv"
FILE_EXCEL = "presensi.xlsx"

# Queue Presensi
queue_presensi = deque()

# Dictionary (Hash Map)
data_karyawan = {}

# ==========================
# INISIALISASI FILE CSV
# ==========================

def inisialisasi_file():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID",
                "Nama",
                "Jabatan",
                "Tanggal",
                "Jam_Masuk",
                "Status"
            ])

# ==========================
# BACA CSV KE DICTIONARY
# ==========================

def load_data():
    data_karyawan.clear()

    with open(FILE_CSV, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data_karyawan[row["ID"]] = row

# ==========================
# SIMPAN KE CSV
# ==========================

def simpan_csv():
    with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID",
            "Nama",
            "Jabatan",
            "Tanggal",
            "Jam_Masuk",
            "Status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for data in data_karyawan.values():
            writer.writerow(data)

# ==========================
# EXPORT KE EXCEL
# ==========================

def export_excel():
    df = pd.read_csv(FILE_CSV)
    df.to_excel(FILE_EXCEL, index=False)

# ==========================
# CREATE (TAMBAH DATA)
# ==========================

def tambah_data():
    print("\n=== TAMBAH DATA ===")

    id_karyawan = input("ID Karyawan : ")

    if id_karyawan in data_karyawan:
        print("ID sudah ada!")
        return

    nama = input("Nama : ")
    jabatan = input("Jabatan : ")
    tanggal = input("Tanggal : ")
    jam_masuk = input("Jam Masuk : ")
    status = input("Status : ")

    data = {
        "ID": id_karyawan,
        "Nama": nama,
        "Jabatan": jabatan,
        "Tanggal": tanggal,
        "Jam_Masuk": jam_masuk,
        "Status": status
    }

    # Masuk Queue
    queue_presensi.append(data)

    # Masuk Dictionary
    data_karyawan[id_karyawan] = queue_presensi.popleft()

    simpan_csv()
    export_excel()

    print("Data berhasil ditambahkan!")

# ==========================
# READ (LIHAT DATA)
# ==========================

def lihat_data():
    print("\n=== DATA PRESENSI ===")

    if len(data_karyawan) == 0:
        print("Data kosong!")
        return

    for data in data_karyawan.values():
        print("-" * 50)
        print("ID       :", data["ID"])
        print("Nama     :", data["Nama"])
        print("Jabatan  :", data["Jabatan"])
        print("Tanggal  :", data["Tanggal"])
        print("Jam      :", data["Jam_Masuk"])
        print("Status   :", data["Status"])

# ==========================
# LINEAR SEARCH
# ==========================

def cari_index(id_cari):
    data_list = list(data_karyawan.values())

    for i in range(len(data_list)):
        if data_list[i]["ID"] == id_cari:
            return i

    return -1

# ==========================
# SEARCH (CARI DATA)
# ==========================

def cari_data():
    print("\n=== CARI DATA ===")

    id_cari = input("Masukkan ID : ")

    indeks = cari_index(id_cari)

    if indeks == -1:
        print("Data tidak ditemukan!")
        return

    data = data_karyawan[id_cari]

    print("\nData ditemukan")
    print("Nama     :", data["Nama"])
    print("Jabatan  :", data["Jabatan"])
    print("Tanggal  :", data["Tanggal"])
    print("Jam      :", data["Jam_Masuk"])
    print("Status   :", data["Status"])

# ==========================
# UPDATE DATA
# ==========================

def update_data():
    print("\n=== UPDATE DATA ===")

    id_karyawan = input("ID yang diubah : ")

    if id_karyawan not in data_karyawan:
        print("Data tidak ditemukan!")
        return

    data = data_karyawan[id_karyawan]

    data["Nama"] = input("Nama Baru : ")
    data["Jabatan"] = input("Jabatan Baru : ")
    data["Tanggal"] = input("Tanggal Baru : ")
    data["Jam_Masuk"] = input("Jam Baru : ")
    data["Status"] = input("Status Baru : ")

    simpan_csv()
    export_excel()

    print("Data berhasil diubah!")

# ==========================
# DELETE DATA
# ==========================

def hapus_data():
    print("\n=== HAPUS DATA ===")

    id_karyawan = input("ID yang dihapus : ")

    if id_karyawan not in data_karyawan:
        print("Data tidak ditemukan!")
        return

    del data_karyawan[id_karyawan]

    simpan_csv()
    export_excel()

    print("Data berhasil dihapus!")

# ==========================
# BUBBLE SORT
# ==========================

def bubble_sort(data_list, key):
    n = len(data_list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if data_list[j][key] > data_list[j + 1][key]:
                data_list[j], data_list[j + 1] = (
                    data_list[j + 1],
                    data_list[j]
                )

    return data_list

# ==========================
# SORTING DATA
# ==========================

def urutkan_data():
    print("\n=== URUTKAN DATA ===")
    print("1. Nama")
    print("2. Tanggal")

    pilihan = input("Pilih : ")

    data_list = list(data_karyawan.values())

    if pilihan == "1":
        hasil = bubble_sort(data_list, "Nama")

    elif pilihan == "2":
        hasil = bubble_sort(data_list, "Tanggal")

    else:
        print("Pilihan tidak valid!")
        return

    print("\nHASIL PENGURUTAN")

    for data in hasil:
        print("-" * 50)
        print("ID       :", data["ID"])
        print("Nama     :", data["Nama"])
        print("Jabatan  :", data["Jabatan"])
        print("Tanggal  :", data["Tanggal"])
        print("Jam      :", data["Jam_Masuk"])
        print("Status   :", data["Status"])

# ==========================
# MENU UTAMA
# ==========================

def menu():
    while True:

        print("\n===== SISTEM PRESENSI RFID =====")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("6. Urutkan Data")
        print("7. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_data()

        elif pilih == "2":
            lihat_data()

        elif pilih == "3":
            update_data()

        elif pilih == "4":
            hapus_data()

        elif pilih == "5":
            cari_data()

        elif pilih == "6":
            urutkan_data()

        elif pilih == "7":
            print("\nTerima Kasih")
            break

        else:
            print("Pilihan tidak valid!")

# ==========================
# MAIN PROGRAM
# ==========================

inisialisasi_file()
load_data()
export_excel()
menu()