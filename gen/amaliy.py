"""A1–A15 amaliy mashg'ulotlar mazmuni."""

A = []

A.append(dict(n=1, lec=10, sim="mosc", tn=["TN4", "TN13", "TN17"],
 title="Metall–dielektrik–yarimo‘tkazgich tuzilmalar. Sirt holatlari, sig‘im usullari",
 goal="MDYa strukturaning C–V xarakteristikasidan oksid qalinligi, taglik legirlanishi, tekis zonalar kuchlanishi, oksid zaryadi va sirt holatlari zichligini aniqlashni o‘rganish.",
 theory=r"""<p>Asosiy munosabatlar: \(C_{ox}=\varepsilon_{ox}/d_{ox}\); \(V_{FB}=\varphi_{ms}-Q_f/C_{ox}\); yuqori chastotali minimal sig‘im \(C_{min}=\left(\frac1{C_{ox}}+\frac{W_{max}}{\varepsilon_s}\right)^{-1}\), \(W_{max}=\sqrt{\frac{4\varepsilon_s\varphi_F}{qN_a}}\). Sirt holatlari zichligi past va yuqori chastotali egri chiziqlar farqidan:</p>
$$qD_{it}=\left(\frac{1}{C_{LF}}-\frac{1}{C_{ox}}\right)^{-1}-\left(\frac{1}{C_{HF}}-\frac{1}{C_{ox}}\right)^{-1}$$
<p>Harakatchan ionlar zaryadi “zo‘riqish ostida qizdirish” (BTS) sinovida \(V_{FB}\) siljishidan: \(N_m=C_{ox}\Delta V_{FB}/q\).</p>""",
 solved=[("Oksid qalinligi va qo‘zg‘almas zaryad", r"Zatvor yuzasi \(A=10^{-3}\) sm², akkumulyatsiyadagi sig‘im \(C_{max}=345\) pF, ideal \(V_{FB}=-0{,}9\) V, o‘lchangan \(V_{FB}=-1{,}2\) V. \(d_{ox}\) va \(Q_f/q\) ni toping.",
          r"\(C_{ox}=345\ \text{pF}/10^{-3}\ \text{sm}^2=3{,}45\cdot10^{-7}\) F/sm² ⇒ \(d_{ox}=3{,}45\cdot10^{-13}/3{,}45\cdot10^{-7}=10\) nm. \(\Delta V_{FB}=-0{,}3\) V ⇒ \(Q_f/q=0{,}3\cdot3{,}45\cdot10^{-7}/1{,}602\cdot10^{-19}\approx6{,}5\cdot10^{11}\) sm⁻² (musbat)."),
         ("Sirt holatlari zichligi", r"Biror \(V_G\) da \(C_{ox}=345\), \(C_{LF}=250\), \(C_{HF}=200\) nF/sm². \(D_{it}\) ni toping.",
          r"\((1/250-1/345)^{-1}=908\) nF/sm²; \((1/200-1/345)^{-1}=476\) nF/sm². \(qD_{it}=432\) nF/sm² ⇒ \(D_{it}=4{,}32\cdot10^{-7}/1{,}602\cdot10^{-19}\approx2{,}7\cdot10^{12}\) sm⁻²eV⁻¹ (sifati past chegara).")],
 tasks=[(r"\(d_{ox}=20\) nm SiO₂ uchun \(C_{ox}\) ni nF/sm² da toping.", "172,5 nF/sm²"),
        (r"BTS sinovida \(d_{ox}=50\) nm, \(\Delta V_{FB}=-0{,}15\) V. Harakatchan ionlar zichligi \(N_m\) = ?", r"\(C_{ox}=69\) nF/sm² ⇒ \(N_m\approx6{,}5\cdot10^{10}\) sm⁻²"),
        (r"p-Si, \(N_a=10^{16}\) sm⁻³ uchun \(\varphi_F\) va \(W_{max}\) ni toping (\(n_i=10^{10}\)).", r"\(\varphi_F=0{,}357\) V, \(W_{max}\approx0{,}30\) mkm"),
        (r"Simulyatorda \(N_a=10^{16}\), \(d_{ox}=50\) nm o‘rnatib \(C_{min}/C_{ox}\) ni o‘qing va qo‘lda hisob bilan solishtiring.", "≈ 0,2–0,25 (simulyator qiymati bilan tekshiriladi)")],
 model=("python", """import numpy as np
q, eps_s, eps_ox, kT = 1.602e-19, 11.7*8.854e-14, 3.9*8.854e-14, 0.02585
Na, dox, Vfb, ni = 1e17, 10e-7, -0.9, 1e10
Cox = eps_ox/dox; phiF = kT*np.log(Na/ni); gam = np.sqrt(2*q*eps_s*Na)/Cox
VT = Vfb + 2*phiF + gam*np.sqrt(2*phiF)
def C_hf(V):
    if V <= Vfb: return Cox
    if V >= VT:  ps = 2*phiF
    else:        ps = ((-gam + np.sqrt(gam**2 + 4*(V - Vfb)))/2)**2
    W = np.sqrt(2*eps_s*ps/(q*Na)); return 1/(1/Cox + W/eps_s)
for V in np.linspace(-3, 3, 13): print(f"{V:5.1f} V  C/Cox = {C_hf(V)/Cox:.3f}")
print("VT =", round(VT, 3), "V")"""),
 questions=["Nima uchun C–V o‘lchovi odatda 1 MGs da o‘tkaziladi?", "Qo‘zg‘almas va harakatchan oksid zaryadini qanday farqlash mumkin?", "Sirt holatlari C–V egri chizig‘iga qanday ta’sir qiladi?", "Poli-Si zatvorda \\(\\varphi_{ms}\\) qanday aniqlanadi?"]))

A.append(dict(n=2, lec=6, sim="bjt", tn=["TN3", "TN4", "TN13"],
 title="Tranzistorlarning ishlash tamoyillari",
 goal="Bipolyar tranzistor toklari, \\(\\alpha\\), \\(\\beta\\), emitter samaradorligi va Erli effektini masalalar orqali mustahkamlash.",
 theory=r"""<p>\(I_E=I_C+I_B\), \(I_C=\alpha I_E\), \(\beta=\alpha/(1-\alpha)\), \(\alpha=\beta/(\beta+1)\). Aktiv rejimda \(I_C=I_Se^{V_{BE}/V_T}(1+V_{CE}/V_A)\). Emitter samaradorligi va ko‘chish koeffitsiyenti: \(\gamma\approx\left(1+\frac{D_EN_BW_B}{D_BN_EW_E}\right)^{-1}\), \(\alpha_T\approx1-\frac{W_B^2}{2L_B^2}\).</p>""",
 solved=[("Toklar va koeffitsiyentlar", r"\(I_E=2\) mA, \(\alpha=0{,}98\). \(I_C\), \(I_B\), \(\beta\) ni toping.", r"\(I_C=1{,}96\) mA, \(I_B=40\) mkA, \(\beta=0{,}98/0{,}02=49\)."),
         ("Eksponensial bog‘liqlik va Erli effekti", r"\(I_S=10^{-15}\) A, \(V_{BE}=0{,}65\) V, \(V_A=100\) V, \(V_{CE}=5\) V, 300 K. \(I_C\) ni toping. \(V_{BE}\) 18 mV ga oshsa, tok necha marta ortadi?",
          r"\(I_C=10^{-15}e^{0{,}65/0{,}02585}(1+0{,}05)\approx8{,}3\cdot10^{-5}\cdot1{,}05\approx87\) mkA. \(e^{18/25{,}85}\approx2{,}0\) — har ≈ 18 mV da tok ikki marta, har ≈ 60 mV da 10 marta ortadi.")],
 tasks=[(r"\(\beta=200\) bo‘lsa, \(\alpha\) = ?", "0,995"),
        (r"\(I_C=1\) mA, \(I_B=8\) mkA. \(\beta\) va \(\alpha\) = ?", "β = 125, α = 0,992"),
        (r"\(N_E=5\cdot10^{18}\), \(N_B=5\cdot10^{16}\) sm⁻³, \(D_E=D_B/10\), \(W_E=W_B\). \(\gamma\) = ?", "γ ≈ 0,999"),
        (r"\(I_C=2\) mA, \(V_A=50\) V. \(r_o\) va \(g_m\) ni toping.", "r_o = 25 kΩ, g_m ≈ 77 mS")],
 model=("spice", """* BT chiqish xarakteristikalari (ngspice)
.model QN NPN(IS=1e-15 BF=150 VAF=80)
VCE c 0 DC 0
IB 0 b DC 10u
Q1 c b 0 QN
.dc VCE 0 12 0.05 IB 10u 60u 10u
.control
run
plot -i(VCE)
.endc
.end"""),
 questions=["Nima uchun baza toki kichik?", "Invers rejimda tranzistor qanday ishlaydi?", "Erli kuchlanishini grafikdan qanday aniqlaymiz?", "β ning harorat bilan o‘zgarishi qanday?"]))

