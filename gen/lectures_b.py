"""M9–M15 ma'ruzalar mazmuni."""

L = []

L.append(dict(
 n=9, short="Boshqariluvchi p-n o‘tishli MT", sim="jfet", refs=[1, 4, 5], intl=["sze", "sedra", "neamen"], tn=["TN4", "TN5", "TN11"],
 title="Boshqariluvchi p-n o‘tishli maydonli tranzistorlar (JFET)",
 goal="P-n o‘tish bilan boshqariladigan maydonli tranzistorning ishlash tartibi, kanal berkilishi, o‘tish va chiqish xarakteristikalarini hisoblash usullari, xarakteristika tikligi va qo‘llanish sohalarini o‘rganish.",
 outcomes=["kanal kengligining zatvor kuchlanishi bilan modulyatsiyasini tushuntiradi;", "berkilish kuchlanishi \\(V_P\\) ni tuzilma parametrlaridan hisoblaydi;", "Shokli tenglamasi bo‘yicha \\(I_D(V_{GS})\\) va tiklik \\(g_m\\) ni topadi;", "JFET ni BT va MOSFET bilan kirish qarshiligi, shovqin va tezlik bo‘yicha solishtiradi."],
 plan=["Tuzilishi va ishlash tartibi", "Kanalning berkilishi, \\(V_P\\)", "Chiqish xarakteristikasi: chiziqli va to‘yinish sohalari", "O‘tish xarakteristikasi, tiklik", "Qo‘llanish sohalari, MESFET"],
 terms=["kanal", "zatvor, istok, stok", "berkilish kuchlanishi \\(V_P\\)", "\\(I_{DSS}\\)", "tiklik (krutizna) \\(S=g_m\\)", "to‘yinish sohasi", "MESFET"],
 theory=[
  ("Tuzilishi va ishlash tartibi", r"""<p>n-kanalli JFETda n-tip kanal ikki tomondan p⁺-zatvor sohalari bilan o‘ralgan. Zatvor–kanal o‘tishi teskari siljitiladi, shuning uchun zatvor toki juda kichik (pA–nA), kirish qarshiligi \(10^9\)–\(10^{12}\) Ω. Teskari kuchlanish oshganda kambag‘allashgan qatlamlar kanalga kirib, uning o‘tkazuvchan qismini toraytiradi — tok zatvor maydoni bilan boshqariladi. Tok faqat asosiy tashuvchilar bilan tashiladi (unipolyar asbob).</p>"""),
  ("Berkilish kuchlanishi", r"""<p>Yarim qalinligi \(a\) bo‘lgan bir jinsli kanal ikkala tomondan to‘liq kambag‘allashganda kanal berkiladi:</p>
$$V_{P0}=\frac{qN_da^2}{2\varepsilon_s},\qquad V_P=-(V_{P0}-V_{bi})$$
<p>\(V_{P0}\) — ichki berkilish kuchlanishi, \(V_P\) — tashqi zatvor kuchlanishi bilan o‘lchanadigan berkilish kuchlanishi (n-kanal uchun manfiy).</p>"""),
  ("Chiqish va o‘tish xarakteristikalari", r"""<p>Kichik \(V_{DS}\) da kanal qarshilik kabi ishlaydi (chiziqli soha). \(V_{DS}\) oshganda stok tomonida kanal torayadi va \(V_{DS,sat}=V_{GS}-V_P\) da stok yaqinida berkiladi; tok deyarli to‘yinadi. To‘yinish sohasi uchun Shokli kvadratik yaqinlashuvi:</p>
$$I_D=I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)^2,\qquad V_P\le V_{GS}\le0$$
<p>Chiziqli sohada: \(I_D=\dfrac{I_{DSS}}{V_P^2}\left[2(V_{GS}-V_P)V_{DS}-V_{DS}^2\right]\).</p>"""),
  ("Xarakteristika tikligi va qo‘llanilishi", r"""<p>Tiklik (o‘tkazuvchanlik) — kuchaytirish xususiyatining asosiy o‘lchovi:</p>
$$S=g_m=\frac{\partial I_D}{\partial V_{GS}}=\frac{2I_{DSS}}{|V_P|}\left(1-\frac{V_{GS}}{V_P}\right)=g_{m0}\sqrt{\frac{I_D}{I_{DSS}}}$$
<p>JFETlar kam shovqinli kirish kaskadlarida (pyezo- va kondensator mikrofonlar, dozimetriya, ionizatsion datchiklar), tok stabilizatorlarida (zatvor istokka ulanganda \(I=I_{DSS}\)), boshqariladigan rezistor va analog kalitlarda ishlatiladi. GaAs MESFET (Shottki zatvorli) — YuCh va SVCh kuchaytirgichlar asosi.</p>""")],
 example=("JFET parametrlarini hisoblash",
  r"(a) Si kanal: \(N_d=10^{16}\) sm⁻³, \(a=1\) mkm, \(V_{bi}=0{,}8\) V. \(V_{P0}\) va \(V_P\) ni toping. (b) \(I_{DSS}=10\) mA, \(V_P=-4\) V, \(V_{GS}=-1{,}5\) V da \(I_D\), \(g_m\) va \(V_{DS,sat}\) ni toping.",
  r"(a) \(V_{P0}=\frac{1{,}602\cdot10^{-19}\cdot10^{16}\cdot10^{-8}}{2\cdot1{,}036\cdot10^{-12}}\approx7{,}73\) V, \(V_P\approx-6{,}9\) V. (b) \(I_D=10(1-0{,}375)^2=3{,}91\) mA; \(g_m=\frac{2\cdot10}{4}\cdot0{,}625=3{,}13\) mS; \(V_{DS,sat}=-1{,}5-(-4)=2{,}5\) V."),
 simtask=["Misolning (b) qismidagi qiymatlarni o‘rnatib, simulyator natijasini tekshiring.", "\\(V_{GS}\\) ni 0 dan \\(V_P\\) gacha o‘zgartirib, \\(g_m\\) ning \\(\\sqrt{I_D}\\) ga proporsionalligini tekshiring.", "Chiqish xarakteristikasidagi sariq chiziq (to‘yinish chegarasi) parabola ekanini isbotlang."],
 mistakes=[("“Zatvorga to‘g‘ri kuchlanish berib tokni oshirish mumkin.”", "Zatvor o‘tishi ochilib, katta zatvor toki oqadi va kirish qarshiligi yo‘qoladi; odatda \\(V_{GS}\\le0\\) (n-kanal)."),
           ("“To‘yinishda kanal butunlay berkiladi va tok to‘xtaydi.”", "Stok yaqinidagi berk sohada tashuvchilar kuchli maydon bilan o‘tkaziladi; tok saqlanadi va deyarli o‘zgarmaydi."),
           ("“Tiklik doimiy.”", "\\(g_m\\) ishchi nuqtaga bog‘liq: \\(V_{GS}=0\\) da maksimal, \\(V_P\\) da nol.")],
 ai="""Sen analog sxemotexnika assistentisan. Menda 2N5457 JFET datasheet’i bor (I_DSS va V_GS(off) qiymatlarini men beraman).
1) Avtosiljitish (self-bias) sxemasida R_S ni I_D = 1 mA uchun hisobla; Shokli tenglamasi va yuklama chizig‘i kesishmasini grafikda ko‘rsat (Python).
2) g_m va UI kaskad kuchaytirishini hisobla.
3) I_DSS va V_P ning tarqalishi (datasheet min/max) ishchi nuqtaga qanday ta’sir qilishini Monte-Karlo bilan baholovchi kod yoz.""",
 quiz=[("JFETda tok qanday tashuvchilar bilan tashiladi?", ["faqat asosiy tashuvchilar", "faqat asosiy bo‘lmagan", "ikkalasi teng", "teshiklar va ionlar"], 0, "Unipolyar asbob."),
       ("\\(I_{DSS}=12\\) mA, \\(V_P=-3\\) V, \\(V_{GS}=-1\\) V: \\(I_D\\) = ?", ["8 mA", "5,33 mA", "4 mA", "1,33 mA"], 1, "\\(12(1-1/3)^2=5{,}33\\)."),
       ("\\(V_{P0}\\) kanal yarim qalinligiga qanday bog‘liq?", ["\\(\\propto a\\)", "\\(\\propto a^2\\)", "\\(\\propto1/a\\)", "bog‘liq emas"], 1, "\\(qN_da^2/2\\varepsilon_s\\)."),
       ("JFETning eng muhim afzalligi:", ["juda yuqori kirish qarshiligi va kam shovqin", "eng katta \\(f_T\\)", "eng past narx", "katta quvvat"], 0, "Kirish o‘tishi teskari siljigan.")],
 blits=["\\(V_{GS}=0\\) da JFET qanday ishlaydi (tok manbai)?", "MESFET ning JFETdan farqi?", "JFETni boshqariladigan rezistor sifatida qayerda ishlatamiz?", "Nega JFET shovqini BTnikidan past?", "p-kanalli JFETda kuchlanish qutblari qanday?"]
))

