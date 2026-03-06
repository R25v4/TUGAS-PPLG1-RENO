# Data login
username = "Sawitku2hektar"
password = "wowosawitslayer"

# Penyimpanan data parfum
data_parfum = []

# ===== FUNGSI LOGIN =====
def login():
    print("=== LOGIN WANN FRAGRANCE ===")
    user = input("Masukkan Username: ")
    pw = input("Masukkan Password: ")

    if user == username and pw == password:
        print("Login berhasil!\n")
        menu()
    else:
        print("Username atau Password salah!")

# ===== MENU =====
def menu():
    while True:
        print("\n=== MENU BY WANN FRAGRANCE ===")
        print("1. Lihat Stok Parfum")
        print("2. Tambah Stok Parfum")
        print("3. Ubah Stok Parfum")
        print("4. Hapus Stok Parfum")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")

# ===== FITUR LIHAT DATA =====
def lihat_data():
    if len(data_parfum) == 0:
        print("Stok parfum masih kosong.")
    else:
        print("\n=== DATA PARFUM ===")
        for i, parfum in enumerate(data_parfum):
            print(f"{i+1}. Nama: {parfum['nama']}, Aroma: {parfum['aroma']}, Harga: {parfum['harga']}")

# ===== FITUR TAMBAH DATA =====
def tambah_data():
    nama = input("Masukkan nama parfum: ")
    aroma = input("Masukkan jenis aroma: ")
    harga = input("Masukkan harga: ")

    parfum = {
        "nama": nama,
        "aroma": aroma,
        "harga": harga
    }

    data_parfum.append(parfum)
    print("Stok parfum berhasil ditambahkan.")

# ===== FITUR UBAH DATA =====
def ubah_data():
    lihat_data()
    nomor = int(input("Pilih nomor Stok yang ingin diubah: ")) - 1

    if nomor < len(data_parfum):
        nama = input("Nama parfum baru: ")
        aroma = input("Aroma baru: ")
        harga = input("Harga baru: ")

        data_parfum[nomor]["nama"] = nama
        data_parfum[nomor]["aroma"] = aroma
        data_parfum[nomor]["harga"] = harga

        print("Data berhasil diubah.")
    else:
        print("Data tidak ditemukan.")

# ===== FITUR HAPUS DATA =====
def hapus_data():
    lihat_data()
    nomor = int(input("Pilih nomor data yang ingin dihapus: ")) - 1

    if nomor < len(data_parfum):
        data_parfum.pop(nomor)
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

# Menjalankan program
login()