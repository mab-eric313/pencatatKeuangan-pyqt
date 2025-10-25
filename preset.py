# File ini hanya digunakan untuk pengembangan

riwayat: list = []
kategoriPendapatan = ["Gaji", "Laba", "Donasi"]
kategoriPengeluaran = ["Makan-Minum", "Jajan", "Belanja", "Transportasi"]

dompet: dict = {
    "BCA": 0,
    "BRI": 0,
    "Dana": 25_000,
    "Gopay": 100_000,
    "Jago": 500_000,
    "Jenius": 0,
    "Mandiri": 0,
    "OVO": 0,
    "Uang Tunai": 250_000,
}
total_balance = sum(dompet.values())
dompet["Total Balance"] = total_balance