L.append(dict(
 n=10, short="MDYa strukturalar", sim="mosc", refs=[1, 2, 3], intl=["nicollian", "sze", "schroder", "hu"], tn=["TN5", "TN6", "TN13", "TN17"],
 title="Metall–dielektrik–yarimo‘tkazgich (MDYa) strukturalar",
 goal="MDYa strukturasining zonaviy diagrammalari, sirtoldi qatlami holatlari (boyish, kambag‘allashish, inversiya), sirt o‘tkazuvchanligi, bo‘sag‘a kuchlanishi va C–V xarakteristikalari hamda izolyatsiyalangan zatvorli tranzistorlarga o‘tishni o‘rganish.",
 outcomes=["boyish, kambag‘allashish va kuchli inversiya rejimlarini zonaviy diagrammada ko‘rsatadi;", "\\(C_{ox}\\), \\(\\varphi_F\\), \\(V_{FB}\\), \\(V_T\\) ni hisoblaydi;", "past va yuqori chastotali C–V egri chiziqlarini izohlaydi;", "oksid zaryadlari va sirt holatlarining C–V ga ta’sirini tahlil qiladi."],
 plan=["Ideal MDYa struktura: zonaviy diagrammalar", "Sirt potensiali va sirtoldi qatlam o‘tkazuvchanligi", "Bo‘sag‘a kuchlanishi, tekis zonalar kuchlanishi", "C–V xarakteristikalar", "Izolyatsiyalangan zatvorli MT: turlari, texnologik xossalari"],
 terms=["boyish (akkumulyatsiya)", "kambag‘allashish", "inversiya", "sirt potensiali \\(\\psi_s\\)", "tekis zonalar kuchlanishi \\(V_{FB}\\)", "bo‘sag‘a kuchlanishi \\(V_T\\)", "sirt holatlari \\(D_{it}\\)"],
 theory=[
  ("Ideal MDYa struktura", r"""<p>MDYa (MOS) struktura — metall (yoki poli-Si) zatvor, yupqa dielektrik (SiO₂, HfO₂) va yarimo‘tkazgich taglikdan iborat kondensator. p-taglik uchun zatvor kuchlanishi \(V_G\) ga qarab: \(V_G<V_{FB}\) — teshiklar sirtga to‘planadi (<b>boyish</b>); \(V_{FB}<V_G<V_T\) — teshiklar itariladi, ionlangan aktseptorlar qatlami (<b>kambag‘allashish</b>); \(V_G>V_T\) — sirtda elektronlar konsentratsiyasi teshiklarnikidan oshadi (<b>kuchli inversiya</b>, \(\psi_s=2\varphi_F\)).</p>"""),
  ("Sirt potensiali va o‘tkazuvchanlik", r"""<p>Zatvor kuchlanishi oksid va yarimo‘tkazgich orasida taqsimlanadi:</p>
$$V_G=V_{FB}+\psi_s+\frac{\sqrt{2q\varepsilon_sN_a\psi_s}}{C_{ox}},\qquad C_{ox}=\frac{\varepsilon_{ox}}{d_{ox}},\qquad \varphi_F=\frac{kT}{q}\ln\frac{N_a}{n_i}$$
<p>Inversion qatlam zaryadi \(Q_n\approx-C_{ox}(V_G-V_T)\), sirt (varaq) o‘tkazuvchanligi \(\sigma_\square=\mu_n|Q_n|\). Bu MOSFET kanali tokining asosidir.</p>"""),
  ("Bo‘sag‘a va tekis zonalar kuchlanishi", r"""<p>Real strukturada metall va yarimo‘tkazgich chiqish ishlari farqi \(\varphi_{ms}\) hamda oksiddagi zaryadlar \(Q_{ox}\) hisobga olinadi:</p>
$$V_{FB}=\varphi_{ms}-\frac{Q_{ox}}{C_{ox}},\qquad V_T=V_{FB}+2\varphi_F+\frac{\sqrt{2q\varepsilon_sN_a\cdot2\varphi_F}}{C_{ox}}$$
<p>Oksiddagi zaryad turlari: qo‘zg‘almas (\(Q_f\)), harakatchan ionlar (Na⁺, K⁺), tutib qolingan zaryad (\(Q_{ot}\)) va sirt holatlari zaryadi (\(Q_{it}\)). Sirt holatlari C–V egri chizig‘ini “cho‘zadi”.</p>"""),
  ("C–V xarakteristikalar va izolyatsiyalangan zatvorli MT", r"""<p>Ketma-ket sig‘imlar: \(\dfrac1C=\dfrac1{C_{ox}}+\dfrac1{C_s}\). Boyishda \(C\approx C_{ox}\); kambag‘allashishda \(C_s=\varepsilon_s/W_d\) kamayadi; inversiyada past chastotada (\(f\lesssim10\) Gs) inversion qatlam signalga ulgurib \(C\to C_{ox}\), yuqori chastotada (1 MGs) esa \(C=C_{min}\) da qoladi (\(W_d=W_{max}\)). C–V usuli \(d_{ox}\), \(N_a\), \(V_{FB}\), \(Q_{ox}\), \(D_{it}\) (Terman, yuqori–past chastota usullari) ni aniqlash uchun sanoat standarti. Ushbu struktura asosida <b>izolyatsiyalangan zatvorli maydonli tranzistorlar</b> (IZMT, MOSFET) quriladi: induksiyalangan (boyitish) va qurilgan kanalli (kambag‘allashtirish), n- va p-kanalli — jami 4 tur.</p>""")],
 example=("MDYa strukturaning \\(V_T\\) ni hisoblash",
  r"p-Si, \(N_a=10^{17}\) sm⁻³, \(d_{ox}=10\) nm SiO₂ (\(\varepsilon_{ox}=3{,}45\cdot10^{-13}\) F/sm), \(V_{FB}=-0{,}9\) V, \(n_i=10^{10}\) sm⁻³. \(C_{ox}\), \(\varphi_F\), \(V_T\), \(W_{max}\) ni toping.",
  r"\(C_{ox}=3{,}45\cdot10^{-13}/10^{-6}=3{,}45\cdot10^{-7}\) F/sm² (345 nF/sm²). \(\varphi_F=0{,}02585\ln10^7=0{,}417\) V. \(\sqrt{2q\varepsilon_sN_a\cdot2\varphi_F}=\sqrt{2\cdot1{,}602\cdot10^{-19}\cdot1{,}036\cdot10^{-12}\cdot10^{17}\cdot0{,}833}=1{,}66\cdot10^{-7}\) Kl/sm² ⇒ 0,482 V. \(V_T=-0{,}9+0{,}833+0{,}482\approx0{,}42\) V. \(W_{max}=\sqrt{2\varepsilon_s\cdot2\varphi_F/(qN_a)}\approx0{,}10\) mkm."),
 simtask=["Misoldagi qiymatlarni o‘rnatib, \\(V_T\\) va \\(C_{min}/C_{ox}\\) ni yozing.", "\\(d_{ox}\\) ni 100 nm dan 2 nm gacha kamaytirib, \\(V_T\\) va C–V egri chizig‘ining shakli qanday o‘zgarishini tushuntiring.", "\\(V_{FB}\\) ni siljitib, oksiddagi musbat zaryad egri chiziqni qaysi tomonga siljitishini aniqlang."],
 mistakes=[("“Inversiyada sig‘im har doim \\(C_{ox}\\) ga qaytadi.”", "Faqat past chastotada; yuqori chastotali o‘lchovda \\(C_{min}\\) saqlanadi (yoki chuqur kambag‘allashishda undan ham kamayadi)."),
           ("“\\(V_T\\) faqat oksid qalinligiga bog‘liq.”", "\\(V_T\\) taglik legirlanishi, \\(\\varphi_{ms}\\), oksid zaryadi va harorat bilan ham aniqlanadi."),
           ("“Sirt holatlari faqat \\(V_{FB}\\) ni siljitadi.”", "Ular C–V egri chizig‘ining qiyaligini ham o‘zgartiradi (cho‘zilish) va subbo‘sag‘a qiyalikni yomonlashtiradi.")],
 ai="""Sen yarimo‘tkazgich xarakterizatsiyasi bo‘yicha mutaxassissan. Menda MOS kondensatorining 1 MGs C–V o‘lchov ma’lumotlari (CSV: V_G, C) bor.
1) C_max dan d_ox ni, C_min dan N_a ni (iteratsiya bilan) topadigan Python kodini yoz.
2) Ideal egri chiziqni hisoblab, o‘lchangan egri chiziq bilan solishtirish orqali V_FB va Q_ox ni aniqla.
3) Terman usuli bilan D_it(E) ni baholash qadamlarini tushuntir va qaysi taxminlar natijaga eng ko‘p ta’sir qilishini ayt.""",
 quiz=[("p-tagli MDYa da \\(V_G\\gg V_T\\) bo‘lsa, sirtda:", ["teshiklar to‘planadi", "elektronlar inversion qatlami hosil bo‘ladi", "zaryad yo‘q", "faqat ionlar"], 1, "Kuchli inversiya."),
       ("Kuchli inversiya sharti:", ["\\(\\psi_s=\\varphi_F\\)", "\\(\\psi_s=2\\varphi_F\\)", "\\(\\psi_s=0\\)", "\\(\\psi_s=E_g/q\\)"], 1, "Sirtda \\(n_s=N_a\\)."),
       ("\\(d_{ox}=5\\) nm SiO₂ uchun \\(C_{ox}\\) ≈ ?", ["69 nF/sm²", "690 nF/sm²", "6,9 mkF/sm²", "34,5 nF/sm²"], 1, "\\(3{,}45\\cdot10^{-13}/5\\cdot10^{-7}=6{,}9\\cdot10^{-7}\\)."),
       ("Oksiddagi musbat zaryad \\(V_{FB}\\) ni qanday siljitadi?", ["musbat tomonga", "manfiy tomonga", "o‘zgartirmaydi", "faqat qiyalikni"], 1, "\\(-Q_{ox}/C_{ox}\\).")],
 blits=["High-k dielektriklar nima uchun kerak?", "Poli-Si zatvorning kambag‘allashishi nima?", "Harakatchan ionlarni qanday aniqlash mumkin (BTS)?", "Chuqur kambag‘allashish qachon kuzatiladi?", "Induksiyalangan va qurilgan kanal farqi?"]
))

