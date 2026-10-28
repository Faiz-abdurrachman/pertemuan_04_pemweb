# Panduan Belajar — Praktikum Web Flask (Pertemuan 3)

Portofolio pribadi multi-halaman dengan **Flask + HTML + CSS murni**.
Tanpa framework CSS, tanpa JavaScript, tanpa emoji (ikon pakai SVG).

---

## Daftar Isi

1. [Struktur Folder](#1-struktur-folder)
2. [Cara Menjalankan](#2-cara-menjalankan)
3. [app.py — Backend Flask](#3-apppy--backend-flask)
4. [Templates — Kerangka HTML](#4-templates--kerangka-html)
5. [Jinja2 — Template Engine](#5-jinja2--template-engine)
6. [Sintak HTML yang Dipakai](#6-sintak-html-yang-dipakai)
7. [style.css — Penjelasan Per Bagian](#7-stylecss--penjelasan-per-bagian)
8. [Konsep Inti CSS yang Diajarkan](#8-konsep-inti-css-yang-diajarkan)
9. [Animasi & Transisi](#9-animasi--transisi)
10. [Alur Request Lengkap](#10-alur-request-lengkap)
11. [Latihan Pengembangan](#11-latihan-pengembangan)

---

## 1. Struktur Folder

```
praktikum/
├── app.py                  ← Backend Flask (routing URL → HTML)
├── .venv/                  ← Virtual environment Python
├── templates/              ← SEMUA file HTML (Flask cari di sini)
│   ├── index.html          → route  /
│   ├── about.html          → route  /about
│   ├── skills.html         → route  /skills
│   ├── projects.html       → route  /projects
│   ├── blog.html           → route  /blog
│   └── contact.html        → route  /contact
└── static/                 ← File statis (TIDAK dirender)
    ├── css/
    │   └── style.css       ← Satu-satunya file CSS
    └── images/
        └── profile.jpg     ← Foto profil
```

> **PENTING:** `templates/` dan `static/` adalah nama folder **wajib**.
> Flask otomatis mencari file HTML di `templates/` dan file statis di `static/`.

---

## 2. Cara Menjalankan

```bash
# 1. Aktifkan virtual environment
source .venv/bin/activate

# 2. Jalankan server
python app.py

# 3. Buka browser
http://127.0.0.1:5000
```

Mode `debug=True` membuat server auto-reload tiap file disimpan.

---

## 3. app.py — Backend Flask

```python
from flask import Flask, render_template
```
- `Flask` → kelas utama framework.
- `render_template` → fungsi untuk menampilkan file HTML dari `templates/`.

```python
app = Flask(__name__)
```
Membuat instance aplikasi. `__name__` membantu Flask mengenali lokasi root project.

```python
@app.route("/")
def home():
    return render_template("index.html")
```
- `@app.route("/")` → **decorator** yang mendaftarkan URL `/` ke fungsi di bawahnya.
- Saat user membuka `/`, Flask menjalankan `home()` → render `index.html`.

**Pola yang sama diulang untuk semua halaman:**

| URL | Fungsi | File HTML |
|-----|--------|-----------|
| `/` | `home()` | `index.html` |
| `/about` | `about()` | `about.html` |
| `/skills` | `skills()` | `skills.html` |
| `/projects` | `projects()` | `projects.html` |
| `/blog` | `blog()` | `blog.html` |
| `/contact` | `contact()` | `contact.html` |

```python
if __name__ == "__main__":
    app.run(debug=True)
```
- Hanya jalan kalau file dieksekusi langsung (`python app.py`).
- `debug=True` → auto-reload + tampilkan error detail. **Jangan dipakai di produksi.**

**Inti:** Flask menghubungkan URL di browser ↔ file HTML di `templates/`.

---

## 4. Templates — Kerangka HTML

Setiap file HTML punya struktur **identik**:

```
<html style="...">           ← atribut anti-flash
  <head>
    meta charset
    meta viewport
    title
    <style> anti-flash </style>
    <link> style.css
    <link> Google Fonts
  </head>
  <body>
    <header>                 ← navigasi (SAMA di semua halaman)
      logo + nav (6 link)
    </header>
    <main>                   ← konten UNIK per halaman
      ...
    </main>
    <footer>                 ← copyright
  </body>
</html>
```

### Bagian `<head>`

```html
<meta charset="UTF-8">
```
Encoding karakter. Tanpa ini, huruf/simbol bisa rusak.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Wajib untuk **responsive** — lebar halaman mengikuti lebar layar (HP).

```html
<title>Faiz — Home</title>
```
Judul di tab browser.

```html
<style>html,body{background-color:#0A0A0C}</style>
```
**Anti-flash:** body langsung gelap sebelum `style.css` selesai dimuat.
Ini mencegah "kedipan putih" saat pindah halaman.

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```
Memuat file CSS. `{{ ... }}` adalah sintak Jinja2 (lihat bagian 5).

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk...&family=Inter...&family=JetBrains+Mono...&display=swap" rel="stylesheet">
```
Memuat 3 font Google:
- **Space Grotesk** → heading/display
- **Inter** → body text
- **JetBrains Mono** → label teknis, tag, angka

### Bagian `<header>`

```html
<a href="/" class="logo"><span>F</span>aiz</a>
<nav>
    <a href="/" class="active">Home</a>
    <a href="/about">About</a>
    ...
</nav>
```
- `class="logo"` → logo "Faiz" (huruf F diberi gradient lewat `<span>`).
- `class="active"` → **menandai halaman yang sedang dibuka** (pill putih). Class ini dipindah ke link yang sesuai di setiap halaman.

---

## 5. Jinja2 — Template Engine

Flask memakai **Jinja2** untuk menyisipkan logika Python ke HTML.

```html
{{ url_for('static', filename='css/style.css') }}
```

Output: `/static/css/style.css`

**Kenapa tidak tulis path langsung?**
Karena `url_for` otomatis benar walau struktur folder berubah.

| Sintak | Fungsi |
|--------|--------|
| `{{ ... }}` | Menampilkan nilai (output) |
| `{% ... %}` | Logika (if, for) — belum dipakai di project ini |

`url_for('static', filename=...)` = cari file di folder `static/`.

---

## 6. Sintak HTML yang Dipakai

### Struktur & Teks
| Tag | Fungsi |
|-----|--------|
| `<header>` | Bagian atas/navigasi |
| `<nav>` | Kumpulan link navigasi |
| `<main>` | Konten utama (hanya satu per halaman) |
| `<section>` | Blok konten bertema |
| `<footer>` | Bagian bawah |
| `<h1>`–`<h4>` | Heading (judul) |
| `<p>` | Paragraf |
| `<ul>` / `<li>` | List tidak berurutan / item list |
| `<a href>` | Link |
| `<span>` | Wadah inline (untuk styling sebagian teks) |
| `<div>` | Wadah blok |

### Konten Khusus
```html
<img src="..." alt="Faiz">
```
`alt` = teks alternatif jika gambar gagal dimuat (juga untuk aksesibilitas).

```html
<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
    <path d="..."/>
</svg>
```
- **SVG** = gambar vektor (tidak pecah saat diperbesar). Dipakai untuk semua ikon.
- `viewBox="0 0 24 24"` → kanvas koordinat 24x24.
- `stroke-linecap/linejoin="round"` → ujung garis membulat (kesan halus/premium).
- `<path d="..."/>` → gambar ikonnya.

### Form (di contact.html)
```html
<form action="/contact" method="GET">
    <label for="name">Nama</label>
    <input type="text" id="name" name="name" placeholder="...">
    <textarea id="message" name="message"></textarea>
    <button type="submit" class="btn">Kirim</button>
</form>
```
- `action="/contact"` → ke mana data dikirim.
- `method="GET"` → data dikirim lewat URL (untuk demo; produksi pakai POST).
- `for` pada `<label>` harus sama dengan `id` pada `<input>` → klik label fokus ke input.

### Entity HTML
| Tulis | Hasil |
|-------|-------|
| `&copy;` | © |
| `&mdash;` | — |
| `&amp;` | & |
| `&lt;` / `&gt;` | < / > |

---

## 7. style.css — Penjelasan Per Bagian

### Part 1 — Reset (baris 8)
```css
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
```
- `*` = semua elemen → hapus margin/padding default browser.
- `box-sizing:border-box` → lebar elemen sudah termasuk padding + border.

### Part 2 — Page Transitions (baris 10–35)
```css
html{background-color:#0A0A0C}
@view-transition{ navigation:auto; }
::view-transition-old(root){ animation:pageOut .42s ...; }
::view-transition-new(root){ animation:pageIn .5s ...; }
```
- `@view-transition { navigation:auto }` → aktifkan **View Transitions API** native saat pindah halaman.
- `::view-transition-old(root)` → halaman lama keluar (animasi `pageOut`).
- `::view-transition-new(root)` → halaman baru masuk (animasi `pageIn`).
- `header{view-transition-name:site-header}` → header diam saat transisi.

### Part 3 — Variabel / Design Tokens (baris 37–60)
```css
:root{
  --bg:#0A0A0C;
  --text:#F4F4F6;
  --accent:#9BA8FF;
  --gold:#C9A86A;
  --glass:rgba(255,255,255,0.045);
  --r-lg:20px;
  --font-body:'Inter',...;
}
```
- `:root` = elemen teratas; variabel di sini bisa dipakai di mana saja.
- `--nama:nilai` = **CSS custom property** (variabel), dipakai dengan `var(--nama)`.
- **Ganti satu nilai → berubah seluruh halaman.**

**Palet warna:**

| Variabel | Nilai | Fungsi |
|----------|-------|--------|
| `--bg` | `#0A0A0C` | Background gelap |
| `--text` | `#F4F4F6` | Teks terang |
| `--text-soft` | `#B9B9C6` | Teks sekunder |
| `--text-muted` | `#7C7C8A` | Teks redup |
| `--accent` | `#9BA8FF` | Biru-violet (aksen utama) |
| `--accent-2` | `#CDB8FF` | Lavender |
| `--gold` | `#C9A86A` | Aksen mewah |
| `--glass` | `rgba(255,255,255,.045)` | Permukaan kaca |

**Radius (sudut tumpul):** `--r-xl:26px`, `--r-lg:20px`, `--r-md:14px`, `--r-sm:10px`, `--r-pill:999px`.

### Part 4 — Base & Background (baris 62–95)
```css
body{
  min-height:100vh;
  display:flex; flex-direction:column;
  background-image:radial-gradient(...), radial-gradient(...);
}
```
- `min-height:100vh` → minimal setinggi layar.
- `display:flex; flex-direction:column` → body jadi kolom; `main` nanti `flex:1`.
- `radial-gradient` → cahaya lembut di pojok (efek glow).

```css
body::before{ /* orb cahaya, position:fixed, blur, animasi drift */ }
```
`::before` = elemen palsu untuk "orb" yang bergerak pelan. `z-index:-1` = di belakang.

### Part 5 — Typewriter & Animasi Masuk (baris 97–125)
```css
.typewriter{
  overflow:hidden; white-space:nowrap;
  border-right:2px solid var(--accent);
  animation:typing 2.2s steps(22) forwards, blink .8s step-end infinite;
  width:0;
}
@keyframes typing{to{width:100%}}
@keyframes blink{50%{border-color:transparent}}
```
Lebar dari 0→100% = efek mengetik. `border-right` = kursor, `blink` = kedip.

```css
.stagger>*{animation:riseIn .8s ... both}
.stagger>*:nth-child(1){animation-delay:.05s}
.stagger>*:nth-child(2){animation-delay:.15s}
```
**Staggered animation:** anak ke-1 muncul dulu, ke-2 menyusul, dst.

### Part 6 — Header (baris 127–170)
```css
header{
  position:sticky; top:0; z-index:100;
  backdrop-filter:blur(20px) saturate(140%);
  border-radius:var(--r-pill);
}
```
- `position:sticky; top:0` → header menempel saat scroll.
- `backdrop-filter:blur(20px)` → **efek kaca (glassmorphism)**.
- `saturate(140%)` → warna di belakang lebih vivid.

### Part 7 — Main & Section (baris 172–206)
```css
main{ max-width:1000px; margin:2.8rem auto 0; flex:1; }
```
`max-width` batasi lebar, `margin:auto` center, `flex:1` isi ruang.

```css
.section-title::before{ /* titik gold */ }
.section-title::after { /* garis gradient */ }
```
Dekorasi judul murni dari CSS (tanpa HTML tambahan).

### Part 8 — Hero (baris 208–286)
Kartu kaca besar, `display:flex` (foto + teks sejajar). Foto bulat, cincin putus-putus yang berputar (`animation:spin`).

### Part 9 — Glass Card & Grid (baris 288–341)
```css
.card-grid{ display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); }
```
Bikin kolom sebanyak mungkin, masing-masing minimal 260px.

### Part 10 — Timeline (baris 343–394)
Garis vertikal (`::before`) + titik per item (`::before`). Hover = titik membesar.

### Part 11 — Skill Bar (baris 396–427)
```css
.skill .bar::after{ width:var(--fill,0%); animation:fillBar 1.8s ...; }
```
Lebar bar diambil dari variabel `--fill` yang di-set inline di HTML, mis:
```html
<div class="bar" style="--fill:90%"></div>
```

### Part 12 — Stats Grid (baris 429–486)
Kartu angka. `.number` pakai gradient text:
```css
background:linear-gradient(...); background-clip:text; color:transparent;
```

### Part 13 — Quote, Blog, Project (baris 488–659)
Kartu kaca serupa dengan hover naik. `.quote::before` = tanda kutip besar.

### Part 14 — Form & Contact (baris 661–761)
`input:focus` → glow biru saat diklik. `.btn` → tombol putih dengan hover.

### Part 15 — About, Footer (baris 763–799)
`.about-content` = kartu teks. Footer = pill kaca.

### Part 16 — Responsive (baris 801–819)
```css
@media(max-width:640px){
  header{flex-direction:column}
  .card-grid,...{grid-template-columns:1fr}
}
```
Layar ≤640px (HP): header vertikal, grid jadi 1 kolom.

### Part 17 — Prefers-reduced-motion (baris 821–826)
```css
@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
  @view-transition{navigation:none}
}
```
User yang mengaktifkan "kurangi gerakan" di OS → semua animasi mati. **Ini aksesibilitas.**

### Part 18 — Utility (baris 828–830)
`.mb-3`, `.text-muted` = class bantu cepat.

---

## 8. Konsep Inti CSS yang Diajarkan

### a. Box Model
Setiap elemen = kotak: `content → padding → border → margin`.
`box-sizing:border-box` membuat `width` sudah termasuk padding + border.

### b. Flexbox (1 dimensi)
```css
display:flex; justify-content:space-between; align-items:center; gap:1rem;
```
- `justify-content` → atur sumbu utama (horizontal default).
- `align-items` → atur sumbu silang (vertikal default).
- `gap` → jarak antar item.

Dipakai di: header, hero, main (kolom), dll.

### c. CSS Grid (2 dimensi)
```css
display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr));
```
`auto-fill` + `minmax` = grid responsif otomatis. Dipakai di: card-grid, project-grid, blog-grid, stats-grid.

### d. Position
| Nilai | Arti |
|-------|------|
| `static` | Default |
| `relative` | Relatif ke posisi normal (jadi acuan `absolute`) |
| `absolute` | Ditempatkan relatif ke parent `relative` terdekat |
| `fixed` | Nempel di viewport (tidak ikut scroll) |
| `sticky` | Normal, tapi menempel saat scroll melewati batas |

### e. Pseudo-element & Pseudo-class
- `::before` / `::after` → elemen virtual (dekorasi tanpa HTML).
- `:hover` → saat kursor di atas elemen.
- `:focus` → saat elemen aktif (input diklik).
- `:nth-child(n)` → anak ke-n.

### f. Pseudo-element + `content`
```css
.section-title::before{ content:''; width:6px; height:6px; ... }
```
Wajib ada `content` walau kosong, agar pseudo-element muncul.

---

## 9. Animasi & Transisi

### `transition` — perubahan halus saat state berubah
```css
.card-3d{ transition:transform .4s cubic-bezier(.22,.61,.36,1), box-shadow .4s; }
.card-3d:hover{ transform:translateY(-6px); }
```

### `@keyframes` — animasi mandiri
```css
@keyframes riseIn{
  from{opacity:0; transform:translateY(28px)}
  to{opacity:1; transform:translateY(0)}
}
.stagger>*{ animation:riseIn .8s both; }
```

### Properti animasi
| Properti | Arti |
|----------|------|
| `animation-name` | Nama `@keyframes` |
| `animation-duration` | Durasi |
| `animation-delay` | Jeda sebelum mulai |
| `animation-timing-function` | `ease`, `linear`, `cubic-bezier()` |
| `animation-iteration-count` | `infinite` = terus-menerus |
| `animation-fill-mode` | `both`/`forwards` = tahan state akhir |

### Daftar animasi di project ini
| Nama | Efek | Dipakai di |
|------|------|-----------|
| `pageIn` / `pageOut` | Transisi antar halaman | View Transitions |
| `drift` | Orb cahaya bergerak | body::before |
| `typing` | Teks mengetik | hero |
| `blink` | Kursor berkedip | hero |
| `riseIn` | Muncul dari bawah | .stagger |
| `spin` | Cincin berputar | hero-image |
| `fillBar` | Bar terisi | skill bar |

### Glassmorphism
```css
background:rgba(255,255,255,0.045);
backdrop-filter:blur(20px) saturate(140%);
border:1px solid rgba(255,255,255,0.10);
```
Kunci efek kaca: background transparan + blur + border tipis terang.

---

## 10. Alur Request Lengkap

Contoh: user membuka `http://127.0.0.1:5000/projects`

```
1. Browser minta URL /projects
        ↓
2. Flask cek app.py → ada @app.route("/projects")
        ↓
3. Jalankan projects() → render_template("projects.html")
        ↓
4. Jinja2 ganti {{ url_for(...) }} jadi path asli
        ↓
5. HTML dikirim ke browser
        ↓
6. Browser unduh style.css + font + gambar
        ↓
7. CSS terapkan tema + animasi
        ↓
8. Klik tab lain → View Transitions bikin crossfade-slide mulus
```

---

## 11. Latihan Pengembangan

Coba kembangkan sendiri (tetap HTML+CSS, tanpa framework):

1. **Tambah halaman baru** — buat `templates/galeri.html`, tambahkan route di `app.py`, tambah link di header semua halaman.
2. **Ganti palet warna** — ubah nilai di `:root` dan lihat efeknya ke seluruh halaman.
3. **Buat skill bar baru** — tambah `<div class="skill">` dengan `style="--fill:X%"`.
4. **Tambah animasi** — buat `@keyframes` baru dan pasang ke sebuah elemen.
5. **Ganti font** — coba font Google lain di `<link>` dan variabel `--font-body`.
6. **Buat dark/light mode** — eksperimen dengan `@media(prefers-color-scheme:light)`.

---

## Ringkasan Cepat

| File | Peran |
|------|-------|
| `app.py` | Routing: URL → file HTML |
| `templates/*.html` | Struktur halaman (HTML + Jinja2) |
| `static/css/style.css` | Tampilan: tema, layout, animasi |
| `static/images/` | Gambar (foto profil) |
| `{{ url_for('static', filename=...) }}` | Cara aman menautkan file statis |
| `:root { --var }` | Variabel warna/ukuran global |
| `display:flex` / `display:grid` | Layout modern |
| `@keyframes` + `transition` | Animasi murni CSS |
| `backdrop-filter:blur()` | Efek kaca (glassmorphism) |
| `@media(max-width:640px)` | Responsive untuk HP |