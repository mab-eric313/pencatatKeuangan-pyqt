import argparse
from pathlib import Path

if Path("preset.py").exists():
    import preset
    riwayat = preset.riwayat
    kategoriPendapatan = preset.kategoriPendapatan
    kategoriPengeluaran = preset.kategoriPengeluaran
else:
    riwayat = []
    kategoriPendapatan = []
    kategoriPengeluaran = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Pencatat Keuangan Pribadi")
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Jalankan dalam mode CLI tanpa GUI"
    )
    args = parser.parse_args()

    if args.no_gui:
        import app.cli as c
        c.CLI(riwayat, kategoriPendapatan, kategoriPengeluaran).run_cli()
    else:
        import app.gui as g
        g.GUI(riwayat, kategoriPendapatan, kategoriPengeluaran).run_gui()
