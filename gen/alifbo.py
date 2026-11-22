"""O'zbek lotin alifbosini yangi shaklga o'tkazish (O'RQ-1184, 2026): O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç.
Faqat o'zbekcha matnga qo'llanadi: kod, formula, havola va lang="en|ru" bloklari chetlab o'tiladi."""
import re

APOS = "‘ʻ'`’"  # o‘ / g‘ dagi belgilar (’ faqat o/g dan keyin bo'lsa)
EXCEPT = {"push", "pull", "touch", "match", "batch", "watch", "fresh", "english", "chip", "cmos", "avalanche", "datasheet", "datasheets", "latch", "matching", "punch", "trench", "manchester", "vishay",
          "flash", "smash", "cache", "chrome", "chat", "chatgpt", "shift", "fisher", "schottky", "shockley",
          "esc", "mosfet", "nanohub", "mashanović", "bench", "search", "switch", "patch", "branch", "each",
          "hash", "bash", "shell", "check", "chart", "child", "tech", "much", "such", "which", "machine", "shared"}

_o = re.compile(r"([oOgG])[‘ʻ'`’]")
_word = re.compile(r"[A-Za-zÀ-ž‘ʻ’'`]+")


def _conv_word(w):
    if w.split("’")[0].lower().strip("‘ʻ'`") in EXCEPT:
        return w
    w = _o.sub(lambda m: {"o": "ö", "O": "Ö", "g": "ğ", "G": "Ğ"}[m.group(1)], w)
    w = w.replace("SH", "Ş").replace("Sh", "Ş").replace("sh", "ş").replace("sH", "ş")
    w = w.replace("CH", "Ç").replace("Ch", "Ç").replace("ch", "ç").replace("cH", "ç")
    return w


def to_new(text):
    return _word.sub(lambda m: _conv_word(m.group(0)), text)


def _conv_text_keep_math(t):
    out, pos = [], 0
    for m in re.finditer(r"\\\(.*?\\\)|\$\$.*?\$\$", t, flags=re.S):
        out.append(to_new(t[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(to_new(t[pos:]))
    return "".join(out)


SKIP_TAGS = {"pre", "code", "script", "style", "svg", "math"}
VOID = {"br", "img", "input", "meta", "link", "hr", "source", "wbr", "path", "rect", "stop", "circle", "line", "polyline"}
CONV_ATTRS = ("title", "aria-label", "placeholder", "alt", "content")


def _conv_attrs(tag):
    def rep(m):
        name, q, val = m.group(1), m.group(2), m.group(3)
        if name.lower() in CONV_ATTRS and "http" not in val:
            val = _conv_text_keep_math(val)
        return f'{name}={q}{val}{q}'
    return re.sub(r'([a-zA-Z-]+)=(["\'])(.*?)\2', rep, tag)


def html_to_new(html):
    parts = re.split(r"(<!--.*?-->|<[^>]+>)", html, flags=re.S)
    stack = []  # (tag, skip)
    out = []
    for p in parts:
        if not p:
            continue
        if p.startswith("<!--"):
            out.append(p); continue
        if p.startswith("<"):
            m = re.match(r"<\s*(/)?\s*([a-zA-Z0-9]+)", p)
            if not m:
                out.append(p); continue
            closing, tag = m.group(1), m.group(2).lower()
            skipping = any(s for _, s in stack)
            if closing:
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i][0] == tag:
                        del stack[i:]; break
                out.append(p); continue
            sk = tag in SKIP_TAGS or bool(re.search(r'\blang="(en|ru)', p)) or bool(re.search(r'class="[^"]*\b(no-alif|code)\b', p))
            if tag == "pre" and 'class="code"' not in p:
                sk = False  # promptlar (o'zbekcha) konvertatsiya qilinadi
            if not p.endswith("/>") and tag not in VOID and tag != "!doctype":
                stack.append((tag, sk))
            out.append(p if (skipping or sk) else _conv_attrs(p))
            continue
        out.append(p if any(s for _, s in stack) else _conv_text_keep_math(p))
    return "".join(out)


JS_SKIP = {"change", "input", "click", "resize", "load", "DOMContentLoaded", "touch", "keydown", "voiceschanged", "visibilitychange"}


def js_to_new(src):
    """Faqat o'zbekcha matnli satr literallarini o'zgartiradi."""
    def rep(m):
        q, body = m.group(1), m.group(2)
        if body in JS_SKIP or not re.search(r"[‘ʻ]|sh|ch|Sh|Ch|SH|CH", body):
            return m.group(0)
        return q + to_new(body) + q
    return re.sub(r"(['`])((?:\\.|(?!\1).)*?)\1", rep, src, flags=re.S)