A.append(dict(n=3, lec=6, sim="bjt", tn=["TN4", "TN14", "TN16"],
 title="Ikki qutbli tranzistorlarning kuchaytirish usullari",
 goal="UE, UB va UK ulanish sxemalarini solishtirish, kuchlanish bo‘luvchili siljitish sxemasida ishchi nuqtani tanlash va kichik signal kuchaytirishni hisoblash.",
 theory=r"""<p>Ulanish sxemalari xossalari:</p>""" + r"""<div class="tw"><table class="t"><thead><tr><th>Sxema</th><th>\(A_v\)</th><th>\(A_i\)</th><th>\(R_{kir}\)</th><th>\(R_{chiq}\)</th><th>Faza</th></tr></thead><tbody><tr><td>UE</td><td>\(-g_m(R_C\parallel R_L)\), katta</td><td>\(\beta\)</td><td>\(r_\pi\) (o‘rtacha)</td><td>\(R_C\)</td><td>180°</td></tr><tr><td>UB</td><td>\(g_m(R_C\parallel R_L)\), katta</td><td>\(\approx1\)</td><td>\(\approx1/g_m\) (kichik)</td><td>\(R_C\)</td><td>0°</td></tr><tr><td>UK (emitter takrorlagich)</td><td>\(\approx1\)</td><td>\(\beta+1\)</td><td>\(r_\pi+(\beta+1)R_E\) (katta)</td><td>\(\approx1/g_m\) (kichik)</td><td>0°</td></tr></tbody></table></div>
<p>Kuchlanish bo‘luvchili siljitish: \(V_{Th}=V_{CC}\frac{R_2}{R_1+R_2}\), \(R_{Th}=R_1\parallel R_2\), \(I_B=\dfrac{V_{Th}-V_{BE}}{R_{Th}+(\beta+1)R_E}\).</p>""",
 solved=[("Ishchi nuqtani hisoblash", r"\(V_{CC}=12\) V, \(R_1=47\) kΩ, \(R_2=10\) kΩ, \(R_C=2{,}2\) kΩ, \(R_E=1\) kΩ, \(\beta=150\), \(V_{BE}=0{,}65\) V. Q-nuqtani toping.",
          r"\(V_{Th}=2{,}105\) V, \(R_{Th}=8{,}25\) kΩ. \(I_B=1{,}455/(8{,}25+151)\ \text{k}\Omega=9{,}14\) mkA; \(I_C=1{,}37\) mA; \(V_{CE}=12-1{,}37\cdot2{,}2-1{,}38\cdot1\approx7{,}6\) V — aktiv rejim, Q-nuqta o‘rtaga yaqin."),
         ("Kuchaytirish koeffitsiyenti", r"Yuqoridagi sxemada \(R_E\) kondensator bilan shuntlangan, \(R_L=10\) kΩ. \(g_m\), \(r_\pi\), \(A_v\) = ?",
          r"\(g_m=1{,}37/25{,}85=53\) mS; \(r_\pi=150/0{,}053=2{,}83\) kΩ; \(A_v=-g_m(R_C\parallel R_L)=-0{,}053\cdot1803\approx-96\).")],
 tasks=[(r"Shuntlanmagan \(R_E=1\) kΩ bilan \(A_v\) ≈ ? (\(R_L=10\) kΩ)", r"\(A_v\approx-\frac{R_C\parallel R_L}{R_E+1/g_m}\approx-1{,}78\)"),
        (r"Emitter takrorlagich: \(g_m=40\) mS, \(R_E=1\) kΩ. \(A_v\) = ?", "≈ 0,976"),
        (r"\(\beta\) 150 dan 300 ga o‘zgarsa, misoldagi \(I_C\) qanchaga o‘zgaradi?", "≈ 1,37 → 1,41 mA (≈ 3 %) — bo‘luvchi va R_E barqarorlashtiradi"),
        ("UB sxemasining kirish qarshiligi \\(I_C=1\\) mA da qancha?", "≈ 1/g_m ≈ 26 Ω")],
 model=("spice", """* UE kuchaytirgich: .op va .ac
.model QN NPN(IS=1e-15 BF=150 VAF=80 CJC=2p CJE=10p TF=0.3n)
VCC vcc 0 12
VIN in 0 AC 1m
CIN in b 10u
R1 vcc b 47k
R2 b 0 10k
RC vcc c 2.2k
RE e 0 1k
CE e 0 100u
COUT c out 10u
RL out 0 10k
Q1 c b e QN
.control
op
print v(c) v(e) i(VCC)
ac dec 20 10 100meg
plot db(v(out)/v(in))
.endc
.end"""),
 questions=["Nima uchun UE sxema eng ko‘p ishlatiladi?", "R_E qanday teskari aloqa beradi?", "Emitter takrorlagich qayerda kerak?", "Q-nuqtani nima uchun o‘rtaga joylashtiramiz?"]))

