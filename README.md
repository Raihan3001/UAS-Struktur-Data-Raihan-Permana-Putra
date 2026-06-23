# UAS-Struktur-Data-Raihan-Permana-Putra
Sistem Presensi Karyawan Berbasis RFID

Deskripsi

Aplikasi ini merupakan sistem presensi karyawan berbasis RFID yang dibuat menggunakan Python. Data presensi disimpan pada file CSV sebagai database utama dan secara otomatis diekspor ke file Excel (.xlsx) untuk memudahkan pelaporan.

Fitur
Tambah Data Presensi (Create)
Tampilkan Data Presensi (Read)
Ubah Data Presensi (Update)
Hapus Data Presensi (Delete)
Cari Data Menggunakan Linear Search
Urutkan Data Menggunakan Bubble Sort
Penyimpanan Data ke CSV
Ekspor Otomatis ke Excel
Implementasi Queue dan Dictionary
Struktur Data yang Digunakan
Queue

Digunakan untuk menyimpan antrian data presensi yang masuk dari RFID.

Dictionary (Hash Map)

Digunakan untuk menyimpan data karyawan berdasarkan ID sehingga pencarian lebih mudah dilakukan.

Linear Search

Digunakan untuk mencari data berdasarkan ID karyawan.

Bubble Sort

Digunakan untuk mengurutkan data berdasarkan nama atau tanggal presensi.
Cara Menjalankan Program

Jalankan perintah berikut pada terminal:

python main.py
Menu Program
1. Tambah Data
2. Lihat Data
3. Update Data
4. Hapus Data
5. Cari Data
6. Urutkan Data
7. Keluar

Format Data CSV
ID,Nama,Jabatan,Tanggal,Jam_Masuk,Status
133895, Raihan Permana Putra, Operator, 2026-05-18, 06:40, Hadir
127554, Nurfadillah, Operator, 2026-05-18, 06:45, Hadir
134775, Irfan Maulana, Operator, 2026-05-18, 08:30, Terlambat
130535, Yoga Permana, Operator, 2026-05-18, 09:00, Terlambat
132877, Aditya Saputra, Operator, 2026-05-18, 06:50, Hadir
120334, Ahmad Fauzan, Operator, 2026-05-18, 08:45, Terlambat
   
Alur Sistem
RFID
 ↓
Queue
 ↓
Dictionary
 ↓
CRUD
 ↓
CSV
 ↓
Excel (.xlsx)
Teknologi yang Digunakan
Python 3
Pandas
OpenPyXL
CSV (Flat File Database)

Penulis

Nama : Raihan Permana Putra
NIM : 25416255201014
Kelas : IF25B
Mata Kuliah : Struktur Data 
Final Project - Aplikasi Manajemen dengan Database Flat File (CSV)


Kesimpulan

Sistem Presensi Karyawan Berbasis RFID mampu mengelola data presensi menggunakan konsep CRUD dengan penyimpanan data pada file CSV dan ekspor otomatis ke Excel. Implementasi Queue, Dictionary, Linear Search, dan Bubble Sort membuat sistem memenuhi kebutuhan pembelajaran Struktur Data dan Algoritma.