L.append(dict(
 n=11, short="Izolyatsiyalangan zatvorli MT", sim="mosfet", refs=[1, 3, 4], intl=["tsividis", "hu", "sze", "baliga"], tn=["TN5", "TN6", "TN11", "TN12", "TN18"],
 title="Izolyatsiyalangan zatvorli maydonli tranzistorlar: turlari va strukturaviy-texnologik xossalari",
 goal="MDYa tranzistorlarining VAX modellari, turlari, qisqa kanal effektlari, masshtablash qonuniyatlari va zamonaviy strukturalar (SOI, FinFET, GAA, quvvat MOSFET, IGBT) ning texnologik xossalarini o‘rganish.",
 outcomes=["kvadratik model bo‘yicha \\(I_D\\), \\(g_m\\), \\(r_o\\) ni hisoblaydi;", "subbo‘sag‘a qiyalik va qisqa kanal effektlarini (DIBL, tezlik to‘yinishi) izohlaydi;", "Dennard masshtablash qoidalarini va ularning chegaralarini tushuntiradi;", "planar, SOI, FinFET va quvvat strukturalarini qo‘llanishiga ko‘ra tanlaydi."],
 plan=["MOSFET turlari va belgilanishi", "Kvadratik VAX modeli, kanal uzunligi modulyatsiyasi", "Subbo‘sag‘a rejim va qisqa kanal effektlari", "Masshtablash va zamonaviy strukturalar", "Quvvat MDYa tranzistorlar va IGBT"],
 terms=["boyitish / kambag‘allashtirish turi", "kanal uzunligi modulyatsiyasi \\(\\lambda\\)", "subbo‘sag‘a qiyalik \\(S\\)", "DIBL", "tezlik to‘yinishi", "FinFET", "VDMOS, IGBT"],
 theory=[
  ("Turlari", r"""<p>Kanal turiga ko‘ra n- va p-kanalli, boshlang‘ich holatiga ko‘ra <b>induksiyalangan kanalli</b> (boyitish, normal-yopiq, \(V_T>0\) n-kanal uchun) va <b>qurilgan kanalli</b> (kambag‘allashtirish, normal-ochiq) turlar. Raqamli KMOP sxemalarda ikkala kanalli boyitish turi ishlatiladi.</p>"""),
  ("VAX modeli", r"""<p>Gradual kanal yaqinlashuvida:</p>
$$I_D=k\left[(V_{GS}-V_T)V_{DS}-\frac{V_{DS}^2}{2}\right],\ \ V_{DS}<V_{ov};\qquad I_D=\frac{k}{2}V_{ov}^2(1+\lambda V_{DS}),\ \ V_{DS}\ge V_{ov}$$
<p>bu yerda \(k=\mu_nC_{ox}W/L\), \(V_{ov}=V_{GS}-V_T\). Kichik signal parametrlari: \(g_m=kV_{ov}=\sqrt{2kI_D}\), \(r_o\approx1/(\lambda I_D)\). Harorat ortganda \(\mu\propto T^{-1,5}\) (tok kamayadi) va \(V_T\) taxminan −2 mV/K ga kamayadi (tok ortadi) — ular kompensatsiyalanadigan nuqta mavjud.</p>"""),
  ("Subbo‘sag‘a rejim va qisqa kanal effektlari", r"""<p>\(V_{GS}<V_T\) da tok diffuzion va eksponensial: \(I_D\propto\exp\frac{q(V_{GS}-V_T)}{mkT}\). Subbo‘sag‘a qiyalik:</p>
$$S=\ln10\,\frac{kT}{q}\left(1+\frac{C_d}{C_{ox}}\right)\ge60\ \text{mV/dek (300 K)}$$
<p>Kanal qisqarganda: \(V_T\) kamayadi (roll-off), stok kuchlanishi barerni pasaytiradi (<b>DIBL</b>), elektronlar tezligi \(v_{sat}\approx10^7\) sm/s da to‘yinadi va \(I_D\propto V_{ov}\) bo‘lib qoladi, issiq tashuvchilar oksidga injeksiyalanadi.</p>"""),
  ("Masshtablash va zamonaviy strukturalar", r"""<p>Dennard (1974) doimiy maydon masshtablashida barcha o‘lchamlar va kuchlanish \(1/\kappa\) marta kamaytiriladi: kechikish \(1/\kappa\), quvvat zichligi o‘zgarmaydi. ~2005 dan keyin kuchlanishni kamaytirish \(S\ge60\) mV/dek tufayli to‘xtadi. Yangi strukturalar: <b>SOI</b> (yashirin oksid — kichik parazit sig‘im, radiatsiyaga chidamli), <b>high-k/metall zatvor</b>, <b>FinFET</b> (kanal uch tomondan boshqariladi), <b>GAA nanovaraqlar</b>. Texnologik bosqichlar: termik oksidlash, ion implantatsiyasi, o‘z-o‘zidan moslashuvchi zatvor, LDD, silitsidlash, kuchlangan kremniy (strained Si).</p>"""),
  ("Quvvat MDYa tranzistorlar va IGBT", r"""<p><b>VDMOS/Trench MOSFET</b>da tok vertikal oqadi, kanal ikki marta diffuziya bilan hosil qilinadi, kuchsiz legirlangan drift qatlami yuqori kuchlanishni ushlaydi. Ochiq qarshilik \(R_{DS(on)}\) asosan drift qatlamida, unipolyar chegara: \(R_{on,sp}\propto V_{BR}^{2{,}5}\). <b>IGBT</b>da kollektor tomonida p⁺ qatlam drift sohani o‘tkazuvchanlik modulyatsiyasi bilan boyitadi — yuqori kuchlanishda past kuchlanish tushuvi, lekin sekinroq yopilish (dum toki).</p>""")],
 example=("MOSFET ishchi nuqtasi",
  r"n-MOSFET: \(\mu_nC_{ox}=138\) mkA/V², \(W/L=10\), \(V_T=0{,}5\) V, \(\lambda=0{,}02\) V⁻¹. \(V_{GS}=2\) V, \(V_{DS}=3\) V. \(I_D\), \(g_m\), \(r_o\) va o‘z kuchaytirish \(g_mr_o\) ni toping.",
  r"\(k=1{,}38\) mA/V², \(V_{ov}=1{,}5\) V ⇒ to‘yinish (\(V_{DS}>V_{ov}\)). \(I_D=0{,}5\cdot1{,}38\cdot2{,}25\cdot(1+0{,}06)=1{,}65\) mA. \(g_m=kV_{ov}=2{,}07\) mS. \(r_o\approx1/(0{,}02\cdot1{,}55\ \text{mA})\approx32\) kΩ. \(g_mr_o\approx67\)."),
 simtask=["\\(V_{GS}=2{,}5\\) V da haroratni 250 dan 450 K gacha oshirib, to‘yinish toki kamayishini kuzating; \\(V_{GS}\\) ni 1 V ga tushirib, takrorlang — farqni tushuntiring (harorat kompensatsiyasi nuqtasi).", "\\(\\lambda\\) ni oshirib, \\(r_o\\) qanday kamayishini qayd eting.", "\\(k\\) ni 2 marta oshirish uchun W/L ni yoki \\(d_{ox}\\) ni qanday o‘zgartirish kerak?"],
 mistakes=[("“\\(V_{GS}<V_T\\) da tranzistor to‘liq yopiq.”", "Subbo‘sag‘a tok eksponensial kamayadi, lekin nol emas — zamonaviy chiplarda statik quvvatning asosiy manbai."),
           ("“To‘yinish sohasi BTdagi to‘yinish bilan bir xil.”", "Atamalar teskari: MOSFET to‘yinishi BTning aktiv rejimiga mos (kuchaytirish), MOSFET chiziqli sohasi esa BT to‘yinishiga o‘xshash (kalit)."),
           ("“Masshtablash faqat o‘lchamlarni kichraytirish.”", "Legirlash, kuchlanish va oksid qalinligi ham kelishilgan holda o‘zgartirilishi kerak; aks holda qisqa kanal effektlari ustun bo‘ladi.")],
 ai="""Sen KMOP texnologiyasi bo‘yicha o‘qituvchisan.
1) 180 nm, 45 nm va 7 nm (FinFET) texnologiyalar uchun L, d_ox (EOT), V_DD, S va I_on/I_off tipik qiymatlarini jadvalda ber; har bir qiymatni “taxminiy” yoki manbali deb belgila.
2) ngspice’da BSIM yoki Level-1 model bilan n-MOSFET ning I_D–V_DS oilasini va log(I_D)–V_GS (subbo‘sag‘a) grafigini oladigan netlist yoz.
3) Subbo‘sag‘a qiyalikni grafikdan hisoblovchi Python funksiyasini yoz va 60 mV/dek chegarasining fizik sababini tushuntir.""",
 quiz=[("Kvadratik modelda to‘yinish toki:", ["\\(kV_{ov}V_{DS}\\)", "\\(\\frac{k}{2}V_{ov}^2\\)", "\\(kV_{ov}^3\\)", "\\(\\frac{k}{2}V_{DS}^2\\)"], 1, "\\(\\lambda=0\\) holat."),
       ("300 K da subbo‘sag‘a qiyalikning nazariy minimumi:", ["26 mV/dek", "60 mV/dek", "100 mV/dek", "1 V/dek"], 1, "\\(\\ln10\\cdot kT/q\\)."),
       ("DIBL nima?", ["zatvor oksidining teshilishi", "stok kuchlanishi ta’sirida istok barerining pasayishi", "harakatchanlikning kamayishi", "issiq elektronlar"], 1, "Drain-Induced Barrier Lowering."),
       ("IGBT ning MOSFETdan asosiy afzalligi:", ["tezroq yopiladi", "yuqori kuchlanishda o‘tkazuvchanlik modulyatsiyasi hisobiga past kuchlanish tushuvi", "zatvor toki yo‘q", "kichik o‘lcham"], 1, "Bipolyar injeksiya drift qatlamni boyitadi.")],
 blits=["Qurilgan kanalli MOSFET qayerda ishlatiladi?", "Kuchlangan kremniy harakatchanlikni qanday oshiradi?", "FinFET nima uchun DIBL ni kamaytiradi?", "Quvvat MOSFET ichidagi parazit diod nima?", "SOI ning radiatsiyaga chidamliligi qayerdan?"]
))