A.append(dict(n=4, lec=7, sim="bjtfreq", tn=["TN4", "TN8", "TN15"],
 title="Quvvat bo‘yicha kuchaytirish. Tranzistorlarning chastota xususiyatlari",
 goal="Quvvat kuchaytirish koeffitsiyenti, kuchaytirgich sinflari FIKi, Miller effekti va yuqori chegaraviy chastotani hisoblash.",
 theory=r"""<p>\(A_p=A_vA_i\), \(G_p=10\lg A_p\) dB. A-sinf (rezistiv yuklama) maksimal FIK 25 %, transformatorli A-sinf 50 %, B-sinf push-pull \(\pi/4\approx78{,}5\) %. Yuqori chastota: \(C_M=C_\mu(1+g_mR_L')\), \(f_H\approx\dfrac{1}{2\pi R_s'(C_\pi+C_M)}\), \(R_s'=R_s\parallel r_\pi\). Issiqlik: \(T_j=T_a+P(R_{jc}+R_{cs}+R_{sa})\).</p>""",
 solved=[("Quvvat kuchaytirish", r"\(A_v=-100\), \(A_i=50\). \(A_p\) va \(G_p\) = ?", r"\(A_p=5000\), \(G_p=10\lg5000\approx37\) dB."),
         ("Miller effekti va \\(f_H\\)", r"\(C_\mu=2\) pF, \(C_\pi=10\) pF, \(g_m=40\) mS, \(R_L'=2\) kΩ, \(R_s'=1\) kΩ. \(C_M\) va \(f_H\) = ?",
          r"\(C_M=2(1+80)=162\) pF; \(f_H=1/(2\pi\cdot10^3\cdot172\cdot10^{-12})\approx925\) kGs — \(C_\mu\) kichik bo‘lsa ham polosani asosan u cheklaydi.")],
 tasks=[(r"B-sinf kuchaytirgich, \(V_{CC}=\pm15\) V, \(R_L=8\) Ω, maksimal chiqish quvvati?", r"\(P=V^2/(2R_L)\approx14\) Vt (to‘yinishni hisobga olmasdan)"),
        (r"\(\beta_0=100\), \(f_T=250\) MGs. \(f_\beta\) = ?", "2,5 MGs"),
        (r"Tranzistor \(P=20\) Vt, \(T_{j,max}=150\) °C, \(T_a=40\) °C, \(R_{jc}=1{,}5\), \(R_{cs}=0{,}5\) K/Vt. Radiatorning ruxsat etilgan \(R_{sa}\) = ?", "≤ 3,5 K/Vt"),
        ("Kaskod sxemasida Miller sig‘imi qancha bo‘ladi (UE tranzistor yuklamasi ≈ 1/g_m)?", "C_M ≈ 2C_μ")],
 model=("python", """import numpy as np
b0, fT = 150, 300e6
f = np.logspace(3, 10, 400)
beta = b0/np.sqrt(1 + (f*b0/fT)**2)
f_beta = fT/b0
print(f"f_beta = {f_beta/1e6:.2f} MHz, |beta(f_T)| = {b0/np.sqrt(1+b0**2):.3f}")
# Miller: C_M = C_mu*(1+gm*RL)
Cmu, Cpi, gm, RL, Rs = 2e-12, 10e-12, 0.04, 2e3, 1e3
fH = 1/(2*np.pi*Rs*(Cpi + Cmu*(1+gm*RL)))
print(f"f_H = {fH/1e3:.0f} kHz")"""),
 questions=["Nima uchun B-sinfda o‘tish buzilishlari paydo bo‘ladi?", "f_T va f_max qanday farq qiladi?", "Radiator issiqlik qarshiligi qanday tanlanadi?", "Miller effektini kamaytirish usullari?"]))

A.append(dict(n=5, lec=11, sim="mosfet", tn=["TN8", "TN15", "TN19"],
 title="MDYa tranzistorlarining teshilish hodisalari. Xarakteristikalarga issiqlik ta’siri",
 goal="Zatvor oksidining teshilishi, stok ko‘chkisi, o‘tib ketish (punch-through) hodisalarini va haroratning MOSFET parametrlariga ta’sirini hisoblash.",
 theory=r"""<p>Teshilish turlari: (1) zatvor oksidining teshilishi — \(E_{bd}\approx10\) MV/sm (SiO₂), \(V_{bd}\approx E_{bd}d_{ox}\); vaqtga bog‘liq teshilish (TDDB); (2) stok o‘tishining ko‘chkisimon teshilishi va parazit BT tufayli “snapback”; (3) o‘tib ketish — stok va istok kambag‘allashgan qatlamlari tutashadi. Haroratning ta’siri: \(\mu\propto T^{-1{,}5}\), \(dV_T/dT\approx-1\ldots-3\) mV/K. Shu sababli kichik \(V_{GS}\) da tok harorat bilan ortadi, katta \(V_{GS}\) da kamayadi; oraliqda harorat koeffitsiyenti nol nuqtasi (ZTC) bor.</p>""",
 solved=[("Oksid teshilishi", r"\(d_{ox}=5\) nm, \(E_{bd}=10\) MV/sm. \(V_{bd}\) = ? Ishonchlilik uchun maydon 5 MV/sm dan oshmasligi kerak bo‘lsa, maksimal \(V_{GS}\) = ?", r"\(V_{bd}=10^7\cdot5\cdot10^{-7}=5\) V; ruxsat etilgan \(V_{GS}\le2{,}5\) V."),
         ("Harorat ta’siri", r"\(k(300\,\text{K})=4\) mA/V², \(V_T(300)=0{,}7\) V, \(dV_T/dT=-2\) mV/K, \(\mu\propto T^{-1{,}5}\). \(V_{GS}=2{,}5\) V va 1,0 V da to‘yinish tokini 300 K va 400 K da toping.",
          r"\(k(400)=4\cdot(4/3)^{-1{,}5}=2{,}60\) mA/V², \(V_T(400)=0{,}5\) V. \(V_{GS}=2{,}5\): 6,48 → 5,20 mA (kamayadi). \(V_{GS}=1{,}0\): 0,18 → 0,325 mA (ortadi). ZTC nuqtasi ular orasida.")],
 tasks=[(r"Quvvat MOSFET: \(P=10\) Vt, \(R_{jc}=1{,}5\), \(R_{cs}=0{,}5\), \(R_{sa}=3\) K/Vt, \(T_a=25\) °C. \(T_j\) = ?", "75 °C"),
        (r"\(d_{ox}=2\) nm uchun \(V_{bd}\) (10 MV/sm) = ?", "2 V"),
        ("Simulyatorda \\(V_{GS}\\) ni o‘zgartirib, 300 va 400 K da tok deyarli teng bo‘ladigan \\(V_{GS}\\) ni toping.", "≈ 1,6–1,8 V (model parametrlariga bog‘liq)"),
        ("Nima uchun quvvat MOSFETlarni parallel ulash BTlarga qaraganda xavfsizroq (katta \\(V_{GS}\\) da)?", "Tok harorat bilan kamayadi — issiq nuqtaga tok to‘planmaydi")],
 model=("python", """import numpy as np
def Id(Vgs, T, k300=4e-3, Vt300=0.7):
    k = k300*(T/300)**-1.5; Vt = Vt300 - 2e-3*(T-300)
    return 0.5*k*max(Vgs-Vt, 0)**2
for Vgs in np.arange(0.8, 3.01, 0.2):
    print(f"Vgs={Vgs:.1f}  Id300={Id(Vgs,300)*1e3:6.2f} mA  Id400={Id(Vgs,400)*1e3:6.2f} mA")"""),
 questions=["TDDB nima va u qanday baholanadi?", "Snapback qaysi parazit struktura bilan bog‘liq?", "ZTC nuqtasi analog sxemalarda qanday ishlatiladi?", "Issiqlik qochishi (thermal runaway) MOSFETda bo‘ladimi?"]))

