import os, subprocess
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.templates import HtmlDjangoLexer
from pygments.formatters import HtmlFormatter

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    background: #0B0E14;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex; justify-content: center; align-items: center;
    padding: 24px; min-height: 100vh;
}}
.vscode-window {{
    width: 1280px; background: #1E1E1E; border-radius: 12px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.65), 0 0 0 1px rgba(255,255,255,0.12);
    overflow: hidden; display: flex; flex-direction: column;
}}
.titlebar {{
    height: 38px; background: #323233; display: flex; align-items: center;
    padding: 0 16px; color: #cccccc; font-size: 13px; border-bottom: 1px solid #252526;
}}
.window-controls {{ display: flex; gap: 8px; margin-right: 20px; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; }}
.dot-red {{ background: #FF5F56; }}
.dot-yellow {{ background: #FFBD2E; }}
.dot-green {{ background: #27C93F; }}
.window-title {{ flex: 1; text-align: center; color: #aaaaaa; font-size: 12.5px; font-weight: 500; }}
.main-body {{ display: flex; height: {body_height}px; }}
.sidebar {{
    width: 220px; background: #252526; border-right: 1px solid #191919;
    padding: 14px 0; color: #cccccc; font-size: 13px; user-select: none; flex: none;
}}
.sidebar-header {{
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.8px; padding: 0 16px 10px 16px; color: #8FA3BC;
}}
.tree-item {{
    padding: 5px 16px; display: flex; align-items: center; gap: 8px;
    color: #cccccc; font-size: 13px; font-family: -apple-system, sans-serif;
}}
.tree-item.indent {{ padding-left: 34px; }}
.tree-item.active {{ background: #37373D; color: #ffffff; font-weight: 600; border-left: 3px solid #007ACC; }}
.editor-container {{ flex: 1; display: flex; flex-direction: column; background: #1E1E1E; overflow: hidden; }}
.tab-bar {{ height: 38px; background: #252526; display: flex; align-items: flex-end; border-bottom: 1px solid #1E1E1E; }}
.tab {{
    padding: 9px 18px; font-size: 13px; color: #969696; background: #2D2D2D;
    display: flex; align-items: center; gap: 8px; border-right: 1px solid #252526;
}}
.tab.active {{ background: #1E1E1E; color: #ffffff; font-weight: 600; border-top: 2px solid #007ACC; }}
.breadcrumbs {{
    height: 28px; background: #1E1E1E; display: flex; align-items: center;
    padding: 0 16px; color: #888888; font-size: 12px; border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.breadcrumbs span {{ color: #ffffff; font-weight: 500; margin-left: 4px; }}
.code-area {{
    flex: 1; padding: 14px 0; font-family: "JetBrains Mono", "Cascadia Code", "Fira Code", Consolas, monospace;
    font-size: 13px; line-height: 1.6; overflow: hidden; position: relative;
}}
.code-line {{ display: flex; padding: 0 16px; position: relative; min-height: 20.8px; }}
.line-num {{ width: 42px; text-align: right; padding-right: 16px; color: #6E7681; user-select: none; flex: none; }}
.line-content {{ flex: 1; color: #D4D4D4; white-space: pre-wrap; word-break: break-word; }}

/* Highlight box */
.highlight-box {{
    position: absolute; left: 58px; right: 16px;
    border: 2px solid {hl_color}; background: {hl_bg};
    border-radius: 6px; box-shadow: 0 0 15px {hl_glow}; pointer-events: none;
}}
.highlight-badge {{
    position: absolute; right: 12px; top: -12px;
    background: {hl_color}; color: #ffffff; font-size: 11px;
    font-weight: 700; padding: 2px 10px; border-radius: 10px;
    font-family: -apple-system, sans-serif; letter-spacing: 0.5px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.5);
}}

{pygments_css}
</style>
</head>
<body>
<div class="vscode-window">
    <div class="titlebar">
        <div class="window-controls">
            <div class="dot dot-red"></div>
            <div class="dot dot-yellow"></div>
            <div class="dot dot-green"></div>
        </div>
        <div class="window-title">{filename} &mdash; praktikum-p04 &mdash; Visual Studio Code</div>
    </div>
    <div class="main-body">
        <div class="sidebar">
            <div class="sidebar-header">Explorer: PRAKTIKUM-P04</div>
            <div class="tree-item folder">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#858585" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D8A657" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                <span>static</span>
            </div>
            <div class="tree-item indent folder">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#858585" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D8A657" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                <span>css</span>
            </div>
            <div class="tree-item indent folder">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#858585" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D8A657" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                <span>images</span>
            </div>
            <div class="tree-item folder">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#858585" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D8A657" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                <span>templates</span>
            </div>
            <div class="tree-item indent {base_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>base.html</span>
            </div>
            <div class="tree-item indent {index_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>index.html</span>
            </div>
            <div class="tree-item indent {about_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>about.html</span>
            </div>
            <div class="tree-item indent {skills_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>skills.html</span>
            </div>
            <div class="tree-item indent {projects_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>projects.html</span>
            </div>
            <div class="tree-item indent {blog_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>blog.html</span>
            </div>
            <div class="tree-item indent {contact_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#E44D26" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                <span>contact.html</span>
            </div>
            <div class="tree-item {app_active}">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#4B8BBE" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                <span>app.py</span>
            </div>
        </div>
        <div class="editor-container">
            <div class="tab-bar">
                <div class="tab {base_active}">base.html</div>
                <div class="tab {index_active}">index.html</div>
                <div class="tab {skills_active}">skills.html</div>
                <div class="tab {app_active}">app.py</div>
            </div>
            <div class="breadcrumbs">
                {breadcrumb_html}
            </div>
            <div class="code-area">
                {highlight_box_html}
                {rendered_lines}
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

def generate_shot(code, lexer, filename, active_file, hl_start, hl_end, hl_text, hl_type, out_path, start_line_no=1, body_height=None, highlights=None):
    formatter = HtmlFormatter(style="monokai", nowrap=True)
    highlighted = highlight(code, lexer, formatter)
    lines = highlighted.strip().split("\n")
    
    line_height = 20.8
    padding_top = 14
    
    rendered_lines = []
    for i, line in enumerate(lines, start=start_line_no):
        rendered_lines.append(f'<div class="code-line"><span class="line-num">{i}</span><span class="line-content">{line}</span></div>')
    rendered_lines_html = "\n".join(rendered_lines)
    
    # Auto-calculate body height so all lines + padding are fully shown with zero cutoff!
    needed_code_h = padding_top + (len(lines) * line_height) + 32
    needed_body_h = int(38 + 28 + needed_code_h) # tab-bar(38) + breadcrumbs(28) + code area
    if body_height:
        actual_body_height = max(body_height, needed_body_h)
    else:
        actual_body_height = needed_body_h

    highlight_boxes = []
    effective_highlights = highlights if highlights is not None else ([(hl_start, hl_end, hl_text, hl_type)] if hl_start and hl_end else [])
    
    for (h_start, h_end, h_text, h_type) in effective_highlights:
        if h_type == "del":
            hl_color = "#F85149"
            hl_bg = "rgba(248, 81, 73, 0.12)"
            hl_glow = "rgba(248, 81, 73, 0.3)"
        elif h_type == "add":
            hl_color = "#2EA043"
            hl_bg = "rgba(46, 160, 67, 0.14)"
            hl_glow = "rgba(46, 160, 67, 0.35)"
        else: # notice / amber
            hl_color = "#D29922"
            hl_bg = "rgba(210, 153, 34, 0.12)"
            hl_glow = "rgba(210, 153, 34, 0.3)"
            
        rel_start = h_start - start_line_no + 1
        rel_end = h_end - start_line_no + 1
        top_px = padding_top + (rel_start - 1) * line_height - 2
        height_px = (rel_end - rel_start + 1) * line_height + 4
        highlight_boxes.append(f'''
        <div class="highlight-box" style="top: {top_px}px; height: {height_px}px; border-color: {hl_color}; background: {hl_bg}; box-shadow: 0 0 15px {hl_glow};">
            <div class="highlight-badge" style="background: {hl_color};">{h_text}</div>
        </div>
        ''')
    highlight_box_html = "\n".join(highlight_boxes)
        
    if filename == "app.py":
        breadcrumb_html = 'praktikum-p04 &gt; <span style="color:#ffffff;font-weight:600">app.py</span>'
    else:
        breadcrumb_html = f'praktikum-p04 &gt; templates &gt; <span style="color:#ffffff;font-weight:600">{filename}</span>'

    html = TEMPLATE.format(
        pygments_css=HtmlFormatter(style="monokai").get_style_defs('.code-content'),
        filename=filename,
        body_height=actual_body_height,
        breadcrumb_html=breadcrumb_html,
        base_active="active" if active_file == "base" else "",
        index_active="active" if active_file == "index" else "",
        about_active="active" if active_file == "about" else "",
        skills_active="active" if active_file == "skills" else "",
        projects_active="active" if active_file == "projects" else "",
        blog_active="active" if active_file == "blog" else "",
        contact_active="active" if active_file == "contact" else "",
        app_active="active" if active_file == "app" else "",
        hl_color="#2EA043",
        hl_bg="rgba(46, 160, 67, 0.14)",
        hl_glow="rgba(46, 160, 67, 0.35)",
        highlight_box_html=highlight_box_html,
        rendered_lines=rendered_lines_html
    )
    
    tmp_path = f"/tmp/{os.path.basename(out_path)}.html"
    with open(tmp_path, "w") as f:
        f.write(html)
        
    window_w = 1340
    window_h = actual_body_height + 38 + 56
    subprocess.run([
        'chromium', '--headless', '--disable-gpu',
        f'--window-size={window_w},{window_h}',
        f'--screenshot={out_path}',
        f'file://{tmp_path}'
    ], check=True)
    print(f"Saved: {out_path} ({window_w}x{window_h}, lines: {len(lines)})")

def run_all():
    print("Starting generation...")

    # 1. BASE.HTML (Langkah 1)
    code_base = """<!DOCTYPE html>
<html lang="id" style="background-color:#0A0A0C;color-scheme:dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Faiz — {% block title %}Home{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <a href="{{ url_for('home') }}" class="logo"><span>F</span>aiz</a>
        <nav>
            <a href="{{ url_for('home') }}"{% if aktif == 'home' %} class="active"{% endif %}>Home</a>
            <a href="{{ url_for('about') }}"{% if aktif == 'about' %} class="active"{% endif %}>About</a>
            <a href="{{ url_for('keahlian') }}"{% if aktif == 'skills' %} class="active"{% endif %}>Skills</a>
            <a href="{{ url_for('projects') }}"{% if aktif == 'projects' %} class="active"{% endif %}>Projects</a>
            <a href="{{ url_for('blog') }}"{% if aktif == 'blog' %} class="active"{% endif %}>Blog</a>
            <a href="{{ url_for('contact') }}"{% if aktif == 'contact' %} class="active"{% endif %}>Contact</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        &copy; 2026 Faiz
    </footer>
</body>
</html>"""
    generate_shot(code_base, HtmlDjangoLexer(), "base.html", "base", 23, 25, "LUBANG KONTEN ANAK: {% block content %}", "add", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-01-base-html.png")

    # 2. INDEX.HTML BEFORE (Langkah 2: Bagian yang DIHAPUS - KEPALA & EKOR)
    code_index_before = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Faiz — Home</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <header>
        <a href="/" class="logo">Faiz</a>
        <nav>
            <a href="/" class="active">Home</a>
            <a href="/about">About</a>
            <a href="/skills">Skills</a>
            <a href="/projects">Projects</a>
            <a href="/blog">Blog</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h2>Halo, saya Faiz</h2>
            <p>Mahasiswa Informatika yang tertarik dengan Web Development.</p>
        </section>
    </main>

    <footer>
        &copy; 2026 Faiz
    </footer>
</body>
</html>"""
    generate_shot(
        code_index_before, HtmlDjangoLexer(), "index.html", "index", 
        None, None, None, None, 
        "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-02-index-before.png",
        highlights=[
            (1, 20, "1. HAPUS BAGIAN ATAS: HEAD & NAVBAR (Baris 1-20)", "del"),
            (28, 32, "2. HAPUS BAGIAN BAWAH: FOOTER & PENUTUP (Baris 28-32)", "del")
        ]
    )

    # 3. INDEX.HTML AFTER (Langkah 2: Bagian yang DITEMPEL - ATAS & BAWAH)
    code_index_after = """{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<section class="hero">
    <div class="hero-image">
        <img src="{{ url_for('static', filename='images/ultramen.jpg') }}" alt="Faiz">
    </div>
    <div class="hero-text">
        <p class="tagline">Mahasiswa Informatika</p>
        <h2>Halo, saya <span class="highlight">{{ profil.nama }}</span>.<br>
            <span class="typewriter">Saya bikin web.</span></h2>
        <p>Saya tertarik dengan pengembangan web, basis data, dan jaringan komputer.</p>
    </div>
</section>

<section class="section">
    <h3 class="section-title">Mata Kuliah</h3>
    <div class="card-grid stagger">
        <div class="card-3d">
            <h4><span>01</span> Pemrograman Web</h4>
            <p>Belajar membangun web modern.</p>
        </div>
        <div class="card-3d">
            <h4><span>02</span> Basis Data</h4>
            <p>Perancangan dan optimasi SQL.</p>
        </div>
    </div>
</section>
{% endblock %}"""
    generate_shot(
        code_index_after, HtmlDjangoLexer(), "index.html", "index", 
        None, None, None, None,
        "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-02-index-after.png",
        highlights=[
            (1, 5, "1. TEMPEL DI BARIS 1: {% extends %} & {% block content %}", "add"),
            (31, 31, "2. TEMPEL DI PALING BAWAH: {% endblock %}", "add")
        ]
    )

    # 3b. INDEX.HTML FULL (Langkah 2: Tampilan Lengkap)
    code_index_full = """{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<section class="hero">
    <div class="hero-image">
        <img src="{{ url_for('static', filename='images/ultramen.jpg') }}" alt="Faiz">
    </div>
    <div class="hero-text">
        <p class="tagline">Mahasiswa Informatika</p>
        <h2>Halo, saya <span class="highlight">{{ profil.nama }}</span>.<br>
            <span class="typewriter">Saya bikin web.</span></h2>
        <p>Saya tertarik dengan pengembangan web, basis data, dan jaringan komputer.</p>
    </div>
</section>

<section class="section">
    <h3 class="section-title">Mata Kuliah</h3>
    <div class="card-grid stagger">
        <div class="card-3d">
            <h4><span>01</span> Pemrograman Web</h4>
            <p>Belajar membangun web modern.</p>
        </div>
        <div class="card-3d">
            <h4><span>02</span> Basis Data</h4>
            <p>Perancangan dan optimasi SQL.</p>
        </div>
    </div>
</section>

<section class="section stagger">
    <h3 class="section-title">Statistik Cepat</h3>
    <div class="stats-grid">...</div>
</section>
{% endblock %}"""
    generate_shot(code_index_full, HtmlDjangoLexer(), "index.html", "index", 1, 5, "STRUKTUR UTUH INDEX.HTML", "notice", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-02-index-full.png", start_line_no=1)

    # 4. APP.PY (Langkah 5: Tambahkan Data di app.py)
    code_app_py = """from flask import Flask, render_template

app = Flask(__name__)

profil = {
    "nama": "Faiz",
    "umur": 20,
    "kota": "Malang",
    "kampus": "Universitas Brawijaya",
    "semester": 3
}

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
    app.run(debug=True)"""
    generate_shot(code_app_py, PythonLexer(), "app.py", "app", 5, 19, "TAMBAHKAN DATA DI BARIS 5 (profil & skills)", "add", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-05-app-py.png", start_line_no=1)

    code_app_py_routes = """@app.route("/")
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
    app.run(debug=True)"""
    generate_shot(code_app_py_routes, PythonLexer(), "app.py", "app", 21, 33, "PASSING DATA KE TEMPLATE (profil & skills)", "add", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-05-app-py-routes.png", start_line_no=21)

    # 5. SKILLS.HTML LOOP (Langkah 7: Looping Data & If Badge)
    code_skills = """{% extends 'base.html' %}

{% block title %}Skills{% endblock %}

{% block content %}
<section class="section">
    <h3 class="section-title">Keahlian</h3>
    {% for skill in skills %}
    <div class="skill">
        <div class="skill-name">
            <span>{{ skill.nama }}</span>
            <span class="skill-meta">
                {% if skill.level >= 80 %}
                <span class="badge badge-mahir">Mahir</span>
                {% elif skill.level >= 60 %}
                <span class="badge badge-menengah">Menengah</span>
                {% else %}
                <span class="badge badge-dasar">Dasar</span>
                {% endif %}
                <span class="level">{{ skill.level }}%</span>
            </span>
        </div>
        <div class="bar" style="--fill:{{ skill.level }}%"></div>
    </div>
    {% endfor %}
</section>
{% endblock %}"""
    generate_shot(code_skills, HtmlDjangoLexer(), "skills.html", "skills", 8, 25, "GANTIKAN DENGAN LOOP {% for %} & IF BADGE", "add", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-07-skills-loop.png", start_line_no=1)

    # 6. INDEX.HTML VARIABEL (Langkah 6: Ganti teks statis dengan variabel Jinja2)
    code_index_var = """<section class="hero">
    <div class="hero-image">
        <img src="{{ url_for('static', filename='images/ultramen.jpg') }}" alt="Faiz">
    </div>
    <div class="hero-text">
        <p class="tagline">Mahasiswa Informatika</p>
        <h2>Halo, saya <span class="highlight">{{ profil.nama }}</span>.<br>
            <span class="typewriter">Saya bikin web.</span></h2>
        <p>Saya tertarik dengan pengembangan web, basis data, dan jaringan komputer.</p>
    </div>
</section>

<section class="section">
    <h3 class="section-title">Mata Kuliah</h3>
    <div class="card-grid stagger">
        <div class="card-3d">
            <h4><span>01</span> Pemrograman Web</h4>
            <p>Belajar membangun web modern.</p>
        </div>
        <div class="card-3d">
            <h4><span>02</span> Basis Data</h4>
            <p>Perancangan dan optimasi SQL.</p>
        </div>
    </div>
</section>"""
    generate_shot(code_index_var, HtmlDjangoLexer(), "index.html", "index", 6, 8, "GANTI TEKS STATIS DENGAN {{ profil.nama }}", "add", "/home/faiz/asdos/pemweb/web-perkuliahan/P04/img/vscode-step-06-var-display.png", start_line_no=1)

    print("All freshmen screenshots successfully created!")

if __name__ == "__main__":
    run_all()
