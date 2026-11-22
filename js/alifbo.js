/* Yangi o'zbek alifbosi (O'RQ-1184, 2026): O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç.
   YAF_ALIF.A(s) — matnni yangi alifboga o'tkazadi (tarjima rejimida eski shaklda qoldiradi).
   YAF_ALIF.toOld(s) — teskari o'tkazish (Google Translate va o'zbekcha ovoz uchun). */
(() => {
  const EXC = new Set(['push', 'pull', 'touch', 'match', 'batch', 'watch', 'fresh', 'english', 'chip', 'cmos', 'avalanche', 'datasheet', 'datasheets', 'latch', 'matching', 'punch', 'trench', 'manchester', 'vishay', 'flash', 'cache', 'chrome', 'chat', 'chatgpt', 'shift', 'schottky', 'shockley', 'mosfet', 'nanohub', 'bench', 'search', 'switch', 'patch', 'branch', 'each', 'hash', 'bash', 'shell', 'check', 'chart', 'child', 'tech', 'much', 'such', 'which', 'machine', 'shared']);
  const toNew = s => String(s).replace(/[A-Za-zÀ-ž‘ʻ'`]+/g, w => {
    if (EXC.has(w.toLowerCase().replace(/[‘ʻ'`]/g, ''))) return w;
    return w.replace(/([oOgG])[‘ʻ'`]/g, (m, c) => ({ o: 'ö', O: 'Ö', g: 'ğ', G: 'Ğ' })[c])
      .replace(/SH/g, 'Ş').replace(/Sh/g, 'Ş').replace(/sh/g, 'ş')
      .replace(/CH/g, 'Ç').replace(/Ch/g, 'Ç').replace(/ch/g, 'ç');
  });
  const toOld = s => String(s).replace(/Ö/g, 'O‘').replace(/ö/g, 'o‘').replace(/Ğ/g, 'G‘').replace(/ğ/g, 'g‘')
    .replace(/Ş(?=[A-ZÇŞÖĞ])/g, 'SH').replace(/Ş/g, 'Sh').replace(/ş/g, 'sh')
    .replace(/Ç(?=[A-ZÇŞÖĞ])/g, 'CH').replace(/Ç/g, 'Ch').replace(/ç/g, 'ch');
  const old = () => document.documentElement.classList.contains('alif-old');
  window.YAF_ALIF = { toNew, toOld, A: s => (old() ? String(s) : toNew(s)) };
})();