A.append(dict(n=6, lec=10, sim="mosfet", tn=["TN3", "TN4", "TN13"],
 title="MDYa tranzistorlar xarakteristikalariga yarimo‘tkazgich sirtining ta’siri. MDYa tranzistorlar turlari",
 goal="Sirt holatlari, sirt sochilishi va oksid zaryadining harakatchanlik, bo‘sag‘a kuchlanishi va subbo‘sag‘a qiyalikka ta’sirini hisoblash; MDYa tranzistorlar turlarini tasniflash.",
 theory=r"""<p>Effektiv harakatchanlik vertikal maydon ortishi bilan kamayadi: \(\mu_{eff}=\dfrac{\mu_0}{1+\theta(V_{GS}-V_T)}\). Sirt holatlari subbo‘sag‘a qiyalikni oshiradi: \(S=\ln10\frac{kT}{q}\left(1+\frac{C_d+qD_{it}}{C_{ox}}\right)\). To‘rt tur: n-kanal boyitish (\(V_T>0\)), n-kanal kambag‘allashtirish (\(V_T<0\)), p-kanal boyitish (\(V_T<0\)), p-kanal kambag‘allashtirish (\(V_T>0\)).</p>""",
 solved=[("Harakatchanlik degradatsiyasi", r"\(\mu_0=600\) sm²/(V·s), \(\theta=0{,}2\) V⁻¹, \(V_{GS}-V_T=2\) V. \(\mu_{eff}\) = ?", r"\(\mu_{eff}=600/1{,}4\approx429\) sm²/(V·s)."),
         ("Sirt holatlarining S ga ta’siri", r"\(C_{ox}=345\) nF/sm², \(C_d=100\) nF/sm², \(D_{it}=10^{11}\) sm⁻²eV⁻¹, 300 K. S = ?",
          r"\(qD_{it}=16\) nF/sm². \(S=59{,}5(1+116/345)\approx79{,}5\) mV/dek. \(D_{it}=0\) da 76,7 mV/dek.")],
 tasks=[(r"\(D_{it}=10^{12}\) sm⁻²eV⁻¹ bo‘lsa, yuqoridagi misolda S = ?", "≈ 104 mV/dek"),
        ("Qaysi MDYa turi “normal-ochiq”?", "kambag‘allashtirish (qurilgan kanalli)"),
        (r"\(\theta=0{,}5\) V⁻¹ da \(V_{ov}=1\) V va 3 V uchun \(\mu_{eff}/\mu_0\) = ?", "0,67 va 0,4"),
        ("Belgilarda boyitish va kambag‘allashtirish turlari qanday farqlanadi?", "uzuq/uzluksiz kanal chizig‘i")],
 model=("python", """import numpy as np
kT = 0.02585; q = 1.602e-19
Cox, Cd = 345e-9, 100e-9
for Dit in [0, 1e10, 1e11, 1e12]:
    S = np.log(10)*kT*(1 + (Cd + q*Dit)/Cox)*1e3
    print(f"Dit={Dit:.0e} cm^-2 eV^-1  ->  S = {S:.1f} mV/dec")"""),
 questions=["Sirt sochilishi nima uchun kuchli maydonda ortadi?", "Kuchlangan kremniy harakatchanlikni qanday oshiradi?", "Sirt holatlari qayerdan paydo bo‘ladi (uzilgan bog‘lar)?", "Vodorodli qizdirish (forming gas anneal) nima beradi?"]))

A.append(dict(n=7, lec=11, sim="mosfet", tn=["TN7", "TN15", "TN18", "TN19"],
 title="MDYa tranzistorlari to‘g‘risida umumiy ma’lumot. Yuqori quvvatli MDYa tranzistorlari",
 goal="Quvvat MOSFETning datasheet parametrlari (\\(R_{DS(on)}\\), \\(Q_g\\), SOA) asosida o‘tkazish va kalitlash yo‘qotishlarini hisoblash hamda vazifaga mos tranzistor tanlash.",
 theory=r"""<p>Yo‘qotishlar: o‘tkazish \(P_{cond}=I_{rms}^2R_{DS(on)}(T_j)\) (\(R_{DS(on)}\) 125 °C da odatda 1,5–1,8 marta katta); kalitlash \(P_{sw}\approx\frac12V_{DS}I_D(t_r+t_f)f_{sw}\); boshqaruv \(P_{drv}=Q_gV_{GS}f_{sw}\). Unipolyar chegarada \(R_{on,sp}\propto V_{BR}^{2{,}5}\) — shuning uchun 600 V dan yuqorida super-junction MOSFET, IGBT, SiC va GaN asboblar ustun.</p>""",
 solved=[("Yo‘qotishlar balansi", r"Pasaytiruvchi o‘zgartkich: \(V=48\) V, \(I=10\) A, \(R_{DS(on)}(25\,°C)=20\) mΩ (125 °C da ×1,6), \(t_r+t_f=40\) ns, \(f=100\) kGs, \(Q_g=30\) nC, \(V_{GS}=10\) V. To‘ldirish koeffitsiyenti 0,5.",
          r"\(I_{rms}^2=0{,}5\cdot100=50\) A² ⇒ \(P_{cond}=50\cdot0{,}032=1{,}6\) Vt. \(P_{sw}=0{,}5\cdot48\cdot10\cdot40\cdot10^{-9}\cdot10^5=0{,}96\) Vt. \(P_{drv}=30\cdot10^{-9}\cdot10\cdot10^5=30\) mVt. Jami ≈ 2,6 Vt.")],
 tasks=[(r"Yuqoridagi tranzistor uchun \(R_{jc}=1\) K/Vt, \(T_j\le110\) °C, \(T_a=40\) °C. Radiator \(R_{cs}+R_{sa}\) ≤ ?", "≈ 26 K/Vt"),
        ("Kalitlash chastotasi 2 marta oshsa, qaysi yo‘qotishlar o‘zgaradi?", "P_sw va P_drv 2 marta ortadi; P_cond o‘zgarmaydi"),
        ("600 V, 20 A kalit uchun Si MOSFET, IGBT, SiC MOSFET ni solishtiring.", "Javob: jadval ko‘rinishida (R_on, tezlik, narx)"),
        ("Datasheet’da SOA grafigidagi to‘rt chegara chizig‘ini sanang.", "R_DS(on), I_D,max, P_max (issiqlik), V_DS,max")],
 model=("python", """V, I, D = 48, 10, 0.5
Ron25, k125 = 0.020, 1.6
tr_tf, f, Qg, Vgs = 40e-9, 100e3, 30e-9, 10
Pc = D*I**2*Ron25*k125
Ps = 0.5*V*I*tr_tf*f
Pd = Qg*Vgs*f
print(f"P_cond={Pc:.2f} W, P_sw={Ps:.2f} W, P_drv={Pd*1e3:.0f} mW, jami={Pc+Ps+Pd:.2f} W")"""),
 questions=["Nima uchun quvvat MOSFET ichida teskari diod bor?", "Q_g egri chizig‘idagi Miller platosi nima?", "Avalanche energiyasi (E_AS) nima?", "GaN HEMT ning afzalliklari?"]))

