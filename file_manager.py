import csv # Import modul csv untuk memproses file CSV
from sewa import Sewa # Import class Sewa agar bisa buat objek saat load data

FILE_NAME = "sewa_data.csv" # Nama file CSV untuk menyimpan data

def load_data():
    # Membaca semua data dari file CSV dan mengubahnya menjadi list objek Sewa
    sewa_list = []
    try:
        with open(FILE_NAME, mode='r', newline='') as file: #Buka file dengan mode r (read).
            reader = csv.reader(file) #Baca per baris menggunakan csv.reader
            for row in reader:
                sewa = Sewa.from_list(row)
                sewa_list.append(sewa)
    except FileNotFoundError:
        open(FILE_NAME, mode='w').close()  # jika belum ada file, buat file kosong
    return sewa_list

def save_data(sewa_list):
    # Menyimpan list objek Sewa ke file CSV
    with open(FILE_NAME, mode='w', newline='') as file: #Buka file dengan mode w (write)
        writer = csv.writer(file)
        for sewa in sewa_list:
            writer.writerow(sewa.to_list())
