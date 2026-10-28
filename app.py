from flask import Flask, render_template

app = Flask(__name__)

# Data Mahasiswa (Dictionary untuk Variabel Tunggal)
profil = {
    "nama": "Faiz",
    "umur": 20,
    "kota": "Malang",
    "kampus": "Universitas Brawijaya",
    "semester": 3
}

# Daftar Keahlian (List of Dict untuk Loop & Kondisi)
skills = [
    {"nama": "HTML & CSS", "level": 90},
    {"nama": "Flask", "level": 85},
    {"nama": "JavaScript", "level": 75},
    {"nama": "Python", "level": 70}
]

@app.route("/")
def home():
    return render_template("index.html", aktif="home", profil=profil)

@app.route("/about")
def about():
    return render_template("about.html", aktif="about", profil=profil)

@app.route("/skills")
def keahlian():
    return render_template("skills.html", aktif="skills", skills=skills)

@app.route("/projects")
def projects():
    return render_template("projects.html", aktif="projects")

@app.route("/blog")
def blog():
    return render_template("blog.html", aktif="blog")

@app.route("/contact")
def contact():
    return render_template("contact.html", aktif="contact")

if __name__ == "__main__":
    app.run(debug=True)