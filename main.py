import argparse
from pathlib import Path

if Path("preset.py").exists():
    import preset
    riwayat = preset.riwayat
    kategori_pendapatan = preset.kategori_pendapatan
    kategori_pengeluaran = preset.kategori_pengeluaran
else:
    riwayat = []
    kategori_pendapatan = []
    kategori_pengeluaran = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Pencatat Keuangan Pribadi")
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Jalankan dalam mode CLI tanpa GUI"
    )
    args = parser.parse_args()

    if args.no_gui:
        from app.cli import CliApp
        CliApp(riwayat, kategori_pendapatan, kategori_pengeluaran).run()
    else:
        from app.gui import GuiApp
        GuiApp(riwayat, kategori_pendapatan, kategori_pengeluaran).run()
