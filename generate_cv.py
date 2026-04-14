#!/usr/bin/env python3
"""
generate_cv.py — generates cv.tex from _data/profile.yml
Usage:  python generate_cv.py
"""
import sys, re
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML not installed. Run: pip install pyyaml")

BASE    = Path(__file__).parent
IN      = BASE / "_data" / "profile.yml"
TEX_IN  = BASE / "cv.tex.in"
TEX_OUT = BASE / "cv.tex"

# ── Helpers ─────────────────────────────────────────────
def tex_esc(s: str) -> str:
    s = str(s)
    s = s.replace('\\', r'\textbackslash{}')
    for ch in '&%$#_{}':
        s = s.replace(ch, r'\\' + ch)
    s = s.replace('~', r'\textasciitilde{}')
    s = s.replace('^', r'\textasciicircum{}')
    return s

def strip_html(s: str) -> str:
    return re.sub(r'<[^>]+>', '', s)

def flat(items, sep=" ") -> str:
    return sep.join(strip_html(i) for i in items if i)

# ── Build content sections ───────────────────────────────

def make_header(p: dict) -> str:
    name   = tex_esc(p['name'])
    title  = tex_esc(p.get('title', ''))
    email  = tex_esc(p.get('contact', {}).get('email', ''))
    gh_url = tex_esc(p.get('contact', {}).get('github', ''))
    loc    = tex_esc(p.get('location', ''))
    tags_s = "  ".join(r"\cvtag{" + tex_esc(t) + "}" for t in p.get('hero_tags', []))

    # email: pass full mailto: URL so \href works directly
    email_cmd = (r"\emailentry{mailto:" + email + "}") if email else ""
    gh_cmd    = (r"\ghentry{" + gh_url + "}")        if gh_url  else ""
    loc_cmd   = (r"\locentry{" + loc   + "}")        if loc     else ""
    tags_cmd  = (r"\tagsentry{" + tags_s + "}")       if tags_s  else ""

    return "\n".join(filter(None, [
        r"\nameentry{" + name + "}",
        r"\titleentry{" + title + "}",
        email_cmd,
        gh_cmd,
        loc_cmd,
        tags_cmd,
    ]))

def make_about(p: dict) -> str:
    parts = []
    for b in p.get('about', {}).get('background', []):
        parts.append(strip_html(b))
    for b in p.get('about', {}).get('extra', []):
        parts.append(strip_html(b))
    return tex_esc(" ".join(parts))

def make_education(p: dict) -> str:
    items = []
    for edu in p.get('about', {}).get('education', []):
        deg    = tex_esc(edu.get('degree', ''))
        school = tex_esc(edu.get('school', ''))
        grad   = tex_esc(edu.get('graduation', ''))
        meta   = f"{school}  |  Expected {grad}" if grad else school
        det    = [tex_esc(strip_html(d)) for d in edu.get('details', [])]
        det_s  = "  \\\\  ".join(det) if det else ""
        items.append(rf"\cvitem{{{deg}}}{{{meta}}}{{{det_s}}}")
    return "\n".join(items)

def make_skills(p: dict) -> str:
    groups = []
    for grp in p.get('skills', []):
        cat   = tex_esc(grp.get('category', ''))
        items = [tex_esc(i) for i in grp.get('items', [])]
        items_s = '  \\quad  '.join(items)
        groups.append(f"    \\skillgroup{{{cat}}}{{{items_s}}}")
    return "\n".join(groups)

def make_projects(p: dict) -> str:
    blocks = []
    for proj in p.get('projects', []):
        title  = tex_esc(proj.get('title', ''))
        period = tex_esc(proj.get('period', ''))
        tag    = tex_esc(proj.get('tag', ''))
        meta   = f"{period}  |  {tag}" if tag else period
        desc   = tex_esc(strip_html(proj.get('description', '')))
        gh     = tex_esc(proj.get('github', ''))

        detail_lines = []
        for d in proj.get('details', []):
            key = tex_esc(d.get('key', ''))
            val = tex_esc(strip_html(d.get('val', '')))
            detail_lines.append(f"\\cveventbullet{{{key}}}{{{val}}}")
        detail_s = "  \\\\      ".join(detail_lines)

        blocks.append(
            f"  \\cvproject{{{title}}}{{{meta}}}{{{desc}}}{{{detail_s}}}{{{gh}}}"
        )
    return "\n".join(blocks)

# ── Main ────────────────────────────────────────────────
def main():
    if not IN.exists():
        sys.exit(f"ERROR: {IN} not found")
    if not TEX_IN.exists():
        sys.exit(f"ERROR: {TEX_IN} not found")

    with open(IN, encoding='utf-8') as f:
        p = yaml.safe_load(f)

    with open(TEX_IN, encoding='utf-8') as f:
        template = f.read()

    substitutions = {
        "!!HEADER!!":    make_header(p),
        "!!ABOUT!!":     make_about(p),
        "!!EDUCATION!!": make_education(p),
        "!!SKILLS!!":    make_skills(p),
        "!!PROJECTS!!":  make_projects(p),
        "!!FOOTER!!":    tex_esc(
            p.get('contact', {}).get('github', '').replace('https://', '')
        ),
    }

    for key, val in substitutions.items():
        template = template.replace(key, val)

    TEX_OUT.write_text(template, encoding='utf-8')
    print(f"Generated: {TEX_OUT}")

if __name__ == '__main__':
    main()
