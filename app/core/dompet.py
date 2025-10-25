"""Modul yang menyediakan class Dompet"""

saldo_kosong: dict = {
    "BCA": 0,
    "BRI": 0,
    "Dana": 0,
    "Gopay": 0,
    "Jago": 0,
    "Jenius": 0,
    "Mandiri": 0,
    "OVO": 0,
}
total_balance = sum(saldo_kosong.values())
saldo_kosong["Total Balance"] = total_balance


class Dompet:
    def __init__(self, saldo: dict = saldo_kosong):
        self.saldo = saldo

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
            print(f"{k:12s}: Rp.{v:,}")
        print()
