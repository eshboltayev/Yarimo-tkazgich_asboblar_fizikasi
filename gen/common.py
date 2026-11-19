"""Umumiy shablonlar: sarlavha, navigatsiya, footer, bo'limlar."""
import html as _h

SITE = "Yarimo‘tkazgich asboblar fizikasi"
AUTHOR = "I.M. Eshboltayev"
AUTHOR_FULL = "Eshboltayev Iqbol Mamirjonovich"

NAV = [
    ("annotatsiya.html", "Darslik haqida"),
    ("index.html#maruzalar", "Ma’ruzalar"),
    ("index.html#amaliy", "Amaliy mashg‘ulotlar"),
    ("mustaqil.html", "Mustaqil ta’lim"),
    ("index.html#simulyatorlar", "Simulyatorlar"),
    ("baholash.html", "Baholash"),
    ("oqituvchi.html", "O‘qituvchi uchun"),
    ("glossariy.html", "Lug‘at"),
    ("vositalar.html", "Vositalar"),
    ("index.html#muallif", "Muallif"),
]

# Fan dasturidagi adabiyotlar (raqamlar dasturdagi [1..5] havolalarga mos)
BASE_LIT = {
    1: "Rasulov R., Rasulov V. Qattiq jismlar nazariyasi. — Farg‘ona: Classik, 2020.",
    2: "Eshboltayev I. Uch va ikki o‘lchamli yarimo‘tkazgichlarda ko‘p fotonli optik va fotog… — 2019. (to‘liq nomi fan dasturida qisqartirilgan)",
    3: "Mamadaliyeva N. O‘rkachsimon zonali yarimo‘tkazgichlarda o‘lchamli kvantlashish. — 2019.",
    4: "Gataullin Sh. O‘rta maktab fizika kursida yarimo‘tkazgichlarni o‘rganish. — 1989.",
    5: "Zaynobiddinov S., Teshaboyev A.T. Yarimo‘tkazgichlar fizikasi. — T.: O‘qituvchi, 1999. (dasturdagi 5-asosiy manba 3-manba bilan takrorlangani uchun qo‘shimcha ro‘yxatdan olindi)",
}
INTL = {
    "sze": "Sze S.M., Ng K.K. Physics of Semiconductor Devices. 3rd ed. — Hoboken: Wiley, 2007.",
    "neamen": "Neamen D.A. Semiconductor Physics and Devices: Basic Principles. 4th ed. — New York: McGraw-Hill, 2012.",
    "streetman": "Streetman B.G., Banerjee S.K. Solid State Electronic Devices. 7th ed. — Pearson, 2015.",
    "pierret": "Pierret R.F. Semiconductor Device Fundamentals. — Reading: Addison-Wesley, 1996.",
    "hu": "Hu C. Modern Semiconductor Devices for Integrated Circuits. — Pearson, 2010.",
    "grove": "Grove A.S. Physics and Technology of Semiconductor Devices. — New York: Wiley, 1967.",
    "rhoderick": "Rhoderick E.H., Williams R.H. Metal–Semiconductor Contacts. 2nd ed. — Oxford: Clarendon Press, 1988.",
    "nicollian": "Nicollian E.H., Brews J.R. MOS (Metal Oxide Semiconductor) Physics and Technology. — New York: Wiley, 1982.",
    "schroder": "Schroder D.K. Semiconductor Material and Device Characterization. 3rd ed. — Wiley-IEEE Press, 2006.",
    "baliga": "Baliga B.J. Fundamentals of Power Semiconductor Devices. — New York: Springer, 2008.",
    "green": "Green M.A. Solar Cells: Operating Principles, Technology and System Applications. — Prentice-Hall, 1982.",
    "coldren": "Coldren L.A., Corzine S.W., Mašanović M.L. Diode Lasers and Photonic Integrated Circuits. 2nd ed. — Wiley, 2012.",
    "schubert": "Schubert E.F. Light-Emitting Diodes. 2nd ed. — Cambridge University Press, 2006.",
    "janesick": "Janesick J.R. Scientific Charge-Coupled Devices. — Bellingham: SPIE Press, 2001.",
    "rabaey": "Rabaey J.M., Chandrakasan A., Nikolić B. Digital Integrated Circuits: A Design Perspective. 2nd ed. — Prentice Hall, 2003.",
    "holmes": "Holmes-Siedle A., Adams L. Handbook of Radiation Effects. 2nd ed. — Oxford University Press, 2002.",
    "sedra": "Sedra A.S., Smith K.C. Microelectronic Circuits. 7th ed. — Oxford University Press, 2015.",
    "tsividis": "Tsividis Y., McAndrew C. Operation and Modeling of the MOS Transistor. 3rd ed. — Oxford University Press, 2011.",
}