L.append(dict(
 n=12, short="Quyosh nurlanishini qabul qiluvchilar", sim="solar", refs=[1, 2, 3], intl=["green", "sze", "schubert"], tn=["TN7", "TN8", "TN16"],
 title="Quyosh nurlanishini qabul qiluvchilar. Fotodiodlar va quyosh elementlari",
 goal="Yorug‘likning yarimo‘tkazgichda yutilishi, fotogeneratsiya, fotodiod va quyosh elementining ishlash rejimlari, asosiy xarakteristikalari (sezgirlik, kvant samaradorligi, \\(V_{oc}\\), \\(J_{sc}\\), FF) va FIKni hisoblashni o‘rganish.",
 outcomes=["yutilish koeffitsiyenti va kirish chuqurligi orqali fotogeneratsiya profilini baholaydi;", "fotodiodning sezgirligini \\(R=\\eta q\\lambda/hc\\) bo‘yicha hisoblaydi;", "quyosh elementining VAXidan \\(V_{oc}\\), \\(J_{sc}\\), FF va \\(\\eta\\) ni topadi;", "FIKni cheklovchi omillarni (Shokli–Kvaysser chegarasi, rekombinatsiya, qarshiliklar) tahlil qiladi."],
 plan=["Yorug‘lik yutilishi va fotogeneratsiya", "Fotodiod: fotodiod va fotogalvanik rejimlar", "Asosiy xarakteristikalar: sezgirlik, kvant samaradorligi, tezkorlik, shovqin", "Quyosh elementi VAXi va FIK", "FIK chegaralari va zamonaviy elementlar"],
 terms=["yutilish koeffitsiyenti \\(\\alpha\\)", "ichki/tashqi kvant samaradorligi", "sezgirlik \\(R\\) (A/Vt)", "qisqa tutashuv toki \\(J_{sc}\\)", "salt yurish kuchlanishi \\(V_{oc}\\)", "to‘ldirish koeffitsiyenti FF", "AM1.5"],
 theory=[
  ("Yutilish va fotogeneratsiya", r"""<p>\(h\nu\ge E_g\) bo‘lgan foton elektron-teshik juftini hosil qiladi. Intensivlik chuqurlik bo‘yicha \(I(x)=I_0e^{-\alpha x}\) kamayadi, generatsiya tezligi \(G(x)=\alpha\Phi_0e^{-\alpha x}\). To‘g‘ri zonali GaAs da \(\alpha\sim10^4\) sm⁻¹ (bir necha mkm yetarli), egri zonali Si da qizil va IQ yorug‘lik uchun \(1/\alpha\) 10–100 mkm ga yetadi. Chegaraviy to‘lqin uzunligi \(\lambda_c=1{,}24/E_g\) (mkm, eV).</p>"""),
  ("Fotodiod", r"""<p>Kambag‘allashgan qatlamda va undan diffuziya uzunligi masofasida hosil bo‘lgan juftlar o‘tish maydoni bilan ajratiladi va fototok beradi:</p>
$$I=I_s\left(e^{qV/nkT}-1\right)-I_{ph},\qquad I_{ph}=q\eta\frac{P}{h\nu},\qquad R=\frac{I_{ph}}{P}=\frac{\eta q\lambda}{hc}=\eta\frac{\lambda[\text{mkm}]}{1{,}24}\ \text{A/Vt}$$
<p>Fotodiod rejimi — teskari siljish: chiziqli javob, kichik sig‘im, yuqori tezlik. Fotogalvanik rejim — tashqi manbasiz, kuchlanish hosil qiladi. PIN-fotodiodlarda keng i-qatlam kvant samaradorlik va tezlikni oshiradi; ko‘chkisimon fotodiodlar (APD) ichki kuchaytirish \(M\) beradi.</p>"""),
  ("Quyosh elementi VAXi va FIK", r"""<p>Yoritilgan quyosh elementi uchun (tok yo‘nalishi generator sifatida):</p>
$$J=J_{sc}-J_0\left(e^{qV/nkT}-1\right),\qquad V_{oc}=\frac{nkT}{q}\ln\!\left(\frac{J_{sc}}{J_0}+1\right)$$
$$FF=\frac{J_mV_m}{J_{sc}V_{oc}}\approx\frac{v_{oc}-\ln(v_{oc}+0{,}72)}{v_{oc}+1},\quad v_{oc}=\frac{qV_{oc}}{nkT};\qquad \eta=\frac{FF\cdot J_{sc}V_{oc}}{P_{in}}$$
<p>Standart sinov sharoiti: AM1.5G, 1000 Vt/m² (100 mVt/sm²), 25 °C. Ketma-ket qarshilik FF ni, shunt qarshilik kichik yoritilganlikdagi ishni yomonlashtiradi.</p>"""),
  ("FIK chegaralari va zamonaviy elementlar", r"""<p>Bitta o‘tishli element uchun Shokli–Kvaysser chegarasi ≈ 33 % (\(E_g\approx1{,}34\) eV). Yo‘qotishlar: \(h\nu<E_g\) fotonlar yutilmaydi, ortiqcha energiya termallashadi, radiatsion va noradiatsion rekombinatsiya, aks etish, kontaktlar soyasi. Zamonaviy kremniy elementlar (PERC, TOPCon, HJT) 22–26 %, ko‘p o‘tishli III–V elementlar konsentratorda 45 % dan yuqori; perovskit/Si tandemlar jadal rivojlanmoqda. Quyosh elementining harorat koeffitsiyenti Si uchun ≈ −0,3…−0,45 %/K (asosan \(V_{oc}\) kamayishi hisobiga).</p>""")],
 example=("Fotodiod sezgirligi va quyosh elementi FIK",
  r"(a) Si fotodiod \(\lambda=0{,}85\) mkm, \(\eta=0{,}8\). Sezgirlik va \(P=1\) mkVt da fototokni toping. (b) Quyosh elementi: \(J_{sc}=35\) mA/sm², \(J_0=10^{-12}\) A/sm², \(n=1\), 300 K, AM1.5 (100 mVt/sm²). \(V_{oc}\), FF va \(\eta\) ni toping.",
  r"(a) \(R=0{,}8\cdot0{,}85/1{,}24=0{,}548\) A/Vt; \(I_{ph}=0{,}55\) mkA. (b) \(V_{oc}=0{,}02585\ln(3{,}5\cdot10^{10})=0{,}628\) V; \(v_{oc}=24{,}3\) ⇒ \(FF=(24{,}3-\ln25{,}0)/25{,}3\approx0{,}83\); \(\eta=0{,}83\cdot35\cdot0{,}628/100\approx18{,}3\) %."),
 simtask=["Misolning (b) qismini simulyatorda tekshiring (MPP nuqtasi va FF).", "Yoritilganlikni 1000 dan 200 Vt/m² ga kamaytirib, \\(V_{oc}\\) ning logarifmik, \\(J_{sc}\\) ning chiziqli kamayishini ko‘rsating.", "Haroratni 300 dan 330 K ga oshirib, \\(\\eta\\) ning nisbiy harorat koeffitsiyentini (%/K) hisoblang."],
 mistakes=[("“Quyosh elementi qancha ko‘p yorug‘lik olsa, kuchlanishi shuncha proporsional ortadi.”", "\\(V_{oc}\\) yorug‘likka logarifmik bog‘liq; proporsional ortadigani — \\(J_{sc}\\)."),
           ("“Fotodiod rejimida teskari kuchlanish fototokni oshiradi.”", "Fototok deyarli o‘zgarmaydi; teskari kuchlanish sig‘imni kamaytirib tezlikni va chiziqlilikni yaxshilaydi."),
           ("“FIKni oshirish uchun \\(E_g\\) imkon qadar kichik bo‘lishi kerak.”", "Kichik \\(E_g\\) da \\(J_{sc}\\) ortadi, ammo \\(V_{oc}\\) kamayadi — optimum ≈ 1,1–1,4 eV.")],
 ai="""Sen fotovoltaika bo‘yicha tadqiqotchisan. Menda quyosh elementining o‘lchangan J–V ma’lumotlari bor (CSV).
1) Bir diodli model (J_sc, J_0, n, R_s, R_sh) parametrlarini scipy.optimize bilan topadigan kod yoz; Lambert-W yoki Nyuton usulini tanlaganingni asosla.
2) V_oc, J_sc, FF, η va MPP ni hisobla; 1000 Vt/m², 25 °C ga keltirish formulasini (IEC 60891) qo‘lla.
3) Natijani Shokli–Kvaysser chegarasi bilan solishtirib, eng katta yo‘qotish manbasini ko‘rsat.""",
 quiz=[("Fotodiod sezgirligi \\(\\lambda=1{,}24\\) mkm, \\(\\eta=1\\) da:", ["0,5 A/Vt", "1 A/Vt", "1,24 A/Vt", "0,8 A/Vt"], 1, "\\(R=\\eta\\lambda/1{,}24\\)."),
       ("\\(V_{oc}\\) yoritilganlikka qanday bog‘liq?", ["chiziqli", "logarifmik", "kvadratik", "bog‘liq emas"], 1, "\\(V_{oc}\\propto\\ln J_{sc}\\)."),
       ("Bitta o‘tishli element uchun Shokli–Kvaysser chegarasi:", ["≈ 15 %", "≈ 33 %", "≈ 60 %", "≈ 86 %"], 1, "AM1.5 uchun ~33 %."),
       ("FF ni eng ko‘p kamaytiradigan parazit parametr:", ["katta \\(R_{sh}\\)", "katta \\(R_s\\)", "kichik \\(J_0\\)", "kichik harorat"], 1, "Ketma-ket qarshilik VAX “burchagini” yumaloqlaydi.")],
 blits=["Ichki va tashqi kvant samaradorligi farqi?", "Nega Si quyosh elementi yuzasi teksturalanadi?", "APD ning shovqin omili nima?", "AM1.5 nimani anglatadi?", "Perovskit elementlarning asosiy muammosi?"]
))