A.append(dict(n=8, lec=9, sim="jfet", tn=["TN3", "TN4", "TN13"],
 title="Ajratilgan boshqaruvchi elektrodli va p-n o‘tishli maydon tranzistorlari: ishlash tamoyillari va turlari",
 goal="JFET va MDYa tranzistorlarni tuzilishi, ishlash prinsipi va parametrlari bo‘yicha solishtirish; JFET turlarini va berkilish kuchlanishini hisoblashni o‘rganish.",
 theory=r"""<p>JFET: kanal p-n o‘tish kambag‘allashgan qatlami bilan toraytiriladi (n- va p-kanalli; GaAs MESFET — Shottki zatvorli turi). Ajratilgan (izolyatsiyalangan) zatvorli MT: kanal oksid orqali maydon bilan boshqariladi. Ichki berkilish kuchlanishi \(V_{P0}=qN_da^2/(2\varepsilon_s)\), \(|V_P|=V_{P0}-V_{bi}\).</p>""",
 solved=[("Berkilish kuchlanishi", r"n-kanal: \(N_d=5\cdot10^{15}\) sm⁻³, \(a=1{,}5\) mkm, \(V_{bi}=0{,}8\) V. \(V_P\) = ?", r"\(V_{P0}=\frac{1{,}602\cdot10^{-19}\cdot5\cdot10^{15}\cdot2{,}25\cdot10^{-8}}{2\cdot1{,}036\cdot10^{-12}}\approx8{,}7\) V ⇒ \(V_P\approx-7{,}9\) V."),
         ("JFET va MOSFET taqqoslash", "Kirish qarshiligi, shovqin, kalit sifatida ishlash va integratsiya bo‘yicha solishtiring.", "JFET: \\(R_{kir}\\sim10^{9}\\)–\\(10^{12}\\) Ω, past 1/f shovqin, normal-ochiq. MOSFET: \\(R_{kir}>10^{14}\\) Ω, boyitish turida normal-yopiq, KMOP integratsiyasi uchun qulay, lekin 1/f shovqin yuqoriroq.")],
 tasks=[(r"\(a\) 2 marta kamaysa, \(V_{P0}\) qanday o‘zgaradi?", "4 marta kamayadi"),
        (r"p-kanal JFETda \(V_P\) va \(V_{GS}\) ishoralari qanday?", "V_P > 0, 0 ≤ V_GS ≤ V_P"),
        (r"\(N_d=10^{16}\), \(|V_P|=3\) V, \(V_{bi}=0{,}8\) V talab qilinsa, \(a\) = ?", "≈ 0,70 mkm"),
        ("MESFET nima uchun GaAs da, Si da emas, keng tarqalgan?", "GaAs da sifatli oksid yo‘q va harakatchanlik yuqori")],
 model=("python", """q, eps = 1.602e-19, 1.036e-12
def Vp(Nd, a_um, Vbi=0.8):
    Vp0 = q*Nd*(a_um*1e-4)**2/(2*eps); return Vp0, -(Vp0 - Vbi)
for a in [0.5, 1.0, 1.5]:
    print(a, "um ->", [round(x, 2) for x in Vp(5e15, a)])"""),
 questions=["Nima uchun JFET zatvori to‘g‘ri yo‘nalishda siljitilmaydi?", "MESFET va HEMT farqi?", "Kambag‘allashtirish MOSFET va JFET o‘xshashligi?", "JFET qaysi datchiklarda ishlatiladi?"]))

A.append(dict(n=9, lec=9, sim="jfet", tn=["TN4", "TN14", "TN19"],
 title="Boshqariluvchi p-n o‘tishli maydon tranzistorlari xarakteristikasining asosiy hisobi",
 goal="Shokli tenglamasi asosida avtosiljitish sxemasida ishchi nuqtani, tiklikni va kuchaytirishni hisoblash.",
 theory=r"""<p>\(I_D=I_{DSS}(1-V_{GS}/V_P)^2\); avtosiljitishda \(V_{GS}=-I_DR_S\). Kvadrat tenglamaning \(|V_{GS}|<|V_P|\) shartini qanoatlantiruvchi ildizi olinadi. \(g_m=\frac{2I_{DSS}}{|V_P|}(1-V_{GS}/V_P)\), UI kaskad: \(A_v=-g_m(R_D\parallel r_d)\).</p>""",
 solved=[("Avtosiljitish", r"\(I_{DSS}=10\) mA, \(V_P=-4\) V, \(R_S=500\) Ω. \(I_D\), \(V_{GS}\), \(g_m\) = ?",
          r"\(I_D=10(1-0{,}125I_D)^2\) (mA) ⇒ \(0{,}15625I_D^2-3{,}5I_D+10=0\) ⇒ \(I_D=3{,}36\) mA (ikkinchi ildiz 19 mA > \(I_{DSS}\) — tashlanadi). \(V_{GS}=-1{,}68\) V, \(g_m=5(1-0{,}42)=2{,}9\) mS."),
         ("Kuchaytirish", r"Yuqoridagi sxemada \(R_D=2{,}2\) kΩ, \(r_d=50\) kΩ, \(R_S\) shuntlangan. \(A_v\) = ?", r"\(A_v=-2{,}9\cdot(2{,}2\parallel50)=-2{,}9\cdot2{,}11\approx-6{,}1\).")],
 tasks=[(r"\(I_D=2\) mA kerak (\(I_{DSS}=10\) mA, \(V_P=-4\) V). \(V_{GS}\) va \(R_S\) = ?", "V_GS = −2,21 V, R_S ≈ 1,1 kΩ"),
        (r"\(V_{GS}=0\) da \(g_{m0}\) = ?", "5 mS"),
        (r"\(V_{DD}=15\) V, \(I_D=3{,}36\) mA, \(R_D=2{,}2\) kΩ, \(R_S=0{,}5\) kΩ. \(V_{DS}\) va rejim?", "V_DS ≈ 5,9 V > V_GS − V_P = 2,32 V ⇒ to‘yinish"),
        ("JFETni tok stabilizatori sifatida ulash sxemasini chizing.", "zatvor istokka ulangan: I = I_DSS")],
 model=("python", """import numpy as np
Idss, Vp, Rs = 10e-3, -4.0, 500.0
# I = Idss*(1 + I*Rs/Vp)**2  ->  kvadrat tenglama
a = Idss*(Rs/Vp)**2; b = 2*Idss*Rs/Vp - 1; c = Idss
roots = np.roots([a, b, c]); I = min(r.real for r in roots if 0 < r.real < Idss)
Vgs = -I*Rs; gm = 2*Idss/abs(Vp)*(1 - Vgs/Vp)
print(f"I_D={I*1e3:.2f} mA, V_GS={Vgs:.2f} V, gm={gm*1e3:.2f} mS")"""),
 questions=["Nima uchun ikkinchi ildiz fizik emas?", "Avtosiljitishning afzalligi?", "I_DSS tarqalishi Q-nuqtaga qanday ta’sir qiladi?", "r_d qanday o‘lchanadi?"]))

