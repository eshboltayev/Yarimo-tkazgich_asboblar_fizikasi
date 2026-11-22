/* Yarimo'tkazgich asboblar fizikasi — interaktiv simulyatorlar.
   Har bir simulyator HTML'da <div class="sim-box" data-sim="KALIT"></div> ko'rinishida chaqiriladi.
   Modellar o'quv maqsadida soddalashtirilgan (300 K, Si uchun standart parametrlar). */
(() => {
  'use strict';
  const q = 1.602e-19, kB = 8.617e-5, eps0 = 8.854e-14, epsSi = 11.7 * eps0, epsOx = 3.9 * eps0;
  const Vt = T => kB * T;
  const A = s => (window.YAF_ALIF ? window.YAF_ALIF.A(s) : String(s));
  const C = { cyan:'#22d3ee', green:'#34d399', amber:'#fbbf24', rose:'#fb7185', violet:'#a78bfa', blue:'#60a5fa', grid:'#1e2c44', axis:'#64748b', text:'#cbd5e1' };
  const SUP = { '-':'⁻', '0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹' };
  const sci = (v, d = 2) => {
    if (!isFinite(v)) return '—';
    if (v === 0) return '0';
    const e = Math.floor(Math.log10(Math.abs(v)));
    if (e >= -2 && e <= 3) return v.toFixed(Math.max(0, d - (e > 0 ? e : 0)));
    const m = v / 10 ** e;
    return `${m.toFixed(d)}·10${String(e).split('').map(ch => SUP[ch]).join('')}`;
  };
  const fx = (v, d = 3) => (isFinite(v) ? Number(v).toFixed(d) : '—');

  function ctx2d(canvas) {
    const r = canvas.getBoundingClientRect();
    const zoom = parseFloat(getComputedStyle(document.documentElement).zoom) || 1;
    const dpr = Math.min((window.devicePixelRatio || 1) * zoom, 4);
    const w = Math.max(1, Math.floor(canvas.clientWidth || r.width)), h = Math.max(1, Math.floor(canvas.clientHeight || r.height));
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) { canvas.width = w * dpr; canvas.height = h * dpr; }
    const c = canvas.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, w, h);
    return { c, w, h };
  }

  function niceTicks(a, b, n = 5) {
    const span = b - a; if (span <= 0) return [a];
    const raw = span / n, mag = 10 ** Math.floor(Math.log10(raw));
    const step = [1, 2, 2.5, 5, 10].map(s => s * mag).find(s => span / s <= n + .5) || mag * 10;
    const out = []; for (let t = Math.ceil(a / step) * step; t <= b + step * 1e-6; t += step) out.push(+t.toPrecision(10));
    return out;
  }

  /* Umumiy grafik chizuvchi */
  function plot(c, box, o) {
    const [X0, Y0, W, H] = box, L = 54, R = 12, T = 22, B = 36;
    const px = X0 + L, py = Y0 + T, pw = W - L - R, ph = H - T - B;
    const tx = v => (o.logx ? Math.log10(v) : v), ty = v => (o.logy ? Math.log10(Math.max(v, 1e-300)) : v);
    const [xa, xb] = o.xr.map(tx), [ya, yb] = o.yr.map(ty);
    const X = v => px + (tx(v) - xa) / (xb - xa) * pw;
    const Y = v => py + ph - (ty(v) - ya) / (yb - ya) * ph;
    c.save(); c.font = '11px JetBrains Mono, monospace'; c.lineWidth = 1;
    const xt = o.logx ? range(Math.ceil(xa), Math.floor(xb)).map(e => 10 ** e) : niceTicks(o.xr[0], o.xr[1], o.nx || 6);
    const yt = o.logy ? range(Math.ceil(ya), Math.floor(yb)).filter((e, i, arr) => arr.length < 9 || i % 2 === 0).map(e => 10 ** e) : niceTicks(o.yr[0], o.yr[1], o.ny || 5);
    c.strokeStyle = C.grid; c.fillStyle = C.axis; c.textAlign = 'center';
    xt.forEach(t => { const x = X(t); c.beginPath(); c.moveTo(x, py); c.lineTo(x, py + ph); c.stroke(); c.fillText(o.logx ? sci(t, 0) : fmtTick(t), x, py + ph + 15); });
    c.textAlign = 'right';
    yt.forEach(t => { const y = Y(t); c.beginPath(); c.moveTo(px, y); c.lineTo(px + pw, y); c.stroke(); c.fillText(o.logy ? sci(t, 0) : fmtTick(t), px - 6, y + 4); });
    c.strokeStyle = C.axis; c.strokeRect(px, py, pw, ph);
    if (!o.logy && o.yr[0] < 0 && o.yr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(px, Y(0)); c.lineTo(px + pw, Y(0)); c.stroke(); }
    if (!o.logx && o.xr[0] < 0 && o.xr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(X(0), py); c.lineTo(X(0), py + ph); c.stroke(); }
    c.fillStyle = C.text; c.textAlign = 'center'; c.fillText(A(o.xl || ''), px + pw / 2, py + ph + 30);
    c.textAlign = 'left'; c.fillText(A(o.yl || ''), px, py - 8);
    c.beginPath(); c.rect(px, py, pw, ph); c.clip();
    (o.fill || []).forEach(f => { c.fillStyle = f.c; c.beginPath(); f.pts.forEach(([x, y], i) => (i ? c.lineTo(X(x), Y(y)) : c.moveTo(X(x), Y(y)))); c.closePath(); c.fill(); });
    (o.series || []).forEach(s => {
      c.strokeStyle = s.c || C.cyan; c.lineWidth = s.w || 2; c.setLineDash(s.dash || []); c.beginPath(); let started = false;
      s.pts.forEach(([x, y]) => { if (!isFinite(y) || !isFinite(x) || (o.logy && y <= 0) || (o.logx && x <= 0)) { started = false; return; } const xx = X(x), yy = Y(y); if (!started) { c.moveTo(xx, yy); started = true; } else c.lineTo(xx, yy); });
      c.stroke(); c.setLineDash([]);
    });
    (o.vl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(v.x), py); c.lineTo(X(v.x), py + ph); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), X(v.x) + 4, py + 12); } });
    (o.hl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(px, Y(v.y)); c.lineTo(px + pw, Y(v.y)); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), px + 6, Y(v.y) - 5); } });
    (o.marks || []).forEach(m => { c.fillStyle = m.c || '#fff'; c.beginPath(); c.arc(X(m.x), Y(m.y), m.r || 5, 0, 7); c.fill(); if (m.l) { c.fillText(A(m.l), X(m.x) + 8, Y(m.y) - 8); } });
    c.restore();
    if ((o.legend || []).length) { c.fillStyle = 'rgba(3,7,18,.82)'; c.fillRect(px + pw - 156, py + 2, 152, o.legend.length * 16 + 8); }
    (o.legend || []).forEach((g, i) => { c.font = '11px Inter, sans-serif'; c.fillStyle = g.c; c.fillRect(px + pw - 150, py + 8 + i * 16, 12, 3); c.fillStyle = C.text; c.textAlign = 'left'; c.fillText(A(g.l), px + pw - 133, py + 13 + i * 16); });
    return { X, Y };
  }
  const fmtTick = t => (Math.abs(t) >= 1000 || (Math.abs(t) < .01 && t !== 0) ? sci(t, 1) : String(+t.toFixed(3)));
  const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
  const lin = (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1));
  const label = (c, t, x, y, col = C.text, al = 'left') => { c.fillStyle = col; c.font = '12px Inter, sans-serif'; c.textAlign = al; c.fillText(A(t), x, y); };

  const MAT = {
    Si: { Eg0: 1.17, a: 4.73e-4, b: 636, Nc: 3.2e19, Nv: 1.8e19, eps: 11.7 },
    Ge: { Eg0: .7437, a: 4.774e-4, b: 235, Nc: 1.04e19, Nv: 6.0e18, eps: 16.0 },
    GaAs: { Eg0: 1.519, a: 5.405e-4, b: 204, Nc: 4.7e17, Nv: 9.0e18, eps: 12.9 }
  };
  const Eg = (m, T) => m.Eg0 - m.a * T * T / (T + m.b);
  const niOf = (m, T) => Math.sqrt(m.Nc * m.Nv) * (T / 300) ** 1.5 * Math.exp(-Eg(m, T) / (2 * Vt(T)));
  const nOf = (Nd, ni) => Nd / 2 + Math.sqrt(Nd * Nd / 4 + ni * ni);

  const S = {};

  /* M1 — Zaryad tashuvchilar konsentratsiyasi va Fermi sathi */
  S.fermi = {
    title: 'Konsentratsiya va Fermi sathi',
    params: [
      { k: 'mat', l: 'Material', type: 'sel', opts: ['Si', 'Ge', 'GaAs'], v: 'Si' },
      { k: 'Nd', l: 'Donor konsentratsiyasi N_d, sm⁻³', min: 13, max: 19, step: .1, v: 16, log: true },
      { k: 'T', l: 'Harorat T, K', min: 200, max: 700, step: 5, v: 300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), m = MAT[P.mat];
      const ni = niOf(m, P.T), n = nOf(P.Nd, ni), p = ni * ni / n, eg = Eg(m, P.T);
      const dEF = Vt(P.T) * Math.log(n / ni);
      const Ts = lin(200, 700, 120);
      plot(c, [w * .42, 0, w * .58, h], {
        xr: [200, 700], yr: [1e8, 1e20], logy: true, xl: 'T, K', yl: 'n, p, nᵢ (sm⁻³)',
        series: [
          { pts: Ts.map(T => [T, niOf(m, T)]), c: C.amber, dash: [6, 4] },
          { pts: Ts.map(T => [T, nOf(P.Nd, niOf(m, T))]), c: C.cyan },
          { pts: Ts.map(T => { const ni2 = niOf(m, T); return [T, ni2 * ni2 / nOf(P.Nd, ni2)]; }), c: C.rose }
        ],
        marks: [{ x: P.T, y: n, c: C.cyan }],
        legend: [{ c: C.cyan, l: 'n (elektronlar)' }, { c: C.rose, l: 'p (teshiklar)' }, { c: C.amber, l: 'nᵢ (xususiy)' }]
      });
      // zonaviy diagramma
      const bx = 20, bw = w * .36, top = 40, bot = h - 40, sc = (bot - top) / (eg + .3);
      const yEc = top + .15 * sc, yEv = yEc + eg * sc, yEi = (yEc + yEv) / 2, yEF = yEi - dEF * sc;
      c.fillStyle = '#1d4ed822'; c.fillRect(bx, top, bw, yEc - top); c.fillStyle = '#e11d4818'; c.fillRect(bx, yEv, bw, bot - yEv);
      [[yEc, C.blue, 'E_c'], [yEv, C.rose, 'E_v'], [yEi, '#94a3b8', 'E_i'], [yEF, C.green, 'E_F']].forEach(([y, col, t], i) => {
        c.strokeStyle = col; c.lineWidth = 2; c.setLineDash(i >= 2 ? [6, 4] : []); c.beginPath(); c.moveTo(bx, y); c.lineTo(bx + bw, y); c.stroke(); c.setLineDash([]); label(c, t, bx + bw + 4, y + 4, col);
      });
      label(c, `E_g = ${eg.toFixed(3)} eV`, bx, top - 12, C.text);
      return { 'E_g(T), eV': fx(eg), 'nᵢ, sm⁻³': sci(ni), 'n₀, sm⁻³': sci(n), 'p₀, sm⁻³': sci(p), 'E_F − E_i, eV': fx(dEF), 'σ = qnμₙ (μ=1350), S/sm': sci(q * n * 1350) };
    }
  };

  /* M2 — Metall–yarimo'tkazgich (Shottki) kontakti */
  S.schottky = {
    title: 'Shottki bareri: VAX',
    params: [
      { k: 'phiB', l: 'Barer balandligi φ_B, eV', min: .4, max: .9, step: .01, v: .72 },
      { k: 'n', l: 'Ideallik koeffitsiyenti n', min: 1, max: 1.5, step: .01, v: 1.05 },
      { k: 'T', l: 'Harorat T, K', min: 250, max: 400, step: 5, v: 300 },
      { k: 'Nd', l: 'N_d, sm⁻³', min: 15, max: 18, step: .1, v: 16, log: true }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), A = 112, vt = Vt(P.T);
      const J0 = A * P.T * P.T * Math.exp(-P.phiB / vt);
      const J0pn = 1e-11 * Math.exp(-(1.12) / vt) / Math.exp(-1.12 / Vt(300));
      const Vs = lin(-.4, .7, 200);
      plot(c, [0, 0, w, h], {
        xr: [-.4, .7], yr: [1e-12, 1e3], logy: true, xl: 'V, V', yl: '|J|, A/sm²',
        series: [
          { pts: Vs.map(V => [V, Math.abs(J0 * (Math.exp(V / (P.n * vt)) - 1))]), c: C.cyan },
          { pts: Vs.map(V => [V, Math.abs(J0pn * (Math.exp(V / vt) - 1))]), c: C.rose, dash: [6, 4] }
        ],
        hl: [{ y: 1e-3, l: '1 mA/sm²', c: '#64748b' }],
        legend: [{ c: C.cyan, l: 'Shottki diodi' }, { c: C.rose, l: 'p-n diod (taqqoslash)' }]
      });
      const Vbi = P.phiB - vt * Math.log(2.8e19 / P.Nd);
      const W = Math.sqrt(2 * epsSi * Math.max(Vbi, 0) / (q * P.Nd));
      const Von = P.n * vt * Math.log(1e-3 / J0 + 1);
      return { 'J_s = A*T²e^(−φB/kT), A/sm²': sci(J0), 'V (J = 1 mA/sm²), V': fx(Von), 'V_bi, V': fx(Vbi), 'W (V=0), mkm': fx(W * 1e4), 'C/A (V=0), nF/sm²': fx(epsSi / W * 1e9, 1) };
    }
  };

  /* M3, A12, A13 — p-n o'tish */
  S.pn = {
    title: 'p-n o‘tish: zonalar, maydon, sig‘im',
    params: [
      { k: 'Na', l: 'N_a (p-soha), sm⁻³', min: 14, max: 19, step: .1, v: 17, log: true },
      { k: 'Nd', l: 'N_d (n-soha), sm⁻³', min: 14, max: 19, step: .1, v: 16, log: true },
      { k: 'Va', l: 'Tashqi kuchlanish V, V', min: -10, max: .6, step: .05, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vt = Vt(300), ni = 1e10;
      const Vbi = vt * Math.log(P.Na * P.Nd / ni / ni), Vj = Math.max(Vbi - P.Va, .01);
      const W = Math.sqrt(2 * epsSi / q * (P.Na + P.Nd) / (P.Na * P.Nd) * Vj);
      const xn = W * P.Na / (P.Na + P.Nd), xp = W * P.Nd / (P.Na + P.Nd), Em = q * P.Nd * xn / epsSi;
      const span = Math.max(W * 1.8, 2e-5), xs = lin(-span, span, 300);
      const phi = x => (x <= -xp ? 0 : x < 0 ? q * P.Na / (2 * epsSi) * (x + xp) ** 2 : x < xn ? Vj - q * P.Nd / (2 * epsSi) * (xn - x) ** 2 : Vj);
      const Ec = x => 1.12 - phi(x) + .3, Ev = x => Ec(x) - 1.12;
      const EFp = .3 + vt * Math.log(1.8e19 / P.Na), EFn = 1.42 - Vj - vt * Math.log(3.2e19 / P.Nd);
      plot(c, [0, 0, w * .55, h], {
        xr: [-span * 1e4, span * 1e4], yr: [.1 - Vj, 1.65], xl: 'x, mkm', yl: 'E, eV (zonaviy diagramma)',
        series: [{ pts: xs.map(x => [x * 1e4, Ec(x)]), c: C.blue }, { pts: xs.map(x => [x * 1e4, Ev(x)]), c: C.rose },
          { pts: [[-span * 1e4, EFp], [0, EFp]], c: C.green, dash: [6, 4] }, { pts: [[0, EFn], [span * 1e4, EFn]], c: C.green, dash: [6, 4] }],
        vl: [{ x: -xp * 1e4, c: '#475569' }, { x: xn * 1e4, c: '#475569' }],
        legend: [{ c: C.blue, l: 'E_c' }, { c: C.rose, l: 'E_v' }, { c: C.green, l: 'E_F (kvazi)' }]
      });
      plot(c, [w * .56, 0, w * .44, h], {
        xr: [-span * 1e4, span * 1e4], yr: [0, Em * 1.15 / 1e3], xl: 'x, mkm', yl: '|E(x)|, kV/sm',
        series: [{ pts: xs.map(x => [x * 1e4, (x <= -xp || x >= xn ? 0 : x < 0 ? q * P.Na * (x + xp) / epsSi : q * P.Nd * (xn - x) / epsSi) / 1e3]), c: C.amber, w: 2.5 }],
        fill: [{ c: '#fbbf2422', pts: [[-xp * 1e4, 0], [0, Em / 1e3], [xn * 1e4, 0]] }]
      });
      const Cj = epsSi / W;
      return { 'V_bi, V': fx(Vbi), 'W, mkm': fx(W * 1e4), 'x_n / x_p, mkm': `${fx(xn * 1e4)} / ${fx(xp * 1e4)}`, 'E_max, kV/sm': fx(Em / 1e3, 1), 'C_j/A, nF/sm²': fx(Cj * 1e9, 2) };
    }
  };

  /* M4 — Haqiqiy diod VAX */
  S.diode = {
    title: 'Real diod VAX',
    params: [
      { k: 'Is', l: 'To‘yinish toki I_s, A', min: -15, max: -8, step: .1, v: -13, log: true },
      { k: 'n', l: 'Ideallik koeffitsiyenti n', min: 1, max: 2, step: .05, v: 1.2 },
      { k: 'Rs', l: 'Ketma-ket qarshilik R_s, Ω', min: 0, max: 20, step: .5, v: 2 },
      { k: 'T', l: 'Harorat T, K', min: 250, max: 400, step: 5, v: 300 },
      { k: 'log', l: 'Shkala', type: 'sel', opts: ['chiziqli', 'logarifmik'], v: 'chiziqli' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vt = Vt(P.T);
      const Is = P.Is * Math.exp(1.12 / Vt(300) - 1.12 / vt) * (P.T / 300) ** 3;
      const Iarr = lin(-12, -1, 300).map(e => 10 ** e).concat(lin(.1, 1, 40).map(x => x * .1));
      const VofI = (I, rs) => P.n * vt * Math.log(I / Is + 1) + I * rs;
      const lg = P.log === 'logarifmik';
      plot(c, [0, 0, w, h], {
        xr: [0, 1.2], yr: lg ? [1e-12, .1] : [0, 100], logy: lg, xl: 'V, V', yl: lg ? 'I, A' : 'I, mA',
        series: [
          { pts: Iarr.map(I => [VofI(I, 0), lg ? I : I * 1e3]), c: '#64748b', dash: [5, 4] },
          { pts: Iarr.map(I => [VofI(I, P.Rs), lg ? I : I * 1e3]), c: C.cyan, w: 2.5 }
        ],
        legend: [{ c: C.cyan, l: 'real (Rₛ bilan)' }, { c: '#64748b', l: 'ideal (Rₛ = 0)' }]
      });
      const I10 = .01;
      return { 'I_s(T), A': sci(Is), 'V (I = 10 mA), V': fx(VofI(I10, P.Rs)), 'r_d = nV_T/I (10 mA), Ω': fx(P.n * vt / I10, 2), 'V_T = kT/q, mV': fx(vt * 1e3, 2), 'dV/dT (10 mA), mV/K': fx((VofI(I10, 0) - P.n * (1.12 + 3 * vt)) / P.T * 1e3, 2) };
    }
  };

  /* M5 — Teshilish, stabilitron va tunnel diod */
  S.zener = {
    title: 'Teshilish: stabilitron va tunnel diod',
    params: [
      { k: 'mode', l: 'Asbob', type: 'sel', opts: ['stabilitron', 'tunnel diod'], v: 'stabilitron' },
      { k: 'Vz', l: 'Stabilizatsiya kuchlanishi V_Z, V', min: 2.7, max: 15, step: .1, v: 5.6 },
      { k: 'rz', l: 'Differensial qarshilik r_Z, Ω', min: 1, max: 40, step: 1, v: 10 },
      { k: 'Ip', l: 'Tunnel: cho‘qqi toki I_p, mA', min: 1, max: 20, step: .5, v: 10 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vt = Vt(300);
      if (P.mode === 'stabilitron') {
        const Vs = lin(-P.Vz - 2, 1, 400), Is = 1e-14;
        const I = V => (V > -P.Vz ? Is * (Math.exp(V / vt) - 1) * 1e3 : -((-V - P.Vz) / P.rz) * 1e3 - Is * 1e3);
        plot(c, [0, 0, w, h], { xr: [-P.Vz - 2, 1], yr: [-60, 60], xl: 'V, V', yl: 'I, mA', series: [{ pts: Vs.map(V => [V, Math.max(-80, Math.min(80, I(V)))]), c: C.cyan, w: 2.5 }], vl: [{ x: -P.Vz, l: `−V_Z = −${P.Vz} V` }] });
        const mech = P.Vz < 5 ? 'Zener (tunnel) teshilishi, TKN < 0' : P.Vz > 6.5 ? 'Ko‘chkisimon teshilish, TKN > 0' : 'Aralash mexanizm, TKN ≈ 0';
        return { 'Mexanizm': mech, 'ΔV (ΔI = 20 mA), V': fx(.02 * P.rz, 2), 'P (I = 50 mA), mVt': fx(P.Vz * 50, 0) };
      }
      const Vp = .065, Iv = P.Ip * .08, Is = 2e-7;
      const It = V => P.Ip * (V / Vp) * Math.exp(1 - V / Vp) + Iv * (V > 0 ? 1 - Math.exp(-V / .1) : 0) + Is * (Math.exp(V / vt) - 1);
      const Vs = lin(-.05, .55, 400);
      plot(c, [0, 0, w, h], { xr: [-.05, .55], yr: [-2, P.Ip * 1.4], xl: 'V, V', yl: 'I, mA', series: [{ pts: Vs.map(V => [V, It(V)]), c: C.violet, w: 2.5 }], marks: [{ x: Vp, y: It(Vp), c: C.amber, l: 'cho‘qqi' }], vl: [{ x: Vp, c: '#475569' }] });
      let vmin = .2, imin = 1e9; for (let V = .1; V < .5; V += .001) { const i = It(V); if (i < imin) { imin = i; vmin = V; } }
      return { 'V_p, V': fx(Vp, 3), 'I_p, mA': fx(P.Ip, 1), 'V_v (botiq), V': fx(vmin, 3), 'I_v, mA': fx(imin, 2), 'I_p/I_v': fx(P.Ip / imin, 1) };
    }
  };

  /* M6, A2, A3 — Bipolyar tranzistor chiqish xarakteristikalari */
  S.bjt = {
    title: 'BT: chiqish xarakteristikalari va ishchi nuqta',
    params: [
      { k: 'beta', l: 'Tok kuchaytirish β', min: 50, max: 400, step: 5, v: 150 },
      { k: 'VA', l: 'Erli kuchlanishi V_A, V', min: 20, max: 200, step: 5, v: 80 },
      { k: 'Ib', l: 'Baza toki I_B, mkA', min: 5, max: 60, step: 1, v: 30 },
      { k: 'Vcc', l: 'Manba V_CC, V', min: 5, max: 20, step: .5, v: 12 },
      { k: 'Rc', l: 'Yuklama R_C, kΩ', min: .5, max: 5, step: .1, v: 1.5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv);
      const Ic = (ib, v) => P.beta * ib * (1 + v / P.VA) * (1 - Math.exp(-v / .08));
      const Vs = lin(0, P.Vcc * 1.1, 200), series = [];
      [10, 20, 30, 40, 50, 60].forEach(ib => series.push({ pts: Vs.map(v => [v, Ic(ib * 1e-6, v) * 1e3]), c: '#334155', w: 1.2 }));
      series.push({ pts: Vs.map(v => [v, Ic(P.Ib * 1e-6, v) * 1e3]), c: C.cyan, w: 2.5 });
      series.push({ pts: [[0, P.Vcc / P.Rc], [P.Vcc, 0]], c: C.amber, dash: [6, 4] });
      let lo = 0, hi = P.Vcc; for (let i = 0; i < 60; i++) { const m = (lo + hi) / 2; (Ic(P.Ib * 1e-6, m) * P.Rc * 1e3 + m > P.Vcc) ? hi = m : lo = m; }
      const Vq = lo, Iq = Ic(P.Ib * 1e-6, Vq);
      const ymax = Math.max(P.Vcc / P.Rc, Ic(60e-6, P.Vcc) * 1e3) * 1.1;
      plot(c, [0, 0, w, h], { xr: [0, P.Vcc * 1.1], yr: [0, ymax], xl: 'V_KE, V', yl: 'I_K, mA', series, marks: [{ x: Vq, y: Iq * 1e3, c: C.green, l: 'Q' }], legend: [{ c: C.cyan, l: `I_B = ${P.Ib} mkA` }, { c: C.amber, l: 'yuklama chizig‘i' }] });
      const mode = Vq < .3 ? 'to‘yinish' : 'aktiv (kuchaytirish)';
      return { 'I_KQ, mA': fx(Iq * 1e3, 2), 'V_KEQ, V': fx(Vq, 2), 'Rejim': mode, 'P_K = I_K·V_KE, mVt': fx(Iq * Vq * 1e3, 1), 'g_m = I_K/V_T, mS': fx(Iq / Vt(300) * 1e3, 1), 'r_o = V_A/I_K, kΩ': fx(P.VA / Iq / 1e3, 1) };
    }
  };

  /* M7, A4 — Chastotaviy xususiyatlar */
  S.bjtfreq = {
    title: 'β(f) chastotaviy xarakteristika',
    params: [
      { k: 'b0', l: 'Past chastotali β₀', min: 20, max: 400, step: 5, v: 150 },
      { k: 'fT', l: 'Chegaraviy chastota f_T, MGs', min: 10, max: 5000, step: 10, v: 300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), fb = P.fT * 1e6 / P.b0;
      const fs = lin(3, 10.5, 300).map(e => 10 ** e), mag = f => P.b0 / Math.sqrt(1 + (f / fb) ** 2);
      plot(c, [0, 0, w, h], { xr: [1e3, 3e10], yr: [.1, 1000], logx: true, logy: true, xl: 'f, Gs', yl: '|β|',
        series: [{ pts: fs.map(f => [f, mag(f)]), c: C.cyan, w: 2.5 }, { pts: fs.map(f => [f, P.fT * 1e6 / f]), c: '#64748b', dash: [5, 4] }],
        hl: [{ y: 1, l: '|β| = 1' }, { y: P.b0 / Math.SQRT2, l: 'β₀/√2', c: C.green }], vl: [{ x: fb, l: 'f_β', c: C.green }, { x: P.fT * 1e6, l: 'f_T', c: C.rose }] });
      return { 'f_β = f_T/β₀': fb > 1e6 ? fx(fb / 1e6, 3) + ' MGs' : fx(fb / 1e3, 1) + ' kGs', 'f_α ≈ (β₀+1)f_β, MGs': fx((P.b0 + 1) * fb / 1e6, 1), 'GBW = β₀·f_β, MGs': fx(P.b0 * fb / 1e6, 1), 'τ = 1/(2πf_T), ps': fx(1e12 / (2 * Math.PI * P.fT * 1e6), 1) };
    }
  };

  /* M8 — Tiristor */
  S.thyristor = {
    title: 'Tiristor VAX va boshqaruv toki',
    params: [
      { k: 'Vbo', l: 'Ochilish kuchlanishi V_BO (I_G=0), V', min: 50, max: 600, step: 10, v: 400 },
      { k: 'Ig', l: 'Boshqaruv toki I_G, mA', min: 0, max: 30, step: .5, v: 10 },
      { k: 'Igt', l: 'Ochilish uchun I_GT, mA', min: 5, max: 40, step: 1, v: 25 },
      { k: 'Ih', l: 'Ushlab turish toki I_H, mA', min: 5, max: 80, step: 1, v: 30 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv);
      const vbo = ig => Math.max(1.5, P.Vbo * (1 - (ig / P.Igt) ** 2));
      const curve = ig => { const v = vbo(ig), pts = []; lin(0, v, 60).forEach(x => pts.push([x, .05 + .5 * (x / v) ** 6])); pts.push([v, 1]); pts.push([1.1, P.Ih]); lin(1.1, 1.6, 30).forEach(x => pts.push([x, P.Ih + (x - 1.1) * 600])); return pts; };
      const series = [0, .5, .8].map(f => ({ pts: curve(f * P.Igt), c: '#334155', w: 1.2 }));
      series.push({ pts: curve(Math.min(P.Ig, P.Igt)), c: C.cyan, w: 2.5 });
      series.push({ pts: lin(-P.Vbo * 1.1, 0, 50).map(x => [x, -.05]), c: C.rose, w: 2 });
      plot(c, [0, 0, w, h], { xr: [-P.Vbo * .3, P.Vbo * 1.1], yr: [-20, P.Ih * 4 + 100], xl: 'V_AK, V', yl: 'I_A, mA', series, hl: [{ y: P.Ih, l: 'I_H', c: C.green }], vl: [{ x: vbo(Math.min(P.Ig, P.Igt)), l: 'V_BO(I_G)' }] });
      return { 'V_BO(I_G), V': fx(vbo(Math.min(P.Ig, P.Igt)), 1), 'Holat': P.Ig >= P.Igt ? 'boshqaruv bilan darhol ochiladi' : 'yopiq, V_BO gacha', 'Yopilish sharti': `I_A < I_H = ${P.Ih} mA`, 'Ochiq holat kuchl., V': '≈ 1.1–1.6' };
    }
  };

  /* M9, A8, A9 — Boshqariluvchi p-n o'tishli maydonli tranzistor (JFET) */
  S.jfet = {
    title: 'JFET: o‘tish va chiqish xarakteristikasi',
    params: [
      { k: 'Idss', l: 'I_DSS, mA', min: 2, max: 20, step: .5, v: 10 },
      { k: 'Vp', l: 'Berkilish kuchlanishi V_P, V', min: -6, max: -1, step: .1, v: -4 },
      { k: 'Vgs', l: 'Zatvor kuchlanishi V_GS, V', min: -6, max: 0, step: .1, v: -1.5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Vgs = Math.max(P.Vgs, P.Vp);
      const sat = v => (v <= P.Vp ? 0 : P.Idss * (1 - v / P.Vp) ** 2);
      const out = (vg, vd) => { if (vg <= P.Vp) return 0; const vov = vg - P.Vp; return vd < vov ? P.Idss * (2 * vd * vov - vd * vd) / (P.Vp * P.Vp) : sat(vg); };
      plot(c, [0, 0, w * .45, h], { xr: [P.Vp - .5, 0], yr: [0, P.Idss * 1.1], xl: 'V_GS, V', yl: 'I_D, mA (o‘tish)', series: [{ pts: lin(P.Vp, 0, 100).map(v => [v, sat(v)]), c: C.cyan, w: 2.5 }], marks: [{ x: Vgs, y: sat(Vgs), c: C.green }] });
      const vds = lin(0, 15, 150), series = [0, .25, .5, .75].map(f => ({ pts: vds.map(v => [v, out(P.Vp * f, v)]), c: '#334155', w: 1.2 }));
      series.push({ pts: vds.map(v => [v, out(Vgs, v)]), c: C.cyan, w: 2.5 });
      series.push({ pts: lin(0, -P.Vp, 50).map(v => [v, P.Idss * (v / P.Vp) ** 2]), c: C.amber, dash: [5, 4] });
      plot(c, [w * .46, 0, w * .54, h], { xr: [0, 15], yr: [0, P.Idss * 1.1], xl: 'V_SI, V', yl: 'I_D, mA (chiqish)', series });
      const gm = 2 * P.Idss / Math.abs(P.Vp) * (1 - Vgs / P.Vp);
      return { 'I_D (to‘yinish), mA': fx(sat(Vgs), 2), 'Tiklik S = g_m, mA/V': fx(gm, 2), 'g_m0 = 2I_DSS/|V_P|, mA/V': fx(2 * P.Idss / Math.abs(P.Vp), 2), 'V_SI,to‘y = V_GS − V_P, V': fx(Vgs - P.Vp, 2) };
    }
  };

  /* M10, A1 — MDYa kondensator C–V */
  S.mosc = {
    title: 'MDYa strukturasi: C–V xarakteristika',
    params: [
      { k: 'Na', l: 'Taglik N_a (p-Si), sm⁻³', min: 15, max: 18, step: .1, v: 17, log: true },
      { k: 'tox', l: 'Oksid qalinligi d, nm', min: 2, max: 100, step: 1, v: 10 },
      { k: 'Vfb', l: 'Tekis zonalar kuchl. V_FB, V', min: -2, max: 1, step: .05, v: -.9 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vt = Vt(300), Cox = epsOx / (P.tox * 1e-7);
      const phiF = vt * Math.log(P.Na / 1e10), gam = Math.sqrt(2 * q * epsSi * P.Na) / Cox;
      const VT = P.Vfb + 2 * phiF + gam * Math.sqrt(2 * phiF);
      const Wmax = Math.sqrt(2 * epsSi * 2 * phiF / (q * P.Na)), Cmin = 1 / (1 / Cox + Wmax / epsSi);
      const Vs = lin(P.Vfb - 3, VT + 3, 300);
      const hf = V => { if (V <= P.Vfb) return Cox; if (V >= VT) return Cmin; const s = (-gam + Math.sqrt(gam * gam + 4 * (V - P.Vfb))) / 2, ps = s * s; const Wd = Math.sqrt(2 * epsSi * ps / (q * P.Na)); return 1 / (1 / Cox + Wd / epsSi); };
      const lf = V => (V >= VT ? Math.min(Cox, Cmin + (Cox - Cmin) * (1 - Math.exp(-(V - VT) / .25))) : hf(V));
      plot(c, [0, 0, w, h], { xr: [P.Vfb - 3, VT + 3], yr: [0, 1.08], xl: 'V_G, V', yl: 'C/C_ox',
        series: [{ pts: Vs.map(V => [V, lf(V) / Cox]), c: C.green, dash: [6, 4] }, { pts: Vs.map(V => [V, hf(V) / Cox]), c: C.cyan, w: 2.5 }],
        vl: [{ x: P.Vfb, l: 'V_FB', c: '#94a3b8' }, { x: VT, l: 'V_T', c: C.rose }], legend: [{ c: C.cyan, l: 'yuqori chastota' }, { c: C.green, l: 'past chastota' }] });
      return { 'C_ox, nF/sm²': fx(Cox * 1e9, 1), 'φ_F, V': fx(phiF), 'W_max, mkm': fx(Wmax * 1e4), 'C_min/C_ox': fx(Cmin / Cox), 'V_T, V': fx(VT) };
    }
  };

  /* M11, A5–A7 — MOSFET */
  S.mosfet = {
    title: 'MDYa tranzistor (MOSFET) xarakteristikalari',
    params: [
      { k: 'Vt', l: 'Bo‘sag‘a kuchlanishi V_T (300 K), V', min: .3, max: 2, step: .05, v: .7 },
      { k: 'k', l: 'k = μC_ox·W/L, mA/V²', min: .5, max: 20, step: .5, v: 4 },
      { k: 'lam', l: 'Kanal uzunligi modulyatsiyasi λ, V⁻¹', min: 0, max: .1, step: .005, v: .02 },
      { k: 'Vgs', l: 'V_ZI, V', min: 0, max: 5, step: .1, v: 2.5 },
      { k: 'T', l: 'Harorat T, K', min: 250, max: 450, step: 5, v: 300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), kT = P.k * (P.T / 300) ** -1.5, VT = P.Vt - .002 * (P.T - 300);
      const Id = (vg, vd) => { const ov = vg - VT; if (ov <= 0) return 0; return vd < ov ? kT * (ov * vd - vd * vd / 2) * (1 + P.lam * vd) : .5 * kT * ov * ov * (1 + P.lam * vd); };
      const vds = lin(0, 6, 200), series = [1, 2, 3, 4, 5].map(vg => ({ pts: vds.map(v => [v, Id(vg, v)]), c: '#334155', w: 1.2 }));
      series.push({ pts: vds.map(v => [v, Id(P.Vgs, v)]), c: C.cyan, w: 2.5 });
      series.push({ pts: lin(0, 5 - VT, 60).map(v => [v, .5 * kT * v * v]), c: C.amber, dash: [5, 4] });
      plot(c, [0, 0, w, h], { xr: [0, 6], yr: [0, Math.max(1, .5 * kT * (5 - VT) ** 2 * 1.25)], xl: 'V_SI, V', yl: 'I_S, mA', series, legend: [{ c: C.cyan, l: `V_ZI = ${P.Vgs} V` }, { c: C.amber, l: 'to‘yinish chegarasi' }] });
      const ov = Math.max(P.Vgs - VT, 0), idsat = .5 * kT * ov * ov;
      return { 'V_T(T), V': fx(VT), 'k(T), mA/V²': fx(kT, 2), 'I_S,to‘y (V_SI=V_ov), mA': fx(idsat, 2), 'g_m = k·V_ov, mS': fx(kT * ov, 2), 'r_o ≈ 1/(λI_S), kΩ': P.lam && idsat ? fx(1 / (P.lam * idsat), 1) : '∞' };
    }
  };

  /* M12 — Fotodiod va quyosh elementi */
  S.solar = {
    title: 'Fotodiod / quyosh elementi VAX',
    params: [
      { k: 'G', l: 'Yoritilganlik G, Vt/m²', min: 0, max: 1200, step: 10, v: 1000 },
      { k: 'J0', l: 'Qorong‘i tok J₀, A/sm²', min: -14, max: -8, step: .1, v: -12, log: true },
      { k: 'n', l: 'Ideallik n', min: 1, max: 2, step: .05, v: 1 },
      { k: 'T', l: 'Harorat T, K', min: 270, max: 360, step: 1, v: 300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vt = Vt(P.T), Jsc = 35e-3 * P.G / 1000;
      const J0 = P.J0 * (P.T / 300) ** 3 * Math.exp(1.12 / Vt(300) - 1.12 / vt);
      const J = V => Jsc - J0 * (Math.exp(V / (P.n * vt)) - 1);
      const Voc = Jsc > 0 ? P.n * vt * Math.log(Jsc / J0 + 1) : 0;
      let pm = 0, vm = 0; lin(0, Math.max(Voc, .01), 400).forEach(V => { const p = V * J(V); if (p > pm) { pm = p; vm = V; } });
      const Vs = lin(-.5, .8, 300);
      plot(c, [0, 0, w, h], { xr: [-.5, .8], yr: [-5, 45], xl: 'V, V', yl: 'J, mA/sm² ;  P, mVt/sm²',
        series: [{ pts: Vs.map(V => [V, J(V) * 1e3]), c: C.cyan, w: 2.5 }, { pts: Vs.filter(V => V >= 0 && V <= Voc).map(V => [V, V * J(V) * 1e3]), c: C.amber }, { pts: Vs.map(V => [V, -J0 * (Math.exp(V / (P.n * vt)) - 1) * 1e3]), c: '#64748b', dash: [5, 4] }],
        marks: pm > 0 ? [{ x: vm, y: J(vm) * 1e3, c: C.green, l: 'MPP' }] : [], legend: [{ c: C.cyan, l: 'yoritilgan J(V)' }, { c: C.amber, l: 'quvvat P(V)' }, { c: '#64748b', l: 'qorong‘i' }] });
      const Pin = P.G / 10; // mVt/sm²
      return { 'J_sc, mA/sm²': fx(Jsc * 1e3, 1), 'V_oc, V': fx(Voc), 'P_max, mVt/sm²': fx(pm * 1e3, 2), 'FF': Jsc ? fx(pm / (Jsc * Voc)) : '—', 'FIK η, %': Pin ? fx(pm * 1e3 / Pin * 100, 1) : '—' };
    }
  };

  /* M13 — Svetodiod va yarimo'tkazgichli lazer */
  S.led = {
    title: 'Svetodiod spektri va lazer L–I',
    params: [
      { k: 'Eg', l: 'Taqiqlangan zona E_g, eV', min: 1.3, max: 3.4, step: .01, v: 1.9 },
      { k: 'T', l: 'Harorat T, K', min: 250, max: 400, step: 5, v: 300 },
      { k: 'Ith', l: 'Lazer bo‘sag‘a toki I_th, mA', min: 5, max: 60, step: 1, v: 20 },
      { k: 'eta', l: 'Differensial kvant FIK η_d', min: .1, max: .9, step: .05, v: .5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Eg = P.Eg - 4.5e-4 * (P.T - 300), lam = 1239.84 / Eg, kT = Vt(P.T);
      const Es = lin(Eg - .1, Eg + .25, 200), spec = E => (E < Eg ? 0 : Math.sqrt(E - Eg) * Math.exp(-(E - Eg) / kT));
      const mx = Math.max(...Es.map(spec));
      const r = plot(c, [0, 0, w * .55, h], { xr: [lam - 80, lam + 50], yr: [0, 1.15], xl: 'λ, nm', yl: 'Nisbiy intensivlik', series: [{ pts: Es.map(E => [1239.84 / E, spec(E) / mx]), c: wl2rgb(lam), w: 3 }] });
      void r;
      const hv = Eg, Is = lin(0, 100, 200), Pout = I => (I < P.Ith ? .01 * I * hv : .01 * P.Ith * hv + P.eta * hv * (I - P.Ith));
      plot(c, [w * .56, 0, w * .44, h], { xr: [0, 100], yr: [0, Pout(100) * 1.1], xl: 'I, mA', yl: 'P, mVt (lazer)', series: [{ pts: Is.map(I => [I, Pout(I)]), c: C.rose, w: 2.5 }], vl: [{ x: P.Ith, l: 'I_th' }] });
      const color = lam < 450 ? 'binafsha/ko‘k' : lam < 495 ? 'ko‘k' : lam < 570 ? 'yashil' : lam < 590 ? 'sariq' : lam < 620 ? 'to‘q sariq' : lam < 750 ? 'qizil' : 'infraqizil';
      return { 'E_g(T), eV': fx(Eg), 'λ ≈ 1240/E_g, nm': fx(lam, 0), 'Rang': color, 'Spektr kengligi ≈ 1.8kT, meV': fx(1.8 * kT * 1e3, 1), 'Qiyalik dP/dI, Vt/A': fx(P.eta * hv, 2) };
    }
  };
  function wl2rgb(l) { let r = 0, g = 0, b = 0; if (l < 440) { r = (440 - l) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; } else if (l < 510) { g = 1; b = (510 - l) / 20; } else if (l < 580) { r = (l - 510) / 70; g = 1; } else if (l < 645) { r = 1; g = (645 - l) / 65; } else { r = 1; } if (l > 780) { r = .6; g = .2; b = .2; } return `rgb(${Math.round(r * 255)},${Math.round(g * 255)},${Math.round(b * 255)})`; }

  /* M14, A10, A11 — Zaryad aloqali asboblar (ZAA/CCD) */
  S.ccd = {
    title: 'ZAA: uch fazali zaryad uzatish',
    anim: true,
    params: [
      { k: 'cte', l: 'Uzatish samaradorligi CTE', min: .99, max: .99999, step: .00001, v: .9995 },
      { k: 'N', l: 'Uzatishlar soni N', min: 10, max: 3000, step: 10, v: 1024 },
      { k: 'speed', l: 'Animatsiya tezligi', min: .2, max: 3, step: .1, v: 1 }
    ],
    state: { t: 0 },
    draw(cv, P, dt = 0) {
      const { c, w, h } = ctx2d(cv); this.state.t += dt * P.speed;
      const cells = 12, gw = (w - 40) / cells, y0 = 24, dOn = h * .2, dOff = h * .06, phase = Math.floor(this.state.t * 2) % 3;
      c.font = '11px JetBrains Mono, monospace';
      for (let i = 0; i < cells; i++) {
        const x = 20 + i * gw, ph = i % 3, on = ph === phase;
        c.fillStyle = on ? '#2563eb' : '#1e293b'; c.fillRect(x + 2, y0, gw - 4, 14);
        c.fillStyle = C.text; c.textAlign = 'center'; c.fillText(`Φ${ph + 1}`, x + gw / 2, y0 - 6);
        const depth = on ? dOn : dOff; c.strokeStyle = on ? C.cyan : '#334155'; c.lineWidth = 2; c.strokeRect(x + 4, y0 + 18, gw - 8, depth);
      }
      const pos = (this.state.t * 2) % cells;
      for (let k = 0; k < 4; k++) { const idx = (Math.floor(pos) + k * 3) % cells; const x = 20 + idx * gw + gw / 2; const frac = P.cte ** (k * 3 + Math.floor(pos)); c.fillStyle = `rgba(52,211,153,${.35 + .6 * frac})`; c.beginPath(); c.arc(x, y0 + 18 + dOn * .6, Math.min(gw * .3, dOn * .35) * (.6 + .4 * frac), 0, 7); c.fill(); }
      const Ns = lin(0, P.N, 200);
      plot(c, [0, h * .34, w, h * .66], { xr: [0, P.N], yr: [0, 1.02], xl: 'Uzatishlar soni n', yl: 'Qolgan zaryad Q/Q₀ = CTEⁿ', series: [{ pts: Ns.map(n => [n, P.cte ** n]), c: C.green, w: 2.5 }], marks: [{ x: P.N, y: P.cte ** P.N, c: C.amber }] });
      return { 'Q_N/Q₀ = CTEᴺ': fx(P.cte ** P.N, 4), 'Yo‘qotish, %': fx((1 - P.cte ** P.N) * 100, 2), 'CTI = 1 − CTE': sci(1 - P.cte), 'Faol faza': `Φ${phase + 1}` };
    }
  };

  /* M15 — KMOP invertor va radiatsiya ta'siri */
  S.cmos = {
    title: 'KMOP invertor uzatish xarakteristikasi',
    params: [
      { k: 'Vdd', l: 'Manba V_DD, V', min: 1, max: 5, step: .1, v: 3.3 },
      { k: 'Vtn', l: 'V_Tn, V', min: .2, max: 1, step: .05, v: .5 },
      { k: 'Vtp', l: '|V_Tp|, V', min: .2, max: 1, step: .05, v: .5 },
      { k: 'r', l: 'k_n / k_p nisbati', min: .3, max: 4, step: .1, v: 1 },
      { k: 'D', l: 'Nurlanish dozasi, krad(Si)', min: 0, max: 300, step: 5, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), sh = .0012 * P.D, Vtn = P.Vtn - sh, Vtp = P.Vtp + sh, kn = P.r, kp = 1;
      const I = (k, vg, vd) => { if (vg <= 0) return 0; return vd < vg ? k * (vg * vd - vd * vd / 2) : .5 * k * vg * vg; };
      const vout = vin => { let lo = 0, hi = P.Vdd; for (let i = 0; i < 60; i++) { const m = (lo + hi) / 2; const d = I(kn, vin - Vtn, m) - I(kp, P.Vdd - vin - Vtp, P.Vdd - m); d > 0 ? hi = m : lo = m; } return (lo + hi) / 2; };
      const vins = lin(0, P.Vdd, 300), vo = vins.map(vout);
      const VM = (P.Vdd - Vtp + Vtn * Math.sqrt(kn / kp)) / (1 + Math.sqrt(kn / kp));
      let VIL = 0, VIH = P.Vdd; for (let i = 1; i < vins.length; i++) { const g = (vo[i] - vo[i - 1]) / (vins[i] - vins[i - 1]); if (g < -1 && VIL === 0) VIL = vins[i]; if (g < -1) VIH = vins[i]; }
      plot(c, [0, 0, w, h], { xr: [0, P.Vdd], yr: [0, P.Vdd * 1.05], xl: 'V_kir, V', yl: 'V_chiq, V', series: [{ pts: vins.map((v, i) => [v, vo[i]]), c: C.cyan, w: 2.5 }, { pts: [[0, 0], [P.Vdd, P.Vdd]], c: '#334155', dash: [4, 4] }], vl: [{ x: VM, l: 'V_M', c: C.green }] });
      return { 'V_M (o‘tish bo‘sag‘asi), V': fx(VM), 'V_IL / V_IH, V': `${fx(VIL, 2)} / ${fx(VIH, 2)}`, 'NM_L ≈ V_IL, V': fx(VIL, 2), 'NM_H ≈ V_DD − V_IH, V': fx(P.Vdd - VIH, 2), 'ΔV_T (nurlanish), V': fx(-sh) };
    }
  };

  /* A14, A15 — Bir jinsli bo'lmagan qatlam: qatlam qarshiligi */
  S.resist = {
    title: 'Diffuziyalangan qatlam: R_□ va ρ(x)',
    params: [
      { k: 'Ns', l: 'Sirt konsentratsiyasi N_s, sm⁻³', min: 17, max: 20.5, step: .1, v: 19.5, log: true },
      { k: 'Ld', l: 'Diffuziya uzunligi 2√(Dt), mkm', min: .2, max: 3, step: .05, v: 1 },
      { k: 'd', l: 'Olib tashlangan qatlam d, mkm', min: 0, max: 3, step: .05, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Nb = 1e15;
      const N = x => P.Ns * Math.exp(-((x / (P.Ld * 1e-4)) ** 2));
      const mu = n => 65 + 1265 / (1 + (n / 8.5e16) ** .72);
      const xj = P.Ld * 1e-4 * Math.sqrt(Math.log(P.Ns / Nb));
      const Rs = d0 => { let s = 0; const n = 400, dx = Math.max(xj - d0, 0) / n; for (let i = 0; i < n; i++) { const x = d0 + (i + .5) * dx; const nn = N(x) - Nb; if (nn > 0) s += q * mu(nn) * nn * dx; } return s ? 1 / s : Infinity; };
      const xs = lin(0, xj * 1e4 * 1.1, 200);
      plot(c, [0, 0, w * .5, h], { xr: [0, xj * 1e4 * 1.1], yr: [1e14, 1e21], logy: true, xl: 'x, mkm', yl: 'N(x), sm⁻³', series: [{ pts: xs.map(x => [x, N(x * 1e-4)]), c: C.cyan, w: 2.5 }], hl: [{ y: Nb, l: 'N_B (taglik)' }], vl: [{ x: xj * 1e4, l: 'x_j', c: C.rose }, { x: P.d, l: 'd', c: C.green }] });
      const ds = lin(0, xj * 1e4 * .95, 60);
      plot(c, [w * .51, 0, w * .49, h], { xr: [0, xj * 1e4], yr: [1, 1e6], logy: true, xl: 'd, mkm', yl: 'R_□(d), Ω/□', series: [{ pts: ds.map(d => [d, Rs(d * 1e-4)]), c: C.amber, w: 2.5 }], marks: [{ x: Math.min(P.d, xj * 1e4 * .95), y: Rs(Math.min(P.d, xj * 1e4 * .95) * 1e-4), c: C.green }] });
      const r0 = Rs(P.d * 1e-4), nd = N(P.d * 1e-4);
      return { 'x_j, mkm': fx(xj * 1e4), 'R_□(d), Ω/□': isFinite(r0) ? fx(r0, 1) : '∞', 'ρ(d) = 1/(qμN), Ω·sm': sci(1 / (q * mu(nd) * nd)), '4 zondli: V/I = R_□/4.532, Ω': isFinite(r0) ? fx(r0 / 4.532, 2) : '∞' };
    }
  };

  /* ---------- Simulyator konteynerini qurish ---------- */
  function build(box) {
    const key = box.dataset.sim, sim = S[key]; if (!sim) return;
    const id = `${key}-${Math.random().toString(36).slice(2, 7)}`;
    const ctrls = sim.params.map(p => {
      if (p.type === 'sel') return `<label class="control">${A(p.l)}<select data-k="${p.k}">${p.opts.map(o => `<option value="${o}"${o === p.v ? ' selected' : ''}>${A(o)}</option>`).join('')}</select></label>`;
      return `<label class="control">${A(p.l)} <output data-o="${p.k}"></output><input type="range" data-k="${p.k}" min="${p.min}" max="${p.max}" step="${p.step}" value="${p.v}"></label>`;
    }).join('');
    box.innerHTML = `<div class="sim-layout"><div class="card controls"><h3>${A(sim.title)}</h3>${ctrls}<div class="actions"><button class="secondary" type="button" data-reset>${A('Boshlang‘ich qiymatlar')}</button></div><div class="readout" aria-live="polite"></div></div><div class="card canvas-card"><div class="toolbar"><span>${A(sim.title)}</span><span class="stat notranslate">model · 300 K · Si</span></div><canvas id="${id}" role="img" aria-label="${A(sim.title)}"></canvas></div></div>`;
    const cv = box.querySelector('canvas'), ro = box.querySelector('.readout');
    const read = () => { const P = {}; box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); P[p.k] = p.type === 'sel' ? el.value : (p.log ? 10 ** +el.value : +el.value); const o = box.querySelector(`[data-o="${p.k}"]`); if (o) o.textContent = p.log ? sci(10 ** +el.value, 1) : (+el.value).toString(); }); return P; };
    const render = (dt) => { const r = sim.draw(cv, read(), dt || 0); ro.innerHTML = Object.entries(r || {}).map(([k, v]) => `<span>${A(k)}</span><b>${A(v)}</b>`).join(''); };
    box.addEventListener('input', () => render()); box.addEventListener('change', () => render());
    box.querySelector('[data-reset]').addEventListener('click', () => { box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); el.value = p.v; }); render(); });
    window.addEventListener('resize', () => render());
    render();
    if (sim.anim) { let last = performance.now(), vis = true; new IntersectionObserver(e => { vis = e[0].isIntersecting; }).observe(box); const loop = now => { if (vis) render(Math.min((now - last) / 1000, .1)); last = now; requestAnimationFrame(loop); }; requestAnimationFrame(loop); }
  }
  window.YAF_SIMS = S;
  const init = () => document.querySelectorAll('.sim-box[data-sim]').forEach(build);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