L.append(dict(
 n=13, short="Fotosezgir va yorug‘lik chiqaruvchi asboblar", sim="led", refs=[1, 3, 5], intl=["schubert", "coldren", "sze"], tn=["TN7", "TN8", "TN10"],
 title="Fotosezgir va yorug‘lik hosil qiladigan yarimo‘tkazgichli asboblar: fototranzistorlar, PZS, svetodiodlar, lazerlar",
 goal="Fotodiod va fototranzistorlar, PZS (zaryad bog‘lanishli) fotoqabul qiluvchi tuzilmalar, svetodiodlarda nurlanishli rekombinatsiya va yarimo‘tkazgichli lazerlarda generatsiya shartlarini o‘rganish.",
 outcomes=["fototranzistorning ichki kuchaytirishini va tezkorlik bilan murosasini tushuntiradi;", "svetodiod to‘lqin uzunligi va samaradorlik komponentlarini hisoblaydi;", "lazer generatsiyasi uchun inversiya (Bernard–Duraffur) va bo‘sag‘a shartlarini yozadi;", "L–I xarakteristikasidan bo‘sag‘a toki va differensial samaradorlikni aniqlaydi."],
 plan=["Fototranzistorlar va fotorezistorlar", "PZS (CCD) fotoqabul qiluvchi tuzilmalar", "Svetodiodlar: nurlanishli rekombinatsiya, samaradorlik", "Yarimo‘tkazgichli lazer: inversiya, rezonator, bo‘sag‘a", "Geterostrukturalar va qo‘llanilishi"],
 terms=["fototranzistor", "PZS (CCD) piksel", "nurlanishli rekombinatsiya", "ichki kvant samaradorligi \\(\\eta_{int}\\)", "chiqarib olish samaradorligi \\(\\eta_{ext}\\)", "populyatsiya inversiyasi", "bo‘sag‘a toki \\(I_{th}\\)"],
 theory=[
  ("Fototranzistorlar va PZS tuzilmalar", r"""<p><b>Fototranzistor</b>da baza–kollektor o‘tishi fotodiod vazifasini bajaradi; fototok baza toki sifatida \(\beta\) marta kuchaytiriladi: \(I_C\approx(1+\beta)I_{ph}\). Narxi — katta Miller sig‘imi tufayli past tezlik (mks). <b>PZS (ZAA, CCD)</b> fotoqabul qiluvchi tuzilmalarda har bir MDYa kondensator potensial chuqurligida yorug‘lik hosil qilgan zaryadni to‘playdi; zaryad paketlari keyin ketma-ket siljitilib o‘qiladi (M14). Zamonaviy kameralarda KMOP faol pikselli sensorlar (APS) ustun.</p>"""),
  ("Svetodiodlar", r"""<p>To‘g‘ri siljitilgan p-n o‘tishda injeksiyalangan tashuvchilar nurlanish bilan rekombinatsiyalanadi. Nurlanish energiyasi \(h\nu\approx E_g\), to‘lqin uzunligi va spektral kenglik:</p>
$$\lambda[\text{nm}]\approx\frac{1240}{E_g[\text{eV}]},\qquad \Delta E\approx1{,}8kT,\qquad \eta_{ext}=\eta_{int}\cdot\eta_{extr}$$
<p>To‘g‘ri zonali materiallar (GaAs, AlGaInP — qizil/sariq, InGaN — ko‘k/yashil) ishlatiladi. Yuqori sindirish ko‘rsatkichi (\(n\approx3{,}5\)) tufayli to‘liq ichki qaytish chiqarib olishni cheklaydi (\(\eta_{extr}\approx\frac{1}{4n^2}\) bitta sirt uchun); teksturalash, gumbaz va teskari piramida shakllar ishlatiladi. Oq svetodiod — ko‘k InGaN + sariq fosfor (YAG:Ce).</p>"""),
  ("Yarimo‘tkazgichli lazer", r"""<p>Majburiy nurlanish yutilishdan ustun bo‘lishi uchun <b>Bernard–Duraffur sharti</b> bajarilishi kerak: \(E_{Fn}-E_{Fp}>h\nu>E_g\). Rezonator (kristall qirralari — Fabri–Pero, \(R\approx0{,}3\)) teskari aloqani ta’minlaydi. Generatsiya bo‘sag‘asi — kuchayish yo‘qotishlarga teng:</p>
$$\Gamma g_{th}=\alpha_i+\frac{1}{2L}\ln\frac{1}{R_1R_2},\qquad P=\eta_d\frac{h\nu}{q}(I-I_{th}),\ I>I_{th}$$
<p>Ikki tomonlama geterostruktura (Alferov, Kremer — 2000 y. Nobel) tashuvchilarni va yorug‘likni faol qatlamda cheklab, \(J_{th}\) ni 10⁵ dan ~10² A/sm² gacha kamaytirdi. Kvant chuqurli, VCSEL va DFB lazerlar optik aloqa, LiDAR va o‘qish qurilmalarida ishlatiladi. \(I_{th}\) harorat bilan eksponensial ortadi: \(I_{th}\propto e^{T/T_0}\).</p>""")],
 example=("Svetodiod va lazer parametrlari",
  r"(a) GaAs (\(E_g=1{,}424\) eV) va InGaN (\(E_g=2{,}7\) eV) svetodiodlari to‘lqin uzunligini va 300 K dagi spektral kenglikni (meV) toping. (b) GaAs lazer: \(I_{th}=20\) mA, \(\eta_d=0{,}5\). \(I=50\) mA da chiqish quvvati qancha?",
  r"(a) GaAs: \(1240/1{,}424\approx871\) nm (IQ); InGaN: \(1240/2{,}7\approx459\) nm (ko‘k). \(\Delta E\approx1{,}8\cdot25{,}85\approx47\) meV. (b) qiyalik \(\eta_dh\nu/q=0{,}5\cdot1{,}424=0{,}71\) Vt/A; \(P=0{,}71\cdot0{,}03\approx21\) mVt."),
 simtask=["\\(E_g\\) ni 1,4 dan 3,4 eV gacha o‘zgartirib, ko‘rinadigan diapazon chegaralariga mos \\(E_g\\) larni toping.", "Haroratni oshirib, \\(E_g\\) kamayishi spektrni qaysi tomonga siljitishini kuzating.", "L–I grafikdan \\(I_{th}\\) va qiyalikni o‘qib, \\(\\eta_d\\) ni qayta tiklang."],
 mistakes=[("“Kremniydan samarali svetodiod qilish mumkin.”", "Si egri zonali — nurlanishli rekombinatsiya fonon talab qiladi va juda kam ehtimolli."),
           ("“Lazer — juda yorqin svetodiod.”", "Lazer majburiy nurlanish va rezonatorga ega: kogerent, tor spektrli, yo‘nalgan nur va aniq bo‘sag‘a."),
           ("“Fototranzistor fotodioddan har jihatdan yaxshi.”", "Kuchaytirish yuqori, lekin tezlik va chiziqlilik past.")],
 ai="""Sen optoelektronika bo‘yicha o‘qituvchisan.
1) Qizil (AlGaInP), yashil (InGaN), ko‘k (InGaN) va IQ (GaAs) svetodiodlari uchun E_g, λ va tipik tashqi kvant samaradorligini jadvalda ber; manbasiz raqamlarni “tipik” deb belgila.
2) “Green gap” muammosini tushuntir.
3) Lazer L–I o‘lchov ma’lumotlaridan (CSV) I_th ni ikki chiziqli moslash usuli bilan topadigan va T_0 ni bir necha haroratdagi I_th dan hisoblaydigan Python kod yoz.""",
 quiz=[("\\(E_g=1{,}9\\) eV svetodiod rangi:", ["ko‘k", "yashil", "qizil", "IQ"], 2, "≈ 653 nm."),
       ("Lazer generatsiyasi uchun Bernard–Duraffur sharti:", ["\\(E_{Fn}-E_{Fp}>h\\nu\\)", "\\(h\\nu<kT\\)", "\\(E_g=0\\)", "\\(I<I_{th}\\)"], 0, "Inversiya sharti."),
       ("Fototranzistorning fotodioddan asosiy farqi:", ["ichki kuchaytirish \\(\\approx\\beta\\)", "kattaroq tezlik", "kichik qorong‘i tok", "yorug‘lik chiqaradi"], 0, "Fototok baza toki kabi kuchaytiriladi."),
       ("Geterostruktura lazerning asosiy afzalligi:", ["tashuvchilar va yorug‘likni cheklash orqali past \\(J_{th}\\)", "arzonlik", "kremniy bilan mos", "ko‘k nur"], 0, "Ikki tomonlama cheklash.")],
 blits=["Oq svetodiod qanday olinadi?", "VCSEL ning afzalligi?", "\\(T_0\\) parametri nimani ko‘rsatadi?", "PZS va KMOP sensor farqi?", "LED samaradorligining “droop” effekti nima?"]
))

