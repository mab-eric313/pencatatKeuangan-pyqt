# Tugas 1 RPL
1. Ide Awal Proyek
    - Pencatat Keuangan Pribadi

2. End-user (pengguna) : 
    - Pengguna individu yang ingin mencatat dan mengelola finansial pribadi seperti, pemasukan, pengeluaran, transfer antar bank maupun e-wallet, hutang-piutang, dan melihat laporan transaksi dalam sebulan tanpa bergantung pada aplikasi yang beriklan maupun berbayar

3. SDLC yang digunakan dan alasannya : 
    - SDLC: Iterative and Incremental
        - Alur siklus pengembangan:
            1. Requirement Analysis
            2. Design
            3. Coding Implementation
            4. Testing
            5. Deployment/Release (next iteration)
    - Alasan: 
        1. Fleksibel terhadap perubahan kebutuhan
        2. Memungkinkan untuk menambah fitur di setiap iterasi
        3. Memungkinkan prioritas fitur yang dapat berubah seiring waktu
        4. Memudahkan deteksi dan perbaikan bug dan error secara bertahap
        5. Memungkinkan desain program yang dapat berubah-ubah sesuai yang kebutuhan

4. Rencana timeline pengerjaan sistem (20 Oktober 2025 - Januari)
    - Catatan: Antarmuka CLI hanya untuk pengembangan saja memastikan fitur-fitur yang ada bekerja dengan baik, bukan aplikasi yang akan di deploy
    - (Minggu ke-1 dan 2, 20-Okt - 01-Nov) Setup kebutuhan project, seperti install python, python env, library yang digunakan, dll.
    - (Pertengahan November) Versi pengembangan 0.1-development
        - CLI: 
            1. Membangun dan memastikan fondasi logika transaksi (pendapatan, pengeluaran, transfer) berjalan dengan baik 
            2. Menampilkan pendapatan, pengeluaran, balance
        - GUI: Membangun antarmuka layout transaksi sederhana
    - (Akhir November 2025) Versi pengembangan 0.2-development
        - CLI: Logika dasar transaksi, dompet, laporan, hutang-piutang sudah jadi
        - GUI: Antarmuka awal transaksi, dompet, laporan, hutang-piutang sudah jadi
    - (Pertengahan Desember) Versi pengembangan 0.3-development
        - CLI: 
            1. Laporan bulanan dan detail-nya
            2. Fitur ekspor ke excel bekerja dengan baik
        - GUI: Penerapan logika transaksi, dompet, hutang-piutang bekerja dengan baik
    - (Akhir Desember) Versi pengembangan 0.4-development
        - GUI: Meng-implementasikan fitur laporan bulanan
    - (Pertengahan Januari 2026) Versi pengembangan 0.5-development
        - GUI: Meng-implementasikan fitur tanggal
    - (Akhir Januari 2026) Versi pengembangan 1.0-beta
        - GUI: Meng-implementasikan fitur ekspor ke excel dan mendeploy project


5. Kebutuhan awal sistem (fitur) yang akan dikembangkan, arsitektur sistem (web based, mobile based, desktop based)
    - Fitur: 
        1. Mencatat pendapatan, pengeluaran, dan transfer
        2. Mencatat hutang-piutang
        3. Mencatat laporan bulanan
        4. Dapat diekspor ke excel

    - Kekurangan dari Aplikasi Catatan Keuangan karya Sepran Ashari:
        1. Ada Iklan
        2. Tidak ada fitur menyimpan bukti nota

6. Lingkungan pengembangan sistem dan rencana pengembangan sistem (OS, bahasa pemrograman, framework dan tools yang digunakan).
    - Lingkungan pengembangan: 
        - OS: Windows dan Linux
        - Version Control: Git/Github 
        - Manajamen dependensi: Python Virtual Environment
    - Rencana Pengembangan:
        - OS: Desktop (Windows, Linux, macOS)
        - Bahasa Pemrograman: Python
        - Framework/Library:
            1. Qt (PySide6) untuk GUI
            2. JSON untuk penyimpanan histori transaksi di lokal
            3. OpenPyxl untuk ekspor ke excel
            4. PyInstaller untuk mengubah file Python ke file executable
            5. PyQtGraph untuk membuat grafik (opsional jika memungkinkan)
<br>
<br>
Roadmap: <br>
    - 0.0.1:  
        - CLI: 
            1. Membangun dan memastikan fondasi logika transaksi (pendapatan, pengeluaran, transfer) berjalan dengan baik 
            2. Menampilkan pendapatan, pengeluaran, balance
        - GUI: Membangun antarmuka layout transaksi sederhana
    - 0.0.2:
        - CLI: Koneksikan hari, tanggal, bulan, tahun, dan jam ke histori transaksi
        - GUI: Membuat antarmuka pendapatan, pengeluaran, dan transfer