A.append(dict(n=10, lec=14, sim="ccd", tn=["TN4", "TN9", "TN17"],
 title="Zaryad bog‘langan asboblarning (ZBA) ishlash tamoyili. ZBA ning ish rejimlari",
 goal="Chuqur kambag‘allashish rejimida potensial chuqurlikni, saqlanadigan zaryadni va ZBA ish rejimlari (to‘plash, uzatish, o‘qish) vaqtlarini hisoblash.",
 theory=r"""<p>Chuqur kambag‘allashishda (inversion qatlam hali shakllanmagan) sirt potensiali:</p>
$$\psi_s=V_G-V_{FB}+V_0-\sqrt{V_0^2+2V_0(V_G-V_{FB})},\qquad V_0=\frac{q\varepsilon_sN_a}{C_{ox}^2}$$
<p>Zaryad \(Q_{sig}\) to‘planganda chuqur sayozlashadi: \(\psi_s\) ifodasida \(V_G\) o‘rniga \(V_G-Q_{sig}/C_{ox}\). Ish rejimlari: <b>to‘plash (integratsiya)</b> — fotozaryad yig‘iladi; <b>uzatish</b> — taktlash bilan chiqish registriga siljitiladi; <b>o‘qish</b> — chiqish tuguni sig‘imida kuchlanishga aylantiriladi (\(\Delta V=Q/C_{node}\)).</p>""",
 solved=[("Potensial chuqurlik", r"\(N_a=10^{15}\) sm⁻³, \(d_{ox}=100\) nm, \(V_{FB}=0\), \(V_G=10\) V. \(V_0\) va \(\psi_s\) = ?",
          r"\(C_{ox}=34{,}5\) nF/sm²; \(V_0=1{,}602\cdot10^{-19}\cdot1{,}036\cdot10^{-12}\cdot10^{15}/(3{,}45\cdot10^{-8})^2\approx0{,}14\) V. \(\psi_s=10+0{,}14-\sqrt{0{,}0195+2{,}79}\approx8{,}46\) V — kuchlanishning ko‘p qismi yarimo‘tkazgichga tushadi."),
         ("Kadr o‘qish vaqti", r"1024×1024 matritsa, piksel o‘qish chastotasi 10 MGs, bitta chiqish. Kadr o‘qish vaqti va maksimal kadr chastotasi?", r"\(t=1{,}05\cdot10^6/10^7\approx0{,}105\) s ⇒ ≈ 9,5 kadr/s. To‘rt chiqish bilan ≈ 38 kadr/s.")],
 tasks=[(r"Chiqish tuguni sig‘imi \(C=10\) fF. 1000 elektron qanday \(\Delta V\) beradi?", "≈ 16 mV (konversiya ≈ 16 mkV/e⁻)"),
        (r"\(V_G=5\) V (boshqa shartlar misoldagidek) da \(\psi_s\) = ?", "≈ 3,96 V"),
        ("Uch fazali ZBA da 512 pikselni uzatish uchun nechta takt fazasi almashinadi?", "512 × 3 = 1536"),
        ("Integratsiya vaqtida qaysi zatvor kuchlanishi yuqori bo‘ladi?", "piksel markazidagi (yig‘uvchi) faza")],
 model=("python", """import numpy as np
q, eps_s, eps_ox = 1.602e-19, 1.036e-12, 3.45e-13
Na, dox, Vfb = 1e15, 100e-7, 0.0
Cox = eps_ox/dox; V0 = q*eps_s*Na/Cox**2
for Vg in [2, 5, 10, 15]:
    ps = Vg - Vfb + V0 - np.sqrt(V0**2 + 2*V0*(Vg - Vfb))
    print(f"Vg={Vg:4.1f} V  psi_s={ps:6.2f} V")"""),
 questions=["Chuqur kambag‘allashish qancha vaqt saqlanadi?", "Nima uchun ZBA ni sovutish kerak?", "Kadr uzatishli ZBA da mexanik zatvor nima uchun shart emas?", "Korrelyatsiyalangan ikki karrali tanlash (CDS) nimani kamaytiradi?"]))

A.append(dict(n=11, lec=14, sim="ccd", tn=["TN8", "TN9", "TN17"],
 title="Zaryadlar yo‘qolishi mexanizmlari. ZBA asosidagi turli integral sxemalar",
 goal="To‘liq uzatilmaslik, sirt tutqichlari va qorong‘i tok bo‘yicha zaryad yo‘qotishlarini miqdoriy baholash; ZBA asosidagi IS (kechikish liniyalari, transversal filtrlar, xotira, tasvir sensorlari) ni tahlil qilish.",
 theory=r"""<p>Yo‘qotish manbalari: (1) issiqlik diffuziyasi bilan uzatishning so‘nggi bosqichi — vaqt doimiysi \(\tau_{th}=\dfrac{4L^2}{\pi^2D}\); chekka maydonlar uni tezlashtiradi; (2) sirt (yoki hajmiy) tutqichlar — zaryad ushlanib keyingi paketlarga “dum” beradi; (3) qorong‘i tok \(Q_d=J_dA\,t_{int}\); (4) to‘lib toshish (blooming). ZBA asosidagi IS: analog kechikish liniyalari \(t_d=N/f_{clk}\), transversal (FIR) filtrlar, ketma-ket xotira, chiziqli va matritsali tasvir sensorlari.</p>""",
 solved=[("Diffuzion uzatish chegarasi", r"Elektrod uzunligi \(L=10\) mkm, \(D=10\) sm²/s, uzatishga ajratilgan vaqt 200 ns. Faqat diffuziya hisobga olinsa, qolgan ulush va CTE?",
          r"\(\tau_{th}=4\cdot10^{-6}/(9{,}87\cdot10)\approx40\) ns; qolgan ulush \(e^{-200/40}\approx6{,}7\cdot10^{-3}\) ⇒ CTE ≈ 0,9933. Chekka maydonlar va hajmiy kanal tufayli real CTE ancha yuqori."),
         ("Qorong‘i tok zaryadi", r"\(J_d=1\) nA/sm², piksel \(10\times10\) mkm², integratsiya 10 s. Elektronlar soni?", r"\(Q=10^{-9}\cdot10^{-6}\cdot10=10^{-14}\) Kl ≈ \(6{,}2\cdot10^4\) e⁻ — sovutish zarur.")],
 tasks=[(r"\(L=5\) mkm bo‘lsa (boshqa shartlar o‘zgarmagan), \(\tau_{th}\) = ?", "≈ 10 ns"),
        (r"256 bosqichli ZBA kechikish liniyasi, \(f_{clk}=1\) MGs. Kechikish = ?", "256 mks"),
        (r"Qorong‘i tok har 7 K sovutishda ikki marta kamayadi. +20 °C dan −50 °C ga sovutilsa?", "2¹⁰ ≈ 1000 marta"),
        ("Blooming ga qarshi chiqarib yuboruvchi drenaj (anti-blooming) qanday ishlaydi?", "ortiqcha zaryad yon drenajga oqizilib yuboriladi")],
 model=("python", """import numpy as np
L, D = 10e-4, 10.0
tau = 4*L**2/(np.pi**2*D)
for t in [50e-9, 100e-9, 200e-9, 400e-9]:
    print(f"t={t*1e9:4.0f} ns  qolgan ulush={np.exp(-t/tau):.2e}  CTE={1-np.exp(-t/tau):.5f}")"""),
 questions=["Sirt va hajmiy kanalli ZBA da tutqichlar ta’siri qanday farq qiladi?", "“Fat zero” nima va u nima uchun ishlatilgan?", "ZBA transversal filtri qanday ishlaydi?", "Radiatsiya CTE ni nima uchun yomonlashtiradi?"]))

