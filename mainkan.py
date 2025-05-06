from sewa import Sewa # Import fungsi untuk load dan save data
import file_manager # Import class Sewa

def tampilkan_data(sewa_list):
    # Menampilkan semua data sewa di layar
    if not sewa_list:
        print("Belum ada data sewa.")
        return
    print("\nData Sewa Lapangan:")
    for idx, sewa in enumerate(sewa_list, start=1): #enumerate digunakan untuk melakukan perulangan sebuah list, sekaligus mendapatkan indeks (urutan) dari setiap item-nya.
        durasi = sewa.hitung_durasi()
        biaya = sewa.hitung_biaya()
        print(f"{idx}. {sewa.nama_penyewa} | {sewa.no_telp} | {sewa.tanggal_sewa} | {sewa.alamat_sewa} | {sewa.jam_mulai}-{sewa.jam_selesai} | Durasi: {durasi:.2f} jam | Biaya: Rp{biaya:,.0f}")
        # f idx cara memformat string dengan menyisipkan nilai variabel ke dalam teks.
        # function ini menampilkan semua info, termasuk durasi dan biaya yang sudah dihitung otomatis

def tambah_data(sewa_list):
    # Menambah data sewa baru
    print("\nTambah Data Sewa:")
    nama = input("Nama Penyewa: ")
    telp = input("No. Telp: ")
    tanggal = input("Tanggal Sewa (YYYY-MM-DD): ")
    alamat = input("Alamat Penyewa: ")
    mulai = input("Jam Mulai (HH:MM): ")
    selesai = input("Jam Selesai (HH:MM): ")

    sewa = Sewa(nama, telp, tanggal, alamat, mulai, selesai)
    sewa_list.append(sewa)
    file_manager.save_data(sewa_list)
    print("Data berhasil ditambahkan!")

def edit_data(sewa_list):
    # Mengedit data sewa yang sudah ada
    tampilkan_data(sewa_list)
    idx = int(input("\nPilih nomor data yang ingin diedit: ")) - 1
    if 0 <= idx < len(sewa_list):
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        sewa = sewa_list[idx]
        nama = input(f"Nama Penyewa [{sewa.nama_penyewa}]: ") or sewa.nama_penyewa
        telp = input(f"No. Telp [{sewa.no_telp}]: ") or sewa.no_telp
        alamat = input(f"Alamat Penyewa [{sewa.alamat_sewa}]: ") or sewa.alamat_sewa
        tanggal = input(f"Tanggal Sewa [{sewa.tanggal_sewa}]: ") or sewa.tanggal_sewa
        mulai = input(f"Jam Mulai [{sewa.jam_mulai}]: ") or sewa.jam_mulai
        selesai = input(f"Jam Selesai [{sewa.jam_selesai}]: ") or sewa.jam_selesai

        sewa_list[idx] = Sewa(nama, telp, tanggal, alamat, mulai, selesai)
        file_manager.save_data(sewa_list)
        print("Data berhasil diubah!")
    else:
        print("Pilihan tidak valid.")

def hapus_data(sewa_list):
    # Menghapus data sewa berdasarkan pilihan
    tampilkan_data(sewa_list)
    idx = int(input("\nPilih nomor data yang ingin dihapus: ")) - 1
    if 0 <= idx < len(sewa_list):
        del sewa_list[idx]
        file_manager.save_data(sewa_list)
        print("Data berhasil dihapus!")
    else:
        print("Pilihan tidak valid.")

def main():
    # Fungsi utama untuk menjalankan menu aplikasi
    sewa_list = file_manager.load_data()

    while True:
        print("\n=== Aplikasi Sewa Lapangan ===")
        print("1. Lihat Data Sewa")
        print("2. Tambah Data Sewa")
        print("3. Edit Data Sewa")
        print("4. Hapus Data Sewa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tampilkan_data(sewa_list)
        elif pilihan == '2':
            tambah_data(sewa_list)
        elif pilihan == '3':
            edit_data(sewa_list)
        elif pilihan == '4':
            hapus_data(sewa_list)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()