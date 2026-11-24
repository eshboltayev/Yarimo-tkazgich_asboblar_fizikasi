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
    if (LANG === 'uz') { const url = await mp3For(uzSpeech(text)); if (sid !== session) return; if (url && (await playMp3(url, sid)) !== 'err') return 'mp3'; }
    if (!synth) { toast(A('Bu brauzer ovozli o‘qishni qo‘llab-quvvatlamaydi. Chrome, Edge yoki Safari’dan foydalaning.')); return; }
    const { v, mode } = await pickVoice(LANG);
    if (LANG === 'uz' && mode !== 'native' && !warned) {
      warned = true;
      toast(A(mode === 'tr' ? 'Qurilmada o‘zbekcha ovoz topilmadi — vaqtincha turkcha ovoz ishlatilmoqda. O‘zbekcha tabiiy ovozlar (Madina, Sardor) Microsoft Edge brauzerida mavjud.' : 'Qurilmada o‘zbekcha ovoz topilmadi. Microsoft Edge brauzerida o‘zbekcha tabiiy ovozlar (Madina, Sardor) mavjud; telefonda esa matnni ovozga aylantirish sozlamalarini tekshiring.'), 11000);
    }
    if (!v && !(synth.getVoices() || []).length) { await new Promise(r => setTimeout(r, Math.min(text.length * 60, 12000))); return; }
    const say = LANG === 'uz' && mode === 'native' ? uzSpeech(text) : text;
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
  function stopAll() { session++; synth?.cancel(); if (typeof audioStop === 'function') audioStop(); if (typeof RD !== 'undefined' && RD.state && RD.state !== 'idle') { RD.state = 'idle'; RD.bi = 0; RD.ci = 0; RD.bar && (RD.bar.hidden = true); document.body.classList.remove('has-player'); } $$('.reading').forEach(e => e.classList.remove('reading')); $$('.voice-btn.on').forEach(b => { b.classList.remove('on'); const s = $('span', b); if (s && b.dataset.label) s.textContent = b.dataset.label; }); $$('.sim-box.touring').forEach(b => b.classList.remove('touring')); }

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
      if (c === '^') {
        i++; const g = group();
        if (g === '2') out.push(W.sq); else if (g === '3') out.push(W.cube);
        else if (lang === 'uz') { const e = tex2words(g, lang); const simple = /^(minus )?[A-Za-z0-9]{1,3}$/.test(e); const b = out.pop() || ''; out.push(`${b} ning ${e}${simple ? '-darajasi' : ' darajasi'},`); }
        else out.push(`${W.pow} ${tex2words(g, lang)}`);
        continue;
      }
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
        else if (n.tagName === 'SUP') t += '^{' + n.textContent + '}';
        else if (n.tagName === 'SUB') t += ' ' + n.textContent + ' ';
        else if (!/^(BUTTON|SCRIPT|STYLE|INPUT|SELECT|CANVAS)$/.test(n.tagName)) t += textOf(n) + (/^(P|LI|TD|TH|H2|H3|DIV)$/.test(n.tagName) ? '. ' : '');
      }
    });
    return t.replace(/\s+/g, ' ').trim();
  }

  /* ---- O'zbekcha neyron ovoz: oldindan tayyorlangan MP3 (barcha qurilmalarda bir xil) ---- */
  const SUPD = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-' };
  const UNIT = { eV: 'elektron-volt', meV: 'millielektron-volt', keV: 'kiloelektron-volt', mA: 'milliamper', mkA: 'mikroamper', nA: 'nanoamper', pA: 'pikoamper', kA: 'kiloamper', A: 'amper', mV: 'millivolt', kV: 'kilovolt', mkV: 'mikrovolt', V: 'volt', mVt: 'millivatt', mkVt: 'mikrovatt', kVt: 'kilovatt', Vt: 'vatt', K: 'kelvin', Om: 'om', kOm: 'kiloom', MOm: 'megaom', mOm: 'milliom', mkm: 'mikrometr', nm: 'nanometr', mm: 'millimetr', sm: 'santimetr', km: 'kilometr', m: 'metr', ns: 'nanosekund', ps: 'pikosekund', fs: 'femtosekund', mks: 'mikrosekund', ms: 'millisekund', s: 'sekund', Hz: 'gers', kHz: 'kilogers', Gs: 'gers', kGs: 'kilogers', MGs: 'megagers', GGs: 'gigagers', TGs: 'teragers', mS: 'millisimens', S: 'simens', MHz: 'megagers', GHz: 'gigagers', THz: 'teragers', pF: 'pikofarad', nF: 'nanofarad', mkF: 'mikrofarad', F: 'farad', dB: 'detsibel', Gy: 'grey', rad: 'rad', T: 'tesla', W: 'vatt', Pa: 'paskal', J: 'joul', C: 'kulon' };
  const DEN = ['', 'o‘ndan', 'yuzdan', 'mingdan', 'o‘n mingdan', 'yuz mingdan', 'milliondan'];
  const LET = { a: 'a', b: 'be', c: 'se', d: 'de', e: 'e', f: 'ef', g: 'ge', h: 'ha', i: 'i', j: 'je', k: 'ka', l: 'el', m: 'em', n: 'en', p: 'pe', q: 'ku', r: 'er', s: 'es', t: 'te', v: 've', w: 'dubl-ve', x: 'iks', y: 'igrek', z: 'zet' };
  const MULTI = { ox: 'oks', kT: 'ka te', qV: 'ku ve', qN: 'ku en', qn: 'ku en', qE: 'ku e', Fn: 'ef en', Fp: 'ef pe', max: 'maks', VAX: 'volt-amper xarakteristika', VAXi: 'volt-amper xarakteristikasi', VAXini: 'volt-amper xarakteristikasini', VAXlari: 'volt-amper xarakteristikalari', VAXda: 'volt-amper xarakteristikada' };
  const UGR = { 'α': 'alfa', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'Δ': 'delta', 'ε': 'epsilon', 'η': 'eta', 'θ': 'teta', 'λ': 'lyambda', 'μ': 'myu', 'ν': 'nyu', 'π': 'pi', 'ρ': 'ro', 'σ': 'sigma', 'τ': 'tau', 'φ': 'fi', 'Φ': 'fi', 'χ': 'xi', 'ψ': 'psi', 'ω': 'omega', 'Ω': 'om', 'ħ': 'h chiziqli', '∞': 'cheksizlik', '±': 'plyus-minus', '∝': 'proporsional', '·': ' ko‘paytirilgan ' };
  const UPL = { a: 'a', b: 'be', c: 'se', d: 'de', e: 'e', f: 'ef', g: 'ge', h: 'ha', i: 'i', j: 'je', k: 'ka', l: 'el', m: 'em', n: 'en', o: 'o', p: 'pe', q: 'qu', r: 'er', s: 'es', t: 'te', u: 'u', v: 've', w: 'dubl-ve', x: 'xa', y: 'ye', z: 'ze', ya: 'ya', yu: 'yu', ch: 'che', sh: 'sha' };
  const KEEP = new Set(['MOSFET', 'SPICE', 'MATLAB', 'NASA', 'GaAs', 'SiGe', 'InGaN', 'GaN', 'InP', 'SiC', 'AlGaAs', 'InAs', 'GaP', 'ZnO', 'Si', 'Ge', 'Al', 'Au', 'Pt', 'Ti', 'Ni', 'Cu', 'Ag', 'Th', 'Fermi', 'Python', 'Multisim', 'LTspice', 'ngspice']);
  function spell(w) {
    const parts = w.match(/Ya|Yu|Ch|Sh|\d+|[A-Za-z]/g) || [];
    let out = '', prevNum = false;
    parts.forEach((x, i) => { const num = /^\d/.test(x); out += (i ? (num || prevNum ? ' ' : '-') : '') + (num ? x : UPL[x.toLowerCase()]); prevNum = num; });
    return out;
  }
  function normUz(t) {
    t = t.replace(/[αβγδΔεηθλμνπρσφΦχψωΩħ∞±∝]/g, c => ' ' + UGR[c] + ' ');
    let s = ' ' + t.replace(/^\s*\d+(\.\d+)+\.?\s+/, '') + ' ';
    s = s.replace(/\(\s*[–−-]\s*\)/g, '(manfiy)').replace(/\(\s*\+\s*\)/g, '(musbat)').replace(/(^|[\s(=])[−–-](\d)/g, '$1minus $2').replace(/−/g, ' minus ');
    s = s.replace(/([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)/g, m => '^{' + [...m].map(c => SUPD[c]).join('') + '}');
    // birliklar: ko'p harfli birlik daraja oldidan yoki "ning" oldidan; har qanday birlik son ortidan
    s = s.replace(/(^|[\s(\/·])([A-Za-z]{2,4})(?=\^\{| ning |\s*bo‘lingan)/g, (m, p, u) => UNIT[u] ? p + UNIT[u] : m);
    s = s.replace(/(\d|\}|kvadrat|kub|kvadrati|kubi|darajasi,?)(\s*)([A-Za-z]{1,4})(?=[\s.,;:)\/^]|$)/g, (m, d, sp, u) => UNIT[u] && (sp || u.length > 1) ? `${d} ${UNIT[u]}` : m);
    s = s.replace(/\/(\s*)([A-Za-z]{1,4})(?=[\s.,;:)^]|$)/g, (m, sp, u) => UNIT[u] ? '/' + UNIT[u] : m);
    s = s.replace(/(\S+)\^\{2\}/g, '$1 kvadrat').replace(/(\S+)\^\{3\}/g, '$1 kub');
    s = s.replace(/(\S+)\^\{(-?)(\d+)\}/g, (m, b, mn, e) => `${b} ning ${mn ? 'minus ' : ''}${e}-darajasi`);
    s = s.replace(/(\d)\s*[·×]\s*(\d)/g, '$1 ko‘paytirilgan $2');
    s = s.replace(/(\d)\s*%/g, '$1 foiz').replace(/(\d)\s*°C/g, '$1 gradus Selsiy').replace(/(\d)\s*°/g, '$1 gradus');
    s = s.replace(/(\d+),(\d+)/g, (m, a, b) => b.length < DEN.length ? `${a} butun ${DEN[b.length]} ${parseInt(b, 10)}` : m);
    s = s.replace(/(\d)\s*[–—-]\s*(\d)/g, '$1 dan $2 gacha');
    s = s.replace(/\s*\/\s*/g, ' bo‘lingan ').replace(/\s*=\s*/g, ' teng ').replace(/\s*≈\s*/g, ' taxminan ').replace(/\s*→\s*/g, ', keyin ').replace(/\s*[≤]\s*/g, ' kichik yoki teng ').replace(/\s*[≥]\s*/g, ' katta yoki teng ');
    // harfiy belgilar (o'zgaruvchilar) odam o'qiganidek: V → ve, kT → ka te, p-n → pe-en
    s = s.replace(/(^|[\s(,\/–-])([A-Za-z][A-Za-z0-9]{0,6})(?=[\s),.;:\/–-]|$)/g, (m, p, w) => {
      if (MULTI[w]) return p + MULTI[w];
      if (w.length === 1 && !/[uoUO]/.test(w)) return p + LET[w.toLowerCase()];
      if (/^[a-zA-Z]\d$/.test(w)) return p + LET[w[0].toLowerCase()] + ' ' + w[1];
      if (KEEP.has(w)) return m;
      const sf = w.match(/^((?:[A-Z]|Ya|Yu|Ch|Sh){2,})(ning|ni|da|dan|dagi|ga|lar|larda|lari|larini|larni|lardan|i|idan|ining|ini|ida)$/);
      if (sf && !KEEP.has(sf[1])) return p + (sf[1] === 'VAX' ? 'volt-amper xarakteristika' + sf[2].replace(/^i/, 'si') : spell(sf[1]) + '-' + sf[2]);
      if (sf) return m;
      if (/^(?:[A-Z]|Ya|Yu|Ch|Sh)(?:[A-Z]|Ya|Yu|Ch|Sh|\d)+$/.test(w) || /^[a-z]{1,2}[A-Z][A-Za-z]?$/.test(w)) return p + spell(w);
      return m;
    });
    s = s.replace(/\s*[—–]\s*/g, ', ').replace(/[«»“”"]/g, '').replace(/\s+([,.;:!?])/g, '$1').replace(/([,.;:])\1+/g, '$1').replace(/\.\s*\./g, '.').replace(/\s{2,}/g, ' ');
    return s.trim();
  }
  function h32(str) { let h = 0x811c9dc5; for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16).padStart(8, '0'); }
  const uzSpeech = t => normUz(AL.toOld(t));
  const TTS = { base: 'audio/uz/', set: null, el: null, bi: -1 };
  const ttsReady = (LANG === 'uz' && window.fetch ? fetch(TTS.base + 'manifest.json', { cache: 'no-cache' }).then(r => r.ok ? r.json() : {}).catch(() => ({})) : Promise.resolve({}))
    .then(j => { TTS.set = new Set(j.files || []); });
  async function mp3For(text) { if (LANG !== 'uz') return null; await ttsReady; const k = h32(text); return TTS.set.has(k) ? `${TTS.base}${k}.mp3` : null; }
  function audioEl() { if (!TTS.el) { TTS.el = new Audio(); TTS.el.preload = 'auto'; } return TTS.el; }
  function prefetch(url) { if (url && window.fetch) fetch(url).catch(() => {}); }
  // url ni ijro etadi; resume=true bo'lsa to'xtagan joyidan davom etadi. 'end' | 'stop' | 'err'
  function playMp3(url, sid, resume) {
    const a = audioEl();
    return new Promise(res => {
      let fin = false; const done = r => { if (fin) return; fin = true; clearInterval(h); a.onended = a.onerror = null; res(r); };
      if (!resume || !a.src.endsWith(url)) { a.src = url; a.currentTime = 0; }
      a.onended = () => done('end'); a.onerror = () => done('err');
      const h = setInterval(() => { if (sid !== session) { a.pause(); done('stop'); } }, 100);
      const p = a.play(); if (p && p.catch) p.catch(() => done('err'));
    });
  }
  function audioStop() { if (TTS.el) { TTS.el.pause(); } TTS.bi = -1; }
  // Ovoz matnlarini yig'ish (GitHub Actions dagi generator uchun)
  window.YAF_TTS = {
    h32, normUz,
    items() {
      const out = [];
      const add = t => { const s = uzSpeech(t); if (s.replace(/[^A-Za-z0-9‘’']/g, '').length > 1) out.push({ h: h32(s), t: s }); };
      if (RD.btn) collectBlocks().forEach(el => add(textOf(el)));
      $$('.tour-steps li').forEach(li => add(textOf(li)));
      add(A('Namoyish tugadi. Endi parametrlarni o‘zingiz o‘zgartirib ko‘ring — natijalar darhol yangilanadi.'));
      return out;
    }
  };

  /* ---- Sahifani o'qish: pauza, davom, oldingi/keyingi, istalgan joydan boshlash ---- */
  const ICON = {
    prev: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 5h2v14H6zM20 5v14L9 12z"/></svg>',
    next: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 5h2v14h-2zM4 5v14l11-7z"/></svg>',
    play: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4v16l13-8z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>',
    stop: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="5" y="5" width="14" height="14" rx="2"/></svg>'
  };
  const RD = { blocks: [], bi: 0, ci: 0, state: 'idle', btn: $('.voice-btn[data-read]'), bar: null, chip: null };
  function collectBlocks() {
    const b = RD.btn; if (!b) return [];
    const secs = (b.dataset.read || '').split(',').map(id => document.getElementById(id)).filter(Boolean);
    const title = $('.page-hero h1'); const out = title ? [title] : [];
    secs.forEach(sec => $$('h2, h3, p, li, tr, .katex-display', sec).forEach(el => {
      if (el.closest('.sim-box,.quiz,.prompt-box,.tour-bar,.tour-cap,.vh')) return;
      if (el.matches('.katex-display') && el.closest('p,li')) return;
      if (el.matches('p,li,h3') && el.parentElement.closest('li,td')) return;
      if (el.matches('tr') && el.querySelector('th')) return;
      out.push(el);
    }));
    return out;
  }
  function heroLabel() {
    const sp = RD.btn && $('span', RD.btn); if (!sp) return;
    sp.textContent = A(RD.state === 'playing' ? 'Pauza' : RD.state === 'paused' ? 'Davom etish' : (RD.btn.dataset.label || 'Tinglash'));
    RD.btn.classList.toggle('on', RD.state === 'playing');
  }
  function ensureBar() {
    if (RD.bar) return RD.bar;
    const bar = document.createElement('div'); bar.className = 'yaf-player'; bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', A('Ovozli o‘qish boshqaruvi'));
    bar.innerHTML = `<button type="button" data-p="prev" title="${A('Oldingi xatboshi')}" aria-label="${A('Oldingi xatboshi')}">${ICON.prev}</button>`
      + `<button type="button" data-p="toggle" class="main" title="${A('Pauza / davom etish')}" aria-label="${A('Pauza / davom etish')}">${ICON.pause}</button>`
      + `<button type="button" data-p="next" title="${A('Keyingi xatboshi')}" aria-label="${A('Keyingi xatboshi')}">${ICON.next}</button>`
      + `<button type="button" data-p="stop" title="${A('To‘xtatish')}" aria-label="${A('To‘xtatish')}">${ICON.stop}</button>`
      + `<span class="info"><b class="pos notranslate"></b><span class="hint">${A('Istalgan xatboshini bosing — o‘sha joydan o‘qiladi')}</span></span>`;
    bar.addEventListener('click', e => {
      const k = e.target.closest('[data-p]')?.dataset.p; if (!k) return;
      if (k === 'toggle') (RD.state === 'playing' ? readerPause() : readLoop());
      else if (k === 'prev') readerJump(RD.bi - 1);
      else if (k === 'next') readerJump(RD.bi + 1);
      else if (k === 'stop') readerStop();
    });
    document.body.appendChild(bar); RD.bar = bar; return bar;
  }
  function updateBar() {
    const bar = ensureBar(); bar.hidden = RD.state === 'idle';
    $('[data-p="toggle"]', bar).innerHTML = RD.state === 'playing' ? ICON.pause : ICON.play;
    $('.pos', bar).textContent = RD.blocks.length ? `${Math.min(RD.bi + 1, RD.blocks.length)} / ${RD.blocks.length}` : '';
    document.body.classList.toggle('has-player', RD.state !== 'idle');
    heroLabel();
  }
  function mark(el) { $$('.reading').forEach(e => e.classList.remove('reading')); if (el) { el.classList.add('reading'); el.scrollIntoView({ behavior: 'smooth', block: 'center' }); } }
  async function sayChunk(text, v, mode, sid) {
    if (sid !== session) return;
    if (!synth) { await sleepR(Math.min(text.length * 60, 12000), sid); return; }
    if (!v && !(synth.getVoices() || []).length) { await sleepR(Math.min(text.length * 60, 12000), sid); return; }
    await new Promise(res => {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = v ? v.lang : (mode === 'tr' ? 'tr-TR' : BCP[LANG]); if (v) u.voice = v;
      u.rate = LANG === 'uz' ? 0.95 : 1;
      const guard = setTimeout(res, 30000 + text.length * 120);
      u.onend = u.onerror = () => { clearTimeout(guard); res(); };
      synth.speak(u);
    });
  }
  const sleepR = (ms, sid) => new Promise(r => { const t0 = Date.now(); const h = setInterval(() => { if (sid !== session || Date.now() - t0 >= ms) { clearInterval(h); r(); } }, 100); });
  async function readLoop() {
    if (!synth && LANG !== 'uz') { toast(A('Bu brauzer ovozli o‘qishni qo‘llab-quvvatlamaydi. Chrome, Edge yoki Safari’dan foydalaning.')); return; }
    if (!RD.blocks.length) RD.blocks = collectBlocks();
    if (RD.bi >= RD.blocks.length) { RD.bi = 0; RD.ci = 0; }
    session++; synth?.cancel(); const sid = session;
    RD.state = 'playing'; updateBar();
    const { v, mode } = await pickVoice(LANG);
    await ttsReady;
    if (LANG === 'uz' && mode !== 'native' && !warned && !TTS.set.size) {
      warned = true;
      toast(A(mode === 'tr' ? 'Qurilmada o‘zbekcha ovoz topilmadi — vaqtincha turkcha ovoz ishlatilmoqda. O‘zbekcha tabiiy ovozlar (Madina, Sardor) Microsoft Edge brauzerida mavjud.' : 'Qurilmada o‘zbekcha ovoz topilmadi. Microsoft Edge brauzerida o‘zbekcha tabiiy ovozlar (Madina, Sardor) mavjud.'), 11000);
    }
    while (RD.bi < RD.blocks.length) {
      if (sid !== session) return;
      const el = RD.blocks[RD.bi]; mark(el); updateBar();
      const raw = textOf(el);
      if (LANG === 'uz') {
        const url = await mp3For(uzSpeech(raw));
        if (sid !== session) return;
        if (url) {
          const nx = RD.blocks[RD.bi + 1]; if (nx) mp3For(uzSpeech(textOf(nx))).then(prefetch);
          const r = await playMp3(url, sid, TTS.bi === RD.bi); TTS.bi = RD.bi;
          if (sid !== session) return;
          if (r !== 'err') { RD.ci = 0; RD.bi++; TTS.bi = -1; continue; }
        }
      }
      let t = raw; if (LANG === 'uz' && mode === 'native') t = uzSpeech(t);
      const cs = chunks(t);
      for (; RD.ci < cs.length; RD.ci++) { if (sid !== session) return; await sayChunk(cs[RD.ci], v, mode, sid); }
      if (sid !== session) return;
      RD.ci = 0; RD.bi++;
    }
    readerStop();
  }
  function readerPause() { if (RD.state !== 'playing') return; const keep = TTS.bi; session++; synth?.cancel(); TTS.el?.pause(); RD.state = 'paused'; TTS.bi = keep; updateBar(); }
  function readerJump(i) {
    if (!RD.blocks.length) RD.blocks = collectBlocks();
    RD.bi = Math.max(0, Math.min(i, RD.blocks.length - 1)); RD.ci = 0; TTS.bi = -1;
    if (RD.state === 'paused') { mark(RD.blocks[RD.bi]); updateBar(); return; }
    readLoop();
  }
  function readerStop() { session++; synth?.cancel(); audioStop(); RD.state = 'idle'; RD.bi = 0; RD.ci = 0; mark(null); updateBar(); }
  RD.stop = readerStop;

  if (RD.btn) {
    RD.btn.dataset.label = $('span', RD.btn)?.textContent || '';
    RD.btn.addEventListener('click', () => {
      if (RD.state === 'playing') readerPause();
      else if (RD.state === 'paused') readLoop();
      else { stopAll(); RD.blocks = collectBlocks(); RD.bi = 0; RD.ci = 0; readLoop(); }
    });
    // Istalgan xatboshidan o'qish: xatboshini bosing → "Shu yerdan o'qish"
    const chip = document.createElement('button'); chip.type = 'button'; chip.className = 'yaf-here'; chip.hidden = true;
    chip.innerHTML = `${ICON.play}<span>${A('Shu yerdan o‘qish')}</span>`; document.body.appendChild(chip); RD.chip = chip;
    let target = -1;
    document.addEventListener('click', e => {
      if (e.target.closest('.yaf-here,.yaf-player')) return;
      chip.hidden = true;
      if (e.target.closest('a,button,input,select,label,summary,textarea,.sim-box,.quiz')) return;
      if (String(window.getSelection?.() || '').length > 2) return;
      if (!RD.blocks.length) RD.blocks = collectBlocks();
      const el = e.target.closest('h1, h2, h3, p, li, tr, .katex-display');
      let i = el ? RD.blocks.indexOf(el) : -1;
      if (i < 0 && el) i = RD.blocks.findIndex(b => b.contains(el) || el.contains(b));
      if (i < 0) return;
      target = i;
      const r = RD.blocks[i].getBoundingClientRect();
      chip.style.top = `${window.scrollY + r.top - 40}px`;
      chip.style.left = `${Math.max(8, Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - 200))}px`;
      chip.hidden = false;
    });
    chip.addEventListener('click', () => {
      chip.hidden = true; if (target < 0) return;
      if (RD.state === 'idle') { stopAll(); RD.blocks = collectBlocks(); }
      RD.bi = target; RD.ci = 0; TTS.bi = -1; readLoop();
    });
    window.addEventListener('keydown', e => { if (e.key === 'Escape' && RD.state !== 'idle') readerStop(); });
  }

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
        const t0 = performance.now(); const how = await speak(t, sid);
        const need = t.length * 55 - (performance.now() - t0); if (how !== 'mp3' && need > 0 && sid === session && !synth?.speaking) await sleep(Math.min(need, 9000));
        ro?.classList.remove('reading'); await sleep(450);
      }
      if (sid === session) { const fin = A('Namoyish tugadi. Endi parametrlarni o‘zingiz o‘zgartirib ko‘ring — natijalar darhol yangilanadi.'); cap.textContent = fin; await speak(fin, sid); if (sid === session) { stopAll(); cap.textContent = fin; } }
    });
  });
  window.addEventListener('pagehide', () => { synth?.cancel(); TTS.el?.pause(); });
  if (synth) getVoices();
})();

/* VOICE-DOCK: pastki o'ng burchakda qotirilgan "Tinglash" tugmasi (elektron doska uchun).
   Yuqoridagi tugmaning aynan nusxasi: bosilganda o'shani bosadi, holati avtomatik sinxronlanadi. */
(() => {
  const top = document.querySelector('.voice-btn[data-read]');
  if (!top) return;
  const dock = document.createElement('button');
  dock.type = 'button'; dock.className = 'voice-btn voice-dock';
  dock.setAttribute('aria-label', top.getAttribute('aria-label') || 'Tinglash');
  dock.setAttribute('translate', 'no');
  const sync = () => {
    dock.innerHTML = top.innerHTML;
    dock.classList.toggle('on', top.classList.contains('on'));
    dock.title = (top.querySelector('span')?.textContent || '').trim();
  };
  sync();
  new MutationObserver(sync).observe(top, { attributes: true, childList: true, subtree: true, characterData: true });
  dock.addEventListener('click', e => { e.stopPropagation(); top.click(); });
  document.body.appendChild(dock);
})();
