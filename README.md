> Project ini terinspirasi oleh aplikasi *Catatan Keuangan* karya Sepran Ashari <br>
> https://play.google.com/store/apps/details?id=com.jmc.catatankeuangan

# Langkah Setup Project

1. Cek apakah python sudah terinstall 
    - Di Windows, buka Command Prompt / PowerShell
        ```cmd
        python --version
        ```
        - Jika terdapat error: <br>
            `'python' is not recognized as an internal or external command, 
            operable program or batch file.
            ` <br>
            itu artinya python belum terinstall, tapi jika merasa sudah diinstall
            ikuti tutorial ini: <br> https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-windows <br>
            scroll ke bawah hingga menemukan video-nya.
    - Di Unix (Linux/MacOS)
        ```bash
        python3 --version
        ```


## Untuk Windows

1. Buka Command Prompt / PowerShell
2. Buat folder untuk project (opsional, tapi direkomendasikan)

```cmd
cd %USERPROFILE%
mkdir python
cd python
mkdir venv
mkdir projects
```

2. Buat virtual environment

```cmd
cd venv
python -m venv venv-pencatatKeuangan-pyqt
```

3. Aktifkan environment

```cmd
venv-pencatatKeuangan-pyqt/bin/activate
```

Kalau berhasil, prompt-mu akan menampilkan (venv-pencatatKeuangan-pyqt) di depan

4. Download Repository ini dengan git
    - Buka Git
        ```bash
        cd %USERPROFILE%\python\projects\
        git clone https://github.com/mab-eric313/pencatatKeuangan-pyqt
        cd pencatatKeuangan-pyqt
        ```
    - Atau tanpa git, dengan lewat Github
        1. `Scroll ke atas > Code > Local > Download ZIP`
        2. Ekstrak file ZIP ke `C:\Users\Username-mu\python\projects\`
        3. Buka CMD
        ```cmd
        cd %USERPROFILE%\python\projects\pencatatKeuangan-pyqt
        ```

5. Install semua library yang dibutuhkan

```cmd
python -m pip install -r requirements.txt
```

## Untuk Unix (Linux/MacOS)

1. Buka terminal
2. Masuk ke direktori python environment
3. Buat virtual environment dan aktifkan environment

```bash
python3 -m venv venv-pencatatKeuangan-pyqt
source venv-pencatatKeuangan-pyqt
```

4. Masuk ke direktori python projects
5. Download Repository ini
6. Masuk ke project 
```bash
cd pencatatKeuangan-pyqt
```
7. Install semua library yang dibutuhkan

```bash
python3 -m pip install -r requirements.txt
```
