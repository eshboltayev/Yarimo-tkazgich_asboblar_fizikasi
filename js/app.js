/* Yarimo'tkazgich asboblar fizikasi — umumiy sahifa skripti (2-versiya)
   Kun/tun rejimi, UZ/RU/EN (Google Translate), ovozli o'qish va modellarning ovozli namoyishi.
   Ovoz brauzerning o'zidagi Web Speech API orqali ishlaydi: API kalit va server talab qilinmaydi. */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const AL = window.YAF_ALIF || { A: s => s, toOld: s => s, toNew: s => s };
  const A = AL.A;
  const html = document.documentElement;
  const LANG = html.dataset.tl || 'uz';

  /* ---------- Menyu (mobil) ---------- */
  const btn = $('.menu-toggle'), nav = $('.nav-links');
  btn?.addEventListener('click', () => { const o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', String(o)); btn.textContent = o ? '✕' : '☰'; });
  $$('.nav-links a').forEach(a => a.addEventListener('click', () => { nav?.classList.remove('open'); if (btn) { btn.textContent = '☰'; btn.setAttribute('aria-expanded', 'false'); } }));

  /* ---------- Kun / tun rejimi ---------- */
  $$('.theme-btn').forEach(b => b.addEventListener('click', () => {
    const t = html.dataset.theme === 'light' ? 'dark' : 'light';
    html.dataset.theme = t; try { localStorage.setItem('yaf-theme', t); } catch (e) { /* xotira yopiq */ }
    window.dispatchEvent(new Event('resize'));
  }));

  /* ---------- Til: UZ / RU / EN ---------- */
  const setCookie = v => {
    const exp = v ? '' : '; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    const val = v ? `/uz/${v}` : '';
    document.cookie = `googtrans=${val}; path=/${exp}`;
    document.cookie = `googtrans=${val}; path=/; domain=${location.hostname}${exp}`;
  };
  $$('.lang-switch button').forEach(b => {
    b.setAttribute('aria-pressed', String(b.dataset.lang === LANG));
    b.addEventListener('click', () => { const l = b.dataset.lang; if (l === LANG) return; setCookie(l === 'uz' ? '' : l); location.reload(); });
  });

  function revertAlphabet() {
    const skip = el => el.closest('script,style,.katex,pre.code,code,.notranslate');
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const nodes = []; while (w.nextNode()) nodes.push(w.currentNode);
    nodes.forEach(n => { if (n.parentElement && !skip(n.parentElement)) n.nodeValue = AL.toOld(n.nodeValue); });
    $$('[title],[placeholder],[aria-label]').forEach(el => ['title', 'placeholder', 'aria-label'].forEach(a => { if (el.hasAttribute(a)) el.setAttribute(a, AL.toOld(el.getAttribute(a))); }));
    document.title = AL.toOld(document.title);
  }

  function startTranslate() {
    if (LANG === 'uz') return;
    revertAlphabet();
    const holder = document.createElement('div'); holder.id = 'gt-el'; document.body.appendChild(holder);
    window.gtInit = () => { try { new google.translate.TranslateElement({ pageLanguage: 'uz', includedLanguages: 'en,ru', autoDisplay: false }, 'gt-el'); } catch (e) { /* tarmoq yo'q */ } };
    const s = document.createElement('script'); s.src = 'https://translate.google.com/translate_a/element.js?cb=gtInit'; s.async = true;
    s.onerror = () => toast('Tarjima xizmatiga ulanib bo‘lmadi. Internet aloqasini tekshiring.');
    document.body.appendChild(s);
  }

  /* ---------- Formulalar (KaTeX) ---------- */
  const renderMath = () => {
    if (window.renderMathInElement) renderMathInElement(document.body, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '\\(', right: '\\)', display: false }], throwOnError: false });
    $$('.katex').forEach(k => { k.classList.add('notranslate'); k.setAttribute('translate', 'no'); });
    $$('pre.code').forEach(p => { p.classList.add('notranslate'); p.setAttribute('translate', 'no'); });
    startTranslate();
  };
  if (document.readyState === 'complete') renderMath(); else window.addEventListener('load', renderMath);

  /* ---------- Mundarija ---------- */
  const links = $$('.toc a');
  if (links.length && 'IntersectionObserver' in window) {
    const map = new Map(links.map(a => [a.getAttribute('href').slice(1), a]));
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { links.forEach(l => l.classList.remove('on')); map.get(e.target.id)?.classList.add('on'); } }), { rootMargin: '-30% 0px -60% 0px' });
    map.forEach((_, id) => { const el = document.getElementById(id); if (el) io.observe(el); });
  }

  /* ---------- Nusxa olish ---------- */
  $$('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const src = document.getElementById(b.dataset.copy); const t = src?.innerText || '';
    const label = b.textContent;
    try { await navigator.clipboard.writeText(t); b.textContent = A('Nusxalandi ✓'); } catch { b.textContent = A('Qo‘lda belgilang'); }
    setTimeout(() => { b.textContent = label; }, 1800);
  }));

  /* ---------- Testlar ---------- */
  $$('.quiz').forEach(qz => {
    $('[data-check]', qz)?.addEventListener('click', () => {
      const qs = $$('.q', qz); let ok = 0, ans = 0;
      qs.forEach(q => { q.classList.remove('right', 'wrong'); const sel = $('input:checked', q); if (!sel) return; ans++; const r = sel.value === q.dataset.a; if (r) ok++; q.classList.add(r ? 'right' : 'wrong'); });
      const out = $('.quiz-result', qz);
      out.textContent = ans < qs.length ? A(`Javob berilgan: ${ans}/${qs.length}. To‘g‘ri: ${ok} ta.`) : A(`Natija: ${ok}/${qs.length} (${Math.round(ok / qs.length * 100)}%)`);
    });
    $('[data-reset-quiz]', qz)?.addEventListener('click', () => { $$('.q', qz).forEach(q => q.classList.remove('right', 'wrong')); $$('input', qz).forEach(i => { i.checked = false; }); $('.quiz-result', qz).textContent = ''; });
  });

  /* ---------- Qidiruv filtri ---------- */
  $$('input[data-filter]').forEach(inp => inp.addEventListener('input', () => {
    const norm = s => AL.toOld(s).toLowerCase();
    const v = norm(inp.value.trim()); let n = 0;
    $$(inp.dataset.filter).forEach(el => { const hit = !v || norm(el.textContent).includes(v); el.hidden = !hit; if (hit) n++; });
    const c = document.getElementById(inp.dataset.count || ''); if (c) c.textContent = A(`${n} ta natija`);
  }));

  /* ---------- Baho kalkulyatori ---------- */
  const calc = $('#grade-calc');
  if (calc) {
    const upd = () => {
      const v = k => Number($(`#${k}`, calc).value);
      const jn = v('jn-mt1') + v('jn-df') + v('jn-mt2'), on = v('on'), yn = v('yn');
      $$('output[data-for]', calc).forEach(o => { o.textContent = $(`#${o.dataset.for}`, calc).value; });
      const total = jn + on + yn, pass = jn >= 18 && on >= 12 && yn >= 30;
      const grade = !pass ? 'Qoniqarsiz (saralash bali yetmagan)' : total >= 90 ? 'A’lo (5)' : total >= 70 ? 'Yaxshi (4)' : total >= 60 ? 'Qoniqarli (3)' : 'Qoniqarsiz (2)';
      $('#calc-total').textContent = `${total.toFixed(1)} / 100`;
      $('#calc-grade').textContent = A(grade);
      $('#calc-detail').textContent = A(`JN = ${jn} / 30 (saralash 18) · ON = ${on} / 20 (saralash 12) · YaN = ${yn} / 50 (saralash 30)`);
    };
    calc.addEventListener('input', upd); upd();
  }

  /* ---------- Prompt generatori ---------- */
  $('#gen-prompt')?.addEventListener('click', () => {
    const topic = $('#p-topic').value, lvl = $('#p-level').value, role = $('#p-role').value;
    const txt = role === 'teacher'
      ? `Sen magistratura bosqichida "Yarimo‘tkazgich asboblar fizikasi" fanidan dars beruvchi tajribali professor-metodistsan.\nMavzu: ${topic}.\nTalabalar darajasi: ${lvl}.\nVazifa:\n1) 2 akademik soatlik dars rejasi (kirish → nazariya → xato tushunchalar → simulyatsiya → blits-so‘rov).\n2) 5 ta blits-savol va 3 ta hisoblash masalasi (javoblari va SI birliklari bilan).\n3) Talabalar ko‘p yo‘l qo‘yadigan 3 ta xato tushuncha va ularni tuzatish usuli.\n4) SPICE (ngspice) yoki Python bilan 15 daqiqalik modellashtirish topshirig‘i.\nCheklovlar: formulalarni LaTeX’da yoz; har bir son qiymatni manba yoki hisob bilan asosla; ishonching komil bo‘lmagan joyni ochiq ayt.`
      : `Sen yarimo‘tkazgich asboblari fizikasi bo‘yicha sokratik repetitorsan.\nMavzu: ${topic}. Mening darajam: ${lvl}.\nQoidalar:\n- Javobni darhol berma; avval 2–3 ta yo‘naltiruvchi savol ber.\n- Har bir formulada kattaliklar va SI birliklarini ko‘rsat.\n- Men yozgan hisobni o‘lchamlilik va limit holatlar bo‘yicha tekshir.\n- Oxirida mavzu bo‘yicha 3 ta o‘z-o‘zini tekshirish savolini ber.\nMuhim: men baholanadigan topshiriqni sen bilan yozmayman — faqat tushunishim uchun foydalanaman.`;
    $('#p-out').textContent = A(txt);
  });

  /* =================== OVOZ (Web Speech API) =================== */
  const synth = window.speechSynthesis;
  const BCP = { uz: 'uz-UZ', ru: 'ru-RU', en: 'en-US' };
  let warned = false, session = 0;

  function toast(msg, ms = 7000) {
    let t = $('.yaf-toast'); if (!t) { t = document.createElement('div'); t.className = 'yaf-toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg; t.hidden = false; clearTimeout(t._h); t._h = setTimeout(() => { t.hidden = true; }, ms);
  }
  const getVoices = () => new Promise(res => {
    if (!synth) return res([]);
    const v = synth.getVoices(); if (v.length) return res(v);
    const h = () => { synth.removeEventListener('voiceschanged', h); res(synth.getVoices()); };
    synth.addEventListener('voiceschanged', h); setTimeout(() => res(synth.getVoices()), 1500);
  });
  const rank = v => (/Natural|Online|Neural/i.test(v.name) ? 2 : 0) + (/Google|Microsoft/i.test(v.name) ? 1 : 0);
  async function pickVoice(lang) {
    const vs = await getVoices();
    const by = p => vs.filter(v => v.lang.toLowerCase().replace('_', '-').startsWith(p)).sort((a, b) => rank(b) - rank(a))[0];
    let v = by(lang);
    if (v) return { v, mode: 'native' };
    if (lang === 'uz') { v = by('tr'); if (v) return { v, mode: 'tr' }; }
    return { v: null, mode: 'none' };
  }
  function chunks(text) {
    const parts = text.replace(/\s+/g, ' ').match(/[^.!?;:]+[.!?;:]*|[.!?;:]+/g) || [];
    const out = []; let cur = '';
    parts.forEach(p => { if ((cur + p).length > 220 && cur) { out.push(cur.trim()); cur = p; } else cur += p; });
    if (cur.trim()) out.push(cur.trim());
    return out;
  }
  async function speak(text, sid) {
    if (!synth) { toast(A('Bu brauzer ovozli o‘qishni qo‘llab-quvvatlamaydi. Chrome, Edge yoki Safari’dan foydalaning.')); return; }
    const { v, mode } = await pickVoice(LANG);
    if (LANG === 'uz' && mode !== 'native' && !warned) {
      warned = true;
      toast(A(mode === 'tr' ? 'Qurilmada o‘zbekcha ovoz topilmadi — vaqtincha turkcha ovoz ishlatilmoqda. O‘zbekcha tabiiy ovozlar (Madina, Sardor) Microsoft Edge brauzerida mavjud.' : 'Qurilmada o‘zbekcha ovoz topilmadi. Microsoft Edge brauzerida o‘zbekcha tabiiy ovozlar (Madina, Sardor) mavjud; telefonda esa matnni ovozga aylantirish sozlamalarini tekshiring.'), 11000);
    }
    if (!v && !(synth.getVoices() || []).length) { await new Promise(r => setTimeout(r, Math.min(text.length * 60, 12000))); return; }
    const say = LANG === 'uz' && mode === 'native' ? AL.toOld(text) : text;
    for (const c of chunks(say)) {
      if (sid !== session) return;
      await new Promise(res => {
        const u = new SpeechSynthesisUtterance(c);
        u.lang = v ? v.lang : (mode === 'tr' ? 'tr-TR' : BCP[LANG]); if (v) u.voice = v;
        u.rate = LANG === 'uz' ? 0.95 : 1; u.onend = u.onerror = () => res();
        synth.speak(u);
        const guard = setTimeout(res, 30000 + c.length * 120); u.addEventListener('end', () => clearTimeout(guard));
      });
    }
  }
  function stopAll() { session++; synth?.cancel(); $$('.reading').forEach(e => e.classList.remove('reading')); $$('.voice-btn.on').forEach(b => { b.classList.remove('on'); const s = $('span', b); if (s && b.dataset.label) s.textContent = b.dataset.label; }); $$('.sim-box.touring').forEach(b => b.classList.remove('touring')); }

  /* ---- Formulani so'z bilan aytish (TeX → so'zlar) ---- */
  const DICT = {
    uz: { over: 'bo‘lingan', sqrt: 'kvadrat ildiz ostida', pow: 'darajasi', sq: 'kvadrati', cube: 'kubi', eq: 'teng', approx: 'taxminan teng', lt: 'kichik', gt: 'katta', le: 'kichik yoki teng', ge: 'katta yoki teng', plus: 'plyus', minus: 'minus', times: 'ko‘paytirilgan', exp: 'eksponenta', ln: 'natural logarifm', log: 'logarifm', propto: 'proporsional', to: 'intiladi', infty: 'cheksizlik', parallel: 'parallel', pm: 'plyus-minus', partial: 'xususiy hosila', int: 'integral', sum: 'yig‘indi', dots: 'va hokazo', cdots: 'va hokazo' },
    ru: { over: 'делённое на', sqrt: 'корень из', pow: 'в степени', sq: 'в квадрате', cube: 'в кубе', eq: 'равно', approx: 'приблизительно равно', lt: 'меньше', gt: 'больше', le: 'меньше или равно', ge: 'больше или равно', plus: 'плюс', minus: 'минус', times: 'умножить на', exp: 'экспонента', ln: 'натуральный логарифм', log: 'логарифм', propto: 'пропорционально', to: 'стремится к', infty: 'бесконечность', parallel: 'параллельно', pm: 'плюс-минус', partial: 'частная производная', int: 'интеграл', sum: 'сумма', dots: 'и так далее', cdots: 'и так далее' },
    en: { over: 'over', sqrt: 'square root of', pow: 'to the power', sq: 'squared', cube: 'cubed', eq: 'equals', approx: 'approximately equals', lt: 'less than', gt: 'greater than', le: 'less than or equal to', ge: 'greater than or equal to', plus: 'plus', minus: 'minus', times: 'times', exp: 'exponential', ln: 'natural log', log: 'log', propto: 'is proportional to', to: 'tends to', infty: 'infinity', parallel: 'parallel', pm: 'plus or minus', partial: 'partial', int: 'integral', sum: 'sum', dots: 'and so on', cdots: 'and so on' }
  };
  const GREEK = {
    uz: { alpha: 'alfa', beta: 'beta', gamma: 'gamma', delta: 'delta', Delta: 'delta', varepsilon: 'epsilon', epsilon: 'epsilon', eta: 'eta', theta: 'teta', lambda: 'lyambda', mu: 'myu', nu: 'nyu', pi: 'pi', rho: 'ro', sigma: 'sigma', tau: 'tau', varphi: 'fi', phi: 'fi', Phi: 'fi', psi: 'psi', omega: 'omega', Gamma: 'gamma', hbar: 'h chiziqli', chi: 'xi', kappa: 'kappa' },
    ru: { alpha: 'альфа', beta: 'бета', gamma: 'гамма', delta: 'дельта', Delta: 'дельта', varepsilon: 'эпсилон', epsilon: 'эпсилон', eta: 'эта', theta: 'тета', lambda: 'лямбда', mu: 'мю', nu: 'ню', pi: 'пи', rho: 'ро', sigma: 'сигма', tau: 'тау', varphi: 'фи', phi: 'фи', Phi: 'фи', psi: 'пси', omega: 'омега', Gamma: 'гамма', hbar: 'аш с чертой', chi: 'хи', kappa: 'каппа' },
    en: { alpha: 'alpha', beta: 'beta', gamma: 'gamma', delta: 'delta', Delta: 'delta', varepsilon: 'epsilon', epsilon: 'epsilon', eta: 'eta', theta: 'theta', lambda: 'lambda', mu: 'mu', nu: 'nu', pi: 'pi', rho: 'rho', sigma: 'sigma', tau: 'tau', varphi: 'phi', phi: 'phi', Phi: 'phi', psi: 'psi', omega: 'omega', Gamma: 'gamma', hbar: 'h-bar', chi: 'chi', kappa: 'kappa' }
  };
  function tex2words(tex, lang) {
    const W = DICT[lang] || DICT.uz, G = GREEK[lang] || GREEK.uz;
    let i = 0; const s = tex.replace(/\{,\}/g, ',').replace(/\^\*/g, '');
    const group = () => {
      while (s[i] === ' ') i++;
      if (s[i] === '{') { let d = 0, j = i; for (; j < s.length; j++) { if (s[j] === '{') d++; else if (s[j] === '}' && --d === 0) break; } const g = s.slice(i + 1, j); i = j + 1; return g; }
      if (s[i] === '\\') { let j = i + 1; while (/[a-zA-Z]/.test(s[j] || '')) j++; const g = s.slice(i, Math.max(j, i + 2)); i = Math.max(j, i + 2); return g; }
      return s[i++] || '';
    };
    const out = [];
    while (i < s.length) {
      const c = s[i];
      if (c === '\\') {
        let j = i + 1; while (/[a-zA-Z]/.test(s[j] || '')) j++;
        if (j === i + 1) { const ch = s[j]; i = j + 1; if (ch === '{' || ch === '}') continue; continue; }
        const name = s.slice(i + 1, j); i = j;
        if (/^(d|t)?frac$/.test(name)) { const a = tex2words(group(), lang), b = tex2words(group(), lang); out.push(`${a}, ${W.over} ${b},`); }
        else if (name === 'sqrt') out.push(`${W.sqrt} ${tex2words(group(), lang)},`);
        else if (/^(text|mathrm|mathbf|operatorname|textbf)$/.test(name)) out.push(group());
        else if (/^(left|right|big|Big|bigg|Bigg)$/.test(name)) { if (s[i] === '\\') group(); else i++; }
        else if (/^(quad|qquad|displaystyle|limits|nolimits)$/.test(name)) { /* bo'shliq */ }
        else if (name === 'cdot' || name === 'times') out.push(W.times);
        else if (name === 'lt') out.push(W.lt);
        else if (name === 'gt') out.push(W.gt);
        else if (name === 'le' || name === 'leq') out.push(W.le);
        else if (name === 'ge' || name === 'geq') out.push(W.ge);
        else if (name === 'll') out.push(W.lt);
        else if (name === 'gg') out.push(W.gt);
        else if (name === 'sim') out.push(W.approx);
        else if (W[name]) out.push(W[name]);
        else if (G[name]) out.push(G[name]);
        else out.push(name);
        continue;
      }
      if (c === '^') { i++; const g = group(); out.push(g === '2' ? W.sq : g === '3' ? W.cube : `${W.pow} ${tex2words(g, lang)}`); continue; }
      if (c === '_') { i++; out.push(tex2words(group(), lang)); continue; }
      if (c === '{' || c === '}') { i++; continue; }
      if (c === '=') out.push(W.eq); else if (c === '+') out.push(W.plus); else if (c === '-' || c === '−') out.push(W.minus);
      else if (c === '<') out.push(W.lt); else if (c === '>') out.push(W.gt); else if (c === '/') out.push(W.over);
      else if (/[()[\]|&~]/.test(c)) out.push(' ');
      else if (/[A-Za-z0-9]/.test(c)) { let j = i; while (j < s.length && /[A-Za-z0-9.,]/.test(s[j])) j++; out.push(s.slice(i, j)); i = j; continue; }
      else out.push(c);
      i++;
    }
    return out.join(' ').replace(/\s+([,.])/g, '$1').replace(/\s{2,}/g, ' ').replace(/(\d) , (\d)/g, '$1,$2').trim();
  }
  function textOf(el) {
    let t = '';
    el.childNodes.forEach(n => {
      if (n.nodeType === 3) t += n.nodeValue;
      else if (n.nodeType === 1) {
        if (n.classList.contains('katex')) { const a = n.querySelector('annotation'); t += ' ' + (a ? tex2words(a.textContent, LANG) : n.textContent) + ' '; }
        else if (n.classList.contains('num')) t += '';
        else if (!/^(BUTTON|SCRIPT|STYLE|INPUT|SELECT|CANVAS)$/.test(n.tagName)) t += textOf(n) + (/^(P|LI|TD|TH|H2|H3|DIV)$/.test(n.tagName) ? '. ' : '');
      }
    });
    return t.replace(/\s+/g, ' ').trim();
  }

  /* ---- Sahifani o'qish ---- */
  $$('.voice-btn[data-read]').forEach(b => {
    b.dataset.label = $('span', b)?.textContent || '';
    b.addEventListener('click', async () => {
      if (b.classList.contains('on')) { stopAll(); return; }
      stopAll(); const sid = session; b.classList.add('on'); const sp = $('span', b); if (sp) sp.textContent = A('To‘xtatish');
      const secs = (b.dataset.read || '').split(',').map(id => document.getElementById(id)).filter(Boolean);
      const title = $('.page-hero h1'); const blocks = title ? [title] : [];
      secs.forEach(sec => $$('h2, h3, p, li, tr, .katex-display', sec).forEach(el => {
        if (el.closest('.sim-box,.quiz,.prompt-box,.tour-bar,.tour-cap,.vh')) return;
        if (el.matches('.katex-display') && el.closest('p,li')) return;
        if (el.matches('p,li,h3') && el.parentElement.closest('li,td')) return;
        blocks.push(el);
      }));
      for (const el of blocks) {
        if (sid !== session) return;
        const t = textOf(el); if (!t) continue;
        $$('.reading').forEach(e => e.classList.remove('reading'));
        el.classList.add('reading'); el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        await speak(t, sid);
      }
      if (sid === session) stopAll();
    });
  });

  /* ---- Modellarning ovozli avtomatik namoyishi ---- */
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  function animateTo(box, set, ms = 1100) {
    const jobs = Object.entries(set).map(([k, v]) => {
      const el = box.querySelector(`[data-k="${k}"]`); if (!el) return null;
      if (el.tagName === 'SELECT') { el.selectedIndex = +String(v).replace('#', ''); el.dispatchEvent(new Event('change', { bubbles: true })); return null; }
      return { el, from: +el.value, to: +v };
    }).filter(Boolean);
    if (!jobs.length) return Promise.resolve();
    return new Promise(res => {
      const t0 = performance.now();
      const step = now => {
        const p = Math.min(1, (now - t0) / ms), e = p < .5 ? 2 * p * p : 1 - (-2 * p + 2) ** 2 / 2;
        jobs.forEach(j => { j.el.value = j.from + (j.to - j.from) * e; j.el.dispatchEvent(new Event('input', { bubbles: true })); });
        if (p < 1) requestAnimationFrame(step); else res();
      };
      requestAnimationFrame(step);
    });
  }
  $$('[data-tour]').forEach(b => {
    b.dataset.label = $('span', b)?.textContent || '';
    b.addEventListener('click', async () => {
      if (b.classList.contains('on')) { stopAll(); return; }
      stopAll(); const sid = session;
      const wrap = b.closest('.sim-wrap'), box = $('.sim-box', wrap), cap = $('.tour-cap', wrap), list = document.getElementById(b.dataset.tour);
      if (!box || !list) return;
      b.classList.add('on'); box.classList.add('touring'); const sp = $('span', b); if (sp) sp.textContent = A('To‘xtatish');
      box.scrollIntoView({ behavior: 'smooth', block: 'center' }); await sleep(500);
      for (const li of $$('li', list)) {
        if (sid !== session) return;
        let set = {}; try { set = JSON.parse(li.dataset.set || '{}'); } catch (e) { /* noto'g'ri qadam */ }
        await animateTo(box, set);
        const t = textOf(li); cap.textContent = li.textContent.trim();
        const ro = $('.readout', box); ro?.classList.add('reading');
        const t0 = performance.now(); await speak(t, sid);
        const need = t.length * 55 - (performance.now() - t0); if (need > 0 && sid === session && !synth?.speaking) await sleep(Math.min(need, 9000));
        ro?.classList.remove('reading'); await sleep(450);
      }
      if (sid === session) { stopAll(); cap.textContent = A('Namoyish tugadi. Endi parametrlarni o‘zingiz o‘zgartirib ko‘ring — natijalar darhol yangilanadi.'); }
    });
  });
  window.addEventListener('pagehide', () => synth?.cancel());
  if (synth) getVoices();
})();
