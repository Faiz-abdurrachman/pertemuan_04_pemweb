import os, subprocess
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.templates import HtmlDjangoLexer
from pygments.formatters import HtmlFormatter

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    background: #0e1117;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px;
    min-height: 100vh;
}}
.vscode-window {{
    width: 1080px;
    background: #1e1e1e;
    border-radius: 10px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.1);
    overflow: hidden;
    display: flex;
    flex-direction: column;
}}
.titlebar {{
    height: 38px;
    background: #323233;
    display: flex;
    align-items: center;
    padding: 0 16px;
    color: #cccccc;
    font-size: 13px;
    border-bottom: 1px solid #252526;
}}
.window-controls {{
    display: flex;
    gap: 8px;
    margin-right: 20px;
}}
.dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
}}
.dot-red {{ background: #ff5f56; }}
.dot-yellow {{ background: #ffbd2e; }}
.dot-green {{ background: #27c93f; }}
.window-title {{
    flex: 1;
    text-align: center;
    color: #999999;
    font-size: 12px;
}}
.main-body {{
    display: flex;
    height: 640px;
}}
.sidebar {{
    width: 230px;
    background: #252526;
    border-right: 1px solid #191919;
    padding: 12px 0;
    color: #cccccc;
    font-size: 13px;
    user-select: none;
}}
.sidebar-header {{
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 0 16px 8px 16px;
    color: #888888;
}}
.tree-item {{
    padding: 4px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: #cccccc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}
.tree-item.indent {{
    padding-left: 32px;
}}
.tree-item.active {{
    background: #37373d;
    color: #ffffff;
}}
.editor-container {{
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #1e1e1e;
    overflow: hidden;
}}
.tab-bar {{
    height: 36px;
    background: #252526;
    display: flex;
    align-items: flex-end;
    border-bottom: 1px solid #1e1e1e;
}}
.tab {{
    padding: 8px 18px;
    font-size: 13px;
    color: #969696;
    background: #2d2d2d;
    display: flex;
    align-items: center;
    gap: 8px;
    border-right: 1px solid #252526;
}}
.tab.active {{
    background: #1e1e1e;
    color: #ffffff;
    border-top: 2px solid #007acc;
}}
.breadcrumbs {{
    height: 26px;
    background: #1e1e1e;
    display: flex;
    align-items: center;
    padding: 0 16px;
    color: #888888;
    font-size: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}}
.code-area {{
    flex: 1;
    padding: 16px 0;
    font-family: "JetBrains Mono", "Fira Code", "Courier New", monospace;
    font-size: 14px;
    line-height: 1.55;
    overflow: hidden;
    position: relative;
}}
.code-line {{
    display: flex;
    padding: 0 16px;
    position: relative;
}}
.line-num {{
    width: 36px;
    text-align: right;
    padding-right: 16px;
    color: #6e7681;
    user-select: none;
}}
.line-content {{
    flex: 1;
    color: #d4d4d4;
    white-space: pre;
}}

/* Highlight box */
.highlight-box {{
    position: absolute;
    left: 48px;
    right: 16px;
    border: 2px solid #f85149;
    background: rgba(248, 81, 73, 0.08);
    border-radius: 6px;
    box-shadow: 0 0 15px rgba(248, 81, 73, 0.25);
    pointer-events: none;
}}
.highlight-badge {{
    position: absolute;
    right: 10px;
    top: -12px;
    background: #f85149;
    color: #ffffff;
    font-size: 11px;
    font-weight: bold;
    padding: 2px 10px;
    border-radius: 10px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.4);
}}

/* Pygments styles */
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
        <div class="window-title">{filename} - praktikum-p04 - Visual Studio Code</div>
    </div>
    <div class="main-body">
        <div class="sidebar">
            <div class="sidebar-header">Explorer: PRAKTIKUM-P04</div>
            <div class="tree-item">📁 static</div>
            <div class="tree-item indent">📁 css</div>
            <div class="tree-item indent">📁 images</div>
            <div class="tree-item">📁 templates</div>
            <div class="tree-item indent {base_active}">📄 base.html</div>
            <div class="tree-item indent {index_active}">📄 index.html</div>
            <div class="tree-item indent {about_active}">📄 about.html</div>
            <div class="tree-item indent {contact_active}">📄 contact.html</div>
            <div class="tree-item {app_active}">🐍 app.py</div>
        </div>
        <div class="editor-container">
            <div class="tab-bar">
                <div class="tab {index_active}">index.html</div>
                <div class="tab {base_active}">base.html</div>
                <div class="tab {app_active}">app.py</div>
            </div>
            <div class="breadcrumbs">
                praktikum-p04 &gt; {breadcrumb}
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

def make_screenshot(code, lexer, filename, breadcrumb, active_file, hl_start, hl_end, hl_text, out_path):
    formatter = HtmlFormatter(style="monokai", nowrap=True)
    highlighted = highlight(code, lexer, formatter)
    
    # Split lines
    lines = highlighted.strip().split("\n")
    rendered_lines = []
    line_height = 21.7  # approximate line height in px
    padding_top = 16
    
    for i, line in enumerate(lines, start=1):
        rendered_lines.append(f'<div class="code-line"><span class="line-num">{i}</span><span class="line-content">{line}</span></div>')
    
    rendered_lines_html = "\n".join(rendered_lines)
    
    if hl_start and hl_end:
        top_px = padding_top + (hl_start - 1) * line_height - 2
        height_px = (hl_end - hl_start + 1) * line_height + 4
        highlight_box_html = f'''
        <div class="highlight-box" style="top: {top_px}px; height: {height_px}px;">
            <div class="highlight-badge">{hl_text}</div>
        </div>
        '''
    else:
        highlight_box_html = ""
        
    base_active = "active" if active_file == "base" else ""
    index_active = "active" if active_file == "index" else ""
    about_active = "active" if active_file == "about" else ""
    contact_active = "active" if active_file == "contact" else ""
    app_active = "active" if active_file == "app" else ""
    
    html = TEMPLATE.format(
        pygments_css=HtmlFormatter(style="monokai").get_style_defs('.code-content'),
        filename=filename,
        breadcrumb=breadcrumb,
        base_active=base_active,
        index_active=index_active,
        about_active=about_active,
        contact_active=contact_active,
        app_active=app_active,
        highlight_box_html=highlight_box_html,
        rendered_lines=rendered_lines_html
    )
    
    temp_html = f"/tmp/{os.path.basename(out_path)}.html"
    with open(temp_html, "w") as f:
        f.write(html)
        
    subprocess.run([
        'chromium', '--headless', '--disable-gpu',
        '--window-size=1180,780',
        f'--screenshot={out_path}',
        f'file://{temp_html}'
    ], check=True)
    print(f"Generated {out_path}")

print("Helper ready")
