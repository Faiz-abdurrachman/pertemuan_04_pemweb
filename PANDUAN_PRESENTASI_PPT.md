# 📚 Panduan Lengkap Slide Presentasi PPT: Praktikum 04
**Mata Kuliah**: Praktikum Pemrograman Web  
**Topik**: Modul 04 – Layout dan Template Engine (Jinja2)  
**Target Pembaca**: Asisten Dosen (Slide Deck & Speaker Notes)

---

## 🗺️ Gambaran Alur Presentasi (Overview)

| Slide | Topik / Judul Slide | Jenis Media / Screenshot | Nama File Screenshot |
| :---: | :--- | :--- | :--- |
| **01** | Cover & Capaian Pembelajaran | Bullet points & Icon | - |
| **02** | Masalah di Praktikum 03 (Refleksi) | Poin Analisis DRY Principle | - |
| **03** | Part 1: Membuat Base Template (`base.html`) | VS Code Code Screenshot (Highlight Blocks) | `slide-03-code-base-html.png` |
| **04** | Perbandingan: P-03 vs P-04 (Before vs After) | Side-by-Side Comparison Code | `slide-04-compare-p03-vs-p04.png` |
| **05** | Part 2: Child Template Inheritance (`index.html`) | VS Code Code Screenshot (Highlight `{% extends %}`) | `slide-05-code-index-inheritance.png` |
| **06** | Hasil Live Browser: Template Inheritance | Browser View Screenshot | `slide-06-browser-home.png` |
| **07** | Part 3: Mengoper Data dari Python (`app.py`) | VS Code Code Screenshot (Highlight Dict & List) | `slide-07-code-app-py.png` |
| **08** | Konsep Data Passing: Backend ke Template | Diagram Alur Flask &rarr; Jinja2 | - |
| **09** | Part 4: Perulangan Dinamis (`{% for %}`) | VS Code Code Screenshot (Highlight Loop) | `slide-09-code-loop-for.png` |
| **10** | Hasil Live Browser: Loop Mata Kuliah | Browser View Screenshot | `slide-10-browser-loop-result.png` |
| **11** | Part 5: Percabangan Logika (`{% if %}`) | VS Code Code Screenshot (Highlight If/Else) | `slide-11-code-conditional-if.png` |
| **12** | Hasil Akhir Live Browser Halaman Home | Browser View Screenshot | `slide-12-browser-final.png` |
| **13** | Halaman Tambahan: About & Contact | Browser View Screenshot | `slide-13-browser-about.png` & `slide-14-browser-contact.png` |
| **14** | Tugas Praktikum (Hands-on Mahasiswa) | Instruksi Tugas (30 Menit) | - |
| **15** | Rubrik Penilaian & Sesi Tanya Jawab | Tabel Penilaian (Total 100%) | - |

---

## 📑 Rincian Slide-by-Slide (Lengkap dengan Speaker Notes)

### SLIDE 01: Judul & Capaian Pembelajaran
* **Judul Slide**: Praktikum 04 – Layout dan Template Engine (Jinja2)
* **Poin Isi Slide**:
  1. **Template Inheritance**: Membuat struktur layout induk (`base.html`) dan mewarisinya ke halaman anak.
  2. **Data Passing**: Mengirim data terstruktur (Dictionary & List) dari Python backend ke template HTML.
  3. **Control Structures**: Memanfaatkan logika Jinja2 (`{% for %}` dan `{% if %}`) untuk merender antarmuka dinamis.
* 🎙️ **Speaker Notes**:
  > *"Halo teman-teman praktikan, di pertemuan ke-4 ini kita akan meng-upgrade website profil yang sudah kalian buat minggu lalu di Praktikum 03. Hari ini kita akan belajar template engine Jinja2 agar website kita tidak lagi kaku, kodenya tidak berulang-ulang, dan datanya bisa dikirim dinamis dari Python backend."*

---

