"""Modul yang menyediakan class Transaksi"""


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