esc = _h.escape


def head(title, desc, katex=True, extra_css=True):
    k = ""
    if katex:
        k = ('<link rel="stylesheet" href="vendor/katex/katex.min.css">\n'
             '<script defer src="vendor/katex/katex.min.js"></script>\n'
             '<script defer src="vendor/katex/contrib/auto-render.min.js"></script>\n')
    return f"""<!doctype html>
<html lang="uz">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — {SITE}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{AUTHOR_FULL}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/styles.css">
{'<link rel="stylesheet" href="css/darslik.css">' if extra_css else ''}
{k}</head>
<body>
<a class="skip-link" href="#main">Asosiy mazmunga o‘tish</a>
"""


def header(active=""):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="site-header"><div class="container navbar"><a class="brand" href="index.html"><span class="brand-mark"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4"/></svg></span><span>YARIMO‘TKAZGICH ASBOBLAR FIZIKASI<small>Interaktiv elektron darslik · Magistratura</small></span></a><nav class="nav-links" aria-label="Asosiy navigatsiya">{links}</nav><button class="menu-toggle" type="button" aria-label="Menyuni ochish" aria-expanded="false">☰</button></div></header>
"""


def footer(sims=False):
    return f"""<footer class="footer"><div class="container">{SITE} — ochiq elektron darslik · Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · 2026 · Muallif: <a href="index.html#muallif">{AUTHOR}</a> · Litsenziya: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.uz" rel="license">CC BY-SA 4.0</a><br>Rasmiy topshiriqlar va baholash faqat HEMIS axborot tizimida yuritiladi.</div></footer>
{'<script src="js/sims.js" defer></script>' if sims else ''}
<script src="js/app.js" defer></script>
</body></html>
"""


def hero(crumbs, badge, title, lead="", chips=()):
    cr = " / ".join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for h, t in crumbs)
    ch = "".join(f'<span class="chip {cls}">{t}</span>' for cls, t in chips)
    return f"""<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Yo‘l">{cr}</nav><div class="eyebrow" style="margin-top:1rem">{badge}</div><h1>{title}</h1>{f'<p class="lead">{lead}</p>' if lead else ''}<div class="chips">{ch}</div></div></section>
"""


def sec(sid, num, title, body):
    n = f'<span class="num">{num}</span>' if num else ""
    return f'<section class="doc-sec" id="{sid}"><h2>{n}{title}</h2>{body}</section>\n'


def doc(toc, sections, pager=""):
    t = "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in toc)
    return f"""<div class="container doc-layout"><aside class="toc" aria-label="Sahifa mundarijasi"><h2>Mundarija</h2><ol>{t}</ol></aside><div class="doc">{''.join(sections)}{pager}</div></div>
"""


def quiz(items, qid):
    out = []
    for i, (qs, opts, a, ex) in enumerate(items):
        o = "".join(f'<label><input type="radio" name="{qid}-{i}" value="{j}"> <span>{"ABCD"[j]}) {t}</span></label>' for j, t in enumerate(opts))
        out.append(f'<div class="q" data-a="{a}"><p>{i+1}. {qs}</p>{o}<div class="fb">To‘g‘ri javob: <b>{"ABCD"[a]}</b>. {ex}</div></div>')
    return f'<div class="quiz">{"".join(out)}<div class="actions"><button class="primary" type="button" data-check>Tekshirish</button><button class="secondary" type="button" data-reset-quiz>Qayta boshlash</button></div><div class="quiz-result" aria-live="polite"></div></div>'


def prompt(pid, text):
    return f'<div class="prompt-box"><button class="secondary copy" type="button" data-copy="{pid}">Nusxalash</button><pre id="{pid}">{esc(text)}</pre></div>'


def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


def table(head_, rows):
    h = "".join(f"<th>{c}</th>" for c in head_)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def card_link(href, badge, title, text):
    return f'<a class="card" href="{href}"><span class="badge">{badge}</span><h3>{title}</h3><p class="muted">{text}</p></a>'