A.append(dict(n=12, lec=3, sim="pn", tn=["TN4", "TN13", "TN17"],
 title="Elektr maydonida to‘siq sig‘imini hisoblash uchun asosiy tenglama",
 goal="Puasson tenglamasidan keskin va chiziqli o‘tishlar uchun to‘siq sig‘imi formulalarini keltirib chiqarish va kuchlanishga bog‘liqligini hisoblash.",
 theory=r"""<p>Umumiy ta’rif — differensial sig‘im: \(C=\dfrac{dQ}{dV}=\dfrac{\varepsilon_sA}{W}\). Keskin o‘tish: \(W=\sqrt{\dfrac{2\varepsilon_s(V_{bi}-V)}{qN_{eff}}}\), \(N_{eff}=\dfrac{N_aN_d}{N_a+N_d}\) ⇒ \(C\propto(V_{bi}-V)^{-1/2}\). Chiziqli o‘tish (gradiyent \(a\), sm⁻⁴): \(W=\left(\dfrac{12\varepsilon_s(V_{bi}-V)}{qa}\right)^{1/3}\) ⇒ \(C\propto(V_{bi}-V)^{-1/3}\). Umumiy holda \(C\propto(V_{bi}-V)^{-m}\).</p>""",
 solved=[("Keskin p⁺-n o‘tish sig‘imi", r"\(N_d=10^{16}\) sm⁻³, \(A=10^{-3}\) sm², \(V_{bi}=0{,}8\) V, \(V=-5\) V. \(W\) va \(C\) = ?",
          r"\(W=\sqrt{2\cdot1{,}036\cdot10^{-12}\cdot5{,}8/(1{,}602\cdot10^{-19}\cdot10^{16})}\approx0{,}87\) mkm; \(C=1{,}036\cdot10^{-12}\cdot10^{-3}/8{,}66\cdot10^{-5}\approx12{,}0\) pF."),
         ("Chiziqli o‘tish", r"\(a=10^{20}\) sm⁻⁴, \(V_{bi}-V=5\) V, \(A=10^{-3}\) sm². \(W\), \(C\) = ?",
          r"\(W=(12\cdot1{,}036\cdot10^{-12}\cdot5/(1{,}602\cdot10^{-19}\cdot10^{20}))^{1/3}=(3{,}88\cdot10^{-12})^{1/3}\approx1{,}57\cdot10^{-4}\) sm; \(C\approx6{,}6\) pF.")],
 tasks=[(r"Misol 1 da \(V=0\) bo‘lsa, C = ?", "≈ 32 pF"),
        (r"Keskin o‘tishda teskari kuchlanish 0 dan −8 V ga o‘zgarsa (\(V_{bi}=0{,}8\) V), sig‘im necha marta kamayadi?", "√11 ≈ 3,3 marta"),
        ("Varikapning sozlash koeffitsiyenti \\(C_{max}/C_{min}\\) ni oshirish uchun qanday profil kerak?", "giperkeskin (m > 1/2)"),
        ("Simulyatorda \\(V\\) ni o‘zgartirib, \\(C_j\\) ning \\((V_{bi}-V)^{-1/2}\\) qonuniyatini 3 nuqtada tekshiring.", "C·√(V_bi − V) ≈ const")],
 model=("python", """import numpy as np
q, eps, A = 1.602e-19, 1.036e-12, 1e-3
Nd, Vbi = 1e16, 0.8
for V in [0, -1, -2, -5, -10]:
    W = np.sqrt(2*eps*(Vbi - V)/(q*Nd)); C = eps*A/W
    print(f"V={V:4} V  W={W*1e4:.3f} um  C={C*1e12:6.2f} pF  1/C^2={1/C**2:.3e} F^-2")"""),
 questions=["To‘siq sig‘imi va diffuzion sig‘im qachon teng bo‘ladi?", "Nima uchun to‘g‘ri kuchlanishda C–V o‘lchovi noaniq?", "Chiziqli o‘tish qaysi texnologiyada hosil bo‘ladi?", "Sig‘imning harorat bog‘liqligi qayerdan?"]))

A.append(dict(n=13, lec=3, sim="pn", tn=["TN4", "TN10", "TN13", "TN17"],
 title="P-n o‘tishda kirishmalar konsentratsiyasini va elektr maydonini aniqlash",
 goal="\\(1/C^2-V\\) grafigidan kirishma konsentratsiyasi va profilini, kontakt potensiallar farqini hamda maksimal maydonni aniqlash.",
 theory=r"""<p>Bir tomonlama o‘tish uchun \(\dfrac{1}{C^2}=\dfrac{2(V_{bi}-V)}{q\varepsilon_sN_dA^2}\). Chiziq qiyaligi \(N_d\) ni, absissa bilan kesishishi \(V_{bi}\) ni beradi. Notekis profil uchun (chuqurlik \(x=\varepsilon_sA/C\)):</p>
$$N(x)=\frac{2}{q\varepsilon_sA^2}\left[\frac{d(1/C^2)}{dV}\right]^{-1}$$
<p>Maksimal maydon: \(E_{max}=\sqrt{\dfrac{2qN_d(V_{bi}-V)}{\varepsilon_s}}=\dfrac{2(V_{bi}-V)}{W}\).</p>""",
 solved=[("Konsentratsiyani qiyalikdan topish", r"\(A=10^{-3}\) sm² bo‘lgan p⁺-n diod uchun \(|d(1/C^2)/dV|=1{,}205\cdot10^{21}\) F⁻²V⁻¹, chiziq \(V=0{,}8\) V da absissani kesadi. \(N_d\), \(V_{bi}\) = ?",
          r"\(N_d=\dfrac{2}{1{,}602\cdot10^{-19}\cdot1{,}036\cdot10^{-12}\cdot10^{-6}\cdot1{,}205\cdot10^{21}}\approx1{,}0\cdot10^{16}\) sm⁻³; \(V_{bi}=0{,}8\) V."),
         ("Maksimal maydon", r"Shu diodda \(V=-5\) V. \(E_{max}\) = ?", r"\(E_{max}=\sqrt{2\cdot1{,}602\cdot10^{-19}\cdot10^{16}\cdot5{,}8/1{,}036\cdot10^{-12}}\approx1{,}34\cdot10^5\) V/sm — Si teshilish maydonidan (~3·10⁵) kichik.")],
 tasks=[(r"\(V=-1\) V da C = 25 pF, \(V=-3\) V da C = 17 pF (\(A=10^{-3}\) sm²). \(N_d\) = ?", r"≈ \(1{,}3\cdot10^{16}\) sm⁻³ (qiyalikdan)"),
        (r"Shu o‘lchovlar uchun profil chuqurligi \(x=\varepsilon_sA/C\) = ?", "0,41 va 0,61 mkm"),
        (r"\(N_d=10^{15}\) sm⁻³, \(E_{cr}=3\cdot10^5\) V/sm. Teshilish kuchlanishi \(V_{BR}\approx\varepsilon_sE_{cr}^2/(2qN_d)\) = ?", "≈ 291 V"),
        ("Simulyatorda \\(N_d\\) ni 10 marta oshirib, \\(E_{max}\\) va \\(W\\) qanday o‘zgarishini tekshiring.", "E_max ≈ √10 marta ortadi, W ≈ √10 marta kamayadi")],
 model=("python", """import numpy as np
q, eps, A = 1.602e-19, 1.036e-12, 1e-3
V = np.array([-1, -3]); C = np.array([25e-12, 17e-12])
slope = np.diff(1/C**2)/np.diff(V)
Nd = 2/(q*eps*A**2*abs(slope[0]))
x = eps*A/C
print(f"N_d = {Nd:.2e} cm^-3, x = {x*1e4} um")"""),
 questions=["Ketma-ket qarshilik C–V o‘lchoviga qanday ta’sir qiladi?", "Debay uzunligi profil aniqligini qanday cheklaydi?", "Chuqur sathlar C–V ga qanday ta’sir qiladi?", "Elektrokimyoviy C–V (ECV) usuli nima?"]))

