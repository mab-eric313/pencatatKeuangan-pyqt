"""Modul yang menyediakan UI Command Line Interface"""

from app.core import dompet as d
from app.core import transaksi as t
from pathlib import Path

if Path("preset.py").exists():
    import preset
    dompet_mgr = d.Dompet(preset.dompet)
else:
    dompet_mgr = d.Dompet()


# TODO: fix docstring CLI


class CLI:
    """Class CLI"""

    def __init__(self, riwayat, kategoriPendapatan, kategoriPengeluaran):
        """Inisialisasi Class CLI"""
        super(CLI, self).__init__()
        self.riwayat = riwayat
        self.kategoriPendapatan = kategoriPendapatan
        self.kategoriPengeluaran = kategoriPengeluaran

    def run_cli(self):
        while True:
            dompet_mgr.tampilkan_saldo()
            print("[1] Pendapatan\n[2] Pengeluaran\n[3] Transfer\n[4] Keluar\n")
            pilih = input("Pilih transaksi: ")

            if pilih == "1":
                dompet = input("Dompet: ")
                jumlah = int(input("Jumlah: "))
                judul = input("Judul: ")
                kategori = input(f"Kategori {self.kategoriPendapatan}: ")
                deskripsi = input("Deskripsi (opsional): ")
                dompet_mgr.tambah(dompet, jumlah)
                self.riwayat.append(t.Transaksi("Pendapatan", dompet, jumlah, judul,
                                                kategori, deskripsi))

            elif pilih == "2":
                dompet = input("Dompet: ")
                jumlah = int(input("Jumlah: "))
                judul = input("Judul: ")
                kategori = input(f"Kategori {self.kategoriPengeluaran}: ")
                deskripsi = input("Deskripsi (opsional): ")
                if dompet_mgr.kurang(dompet, jumlah):
                    self.riwayat.append(t.Transaksi("Pengeluaran", dompet, jumlah, judul,
                                                    kategori, deskripsi))

            elif pilih == "3":
                dari = input("Transfer dari: ")
                ke = input("Ke: ")
                jumlah = int(input("Jumlah: "))
                deskripsi = input("Deskripsi (opsional): ")
                if dompet_mgr.transfer(dari, ke, jumlah):
                    self.riwayat.append(t.Transaksi("Transfer", f"{dari}→{ke}", jumlah,
                                                    "Transfer", "-", deskripsi))

            elif pilih == "4":
                print("\n=== Riwayat Transaksi ===")
                for i in self.riwayat:
                    print(i)
                break
            else:
                print("Input tidak valid!")