### SLIDE 02: Refleksi Masalah di Praktikum 03 (Why Jinja2?)
* **Judul Slide**: Mengapa Kita Membutuhkan Jinja2?
* **Poin Isi Slide**:
  * ❌ **Kode Berulang (Violating DRY - Don't Repeat Yourself)**:
    * Tag `<head>`, `<header>`, navigasi `<nav>`, dan `<footer>` di-copy-paste sama persis di `index.html`, `about.html`, dan `contact.html`.
    * Jika ingin menambah 1 menu di navigasi, kita harus mengedit 3 file sekaligus secara manual.
  * ❌ **Data Hardcoded / Statis**:
    * Daftar mata kuliah diketik manual dengan tag `<li>`. Jika mata kuliah bertambah, kita harus mengedit file HTML.
* 🎙️ **Speaker Notes**:
  > *"Coba kalian ingat kembali kode P-03 minggu lalu. Di index, about, dan contact, kalian mengetik ulang header dan footer yang sama persis. Di dunia pemrograman profesional, ada prinsip DRY: Don't Repeat Yourself. Di P-04 ini, kita akan membuat satu template induk saja, dan halaman lain cukup mewarisinya."*

---

### SLIDE 03: Part 1 — Membuat Base Template (`base.html`)
* **Judul Slide**: Part 1: Membuat Layout Induk (`templates/base.html`)
* **Poin Penjelasan**:
  * Menampung seluruh kerangka bersama: `<!DOCTYPE html>`, `<head>`, navigasi, dan `<footer>`.
  * Menyiapkan "lubang dinamis" menggunakan tag Jinja2:
    * `{% block title %}Web Saya{% endblock %}`
    * `{% block content %}{% endblock %}`
  * Helper `url_for('nama_fungsi')`: URL dibuat otomatis oleh Flask, bukan path statis hardcoded.
* 🖼️ **Screenshot**: `screenshots/slide-03-code-base-html.png`
* 🎙️ **Speaker Notes**:
  > *"Perhatikan kotak merah pada kode di layar. Kita membuat file baru bernama `templates/base.html`. Blok `{% block content %}` adalah tempat di mana konten unik tiap halaman akan disisipkan nantinya. Selain itu, tag `<a href>` sekarang menggunakan fungsi `url_for()` milik Flask."*

---

### SLIDE 04: Perbandingan P-03 vs P-04 (Before vs After)
* **Judul Slide**: Perbandingan Kode: Sebelum vs Sesudah Inheritance
* **Poin Penjelasan**:
  * **P-03 (Sebelum)**: 41 baris penuh pengulangan tag HTML dasar.
  * **P-04 (Sesudah)**: Cukup 20 baris! Lebih bersih, mudah dirawat, dan modular.
* 🖼️ **Screenshot**: `screenshots/slide-04-compare-p03-vs-p04.png`
* 🎙️ **Speaker Notes**:
  > *"Lihat perbedaannya di layar. Kode sebelah kiri adalah kode P-03 kalian yang penuh boilerplate. Kode sebelah kanan adalah P-04. Kita menghemat lebih dari setengah baris kode, dan tampilan webnya tetap persis sama!"*

---

### SLIDE 05: Part 2 — Child Template Inheritance (`index.html`)
* **Judul Slide**: Part 2: Mewarisi Base Template (`templates/index.html`)
* **Poin Penjelasan**:
  * `{% extends 'base.html' %}`: Memberi tahu Jinja2 bahwa file ini menggunakan kerangka induk `base.html`.
  * `{% block title %}`: Menentukan judul tab browser spesifik untuk halaman ini.
  * `{% block content %}`: Tempat meletakkan isi konten utama (Profil & Mata Kuliah).
* 🖼️ **Screenshot**: `screenshots/slide-05-code-index-inheritance.png`
* 🎙️ **Speaker Notes**:
  > *"Di file `index.html`, seluruh tag `<html>`, `<head>`, `<header>`, dan `<footer>` kita buang. Kita ganti dengan baris 1: `{% extends 'base.html' %}`. Konten profil cukup kita bungkus di dalam blok content."*

---

### SLIDE 06: Pembuktian di Browser: Inheritance Berfungsi!
* **Judul Slide**: Hasil di Browser: Tampilan Utuh Tanpa Duplikasi
* **Poin Penjelasan**:
  * Website tetap memiliki header, navigasi, dan footer yang rapi.
  * CSS dan foto profil tetap ter-render dengan sempurna.
* 🖼️ **Screenshot**: `screenshots/slide-06-browser-home.png`
* 🎙️ **Speaker Notes**:
  > *"Sekarang saat kita jalankan dan buka `localhost:5000`, tampilannya tetap utuh sempurna! Padahal di `index.html` tidak ada lagi tag header maupun footer. Semua di-inject otomatis oleh Jinja2 dari `base.html`."*

---

### SLIDE 07: Part 3 — Mengoper Data dari Python (`app.py`)
* **Judul Slide**: Part 3: Mengirim Data dari Backend ke Template
* **Poin Penjelasan**:
  * Pada file [app.py](file:///home/faiz/asdos/praktikum-p04/app.py), route `home()` mendefinisikan Dictionary `data`.
  * `data` berisi tipe data primitif (`nama`, `umur`) dan List (`mata_kuliah`).
  * Argumen `render_template("index.html", data=data)` mengirim variabel `data` agar bisa dibaca oleh template Jinja2.
* 🖼️ **Screenshot**: `screenshots/slide-07-code-app-py.png`
* 🎙️ **Speaker Notes**:
  > *"Sekarang kita masuk ke backend di `app.py`. Perhatikan kotak merah. Kita tidak lagi hanya me-render HTML kosong, melainkan mengirimkan dictionary `data`. Ada data nama, umur, dan list mata kuliah. Variabel ini nantinya kita panggil di template HTML."*

---

### SLIDE 08: Part 4 — Looping Data di Template (`{% for %}`)
* **Judul Slide**: Part 4: Perulangan Dinamis dengan `{% for %}`
* **Poin Penjelasan**:
  * Di `templates/index.html`, 3 baris `<li>` manual digantikan oleh sintaks:
    ```html
    <ul>
        {% for mk in data.mata_kuliah %}
            <li>{{ mk }}</li>
        {% endfor %}
    </ul>
    ```
  * Menampilkan variabel tunggal menggunakan kurung kurawal ganda: `{{ data.nama }}`.
* 🖼️ **Screenshot**: `screenshots/slide-09-code-loop-for.png`
* 🎙️ **Speaker Notes**:
  > *"Kemarin kita mengetik `<li>` satu per satu. Sekarang, kita cukup pakai perulangan Jinja `{% for mk in data.mata_kuliah %}`. Berapapun jumlah mata kuliah yang dikirim dari Python, tag `<li>` akan otomatis digenerate sejumlah data tersebut."*

---

### SLIDE 09: Part 5 — Percabangan Logika (`{% if %}`)
* **Judul Slide**: Part 5: Percabangan Logika Tampilan (`{% if %}`)
* **Poin Penjelasan**:
  * Menentukan status usia mahasiswa berdasarkan nilai `data.umur`:
    ```html
    {% if data.umur >= 18 %}
        <span class="status">Dewasa ({{ data.umur }} tahun)</span>
    {% else %}
        <span class="status">Di bawah umur</span>
    {% endif %}
    ```
  * Elemen HTML di dalam blok hanya akan muncul jika kondisi bernilai `True`.
* 🖼️ **Screenshot**: `screenshots/slide-11-code-conditional-if.png`
* 🎙️ **Speaker Notes**:
  > *"Jinja2 juga punya control structure percabangan `{% if %}`. Di sini kita cek: jika umur mahasiswa >= 18 tahun, maka tampilkan label 'Dewasa'. Kalau di bawah 18 tahun, tampilkan 'Di bawah umur'. Ini membuktikan bahwa tampilan website bisa reaktif terhadap data backend!"*

---

### SLIDE 10: Tampilan Akhir Halaman Home (Live Browser)
* **Judul Slide**: Hasil Akhir: Web Profil Dinamis Berbasis Jinja2
* **Poin Penjelasan**:
  * Nama mahasiswa dinamis dari Python (`data.nama`).
  * Badge status usia hijau berhasil ter-render (`Dewasa (20 tahun)`).
  * 3 mata kuliah berhasil di-loop dari Python list.
* 🖼️ **Screenshot**: `screenshots/slide-12-browser-final.png`
* 🎙️ **Speaker Notes**:
  > *"Inilah hasil akhir halaman Home kita. Seluruh data di layar ini bukan lagi teks statis di HTML, melainkan diisi secara dinamis dari backend Flask menggunakan Jinja2."*

---

### SLIDE 11: Penerapan pada Halaman Lain (`about` & `contact`)
* **Judul Slide**: Konsistensi pada Halaman About & Contact
* **Poin Penjelasan**:
  * Halaman [about.html](file:///home/faiz/asdos/praktikum-p04/templates/about.html) dan [contact.html](file:///home/faiz/asdos/praktikum-p04/templates/contact.html) juga mewarisi `base.html`.
  * Desain, header, dan footer otomatis seragam di seluruh halaman website.
* 🖼️ **Screenshot**: `screenshots/slide-13-browser-about.png` & `screenshots/slide-14-browser-contact.png`
* 🎙️ **Speaker Notes**:
  > *"Hal yang sama kita terapkan pada halaman About dan Contact. Keduanya cukup meng-extends `base.html`. Struktur website kita sekarang sangat rapi dan profesional."*

---

### SLIDE 12: Tugas Praktikum Mahasiswa (Hands-on 30 Menit)
* **Judul Slide**: Tugas Praktikum Mahasiswa
* **Instruksi Tugas**:
  1. Buat file `templates/base.html` sebagai layout utama dengan header, navigasi (`url_for`), dan footer.
  2. Pastikan minimal **3 halaman** (`index`, `about`, `contact`) mewarisi (*extends*) `base.html`.
  3. Kirimkan data terstruktur dari salah satu route di `app.py` dan render ke template menggunakan perulangan `{% for %}`.
  4. Tambahkan minimal **satu kondisi percabangan `{% if %}`** untuk menampilkan status data secara dinamis.
  5. Pengumpulan: Kompres proyek menjadi format `.zip` dan kumpulkan ke LMS sebelum batas waktu.

---

### SLIDE 13: Rubrik Penilaian
* **Judul Slide**: Rubrik Penilaian Praktikum 04 (Total: 100%)

| Komponen Penilaian | Bobot | Kriteria Nilai Maksimal (100%) |
| :--- | :---: | :--- |
| **Base Template** | **25%** | `base.html` lengkap, navigasi menggunakan `url_for()`, blok Jinja rapi |
| **Template Inheritance** | **25%** | Minimal 3 halaman berhasil meng-extends `base.html` tanpa duplikasi layout |
| **Data Passing** | **25%** | Data dictionary/list berhasil dikirim dari Python ke template |
| **Control Structures** | **25%** | Menggunakan perulangan `{% for %}` dan percabangan `{% if %}` dengan benar |

---

## 📁 Lokasi Seluruh File Screenshot Siap Pakai
Semua screenshot beresolusi tinggi sudah tersedia di folder:  
`file:///home/faiz/asdos/praktikum-p04/screenshots/`
* [slide-03-code-base-html.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-03-code-base-html.png)
* [slide-04-compare-p03-vs-p04.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-04-compare-p03-vs-p04.png)
* [slide-05-code-index-inheritance.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-05-code-index-inheritance.png)
* [slide-06-browser-home.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-06-browser-home.png)
* [slide-07-code-app-py.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-07-code-app-py.png)
* [slide-09-code-loop-for.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-09-code-loop-for.png)
* [slide-10-browser-loop-result.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-10-browser-loop-result.png)
* [slide-11-code-conditional-if.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-11-code-conditional-if.png)
* [slide-12-browser-final.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-12-browser-final.png)
* [slide-13-browser-about.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-13-browser-about.png)
* [slide-14-browser-contact.png](file:///home/faiz/asdos/praktikum-p04/screenshots/slide-14-browser-contact.png)
