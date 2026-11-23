"""Saytdagi barcha o'zbekcha ovozli matnlarni yig'adi (sahifaning o'z JS mantiqi bilan).

Ishlatish:  python tools/tts_extract.py <sayt_ildizi> <chiqish.json>
Natija: {"texts": {"<xesh>": "<matn>", ...}, "pages": {"lecture1.html": ["<xesh>", ...]}}
Brauzer: playwright chromium (CHROME_PATH muhit o'zgaruvchisi bilan boshqa brauzer berish mumkin).
"""
import functools
import http.server
import json
import os
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


def main(root: str, out: str) -> None:
    root_p = Path(root).resolve()
    pages = sorted(p.name for p in root_p.glob("*.html") if p.name != "404.html")
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=str(root_p))
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as srv:
        port = srv.server_address[1]
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        texts, by_page = {}, {}
        with sync_playwright() as pw:
            kw = {"executable_path": os.environ["CHROME_PATH"]} if os.environ.get("CHROME_PATH") else {}
            browser = pw.chromium.launch(**kw)
            ctx = browser.new_context()
            # tashqi so'rovlar (Google Translate va h.k.) kerak emas
            ctx.route("**/*", lambda r: r.continue_() if r.request.url.startswith(f"http://127.0.0.1:{port}") else r.abort())
            for name in pages:
                pg = ctx.new_page()
                pg.goto(f"http://127.0.0.1:{port}/{name}", wait_until="load")
                pg.wait_for_function("window.YAF_TTS && document.readyState === 'complete'", timeout=20000)
                pg.wait_for_timeout(400)  # KaTeX render
                items = pg.evaluate("window.YAF_TTS.items()")
                pg.close()
                by_page[name] = [it["h"] for it in items]
                for it in items:
                    texts[it["h"]] = it["t"]
                print(f"{name}: {len(items)}")
            browser.close()
        srv.shutdown()
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps({"texts": texts, "pages": by_page}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Jami: {len(texts)} ta noyob matn, {sum(len(t) for t in texts.values())} belgi")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
