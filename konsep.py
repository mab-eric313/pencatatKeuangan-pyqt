class DompetManager:
    def __init__(self):
        self.saldo = {
            "Gopay": 100000,
            "Dana": 25000,
            "BRI": 0,
            "Jago": 500000,
            "Uang Tunai": 250000,
        }

    def tambah(self, dompet, jumlah):
        self.saldo[dompet] += jumlah

    def kurang(self, dompet, jumlah):
        if self.saldo[dompet] < jumlah:
            print(f"Saldo {dompet} tidak cukup!")
            return False
        self.saldo[dompet] -= jumlah
        return True

    def transfer(self, dari, ke, jumlah):
        if self.kurang(dari, jumlah):
            self.tambah(ke, jumlah)
            return True
        return False

    def tampilkan_saldo(self):
        print("\n=== Saldo Dompet ===")
        for k, v in self.saldo.items():
            print(f"{k:12s}: Rp{v}")
        print()


class Transaksi:
    def __init__(self, tipe, dompet, jumlah, judul, kategori, deskripsi=""):
        self.tipe = tipe  # "Pendapatan" / "Pengeluaran" / "Transfer"
        self.dompet = dompet
        self.jumlah = jumlah
        self.judul = judul
        self.kategori = kategori
        self.deskripsi = deskripsi

    def __str__(self):
        return (f"[{self.tipe}] {self.judul} ({self.kategori}) "
                f"Rp{self.jumlah} -> {self.dompet}")


# ========================
# Main Program
# ========================


dompet_mgr = DompetManager()
riwayat = []

kategoriPendapatan = ["Gaji", "Laba", "Donasi"]
kategoriPengeluaran = ["Makan-Minum", "Jajan", "Belanja", "Transportasi"]

while True:
    dompet_mgr.tampilkan_saldo()
    print("1. Pendapatan\n2. Pengeluaran\n3. Transfer\n4. Keluar")
    pilih = input("Pilih transaksi: ")

    if pilih == "1":
        dompet = input("Dompet: ")
        jumlah = int(input("Jumlah: "))
        judul = input("Judul: ")
        kategori = input(f"Kategori {kategoriPendapatan}: ")
        deskripsi = input("Deskripsi (opsional): ")
        dompet_mgr.tambah(dompet, jumlah)
        riwayat.append(Transaksi("Pendapatan", dompet, jumlah, judul, kategori,
                                 deskripsi))

    elif pilih == "2":
        dompet = input("Dompet: ")
        jumlah = int(input("Jumlah: "))
        judul = input("Judul: ")
        kategori = input(f"Kategori {kategoriPengeluaran}: ")
        deskripsi = input("Deskripsi (opsional): ")
        if dompet_mgr.kurang(dompet, jumlah):
            riwayat.append(Transaksi("Pengeluaran", dompet, jumlah, judul,
                                     kategori, deskripsi))

    elif pilih == "3":
        dari = input("Transfer dari: ")
        ke = input("Ke: ")
        jumlah = int(input("Jumlah: "))
        deskripsi = input("Deskripsi (opsional): ")
        if dompet_mgr.transfer(dari, ke, jumlah):
            riwayat.append(Transaksi("Transfer", f"{dari}→{ke}", jumlah,
                                     "Transfer", "-", deskripsi))

    elif pilih == "4":
        print("\n=== Riwayat Transaksi ===")
        for t in riwayat:
            print(t)
        break
    else:
        print("Input tidak valid!")
