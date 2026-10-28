# 004 — — Layout dan Template Engine (Jinja2)

Created: September 21, 2026 9:41 PM
Tags: Offline

# **Layout dan Template Engine (Jinja2)**

## **Capaian Pembelajaran**

Setelah mengikuti praktikum ini, mahasiswa mampu:

1. Mengimplementasikan layout dengan template inheritance di Jinja2
2. Mengoper data dari Python ke HTML
3. Menggunakan control structures dalam template

## **Dasar Teori**

**Jinja2** adalah template engine bawaan Flask yang memungkinkan:

- **Template Inheritance** - Membuat base template yang diwarisi oleh halaman lain
- **Variables** - Menampilkan data dari Python
- **Control Structures** - {% if %}, {% for %}, {% block %}

### **Struktur Template Inheritance:**

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default{% endblock %}</title>
</head>
<body>

    <header>
        {% block header %}{% endblock %}
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        {% block footer %}{% endblock %}
    </footer>

</body>
</html>

```

```html
<!-- child.html -->
{% extends 'base.html' %}

{% block title %}Halaman Saya{% endblock %}

{% block content %}
    <h1>Selamat Datang di Halaman Saya</h1>
    <p>Ini adalah isi konten utama yang diubah dari file anak.</p>
{% endblock %}

```

### **Tools yang Digunakan**

| No | Alat/Bahan | Spesifikasi/Fungsi |
| --- | --- | --- |
| 1 | Flask | Framework web |
| 2 | Jinja2 | Template engine |

## **Langkah Praktikum (45 menit)**

### **Part 1: Membuat Base Template**

1. Buat **`templates/base.html`**
    
    ```html
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}Web Saya{% endblock %}</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <header>
            <h1>{% block header %}Web Saya{% endblock %}</h1>
            <nav>
                <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('about') }}">About</a>
                <a href="{{ url_for('contact') }}">Contact</a>
            </nav>
        </header>
    
        <main>
            {% block content %}{% endblock %}
        </main>
    
        <footer>
            <p>&copy; 2025 - Web Saya</p>
        </footer>
    </body>
    </html>
    ```
    
    ![image.png](004%20%E2%80%94%20%E2%80%94%20Layout%20dan%20Template%20Engine%20(Jinja2)/image.png)
    

### **Part 2: Membuat Child Template**

1. Buat **`templates/index.html`**
    
    ```html
    {% extends 'base.html' %}
    
    {% block title %}Home{% endblock %}
    
    {% block content %}
    <section>
        <h2>Selamat Datang</h2>
        <p>Ini adalah halaman utama website saya.</p>
    </section>
    {% endblock %}
    
    ```
    
    ![image.png](004%20%E2%80%94%20%E2%80%94%20Layout%20dan%20Template%20Engine%20(Jinja2)/image%201.png)
    

### **Part 3: Mengoper Data dari Python ke Template**

1. Update **`app.py`**
    
    ```python
    from flask import Flask, render_template
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        data = {
            'nama': 'Mahasiswa',
            'umur': 20,
            'hobi': ['Coding', 'Membaca', 'Olahraga']
        }
        return render_template('index.html', data=data)
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    if __name__ == '__main__':
        app.run(debug=True)
    
    ```
    
    ![image.png](004%20%E2%80%94%20%E2%80%94%20Layout%20dan%20Template%20Engine%20(Jinja2)/image%202.png)
    

### **Part 4: Menampilkan Data di Template**

1. Update **`templates/about.html`**
    
    ```html
    {% extends 'base.html' %}
    
    {% block title %}Home{% endblock %}
    
    {% block content %}
    <section>
        <h2>Selamat Datang, {{ data.nama }}</h2>
        <p>Umur: {{ data.umur }} tahun</p>
        
        <h3>Hobi Saya:</h3>
        <ul>
            {% for hobi in data.hobi %}
                <li>{{ hobi }}</li>
            {% endfor %}
        </ul>
    </section>
    {% endblock %}
    
    ```
    
    ![image.png](004%20%E2%80%94%20%E2%80%94%20Layout%20dan%20Template%20Engine%20(Jinja2)/image%203.png)
    

### **Part 5: Menggunakan Control Structures**

1. Tambahkan conditional di template
    
    ```html
    {% if data.umur >= 18 %}
        <p>Anda sudah dewasa.</p>
    {% else %}
        <p>Anda masih di bawah umur.</p>
    {% endif %}
    ```
    
    ![image.png](004%20%E2%80%94%20%E2%80%94%20Layout%20dan%20Template%20Engine%20(Jinja2)/image%204.png)
    

## **Tugas Praktikum (30 menit)**

1. Buat base template dengan header, navigasi, footer
2. Buat minimal 3 halaman yang mewarisi base template
3. Kirim data list dari route dan tampilkan di template menggunakan loop
4. Gunakan conditional untuk menampilkan status berdasarkan data

### **Pengumpulan:**

- Upload seluruh file proyek (zip) ke LMS
- Deadline: sebelum pertemuan berikutnya

## **Rubrik Penilaian**

| Kriteria | Bobot | Excellent (100%) | Good (75%) | Fair (50%) | Poor (25%) |
| --- | --- | --- | --- | --- | --- |
| Base Template | 25% | Lengkap, rapi | Lengkap | Kurang lengkap | Tidak ada |
| Inheritance | 25% | Semua halaman mewarisi | 2 halaman | 1 halaman | Tidak ada |
| Data Passing | 25% | Data berhasil dikirim | Berhasil | Sebagian | Tidak ada |
| Control Structures | 25% | Loop dan if berfungsi | Satu berfungsi | Sebagian | Tidak ada |