L.append(dict(
 n=14, short="Zaryad aloqali asboblar", sim="ccd", refs=[1, 2, 3], intl=["janesick", "sze"], tn=["TN9", "TN10", "TN17"],
 title="Zaryad aloqali asboblar (ZAA, CCD)",
 goal="ZAAning ishlash prinsipi (potensial chuqurlar va zaryad uzatish), turlari, asosiy parametrlari (CTE, to‘liq quduq sig‘imi, qorong‘i tok, shovqin) va ishchi xarakteristikalarini hisoblashni o‘rganish.",
 outcomes=["uch fazali taktlash bilan zaryad paketining siljishini tushuntiradi;", "\\(N\\) uzatishdan keyingi zaryad ulushini CTE orqali hisoblaydi;", "to‘liq quduq sig‘imi va dinamik diapazonni baholaydi;", "sirt va hajmiy kanalli, chiziqli va matritsali ZAA turlarini solishtiradi."],
 plan=["MDYa kondensator — potensial chuqur", "Zaryad uzatish: 2-, 3-, 4-fazali taktlash", "ZAA turlari: sirt/hajmiy kanal, chiziqli, matritsali (kadr, qator oralab uzatish)", "Asosiy parametrlar: CTE, to‘liq quduq, qorong‘i tok, shovqin", "Foydalanish sohalari"],
 terms=["potensial chuqur", "zaryad paketi", "taktlash fazalari \\(\\Phi_1,\\Phi_2,\\Phi_3\\)", "zaryad uzatish samaradorligi (CTE)", "to‘liq quduq sig‘imi (FWC)", "qorong‘i tok", "o‘qish shovqini"],
 theory=[
  ("Ishlash prinsipi", r"""<p>ZAA (1969, Boyl va Smit — 2009 y. Nobel) — bir-biriga juda yaqin joylashgan MDYa kondensatorlar zanjiri. Zatvorga musbat impuls berilganda p-taglikda chuqur kambag‘allashish yuzaga keladi — elektronlar uchun <b>potensial chuqur</b>. Yorug‘lik yoki kirish sxemasi hosil qilgan zaryad shu chuqurda saqlanadi. Qo‘shni zatvor kuchlanishi oshirilib, oldingisi kamaytirilsa, zaryad yangi chuqurga oqib o‘tadi. Uch fazali sxemada har bir piksel uchta elektroddan iborat; bir takt davrida paket bitta pikselga siljiydi.</p>"""),
  ("Zaryad uzatish mexanizmlari va CTE", r"""<p>Zaryad uch mexanizm bilan ko‘chadi: o‘z-o‘zidan induksiyalangan dreyf (zaryadlar itarilishi), issiqlik diffuziyasi va chekka maydonlar dreyfi. Har bir uzatishda kichik ulush qoladi; <b>zaryad uzatish samaradorligi</b> CTE bilan:</p>
$$\frac{Q_N}{Q_0}=\text{CTE}^{\,N}\approx e^{-N(1-\text{CTE})}$$
<p>Sirt holatlari zaryadni tutib qoladi, shuning uchun <b>hajmiy (yashirin) kanalli</b> ZAA da kanal sirtdan uzoqlashtirilib CTE > 0,99999 ga erishiladi.</p>"""),
  ("Turlari", r"""<p><b>Chiziqli</b> ZAA (skanerlar, spektrometrlar), <b>matritsali</b>: to‘liq kadrli (mexanik zatvor kerak), kadrni uzatishli (yorug‘likdan himoyalangan saqlash sohasi), qator oralab uzatishli (har bir ustun yonida himoyalangan registr). Orqa tomondan yoritiladigan (back-illuminated) yupqalashtirilgan ZAA kvant samaradorligi 90 % dan yuqori. Elektron ko‘paytiruvchi EMCCD bitta foton sezgirligiga ega.</p>"""),
  ("Asosiy parametrlar va hisob", r"""<p><b>To‘liq quduq sig‘imi</b> \(N_{FW}\approx C_{eff}\Delta V/q\); <b>dinamik diapazon</b> \(DR=N_{FW}/\sigma_{read}\) (dB da \(20\lg DR\)); <b>qorong‘i tok</b> \(\propto T^{3/2}e^{-E_g/2kT}\) — har 6–8 K sovutishda ikki marta kamayadi (astronomik ZAA −100 °C gacha sovutiladi); foton shovqini \(\sqrt{N}\). Signal/shovqin: \(SNR=\dfrac{N}{\sqrt{N+N_d+\sigma_{read}^2}}\). Foydalanish: astronomiya (Habbl, Gaia), tibbiy rentgen, spektroskopiya, analog kechikish liniyalari va filtrlar.</p>""")],
 example=("ZAA ning uzatish yo‘qotishi va dinamik diapazoni",
  r"2048×2048 matritsada eng uzoq piksel zaryadi \(N=4096\) uzatishdan o‘tadi. (a) CTE = 0,99999 va 0,9999 da \(Q_N/Q_0\) ni toping. (b) Piksel saqlash sig‘imi \(C_{eff}=70\) fF, \(\Delta V=1\) V, o‘qish shovqini 5 e⁻. FWC va DR ni toping.",
  r"(a) \(0{,}99999^{4096}=e^{-0{,}041}\approx0{,}960\) (4 % yo‘qotish); \(0{,}9999^{4096}=e^{-0{,}41}\approx0{,}66\) — tasvir “cho‘ziladi”. (b) \(N_{FW}=70\cdot10^{-15}/1{,}602\cdot10^{-19}\approx4{,}4\cdot10^5\) e⁻; \(DR=8{,}7\cdot10^4\) ≈ 99 dB."),
 simtask=["CTE ni 0,9995 dan 0,99999 gacha oshirib, \\(N=1024\\) da yo‘qotishni jadvalga yozing.", "Animatsiyada faol faza qanday almashinishini va zaryad paketining siljish yo‘nalishini tavsiflang.", "Qaysi CTE da 4096 uzatishdan keyin yo‘qotish 1 % dan kam bo‘ladi? Formuladan hisoblab, simulyatorda tekshiring."],
 mistakes=[("“ZAA har bir pikselni alohida o‘qiydi.”", "Zaryad paketlari ketma-ket siljitilib, bitta (yoki bir necha) chiqish kuchaytirgichida o‘qiladi."),
           ("“CTE 0,999 — yaxshi natija.”", "1000 uzatishda 0,999¹⁰⁰⁰ ≈ 0,37 — signalning 63 % i yo‘qoladi."),
           ("“Sovutish faqat shovqinni kamaytiradi.”", "Qorong‘i tokni ham eksponensial kamaytiradi va uzoq ekspozitsiyaga imkon beradi.")],
 ai="""Sen astronomik priborsozlik muhandisisan.
1) Uch fazali ZAA da zaryad uzatishni 1D potensial modelida simulyatsiya qiladigan Python kodini yoz (diffuziya + dreyf, har bir faza uchun potensial profili).
2) CTE ning harorat va taktlash chastotasiga bog‘liqligini sifat jihatidan tushuntir.
3) Qorong‘i tok −100 °C va +20 °C da necha marta farq qilishini E_g/2kT faktor bilan hisobla (taxminlarni ochiq yoz).""",
 quiz=[("CTE = 0,9999, N = 1000 da qolgan zaryad ulushi:", ["0,99", "0,905", "0,37", "0,9999"], 1, "\\(e^{-0{,}1}\\approx0{,}905\\)."),
       ("Hajmiy kanalli ZAA nima uchun yaxshiroq?", ["arzon", "zaryad sirt holatlaridan uzoqda — CTE yuqori", "yorug‘lik chiqaradi", "taktlash kerak emas"], 1, "Sirt tutqichlari chetlab o‘tiladi."),
       ("Uch fazali ZAA da bitta pikselga nechta elektrod to‘g‘ri keladi?", ["1", "2", "3", "4"], 2, "Φ1, Φ2, Φ3."),
       ("Qorong‘i tokni kamaytirishning asosiy usuli:", ["taktlash chastotasini oshirish", "sovutish", "zatvor kuchlanishini oshirish", "pikselni kattalashtirish"], 1, "Termogeneratsiya eksponensial kamayadi.")],
 blits=["Kadrni uzatishli ZAA qanday ishlaydi?", "Blooming nima va unga qarshi qanday choralar bor?", "EMCCD qanday ko‘paytiradi?", "Nega KMOP sensorlar ZAA ni siqib chiqardi?", "Analog kechikish liniyasi sifatida ZAA qanday ishlaydi?"]
))

