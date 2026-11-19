/* Yarimo'tkazgich asboblar fizikasi — umumiy sahifa skripti */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Menyu (mobil)
  const btn = $('.menu-toggle'), nav = $('.nav-links');
  btn?.addEventListener('click', () => { const o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', String(o)); btn.textContent = o ? '✕' : '☰'; });
  $$('.nav-links a').forEach(a => a.addEventListener('click', () => { nav?.classList.remove('open'); if (btn) { btn.textContent = '☰'; btn.setAttribute('aria-expanded', 'false'); } }));

  // Formulalar (KaTeX)
  const renderMath = () => { if (window.renderMathInElement) renderMathInElement(document.body, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '\\(', right: '\\)', display: false }], throwOnError: false }); };
  if (window.renderMathInElement) renderMath(); else window.addEventListener('load', renderMath);

  // Mundarija: joriy bo'limni belgilash
  const links = $$('.toc a');
  if (links.length && 'IntersectionObserver' in window) {
    const map = new Map(links.map(a => [a.getAttribute('href').slice(1), a]));
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { links.forEach(l => l.classList.remove('on')); map.get(e.target.id)?.classList.add('on'); } }), { rootMargin: '-30% 0px -60% 0px' });
    map.forEach((_, id) => { const el = document.getElementById(id); if (el) io.observe(el); });
  }

  // Nusxa olish
  $$('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const src = document.getElementById(b.dataset.copy); const t = src?.innerText || '';
    try { await navigator.clipboard.writeText(t); b.textContent = 'Nusxalandi ✓'; } catch { b.textContent = 'Qo‘lda belgilang'; }
    setTimeout(() => { b.textContent = 'Nusxalash'; }, 1800);
  }));

  // Testlar
  $$('.quiz').forEach(qz => {
    $('[data-check]', qz)?.addEventListener('click', () => {
      const qs = $$('.q', qz); let ok = 0, ans = 0;
      qs.forEach(q => { q.classList.remove('right', 'wrong'); const sel = $('input:checked', q); if (!sel) return; ans++; const r = sel.value === q.dataset.a; if (r) ok++; q.classList.add(r ? 'right' : 'wrong'); });
      const out = $('.quiz-result', qz);
      out.textContent = ans < qs.length ? `Javob berilgan: ${ans}/${qs.length}. Natija: ${ok} ta to‘g‘ri.` : `Natija: ${ok}/${qs.length} (${Math.round(ok / qs.length * 100)}%)`;
    });
    $('[data-reset-quiz]', qz)?.addEventListener('click', () => { $$('.q', qz).forEach(q => q.classList.remove('right', 'wrong')); $$('input', qz).forEach(i => { i.checked = false; }); $('.quiz-result', qz).textContent = ''; });
  });

  // Qidiruv filtri
  $$('input[data-filter]').forEach(inp => inp.addEventListener('input', () => {
    const v = inp.value.trim().toLowerCase(); let n = 0;
    $$(inp.dataset.filter).forEach(el => { const hit = !v || el.textContent.toLowerCase().includes(v); el.hidden = !hit; if (hit) n++; });
    const c = document.getElementById(inp.dataset.count || ''); if (c) c.textContent = `${n} ta natija`;
  }));

  // Baho kalkulyatori (baholash.html)
  const calc = $('#grade-calc');
  if (calc) {
    const upd = () => {
      const v = k => Number($(`#${k}`, calc).value);
      const jn = v('jn-mt1') + v('jn-df') + v('jn-mt2'), on = v('on'), yn = v('yn');
      $$('output[data-for]', calc).forEach(o => { o.textContent = $(`#${o.dataset.for}`, calc).value; });
      const total = jn + on + yn, pass = jn >= 18 && on >= 12 && yn >= 30;
      const grade = !pass ? 'Qoniqarsiz (saralash bali yetmagan)' : total >= 90 ? 'A’lo (5)' : total >= 70 ? 'Yaxshi (4)' : total >= 60 ? 'Qoniqarli (3)' : 'Qoniqarsiz (2)';
      $('#calc-total').textContent = `${total.toFixed(1)} / 100`;
      $('#calc-grade').textContent = grade;
      $('#calc-detail').textContent = `JN = ${jn} / 30 (saralash 18) · ON = ${on} / 20 (saralash 12) · YaN = ${yn} / 50 (saralash 30)`;
    };
    calc.addEventListener('input', upd); upd();
  }

  // AI prompt generatori (bosh sahifa)
  const gen = $('#gen-prompt');
  gen?.addEventListener('click', () => {
    const topic = $('#p-topic').value, lvl = $('#p-level').value, role = $('#p-role').value;
    const txt = role === 'o‘qituvchi'
      ? `Sen magistratura bosqichida "Yarimo‘tkazgich asboblar fizikasi" fanidan dars beruvchi tajribali professor-metodistsan.\nMavzu: ${topic}.\nTalabalar darajasi: ${lvl}.\nVazifa:\n1) 2 akademik soatlik dars rejasi (Hook → Nazariya → Misconception → Simulyatsiya → Blits-so‘rov).\n2) 5 ta blits-savol va 3 ta hisoblash masalasi (javoblari va SI birliklari bilan).\n3) Talabalar ko‘p yo‘l qo‘yadigan 3 ta xato tushuncha va ularni tuzatish usuli.\n4) SPICE (ngspice) yoki Python bilan 15 daqiqalik modellashtirish topshirig‘i.\nCheklovlar: formulalarni LaTeX’da yoz; har bir son qiymatni manba yoki hisob bilan asosla; ishonching komil bo‘lmagan joyni ochiq ayt.`
      : `Sen yarimo‘tkazgich asboblari fizikasi bo‘yicha sokratik repetitorsan.\nMavzu: ${topic}. Mening darajam: ${lvl}.\nQoidalar:\n- Javobni darhol berma; avval 2–3 ta yo‘naltiruvchi savol ber.\n- Har bir formulada kattaliklar va SI birliklarini ko‘rsat.\n- Men yozgan hisobni o‘lchamlilik (dimensional analysis) va limit holatlar bo‘yicha tekshir.\n- Oxirida mavzu bo‘yicha 3 ta o‘z-o‘zini tekshirish savolini ber.\nMuhim: men baholanadigan topshiriqni sen bilan yozmayman — faqat tushunishim uchun foydalanaman.`;
    $('#p-out').textContent = txt;
  });
})();
