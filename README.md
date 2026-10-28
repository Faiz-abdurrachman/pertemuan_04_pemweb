# Praktikum Pemrograman Web — Pertemuan 04
## Layout dan Template Engine (Jinja2)

Repositori ini berisi kode referensi dan *starter kit* resmi untuk **Praktikum Pemrograman Web 2026 (Pertemuan 04)**.

Kode ini merupakan hasil refaktor dari proyek Pertemuan 03, di mana kerangka HTML yang sebelumnya berulang di setiap halaman telah disatukan ke dalam satu template induk (`templates/base.html`) menggunakan template inheritance (`{% extends %}` & `{% block %}`) dan passing data dinamis dari Flask ke Jinja2.

---

## 📂 Struktur Proyek

```
praktikum-p04/
├── app.py                      ← Backend utama Flask (Controller & Data)
├── templates/
│   ├── base.html               ← Layout induk (Header, Nav, Footer & Block)
│   ├── index.html              ← Beranda portofolio
│   ├── about.html              ← Halaman tentang/biodata
│   ├── skills.html             ← Halaman keahlian (Looping {% for %})
│   ├── projects.html           ← Halaman portofolio proyek
│   ├── blog.html               ← Halaman artikel blog statis
│   └── contact.html            ← Halaman kontak
└── static/
    ├── css/
    │   └── style.css           ← Desain CSS modern & token warna
    └── images/
        └── profile.jpg         ← Aset foto profil
```

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repositori
```bash
git clone https://github.com/Faiz-abdurrachman/pertemuan_04_pemweb.git
cd pertemuan_04_pemweb
```

### 2. Buat & Aktifkan Virtual Environment (Venv)
```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (Command Prompt / PowerShell)
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Flask
```bash
pip install flask
```

### 4. Jalankan Aplikasi
```bash
python app.py
```
Buka browser Anda dan akses: `http://127.0.0.1:5000`

---

## 📖 Panduan Lengkap
Untuk penjelasan teori mendalam, bedah kode per baris, dan tutorial langkah-demi-langkah, silakan baca [PANDUAN.md](PANDUAN.md).