L.append(dict(
 n=15, short="Integral sxemalar va radiatsiya", sim="cmos", refs=[1, 3, 5], intl=["rabaey", "holmes", "hu"], tn=["TN12", "TN16", "TN17", "TN18"],
 title="Integral sxemalar. KMOP. Radiatsion nurlanishning ta’siri va radiatsiyaga chidamli strukturalar",
 goal="Raqamli va analog integral sxemalarning asosiy elementlari, KMOP invertorning statik va dinamik xususiyatlari hamda ionlashtiruvchi nurlanishning yarimo‘tkazgich asboblarga ta’siri va radiatsiyaga chidamli strukturalar yaratish usullarini o‘rganish.",
 outcomes=["KMOP invertorning uzatish xarakteristikasi, shovqin zahiralari va quvvat iste’molini hisoblaydi;", "raqamli va analog IS larning asosiy bloklari va ularga qo‘yiladigan talablarni ajratadi;", "jami ionlashtiruvchi doza, siljish shikastlanishi va bitta zarracha effektlarini farqlaydi;", "radiatsiyaga chidamlilikni oshirishning texnologik va sxemotexnik usullarini tanlaydi."],
 plan=["IS lar tasnifi: raqamli, analog, aralash signal", "KMOP invertor: VTC, shovqin zahiralari, quvvat", "Analog IS bloklari: tok ko‘zgusi, differensial juftlik, op-amp", "Radiatsiya ta’siri: TID, DD, SEE", "Radiatsiyaga chidamli strukturalar va IS"],
 terms=["KMOP", "uzatish xarakteristikasi (VTC)", "shovqin zahirasi NM", "dinamik quvvat \\(\\alpha CV^2f\\)", "jami ionlashtiruvchi doza (TID)", "bitta zarracha effekti (SEU, SEL)", "RHBD"],
 theory=[
  ("Integral sxemalar tasnifi", r"""<p>IS — bitta kristallda tayyorlangan va o‘zaro ulangan asboblar majmuasi. Raqamli IS (mantiqiy elementlar, xotira, protsessorlar) ikki holatli signallar bilan, analog IS (operatsion kuchaytirgichlar, ADC/DAC, stabilizatorlar) uzluksiz signallar bilan ishlaydi; aralash signal (mixed-signal) va SoC ikkalasini birlashtiradi. Asosiy texnologiyalar: KMOP (raqamli va ko‘p analog), BiKMOP, SiGe BiCMOS (RF), SOI.</p>"""),
  ("KMOP invertor", r"""<p>n- va p-MOSFET ketma-ket ulangan; har qanday statik holatda bittasi yopiq — statik tok (oqishdan tashqari) yo‘q. Uzatish xarakteristikasida o‘tish bo‘sag‘asi:</p>
$$V_M=\frac{V_{DD}-|V_{Tp}|+V_{Tn}\sqrt{k_n/k_p}}{1+\sqrt{k_n/k_p}}$$
<p>Simmetrik xarakteristika uchun \(k_n=k_p\), ya’ni \((W/L)_p\approx(2\ldots3)(W/L)_n\) (\(\mu_n/\mu_p\) hisobiga). Shovqin zahiralari \(NM_L=V_{IL}-V_{OL}\), \(NM_H=V_{OH}-V_{IH}\) (\(V_{IL}, V_{IH}\) — kuchaytirish −1 bo‘ladigan nuqtalar). Quvvat: \(P=\alpha C_LV_{DD}^2f+I_{leak}V_{DD}\); kechikish \(t_p\approx\dfrac{C_LV_{DD}}{I_{D,sat}}\).</p>"""),
  ("Analog IS bloklari", r"""<p>Tok ko‘zgusi (\(I_{out}=I_{ref}\frac{(W/L)_2}{(W/L)_1}\)), differensial juftlik (umumiy signalni bostirish, CMRR), kaskod va ikki kaskadli operatsion kuchaytirgich, bandgap tayanch manbai (\(V_{BE}\) ning manfiy va \(\Delta V_{BE}\) ning musbat KHKlarini kompensatsiyalash — ~1,2 V). Analog sxemalar uchun moslik (matching), \(g_mr_o\), \(1/f\) shovqin va \(f_T\) muhim.</p>"""),
  ("Radiatsiya ta’siri", r"""<p><b>Jami ionlashtiruvchi doza (TID)</b>: oksidda hosil bo‘lgan teshiklar tutib qolinadi (\(\Delta V_{ot}=-Q_{ot}/C_{ox}<0\)), Si/SiO₂ chegarasida sirt holatlari ortadi. Natija: n-MOSFET \(V_T\) kamayadi (oqish ortadi), p-MOSFET \(|V_T|\) ortadi, izolyatsiya oksidi (STI) ostida parazit kanallar paydo bo‘ladi. \(\Delta V_T\propto d_{ox}^2\) — yupqa oksidlar chidamliroq. <b>Siljish shikastlanishi (DD)</b>: neytron/proton panjara atomlarini siljitadi — tashuvchilar umri kamayadi (\(1/\tau=1/\tau_0+K_\tau\Phi\)), bipolyar tranzistorlarda \(\beta\) pasayadi (Messenger: \(1/\beta=1/\beta_0+K\Phi\)), quyosh elementlari FIK yo‘qotadi. <b>Bitta zarracha effektlari (SEE)</b>: og‘ir ion trekida yig‘ilgan zaryad xotira yacheykasini ag‘darishi (SEU) yoki parazit tiristor strukturasini ochishi (latch-up, SEL) mumkin.</p>"""),
  ("Radiatsiyaga chidamli strukturalar", r"""<p>Texnologik usullar (RHBP): SOI va SOS, yupqa va “qattiqlashtirilgan” oksidlar, epitaksial qatlam, chuqur ariqli izolyatsiya, himoya halqalari (guard rings). Sxemotexnik usullar (RHBD): yopiq geometriyali (ELT) tranzistorlar, uch karrali modulli rezervlash (TMR), DICE xotira yacheykalari, xatolarni tuzatuvchi kodlar (ECC), latch-up uchun tok cheklash. Qo‘llanilishi: kosmik apparatlar, yadro energetikasi, yuqori energiyalar fizikasi detektorlari, tibbiy nurlanish qurilmalari.</p>""")],
 example=("KMOP quvvati va radiatsion \\(V_T\\) siljishi",
  r"(a) Chip: \(\alpha=0{,}1\), umumiy kalitlanuvchi sig‘im \(C=1\) nF, \(V_{DD}=1\) V, \(f=1\) GGs. Dinamik quvvatni toping. (b) Oksidda tutilgan zaryad zichligi \(\Delta N_{ot}=10^{11}\) sm⁻² (musbat), \(d_{ox}=10\) nm. \(\Delta V_T\) ni toping; \(d_{ox}=5\) nm da (bir xil hajmiy tutilish bilan) qancha bo‘ladi?",
  r"(a) \(P=0{,}1\cdot10^{-9}\cdot1\cdot10^9=0{,}1\) Vt. (b) \(\Delta V_T=-q\Delta N_{ot}/C_{ox}=-1{,}602\cdot10^{-8}/3{,}45\cdot10^{-7}\approx-46\) mV. Hajmiy tutilishda \(\Delta N_{ot}\propto d_{ox}\) va \(C_{ox}\propto1/d_{ox}\), shuning uchun \(\Delta V_T\propto d_{ox}^2\): 5 nm da ≈ −12 mV."),
 simtask=["\\(k_n/k_p=1\\) va \\(V_{Tn}=|V_{Tp}|\\) da \\(V_M=V_{DD}/2\\) ekanini tekshiring; nisbatni 3 ga oshirib, \\(V_M\\) siljishini tushuntiring.", "Nurlanish dozasini 0 dan 300 krad gacha oshirib, \\(V_M\\) va shovqin zahiralari o‘zgarishini jadvalga yozing.", "\\(V_{DD}\\) ni 3,3 V dan 1 V ga kamaytirib, dinamik quvvat necha marta kamayishini hisoblang."],
 mistakes=[("“KMOP umuman quvvat iste’mol qilmaydi.”", "Statik quvvat kichik, ammo dinamik (\\(\\alpha CV^2f\\)), qisqa tutashuv va oqish quvvati mavjud."),
           ("“Radiatsiya faqat xotira xatolariga olib keladi.”", "TID parametrlarning asta siljishiga, DD esa bipolyar va optoelektron asboblar degradatsiyasiga olib keladi."),
           ("“Qalin oksid radiatsiyadan yaxshi himoya qiladi.”", "Aksincha, \\(\\Delta V_T\\propto d_{ox}^2\\); qalin izolyatsiya oksidlari TID ga eng sezgir joy.")],
 ai="""Sen kosmik elektronika bo‘yicha muhandissan. Kichik sun’iy yo‘ldosh (LEO, 500 km, 3 yil) uchun mikrokontroller tanlanmoqda.
1) Kutilayotgan TID darajasini sifat jihatidan baholashda nimalarni hisobga olish kerakligini tushuntir (aniq raqam berolmasang, SPENVIS/OMERE kabi vositalarni ko‘rsat).
2) COTS va rad-hard IS ni TID, SEL, SEU va narx bo‘yicha solishtir.
3) Xotira uchun TMR va ECC ni Python’da modellashtirib, SEU tezligi berilganda xato ehtimolini hisoblovchi kod yoz.""",
 quiz=[("KMOP invertorda statik tok deyarli nol, chunki:", ["tranzistorlar juda kichik", "har bir holatda bitta tranzistor yopiq", "\\(V_{DD}\\) past", "zatvor oksidi qalin"], 1, "To‘ldiruvchi juftlik."),
       ("\\(V_{DD}\\) 2 marta kamaytirilsa, dinamik quvvat:", ["2 marta kamayadi", "4 marta kamayadi", "o‘zgarmaydi", "8 marta kamayadi"], 1, "\\(P\\propto V_{DD}^2\\)."),
       ("TID ta’sirida n-MOSFET \\(V_T\\):", ["ortadi", "kamayadi (manfiy siljish)", "o‘zgarmaydi", "nolga teng bo‘ladi"], 1, "Oksidda tutilgan musbat zaryad."),
       ("SEL (latch-up) qaysi strukturaga bog‘liq?", ["parazit p-n-p-n (tiristor)", "Shottki diodi", "ZAA", "kondensator"], 0, "KMOP dagi parazit tiristor.")],
 blits=["Bandgap tayanch manbai qanday ishlaydi?", "Nima uchun SOI latch-up ga chidamli?", "ELT tranzistor TID ga nega chidamli?", "SEU va SEL farqi?", "Messenger formulasi nimani ifodalaydi?"]
))