A.append(dict(n=14, lec=1, sim="resist", tn=["TN4", "TN5", "TN10", "TN13"],
 title="Bir jinsli bo‘lmagan qalinlik bo‘ylab qarshilikni o‘rganish",
 goal="Diffuziyalangan yoki implantatsiyalangan notekis qatlamning qatlam (varaq) qarshiligini, o‘rtacha solishtirma qarshiligini va to‘rt zondli o‘lchov natijalarini hisoblash.",
 theory=r"""<p>Notekis legirlangan qatlam uchun qatlam qarshiligi:</p>
$$R_\square=\left[q\int_0^{x_j}\mu(N(x))\,N(x)\,dx\right]^{-1},\qquad \bar\rho=R_\square\,x_j$$
<p>To‘rt zondli usul (yupqa qatlam, katta namuna): \(R_\square=\dfrac{\pi}{\ln2}\dfrac{V}{I}\approx4{,}532\dfrac{V}{I}\); qalin namuna uchun \(\rho=2\pi s\dfrac{V}{I}\) (\(s\) — zondlar oralig‘i). Harakatchanlik konsentratsiyaga bog‘liq (Caughey–Thomas): \(\mu_n=65+\dfrac{1265}{1+(N/8{,}5\cdot10^{16})^{0{,}72}}\) sm²/(V·s). Diffuziya profillari: cheklanmagan manba — \(\text{erfc}\), cheklangan manba — Gauss.</p>""",
 solved=[("To‘rt zondli o‘lchov", r"\(V/I=10\) Ω, \(x_j=1\) mkm. \(R_\square\) va \(\bar\rho\) = ?", r"\(R_\square=45{,}3\) Ω/□; \(\bar\rho=45{,}3\cdot10^{-4}=4{,}5\cdot10^{-3}\) Ω·sm."),
         ("Bir jinsli qatlam bilan tekshirish", r"n-qatlam \(N_d=10^{18}\) sm⁻³, qalinligi 2 mkm. \(\mu_n\), \(\rho\), \(R_\square\) = ?",
          r"\((10^{18}/8{,}5\cdot10^{16})^{0{,}72}\approx5{,}9\) ⇒ \(\mu_n\approx248\) sm²/(V·s); \(\rho=1/(1{,}602\cdot10^{-19}\cdot10^{18}\cdot248)\approx0{,}025\) Ω·sm; \(R_\square\approx126\) Ω/□.")],
 tasks=[(r"\(R_\square=200\) Ω/□ bo‘lgan qatlamda to‘rt zondli o‘lchovda \(I=1\) mA. \(V\) = ?", "≈ 44 mV"),
        (r"Qalin namuna, \(s=1\) mm, \(V/I=5\) Ω. \(\rho\) = ?", "≈ 3,14 Ω·sm"),
        ("Simulyatorda \\(N_s=3\\cdot10^{19}\\), \\(L_d=1\\) mkm da \\(x_j\\) va \\(R_\\square\\) ni o‘qing; \\(L_d\\) 2 marta oshganda R qanday o‘zgaradi?", "x_j ≈ 3,2 mkm, R_□ ≈ 24 Ω/□; L_d 2 marta oshsa, x_j 2 marta ortadi, R_□ ≈ 2 marta kamayadi"),
        ("Nima uchun \\(\\bar\\rho\\) dan topilgan “o‘rtacha konsentratsiya” sirtdagidan kichik?", "profil chuqurlik bo‘yicha kamayadi")],
 model=("python", """import numpy as np
q = 1.602e-19
mu = lambda N: 65 + 1265/(1 + (N/8.5e16)**0.72)
Ns, Ld, Nb = 3e19, 1e-4, 1e15          # sm^-3, sm, sm^-3
xj = Ld*np.sqrt(np.log(Ns/Nb))
x = np.linspace(0, xj, 2000); N = Ns*np.exp(-(x/Ld)**2) - Nb
Rs = 1/np.trapz(q*mu(N)*N, x)
print(f"x_j = {xj*1e4:.2f} um, R_sheet = {Rs:.1f} Ohm/sq, V/I (4-zond) = {Rs/4.532:.2f} Ohm")"""),
 questions=["Nima uchun to‘rt zondli usul kontakt qarshiligiga sezgir emas?", "Namuna o‘lchamlari uchun tuzatish koeffitsiyentlari qachon kerak?", "Irvin egri chiziqlari nima?", "Hall effekti bilan o‘lchov to‘rt zondlidan nimasi bilan farq qiladi?"]))

A.append(dict(n=15, lec=1, sim="resist", tn=["TN5", "TN10", "TN13", "TN17"],
 title="Chiziqli diagramma usuli bilan bir jinsli bo‘lmagan qatlam bo‘yicha qarshilikni o‘lchash",
 goal="Qatlamni ketma-ket olib tashlash (anod oksidlash + yemirish) va har bosqichda \\(R_\\square\\) ni o‘lchash orqali qatlam o‘tkazuvchanligining chiziqli diagrammasini qurish, solishtirma qarshilik va kirishma profilini tiklash.",
 theory=r"""<p>Olib tashlangan qalinlik \(d\) dan keyin qolgan qatlam o‘tkazuvchanligi \(G(d)=1/R_\square(d)=\int_d^{x_j}\sigma(x)\,dx\). \(G(d)\) ning \(d\) ga bog‘liqligi diagrammasi qurilib, uning har bir oraliqdagi qiyaligidan lokal o‘tkazuvchanlik topiladi:</p>
$$\sigma(x)=-\frac{dG}{dd}\approx\frac{G_i-G_{i+1}}{d_{i+1}-d_i},\qquad \rho(x)=\frac1{\sigma(x)},\qquad N(x)=\frac{\sigma(x)}{q\,\mu(N(x))}$$
<p>Oxirgi tenglama \(\mu(N)\) bog‘liqligi tufayli iteratsiya bilan yechiladi. Diagrammaning bir xil qiyalikli (chiziqli) qismlari bir jinsli legirlangan sohalarga mos keladi.</p>""",
 solved=[("Profilni tiklash", r"O‘lchovlar: \(d=0;\ 0{,}1;\ 0{,}2\) mkm da \(R_\square=50;\ 80;\ 150\) Ω/□ (n-tip). Birinchi va ikkinchi oraliqlar uchun \(\sigma\), \(\rho\) va \(N\) ni toping.",
          r"\(G=0{,}0200;\ 0{,}0125;\ 0{,}00667\) S. \(\sigma_1=(0{,}02-0{,}0125)/10^{-5}=750\) S/sm (\(\rho_1=1{,}33\cdot10^{-3}\) Ω·sm), \(\sigma_2=583\) S/sm (\(\rho_2=1{,}71\cdot10^{-3}\) Ω·sm). Iteratsiya (\(\mu\) Caughey–Thomas): \(N_1\approx6{,}2\cdot10^{19}\), \(N_2\approx4{,}6\cdot10^{19}\) sm⁻³.")],
 tasks=[(r"\(d=0{,}3\) mkm da \(R_\square=400\) Ω/□. Uchinchi oraliqda \(\sigma_3\) = ?", r"\((0{,}00667-0{,}0025)/10^{-5}\approx417\) S/sm"),
        ("Simulyatorda \\(d\\) ni 0,2 mkm qadam bilan oshirib, \\(R_\\square(d)\\) jadvalini tuzing va \\(G(d)\\) diagrammasini chizing.", "jadval + grafik (TN17)"),
        ("Nima uchun olib tashlanadigan qatlam qalinligi aniq o‘lchanishi kerak?", "σ = ΔG/Δd — Δd xatosi to‘g‘ridan-to‘g‘ri σ ga o‘tadi"),
        ("Anod oksidlash usulida 1 V ga necha nm Si sarflanadi (taxminan)?", "kalibrovka bo‘yicha (≈ 0,9–1 nm/V oksid; Si ~0,44 qismi)")],
 model=("python", """import numpy as np
q = 1.602e-19
mu = lambda N: 65 + 1265/(1 + (N/8.5e16)**0.72)
d = np.array([0, 0.1, 0.2, 0.3])*1e-4        # sm
Rs = np.array([50, 80, 150, 400.0])          # Ohm/sq
G = 1/Rs
sigma = -np.diff(G)/np.diff(d)
for i, s in enumerate(sigma):
    N = s/(q*1000)
    for _ in range(50): N = s/(q*mu(N))
    print(f"oraliq {i+1}: sigma={s:6.0f} S/cm  rho={1/s:.2e} Ohm*cm  N={N:.2e} cm^-3")"""),
 questions=["Usulning chuqurlik bo‘yicha aniqligini nima cheklaydi?", "SIMS va spreading resistance usullari bilan taqqoslang.", "Kompensatsiyalangan qatlamda natija qanday buziladi?", "Nega har bosqichda yuzaning tozaligi muhim?"]))
