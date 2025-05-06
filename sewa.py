from datetime import datetime, timedelta
# Import modul datetime untuk memproses waktu (jam mulai, jam selesai) dan menghitung durasi.

class Sewa:
    BIAYA_PER_JAM = 50000  # Tarif sewa per jam

    def __init__(self, nama_penyewa, no_telp, tanggal_sewa, alamat_sewa ,jam_mulai, jam_selesai):
        #__init__ adalah constructor, otomatis dipanggil saat objek Sewa dibuat.
        # Membuat objek baru Sewa dengan atribut
        self.nama_penyewa = nama_penyewa
        self.no_telp = no_telp
        self.tanggal_sewa = tanggal_sewa
        self.alamat_sewa = alamat_sewa
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai
        #self adalah referensi ke diri sendiri (objek yang sedang dibuat).

    def hitung_durasi(self):
         # Menghitung durasi sewa dalam jam
        fmt = "%H:%M" # format jam: jam dan menit, dipisahkan dengan ":"
        jam_mulai_benar = self.jam_mulai.replace('.', ':') #jika user ketik 12.00, diubah ke 12:00.
        jam_selesai_benar = self.jam_selesai.replace('.', ':') #jika user ketik 12.00, diubah ke 12:00.

        mulai = datetime.strptime(jam_mulai_benar, fmt)
        selesai = datetime.strptime(jam_selesai_benar, fmt)
        #Konversi string jam menjadi objek datetime
        #datetime.strptime, mengubah string menjadi objek datetime.

        if selesai < mulai:
            selesai += timedelta(days=1)
        #jika jam selesai lebih kecil dari jam mulai (misal, sewa mulai 23:00 dan selesai 01:00), artinya melewati tengah malam maka tambahkan 1 hari.

        durasi = (selesai - mulai).seconds / 3600
        #selisih detik dibagi 3600 supaya dapat jam bisa desimal (contoh 1.5 jam).
        return durasi

    def hitung_biaya(self):
        # Menghitung biaya sewa berdasarkan durasi
        durasi = self.hitung_durasi()
        return durasi * self.BIAYA_PER_JAM
        # Biaya = durasi jam × tarif per jam

    def to_list(self):
        # Mengubah data objek Sewa menjadi list untuk disimpan ke file csv
        return [
            self.nama_penyewa,
            self.no_telp,
            self.tanggal_sewa,
            self.alamat_sewa, 
            self.jam_mulai,
            self.jam_selesai
        ]

    
    def from_list(data_list):
        # Membuat objek Sewa dari list (data dari file)
        return Sewa(*data_list)
