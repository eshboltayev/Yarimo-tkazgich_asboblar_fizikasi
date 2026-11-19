"""M1–M8 ma'ruzalar mazmuni."""

L = []

L.append(dict(
 n=1, short="Asosiy tenglamalar tizimi", sim="fermi", refs=[1, 2, 4], intl=["sze", "pierret", "neamen"], tn=["TN1", "TN13"],
 title="Yarimo‘tkazgich ishlashi uchun asosiy tenglamalar tizimi",
 goal="Yarimo‘tkazgichli asboblarni tahlil qilishda qo‘llaniladigan beshta tayanch tenglama — zaryad tashuvchilar statistikasi, dreyf-diffuziya toki, Puasson va uzluksizlik tenglamalarini yagona tizim sifatida tushuntirish.",
 outcomes=["ruxsat etilgan zonalardagi elektron va teshiklar konsentratsiyasini \\(N_c, N_v, E_F\\) orqali hisoblaydi;",
           "xususiy konsentratsiya \\(n_i\\) ning harorat va taqiqlangan zona kengligiga bog‘liqligini tahlil qiladi;",
           "dreyf va diffuziya toklarini ajratadi, Eynshteyn munosabatini qo‘llaydi;",
           "Puasson va uzluksizlik tenglamalarini asbob modelining chegaraviy masalasi sifatida yozadi."],
 plan=["Zonalardagi holatlar zichligi va Fermi–Dirak taqsimoti", "Muvozanat konsentratsiyalari, massalar ta’siri qonuni", "Dreyf va diffuziya toklari, Eynshteyn munosabati", "Puasson tenglamasi", "Uzluksizlik tenglamasi va asosiy tenglamalar tizimi"],
 terms=["holatlar zichligi", "Fermi sathi", "xususiy konsentratsiya \\(n_i\\)", "harakatchanlik \\(\\mu\\)", "diffuziya koeffitsiyenti \\(D\\)", "rekombinatsiya tezligi", "elektroneytrallik"],
 theory=[
  ("Zaryad tashuvchilar konsentratsiyasi", r"""<p>O‘tkazuvchanlik zonasidagi elektronlar va valent zonadagi teshiklar konsentratsiyasi holatlar zichligi bilan Fermi–Dirak taqsimotining ko‘paytmasini integrallash orqali topiladi. Aynimagan yarimo‘tkazgichda (\(E_c-E_F \gg kT\)) Boltsman yaqinlashuvi o‘rinli:</p>
$$n_0 = N_c\exp\!\left(-\frac{E_c-E_F}{kT}\right),\qquad p_0 = N_v\exp\!\left(-\frac{E_F-E_v}{kT}\right)$$
<p>Bu yerda \(N_c = 2\left(\frac{2\pi m_n^* kT}{h^2}\right)^{3/2}\) va \(N_v\) — zonalarning effektiv holatlar zichligi (Si uchun 300 K da \(N_c\approx2{,}8\cdot10^{19}\), \(N_v\approx1{,}04\cdot10^{19}\) sm⁻³). Ikkala ifodani ko‘paytirsak, Fermi sathiga bog‘liq bo‘lmagan <b>massalar ta’siri qonuni</b> kelib chiqadi:</p>
$$n_0p_0 = n_i^2 = N_cN_v\exp\!\left(-\frac{E_g}{kT}\right)$$
<p>Kirishmali n-tip yarimo‘tkazgichda to‘liq ionlanish va elektroneytrallik shartidan \(n_0 = \frac{N_d}{2}+\sqrt{\frac{N_d^2}{4}+n_i^2}\approx N_d\), \(p_0=n_i^2/n_0\); Fermi sathi \(E_F-E_i = kT\ln(n_0/n_i)\).</p>"""),
  ("Dreyf va diffuziya toklari", r"""<p>Elektr maydonida zaryad tashuvchilar o‘rtacha dreyf tezligi \(v_d=\mu E\) bilan harakatlanadi, konsentratsiya gradiyenti esa diffuziya oqimini yuzaga keltiradi. Bir o‘lchamli holda to‘liq tok zichliklari:</p>
$$J_n = qn\mu_nE + qD_n\frac{dn}{dx},\qquad J_p = qp\mu_pE - qD_p\frac{dp}{dx}$$
<p>Diffuziya koeffitsiyenti va harakatchanlik <b>Eynshteyn munosabati</b> bilan bog‘langan: \(D/\mu = kT/q\) (300 K da 25,85 mV). Solishtirma o‘tkazuvchanlik \(\sigma = q(n\mu_n+p\mu_p)\).</p>"""),
  ("Puasson tenglamasi", r"""<p>Elektrostatik potensial \(\varphi\) fazoviy zaryad zichligi bilan Puasson tenglamasi orqali bog‘lanadi:</p>
$$\frac{d^2\varphi}{dx^2} = -\frac{dE}{dx} = -\frac{\rho}{\varepsilon_s} = -\frac{q}{\varepsilon_s}\left(p - n + N_d^+ - N_a^-\right)$$
<p>Bu tenglama barcha kontakt hodisalarida (p-n o‘tish, Shottki bareri, MDYa strukturasi) zonalar egilishi va kambag‘allashgan qatlam kengligini aniqlaydi.</p>"""),
  ("Uzluksizlik tenglamasi", r"""<p>Zaryad saqlanish qonunining differensial ko‘rinishi — uzluksizlik tenglamalari — generatsiya \(G\) va rekombinatsiya \(R\) jarayonlarini hisobga oladi:</p>
$$\frac{\partial n}{\partial t} = \frac{1}{q}\frac{\partial J_n}{\partial x} + G_n - R_n,\qquad \frac{\partial p}{\partial t} = -\frac{1}{q}\frac{\partial J_p}{\partial x} + G_p - R_p$$
<p>Kichik injeksiyada \(R_p = (p-p_0)/\tau_p\). Statsionar holda diffuziya uzunligi \(L_p=\sqrt{D_p\tau_p}\) paydo bo‘ladi.</p>
<div class="callout info"><b>Asosiy tenglamalar tizimi</b>Puasson tenglamasi + ikkita tok tenglamasi + ikkita uzluksizlik tenglamasi = \(\varphi(x), n(x), p(x)\) uchun yopiq tizim. Barcha asbob modellari (SPICE, TCAD, COMSOL) aynan shu tizimni sonli yechadi.</div>""")],
 example=("n-Si: konsentratsiya, Fermi sathi va o‘tkazuvchanlik",
  r"Si namuna \(N_d=10^{16}\) sm⁻³ fosfor bilan legirlangan, \(T=300\) K, \(n_i=10^{10}\) sm⁻³, \(\mu_n=1350\) sm²/(V·s). \(n_0, p_0, E_F-E_i, \sigma, \rho\) va \(E=10\) V/sm maydondagi dreyf toki zichligini toping.",
  r"\(n_0\approx N_d=10^{16}\) sm⁻³; \(p_0=n_i^2/n_0=10^{4}\) sm⁻³. \(E_F-E_i=0{,}02585\ln(10^6)=0{,}357\) eV. \(\sigma=qn\mu_n=1{,}602\cdot10^{-19}\cdot10^{16}\cdot1350=2{,}16\) S/sm, \(\rho=0{,}46\) Ω·sm. \(J=\sigma E=21{,}6\) A/sm². Eynshteyn munosabatidan \(D_n=1350\cdot0{,}02585\approx34{,}9\) sm²/s."),
 simtask=["Si uchun \\(N_d\\) ni 10¹⁴ dan 10¹⁸ sm⁻³ gacha o‘zgartirib, \\(E_F-E_i\\) qanday o‘sishini jadvalga yozing va \\(kT\\ln(N_d/n_i)\\) bilan solishtiring.",
          "\\(N_d=10^{15}\\) sm⁻³ da haroratni oshirib, xususiy o‘tkazuvchanlik boshlanadigan haroratni (\\(n_i\\approx N_d\\)) toping. Si, Ge va GaAs uchun natijalarni taqqoslang.",
          "Nima uchun yuqori haroratli elektronika uchun GaAs (va SiC, GaN) qulayroq ekanini grafik asosida izohlang."],
 mistakes=[("“Kirishma qo‘shilsa \\(n_i\\) o‘zgaradi.”", "\\(n_i\\) faqat material va haroratga bog‘liq; kirishma \\(n_0\\) va \\(p_0\\) ni o‘zgartiradi, ko‘paytma \\(n_0p_0=n_i^2\\) saqlanadi."),
           ("“Diffuziya toki elektr maydoni tufayli yuzaga keladi.”", "Diffuziya toki konsentratsiya gradiyenti bilan aniqlanadi va maydon yo‘q joyda ham oqadi."),
           ("“Uzluksizlik tenglamasi faqat statsionar holat uchun.”", "U vaqtga bog‘liq jarayonlarni (o‘tish jarayonlari, fotoo‘tkazuvchanlik so‘nishi) ham tavsiflaydi.")],
 ai="""Sen yarimo‘tkazgichlar fizikasi bo‘yicha sokratik repetitorsan. Mavzu: yarimo‘tkazgichning asosiy tenglamalar tizimi.
1) Puasson, tok va uzluksizlik tenglamalarini yozib, har bir hadning fizik ma’nosini tushuntir.
2) n-Si (N_d = 1e16 sm^-3, 300 K) uchun n0, p0, E_F − E_i ni hisobla — har bir qadamda birliklarni ko‘rsat.
3) Python (numpy, matplotlib) kodida n_i(T) ni 200–700 K oralig‘ida Si, Ge, GaAs uchun chiz; E_g(T) uchun Varshni formulasidan foydalan va parametrlar manbasini ko‘rsat.
4) Javobingda men tekshirishim kerak bo‘lgan 3 ta “xavfli” joyni (taxmin yoki soddalashtirish) alohida sanab ber.""",
 quiz=[("Massalar ta’siri qonuni \\(n_0p_0=n_i^2\\) qachon o‘rinli?", ["Faqat xususiy yarimo‘tkazgichda", "Termodinamik muvozanatdagi aynimagan yarimo‘tkazgichda", "Faqat kuchli injeksiyada", "Faqat metallarda"], 1, "Qonun muvozanat va Boltsman yaqinlashuvidan kelib chiqadi; nomuvozanatda kvazi-Fermi sathlari kiritiladi."),
       ("Eynshteyn munosabati qaysi?", ["\\(D=\\mu kT/q\\)", "\\(D=\\mu q/kT\\)", "\\(D=\\mu\\tau\\)", "\\(D=L/\\tau\\)"], 0, "\\(D/\\mu=kT/q\\approx25{,}85\\) mV (300 K)."),
       ("Puasson tenglamasida o‘ng tomondagi zaryad zichligi nimalardan iborat?", ["Faqat elektronlar", "\\(q(p-n+N_d^+-N_a^-)\\)", "Faqat ionlangan donorlar", "Tok zichligi"], 1, "Erkin tashuvchilar va ionlangan kirishmalar birgalikda fazoviy zaryadni hosil qiladi."),
       ("n-Si da \\(N_d\\) 100 marta oshirilsa, \\(E_F-E_i\\) qanchaga o‘zgaradi (300 K)?", ["≈ 60 meV", "≈ 119 meV", "≈ 26 meV", "o‘zgarmaydi"], 1, "\\(\\Delta=kT\\ln100=0{,}02585\\cdot4{,}605\\approx0{,}119\\) eV.")],
 blits=["Nima uchun Si da \\(N_v<N_c\\)?", "Kompensatsiyalangan yarimo‘tkazgich deb nimaga aytiladi?", "Harakatchanlik qaysi sochilish mexanizmlari bilan cheklanadi?", "Diffuziya uzunligi qanday o‘lchanadi?", "Uzluksizlik tenglamasida \\(G\\) hadi qachon muhim?"]
))

L.append(dict(
 n=2, short="Metall–yarimo‘tkazgich kontakti", sim="schottky", refs=[2, 3, 4], intl=["rhoderick", "sze", "schroder"], tn=["TN2", "TN13", "TN19"],
 title="Metall–yarimo‘tkazgich kontakti. Shottki to‘sig‘i va omik kontaktlar",
 goal="Metall–yarimo‘tkazgich kontaktida potensial taqsimoti, Shottki bareri va omik kontakt hosil bo‘lish shartlarini, termoelektron emissiya (Richardson) asosidagi VAX va kontakt sig‘imini o‘rganish.",
 outcomes=["chiqish ishi va elektronga moyillik orqali ideal barer balandligini hisoblaydi;", "boyitilgan va kambag‘allashgan kontaktlarni zonaviy diagramma bilan farqlaydi;", "Richardson formulasidan Shottki diodi to‘yinish tokini hisoblaydi;", "omik kontakt uchun tunnel o‘tish va solishtirma kontakt qarshiligi mezonlarini tushuntiradi."],
 plan=["Chiqish ishi, elektronga moyillik, kontakt potensiallar farqi", "Kontakt yaqinida potensial taqsimoti", "Boyitilgan va kambag‘allashgan kontaktlar", "Termoelektron emissiya, Richardson formulasi, VAX", "Omik kontaktlar, kontakt sig‘imi"],
 terms=["chiqish ishi \\(\\Phi_m\\)", "elektronga moyillik \\(\\chi\\)", "Shottki bareri \\(\\varphi_B\\)", "Richardson doimiysi \\(A^*\\)", "Fermi sathining mahkamlanishi", "omik kontakt", "tunnel emissiya"],
 theory=[
  ("Kontakt hosil bo‘lishi va barer balandligi", r"""<p>Metall va n-tip yarimo‘tkazgich tutashtirilganda elektronlar Fermi sathlari tenglashguncha kichik chiqish ishiga ega tomondan kattasiga o‘tadi. \(\Phi_m>\Phi_s\) bo‘lsa, yarimo‘tkazgich sirtida musbat ionlangan donorlardan iborat <b>kambag‘allashgan qatlam</b> hosil bo‘ladi, zonalar yuqoriga egiladi. Ideal (Shottki–Mott) model bo‘yicha:</p>
$$q\varphi_B = \Phi_m - \chi,\qquad qV_{bi} = q\varphi_B - (E_c-E_F)$$
<p>Real kontaktlarda sirt holatlari Fermi sathini taqiqlangan zonaning taxminan 1/3 qismida “mahkamlaydi” (Bardeen modeli), shu sababli \(\varphi_B\) metall turiga sust bog‘liq: n-Si uchun odatda 0,5–0,85 eV.</p>"""),
  ("Potensial taqsimoti va sig‘im", r"""<p>Kambag‘allashgan qatlam yaqinlashuvida Puasson tenglamasini yechib, kenglik va maksimal maydon topiladi:</p>
$$W=\sqrt{\frac{2\varepsilon_s\,(V_{bi}-V)}{qN_d}},\qquad E_{max}=\frac{qN_dW}{\varepsilon_s},\qquad \frac{C}{A}=\frac{\varepsilon_s}{W}$$
<p>\(1/C^2\) ning \(V\) ga chiziqli bog‘liqligidan \(N_d\) (qiyalik) va \(V_{bi}\) (absissa bilan kesishish) aniqlanadi — bu C–V usulining asosi.</p>"""),
  ("Termoelektron emissiya va Richardson formulasi", r"""<p>Shottki diodida tok asosiy tashuvchilar — elektronlarning barer ustidan o‘tishi bilan aniqlanadi:</p>
$$J = J_s\left[\exp\!\left(\frac{qV}{nkT}\right)-1\right],\qquad J_s = A^*T^2\exp\!\left(-\frac{q\varphi_B}{kT}\right)$$
<p>\(A^* = \dfrac{4\pi q m^* k^2}{h^3}\) — effektiv Richardson doimiysi (erkin elektron uchun 120 A/(sm²·K²), n-Si uchun ≈ 112). Shottki diodida asosiy bo‘lmagan tashuvchilar yig‘ilmaydi, shuning uchun u juda tez ulanadi va to‘g‘ri yo‘nalishda 0,2–0,4 V past kuchlanish tushuvi beradi.</p>"""),
  ("Omik kontaktlar", r"""<p>Omik kontakt tok yo‘nalishiga bog‘liq bo‘lmagan kichik qarshilikka ega bo‘lishi kerak. Ikki yo‘l bor: (1) \(\Phi_m<\Phi_s\) (n-tip uchun) — boyitilgan kontakt; (2) sirtni kuchli legirlash (\(N_d>10^{19}\) sm⁻³) — barer juda yupqa bo‘lib, elektronlar <b>tunnel</b> o‘tadi. Sifat ko‘rsatkichi — solishtirma kontakt qarshiligi \(\rho_c\) (Ω·sm²); tunnel rejimida \(\rho_c\propto\exp\!\left(\frac{2\sqrt{\varepsilon_s m^*}}{\hbar}\frac{\varphi_B}{\sqrt{N_d}}\right)\).</p>""")],
 example=("Au/n-Si Shottki diodi parametrlari",
  r"n-Si: \(N_d=10^{16}\) sm⁻³, o‘lchangan \(\varphi_B=0{,}72\) eV, \(A^*=112\) A/(sm²K²), \(T=300\) K, \(N_c=2{,}8\cdot10^{19}\) sm⁻³. \(J_s\), \(J=1\) A/sm² uchun kuchlanish, \(V_{bi}\) va \(V=0\) dagi \(W\) ni toping.",
  r"\(J_s=112\cdot300^2\cdot e^{-0{,}72/0{,}02585}=1{,}008\cdot10^7\cdot8{,}0\cdot10^{-13}\approx8{,}1\cdot10^{-6}\) A/sm². \(V=kT/q\cdot\ln(J/J_s)=0{,}02585\cdot\ln(1{,}24\cdot10^5)\approx0{,}30\) V (p-n diodda ≈ 0,6–0,7 V). \(E_c-E_F=kT\ln(N_c/N_d)=0{,}205\) eV ⇒ \(V_{bi}=0{,}515\) V. \(W=\sqrt{2\cdot1{,}036\cdot10^{-12}\cdot0{,}515/(1{,}602\cdot10^{-19}\cdot10^{16})}\approx0{,}26\) mkm."),
 simtask=["\\(\\varphi_B\\) ni 0,5 dan 0,85 eV gacha o‘zgartirib, \\(J_s\\) necha tartibga kamayishini aniqlang; har 0,06 eV ga ≈ 10 marta o‘zgarishini tekshiring.",
          "Haroratni 250–400 K oralig‘ida o‘zgartirib, \\(\\ln(J_s/T^2)\\) ni \\(1/T\\) ga qarab chizing (Richardson grafigi) va qiyalikdan \\(\\varphi_B\\) ni qayta tiklang.",
          "Shottki va p-n diod grafiklarini solishtirib, impulsli kuch manbalarida Shottki diodining afzalligini asoslang."],
 mistakes=[("“Barer balandligi faqat \\(\\Phi_m-\\chi\\) ga teng.”", "Real kontaktda sirt holatlari tufayli Fermi sathi mahkamlanadi; \\(\\varphi_B\\) tajribada C–V, I–V yoki fotoemissiya bilan o‘lchanadi."),
           ("“Omik kontakt — barersiz kontakt.”", "Ko‘pincha barer bor, lekin u shunchalik yupqaki, tunnel o‘tish kichik \\(\\rho_c\\) beradi."),
           ("“Shottki diodi asosiy bo‘lmagan tashuvchilar bilan ishlaydi.”", "Tok asosiy tashuvchilar termoemissiyasi bilan aniqlanadi — shuning uchun diffuzion sig‘im va qayta tiklanish vaqti juda kichik.")],
 ai="""Sen metall–yarimo‘tkazgich kontaktlari bo‘yicha mutaxassissan.
1) Al, Ti, Au, Pt uchun chiqish ishi qiymatlarini manbasi bilan ber va n-Si (χ = 4,05 eV) bilan ideal φ_B ni hisobla.
2) Nima uchun tajribadagi φ_B bu qiymatlardan farq qilishini Bardeen modeli asosida tushuntir.
3) Richardson grafigi (ln(J_s/T²) − 1/T) dan φ_B va A* ni topadigan Python kodini yoz; sintetik ma’lumotga 2% shovqin qo‘sh.
Qoidalar: har bir son uchun birlik va manba; taxminiy qiymatlarni “taxmin” deb belgilab qo‘y.""",
 quiz=[("Ideal Shottki–Mott modelida n-tip uchun barer balandligi:", ["\\(\\Phi_m+\\chi\\)", "\\(\\Phi_m-\\chi\\)", "\\(E_g-\\Phi_m\\)", "\\(\\chi-E_g\\)"], 1, "\\(q\\varphi_B=\\Phi_m-\\chi\\)."),
       ("Richardson formulasida \\(J_s\\) haroratga qanday bog‘liq?", ["\\(\\propto T\\)", "\\(\\propto T^2e^{-q\\varphi_B/kT}\\)", "\\(\\propto T^{3/2}\\)", "bog‘liq emas"], 1, "Termoelektron emissiya tok zichligi."),
       ("Omik kontakt olishning eng keng tarqalgan usuli:", ["Oksid qatlamini qalinlashtirish", "Sirtni kuchli legirlab tunnel o‘tishni ta’minlash", "Haroratni pasaytirish", "\\(\\varphi_B\\) ni oshirish"], 1, "\\(N_d>10^{19}\\) sm⁻³ da barer yupqalashadi."),
       ("\\(1/C^2-V\\) grafigining qiyaligi nimani beradi?", ["\\(\\varphi_B\\) ni", "kirishma konsentratsiyasini", "harakatchanlikni", "\\(A^*\\) ni"], 1, "Qiyalik \\(=2/(q\\varepsilon_sN_dA^2)\\).")],
 blits=["Fermi sathining mahkamlanishi nimaga olib keladi?", "Shottki diodining teskari toki p-n dioddan nega katta?", "Kontakt sig‘imi kuchlanishga qanday bog‘liq?", "Silitsidlar (TiSi₂, NiSi) nima uchun ishlatiladi?", "Ideallik koeffitsiyenti \\(n>1\\) nimani bildiradi?"]
))

L.append(dict(
 n=3, short="p-n o‘tish xususiyatlari", sim="pn", refs=[1, 2, 3], intl=["sze", "neamen", "streetman"], tn=["TN1", "TN2", "TN13"],
 title="P-n o‘tishning xususiyatlari. Zonaviy diagrammalar va ideal o‘tish VAXi",
 goal="P-n o‘tishda zaryad tashuvchilar taqsimoti, kontakt potensiallar farqi, kambag‘allashgan qatlam, diffuzion va dreyf toklar muvozanatini o‘rganish hamda ideal o‘tish VAXini (Shokli tenglamasi) keltirib chiqarish.",
 outcomes=["p-n o‘tishning muvozanat va kuchlanish ostidagi zonaviy diagrammasini chizadi;", "\\(V_{bi}\\), \\(W\\), \\(x_n\\), \\(x_p\\), \\(E_{max}\\) va to‘siq sig‘imini hisoblaydi;", "ideal diod VAXini keltirib chiqaradi va \\(J_s\\) ni material parametrlari orqali ifodalaydi;", "diffuzion va dreyf toklarning muvozanati tushunchasini izohlaydi."],
 plan=["Muvozanatdagi p-n o‘tish: zonaviy diagramma", "Kontakt potensiallar farqi", "Kambag‘allashgan qatlam yaqinlashuvi", "Kuchlanish ostida: kvazi-Fermi sathlari", "Ideal o‘tish VAXi (Shokli)"],
 terms=["kontakt potensiallar farqi \\(V_{bi}\\)", "kambag‘allashgan (fazoviy zaryad) qatlam", "keskin o‘tish", "kvazi-Fermi sathi", "injeksiya", "ekstraksiya", "to‘yinish toki"],
 theory=[
  ("Muvozanat va kontakt potensiallar farqi", r"""<p>p va n sohalar tutashganda elektronlar n-sohadan p-sohaga, teshiklar teskari yo‘nalishda diffuziyalanadi. Natijada ionlangan aktseptor (–) va donorlardan (+) iborat fazoviy zaryad qatlami va unga mos ichki maydon hosil bo‘ladi. Muvozanatda har bir tashuvchi turi uchun diffuziya va dreyf toklari teng va qarama-qarshi, Fermi sathi butun strukturada bir xil:</p>
$$V_{bi}=\frac{kT}{q}\ln\frac{N_aN_d}{n_i^2}$$"""),
  ("Kambag‘allashgan qatlam", r"""<p>Keskin o‘tish va to‘liq kambag‘allashish yaqinlashuvida Puasson tenglamasi ikki kvadratik potensial bo‘lagini beradi. Zaryad neytralligi \(N_ax_p=N_dx_n\) va natijalar:</p>
$$W = x_n+x_p=\sqrt{\frac{2\varepsilon_s}{q}\frac{N_a+N_d}{N_aN_d}\,(V_{bi}-V)},\qquad E_{max}=\frac{qN_dx_n}{\varepsilon_s}$$
<p>Bir tomonlama (\(N_a\gg N_d\)) o‘tishda qatlam deyarli butunlay kuchsiz legirlangan tomonga tarqaladi. To‘siq (barer) sig‘imi \(C_b=\varepsilon_sA/W\propto(V_{bi}-V)^{-1/2}\).</p>"""),
  ("Kuchlanish ostida: kvazi-Fermi sathlari", r"""<p>To‘g‘ri kuchlanish \(V>0\) to‘siqni \(q(V_{bi}-V)\) gacha pasaytiradi, asosiy bo‘lmagan tashuvchilar injeksiyasi boshlanadi. Qatlam chegarasida (Boltsman shartlari):</p>
$$p_n(x_n)=p_{n0}\exp\!\left(\frac{qV}{kT}\right),\qquad n_p(-x_p)=n_{p0}\exp\!\left(\frac{qV}{kT}\right)$$
<p>Elektron va teshiklar uchun alohida kvazi-Fermi sathlari \(E_{Fn}\), \(E_{Fp}\) kiritiladi: \(E_{Fn}-E_{Fp}=qV\).</p>"""),
  ("Ideal o‘tish VAXi", r"""<p>Neytral sohalarda injeksiyalangan tashuvchilar diffuziyalanib rekombinatsiyalanadi (\(\Delta p\propto e^{-x/L_p}\)). Diffuzion toklarni qatlam chegarasida qo‘shib, Shokli tenglamasi olinadi:</p>
$$J=J_s\left[\exp\!\left(\frac{qV}{kT}\right)-1\right],\qquad J_s = qn_i^2\left(\frac{D_p}{L_pN_d}+\frac{D_n}{L_nN_a}\right)$$
<p>Teskari kuchlanishda tok \(-J_s\) ga to‘yinadi; \(n_i^2\propto e^{-E_g/kT}\) bo‘lgani uchun \(J_s\) haroratga kuchli bog‘liq (Si da har 10 K da taxminan 2–3 marta ortadi).</p>""")],
 example=("Keskin Si p⁺-n o‘tish parametrlari",
  r"\(N_a=10^{17}\), \(N_d=10^{16}\) sm⁻³, \(n_i=10^{10}\) sm⁻³, \(\varepsilon_s=1{,}036\cdot10^{-12}\) F/sm, \(V=0\). \(V_{bi}, W, x_n, x_p, E_{max}, C_b/A\) ni toping.",
  r"\(V_{bi}=0{,}02585\ln(10^{33}/10^{20})=0{,}774\) V. \(W=\sqrt{\frac{2\cdot1{,}036\cdot10^{-12}}{1{,}602\cdot10^{-19}}\cdot\frac{1{,}1\cdot10^{17}}{10^{33}}\cdot0{,}774}\approx3{,}32\cdot10^{-5}\) sm = 0,332 mkm. \(x_n=W\frac{N_a}{N_a+N_d}=0{,}302\) mkm, \(x_p=0{,}030\) mkm. \(E_{max}=qN_dx_n/\varepsilon_s\approx4{,}7\cdot10^4\) V/sm. \(C_b/A=\varepsilon_s/W\approx31\) nF/sm²."),
 simtask=["Misoldagi qiymatlarni simulyatorda o‘rnatib, natijalarni tekshiring; so‘ng \\(V=-5\\) V da \\(W\\) va \\(C_j\\) ni yozing.",
          "\\(N_a\\) ni 10¹⁹ ga oshirib (bir tomonlama o‘tish), \\(W\\) qaysi tomonga tarqalishini kuzating.",
          "To‘g‘ri kuchlanishda kvazi-Fermi sathlari orasidagi farq \\(qV\\) ga tengligini grafikdan tekshiring."],
 mistakes=[("“Muvozanatda o‘tish orqali hech qanday tok oqmaydi.”", "Diffuzion va dreyf toklar alohida-alohida katta, lekin ular o‘zaro kompensatsiyalanadi — natijaviy tok nol."),
           ("“\\(V_{bi}\\) ni voltmetr bilan o‘lchash mumkin.”", "Kontakt potensiallar farqi metall kontaktlardagi potensial sakrashlar bilan kompensatsiyalanadi; uni faqat C–V yoki fotoelektrik usullar bilan aniqlash mumkin."),
           ("“To‘g‘ri yo‘nalishda tok qatlam ichida dreyf hisobiga oqadi.”", "Ideal modelda tok neytral sohalardagi asosiy bo‘lmagan tashuvchilar diffuziyasi bilan aniqlanadi.")],
 ai="""Sen p-n o‘tish fizikasi bo‘yicha o‘qituvchisan. Men keskin Si p-n o‘tish (N_a = 1e17, N_d = 1e16 sm^-3) ni hisobladim: V_bi = 0,774 V, W = 0,332 mkm.
1) Hisobimni o‘lchamlilik va kambag‘allashish yaqinlashuvi shartlari bo‘yicha tekshir; to‘g‘ri bo‘lsa ham, qaysi soddalashtirishlar qilinganini ayt.
2) Puasson tenglamasini 1D chekli ayirmalar bilan yechadigan Python skriptini yoz (Nyuton iteratsiyasi), natijani analitik W bilan solishtir.
3) Natijalar orasidagi farq qayerdan kelib chiqishini (Debay uzunligi, qatlam chegarasining “dumi”) tushuntir.""",
 quiz=[("Muvozanatdagi p-n o‘tishda qaysi kattalik butun struktura bo‘ylab o‘zgarmas?", ["\\(E_c\\)", "\\(E_F\\)", "\\(E_i\\)", "potensial \\(\\varphi\\)"], 1, "Muvozanatda Fermi sathi yagona."),
       ("Teskari kuchlanish oshganda \\(W\\) qanday o‘zgaradi?", ["\\(\\propto(V_{bi}-V)^{1/2}\\) bo‘yicha ortadi", "kamayadi", "o‘zgarmaydi", "chiziqli kamayadi"], 0, "Keskin o‘tishda \\(W\\propto\\sqrt{V_{bi}-V}\\)."),
       ("\\(N_a\\gg N_d\\) bo‘lsa, qatlam asosan qayerda joylashadi?", ["p-sohada", "n-sohada", "teng taqsimlanadi", "metall kontaktda"], 1, "\\(N_ax_p=N_dx_n\\) ⇒ \\(x_n\\gg x_p\\)."),
       ("Ideal diodda \\(J_s\\) qaysi kattalikka eng kuchli bog‘liq?", ["\\(n_i^2\\) orqali haroratga", "kontakt maydoniga", "metall turiga", "kuchlanishga"], 0, "\\(J_s\\propto n_i^2\\propto T^3e^{-E_g/kT}\\).")],
 blits=["Kvazi-Fermi sathi nima?", "Bir tomonlama o‘tish qayerda qo‘llanadi?", "Debay uzunligi nima uchun muhim?", "Teskari tok nima sababli to‘yinadi?", "Silliq (chiziqli) o‘tishda \\(W\\) kuchlanishga qanday bog‘liq?"]
))

L.append(dict(
 n=4, short="P-n o‘tishli diodlar", sim="diode", refs=[1, 3, 5], intl=["sze", "sedra", "baliga"], tn=["TN3", "TN4", "TN11", "TN19"],
 title="P-n o‘tishli yarimo‘tkazgich diodlar: haqiqiy VAX, turlari, o‘tish jarayonlari",
 goal="Haqiqiy diod VAXining ideal modeldan chetlanish sabablari, diodlar turlari, ulanish-uzilish (o‘tish) jarayonlari va chastotaviy xususiyatlarini o‘rganish.",
 outcomes=["generatsiya-rekombinatsiya toki, yuqori injeksiya va ketma-ket qarshilik ta’sirini VAXda ajratadi;", "ideallik koeffitsiyenti \\(n\\) ni tajriba grafikdan aniqlaydi;", "teskari tiklanish vaqti va diffuzion sig‘imni hisoblaydi;", "datasheet asosida vazifaga mos diod turini tanlaydi."],
 plan=["Haqiqiy VAX: rekombinatsiya toki, yuqori injeksiya, \\(R_s\\)", "Haroratga bog‘liqlik", "Diod turlari: to‘g‘rilagich, Shottki, varikap, PIN, impulsli", "O‘tish jarayonlari: teskari tiklanish", "Chastotaviy xususiyatlar va kichik signal modeli"],
 terms=["ideallik koeffitsiyenti", "generatsiya-rekombinatsiya toki", "diffuzion sig‘im", "teskari tiklanish vaqti \\(t_{rr}\\)", "varikap", "PIN-diod", "differensial qarshilik"],
 theory=[
  ("Haqiqiy VAX", r"""<p>Real diod toki bir necha komponentdan iborat:</p>
$$I = I_{s}\left(e^{qV/kT}-1\right)+I_{gr}\left(e^{qV/2kT}-1\right),\qquad V_{tash}=V+IR_s$$
<p>Kichik kuchlanishlarda fazoviy zaryad qatlamidagi rekombinatsiya (\(n\approx2\)), o‘rtacha kuchlanishlarda diffuziya (\(n\approx1\)), katta toklarda yuqori injeksiya (\(n\to2\)) va ketma-ket qarshilik ustunlik qiladi. Umumlashgan ifoda: \(I=I_s\left[\exp\frac{q(V-IR_s)}{nkT}-1\right]\). Teskari yo‘nalishda generatsiya toki \(J_{gen}=qn_iW/2\tau_g\) kuchlanish bilan \(\sqrt{V}\) kabi o‘sadi.</p>"""),
  ("Haroratga bog‘liqlik", r"""<p>O‘zgarmas tokda to‘g‘ri kuchlanish harorat ortishi bilan kamayadi:</p>
$$\frac{dV}{dT}\Big|_I\approx\frac{V-\left(E_g/q+3kT/q\right)}{T}\approx-2\ \text{mV/K (Si)}$$
<p>Bu xossa harorat datchiklarida (diodli termometrlar, mikrosxemalardagi PTAT manbalari) ishlatiladi.</p>"""),
  ("Diodlar turlari", r"""<ul><li><b>To‘g‘rilagich diodlar</b> — katta tok va teskari kuchlanish (\(V_{RRM}\)), sekin.</li><li><b>Shottki diodlari</b> — past \(V_F\), juda tez, lekin katta teskari tok.</li><li><b>Varikaplar</b> — to‘siq sig‘imi \(C\propto(V_{bi}-V)^{-m}\) dan sozlanadigan sig‘im sifatida (\(m=1/2\) keskin, \(1/3\) chiziqli, giperkeskin \(m>1/2\)).</li><li><b>PIN-diodlar</b> — keng i-qatlam; YuCh kalitlari, fotodetektorlar.</li><li><b>Impulsli va zaryad to‘planishli diodlar</b> — kichik \(\tau\) (Au yoki Pt bilan legirlash).</li></ul>"""),
  ("O‘tish jarayonlari va chastotaviy xususiyatlar", r"""<p>To‘g‘ri yo‘nalishda neytral sohalarda zaryad \(Q=\tau I_F\) to‘planadi. Diod keskin teskari yo‘nalishga ulanganda bu zaryad so‘riladi; zaryad saqlanish bosqichining davomiyligi:</p>
$$t_s\approx\tau\ln\!\left(1+\frac{I_F}{I_R}\right)$$
<p>Kichik signal modeli: differensial qarshilik \(r_d=nkT/(qI)\), diffuzion sig‘im \(C_d=\tau I/(kT/q)\) (bir tomonlama o‘tish uchun \(\tau/2\) koeffitsiyent bilan) va to‘siq sig‘imi \(C_b\). Kesish chastotasi \(f\approx1/(2\pi r_d(C_d+C_b))\).</p>""")],
 example=("Impulsli diodning tiklanish vaqti va sig‘imi",
  r"Si diod: \(\tau=10\) ns, \(I_F=10\) mA, \(I_R=10\) mA, \(n=1\), 300 K. \(t_s\), \(r_d\) va \(C_d\) (\(C_d=\tau I/V_T\) ko‘rinishda) ni toping.",
  r"\(t_s=10\ \text{ns}\cdot\ln2\approx6{,}9\) ns. \(r_d=25{,}85\ \text{mV}/10\ \text{mA}=2{,}6\) Ω. \(C_d=10^{-8}\cdot0{,}01/0{,}02585\approx3{,}9\) nF. Demak 100 MGs dan yuqori chastotalarda bunday diod to‘g‘rilash xususiyatini yo‘qotadi; Shottki diodida \(C_d\approx0\)."),
 simtask=["Logarifmik shkalada ikki qiyalikli sohani (rekombinatsiya va diffuziya) toping va \\(n\\) qiymatini \\(n=\\frac{q}{kT}\\frac{\\Delta V}{\\Delta\\ln I}\\) orqali hisoblang.",
          "\\(R_s\\) ni 0 dan 20 Ω gacha oshirib, 10 mA dagi kuchlanish o‘sishini \\(IR_s\\) bilan solishtiring.",
          "Haroratni 300 dan 350 K ga ko‘tarib, \\(dV/dT\\) ni o‘lchang va −2 mV/K bilan taqqoslang."],
 mistakes=[("“Diodning ochilish kuchlanishi doimiy 0,7 V.”", "U tok, harorat va \\(I_s\\) ga logarifmik bog‘liq; 0,7 V faqat taxminiy model."),
           ("“Teskari tok \\(-I_s\\) ga teng va kuchlanishga bog‘liq emas.”", "Si diodlarda teskari tokda generatsiya komponenti ustun va u \\(W\\) bilan birga o‘sadi."),
           ("“Diod tezligi faqat to‘siq sig‘imi bilan cheklanadi.”", "p-n diodlarda asosiy cheklovchi — to‘plangan zaryad (diffuzion sig‘im) va \\(t_{rr}\\).")],
 ai="""Sen elektronika laboratoriyasi assistentisan. Menda 1N4148 diodining datasheet’i bor.
1) Datasheet’dagi I_F–V_F grafigidan uchta nuqta olib (qiymatlarni men beraman), I_s, n va R_s ni eng kichik kvadratlar usulida topadigan Python kodini yoz.
2) Shu parametrlar bilan ngspice uchun .model qatorini tuz va tekshirish uchun .dc tahlilini yoz.
3) t_rr ni o‘lchash sxemasini (impuls generator + osillograf) tavsifla.
Eslatma: datasheet raqamlarini o‘zing uydirma — men kiritgan qiymatlardan foydalan.""",
 quiz=[("Kichik to‘g‘ri kuchlanishlarda Si diodda \\(n\\approx2\\) bo‘lishining sababi:", ["yuqori injeksiya", "fazoviy zaryad qatlamidagi rekombinatsiya", "ketma-ket qarshilik", "tunnel tok"], 1, "SRH rekombinatsiya toki \\(\\propto e^{qV/2kT}\\)."),
       ("O‘zgarmas tokda Si diodning \\(dV/dT\\) taxminan:", ["+2 mV/K", "−2 mV/K", "−20 mV/K", "0"], 1, "Harorat datchiklari shu xossaga asoslanadi."),
       ("Varikap qaysi sig‘imdan foydalanadi?", ["diffuzion", "to‘siq (barer)", "parazit montaj", "kirish"], 1, "Teskari kuchlanishda \\(C_b\\) boshqariladi."),
       ("\\(\\tau=10\\) ns, \\(I_F=I_R\\) bo‘lsa, \\(t_s\\) ≈ ?", ["10 ns", "6,9 ns", "20 ns", "1 ns"], 1, "\\(\\tau\\ln2\\).")],
 blits=["PIN-diodning i-qatlami nima beradi?", "Diodda yuqori injeksiya qachon boshlanadi?", "Shottki diodida nega \\(t_{rr}\\approx0\\)?", "Datasheet’dagi \\(V_{RRM}\\) va \\(I_{FSM}\\) nima?", "Diod harorat datchigi sifatida qanday kalibrlanadi?"]
))

L.append(dict(
 n=5, short="O‘tishning teshilishi", sim="zener", refs=[1, 3, 5], intl=["sze", "baliga", "sedra"], tn=["TN2", "TN3", "TN8", "TN14"],
 title="O‘tishning teshilishi. Stabilitronlar va tunnel diodlar",
 goal="P-n o‘tishning teshilish turlari (ko‘chkisimon, tunnel, issiqlik) fizik mexanizmlarini, ularga asoslangan stabilitronlar va tunnel diodlarning xarakteristikalari hamda zamonaviy mikroelektronikadagi qo‘llanilishini o‘rganish.",
 outcomes=["teshilish mexanizmini \\(V_{BR}\\) va harorat koeffitsiyenti bo‘yicha aniqlaydi;", "ko‘paytirish koeffitsiyenti va kritik maydon tushunchasini qo‘llaydi;", "parametrik stabilizator sxemasini hisoblaydi;", "tunnel diodning manfiy differensial qarshiligini zonaviy diagramma bilan tushuntiradi."],
 plan=["Ko‘chkisimon teshilish va zarbali ionlanish", "Tunnel (Zener) teshilishi", "Issiqlik teshilishi", "Stabilitronlar: parametrlar, sxemalar", "Tunnel diodlar va qo‘llanilishi"],
 terms=["zarbali ionlanish", "ko‘paytirish koeffitsiyenti \\(M\\)", "kritik maydon \\(E_{cr}\\)", "stabilizatsiya kuchlanishi \\(V_Z\\)", "kuchlanishning harorat koeffitsiyenti (KHK)", "manfiy differensial qarshilik", "aynigan yarimo‘tkazgich"],
 theory=[
  ("Ko‘chkisimon teshilish", r"""<p>Kuchli maydonda tashuvchilar erkin yugurish yo‘lida ionlanish energiyasidan katta energiya oladi va panjara atomlarini ionlab yangi elektron-teshik juftlarini hosil qiladi. Ko‘paytirish koeffitsiyenti empirik ravishda:</p>
$$M=\frac{1}{1-(V/V_{BR})^m},\qquad m\approx2\ldots6$$
<p>Teshilish sharti — ionlanish integrali birga teng bo‘lishi. Keskin bir tomonlama o‘tish uchun \(V_{BR}=\varepsilon_sE_{cr}^2/(2qN_B)\); Si da \(E_{cr}\approx(3\ldots5)\cdot10^5\) V/sm. Harorat oshganda fonon sochilishi kuchayadi, shuning uchun \(V_{BR}\) <b>ortadi</b> (musbat KHK).</p>"""),
  ("Tunnel (Zener) teshilishi", r"""<p>Ikkala soha kuchli legirlanganda o‘tish juda yupqa (\(W<10\) nm) bo‘ladi va elektronlar valent zonadan o‘tkazuvchanlik zonasiga to‘g‘ridan-to‘g‘ri tunnel o‘tadi. Tunnel ehtimoli \(T\propto\exp\!\left(-\frac{4\sqrt{2m^*}E_g^{3/2}}{3q\hbar E}\right)\). Harorat ortganda \(E_g\) kamayadi, shuning uchun \(V_{BR}\) <b>kamayadi</b> (manfiy KHK). Empirik qoida: \(V_{BR}<4E_g/q\) — tunnel, \(V_{BR}>6E_g/q\) — ko‘chkisimon, oraliqda aralash (Si da ≈ 5–6 V da KHK ≈ 0).</p>"""),
  ("Issiqlik teshilishi", r"""<p>Teskari tok o‘tishni qizdiradi, harorat ortishi esa tokni oshiradi — musbat teskari aloqa. Issiqlik muvozanati sharti \(P=IV=(T_j-T_a)/R_{th}\) buzilsa, teshilish qaytmas bo‘ladi. Bu jarayon radiator va issiqlik qarshiligi \(R_{th}\) hisobini talab qiladi (TN15).</p>"""),
  ("Stabilitronlar va tunnel diodlar", r"""<p><b>Stabilitron</b> teshilish sohasida ishlaydi: tok keng oraliqda o‘zgarganda kuchlanish deyarli o‘zgarmaydi. Asosiy parametrlar: \(V_Z\), \(I_{Z\min}\)–\(I_{Z\max}\), differensial qarshilik \(r_Z\), KHK, \(P_{max}\). Parametrik stabilizatorda ballast qarshilik:</p>
$$R=\frac{V_{kir}-V_Z}{I_{Z\min}+I_{yuk}}$$
<p><b>Tunnel diod</b> (Esaki, 1958) — ikkala soha aynigan; to‘g‘ri yo‘nalishning boshida n-sohadagi band holatlar p-sohadagi bo‘sh holatlar ro‘parasiga kelib, tunnel tok cho‘qqiga (\(I_p\)) chiqadi, so‘ng kamayadi — <b>manfiy differensial qarshilik</b>. U YuCh generatorlar va juda tez kalitlarda ishlatiladi. Zamonaviy mikrosxemalarda stabilitronlar ESD-himoya, TVS-diodlar va tayanch kuchlanish manbalarida, tunnel o‘tish esa TFET va flesh-xotiralarda qo‘llanadi.</p>""")],
 example=("Parametrik stabilizatorni hisoblash",
  r"\(V_{kir}=12\) V, stabilitron \(V_Z=5{,}6\) V, \(r_Z=10\) Ω, \(I_{Z\min}=5\) mA, yuklama toki \(I_{yuk}=20\) mA. Ballast qarshilik \(R\), stabilitron quvvati (yuklama uzilganda) va kirish 1 V ga o‘zgarganda chiqish o‘zgarishini toping.",
  r"\(R=(12-5{,}6)/(0{,}005+0{,}02)=256\) Ω (yaqin standart 240 yoki 270 Ω). Yuklama uzilsa: \(I_Z=6{,}4/256=25\) mA, \(P_Z=5{,}6\cdot0{,}025=0{,}14\) Vt. \(\Delta V_{chiq}\approx\Delta V_{kir}\cdot\frac{r_Z\parallel R_{yuk}}{R+r_Z\parallel R_{yuk}}\approx1\cdot\frac{9{,}6}{265{,}6}\approx36\) mV (\(R_{yuk}=280\) Ω)."),
 simtask=["\\(V_Z\\) ni 3 V, 5,6 V va 12 V qilib, mexanizm va KHK ishorasi qanday o‘zgarishini qayd eting.",
          "\\(r_Z\\) ni 1 dan 40 Ω gacha o‘zgartirib, stabilizatsiya sifatini baholang.",
          "Tunnel diod rejimida \\(I_p/I_v\\) nisbatini toping va manfiy qarshilik sohasining chegaralarini yozing."],
 mistakes=[("“Teshilish har doim asbobning buzilishi.”", "Ko‘chkisimon va tunnel teshilishlar qaytar; faqat issiqlik teshilishi qaytmas."),
           ("“Zener diodlarning hammasi Zener mexanizmida ishlaydi.”", "\\(V_Z>6\\) V li “Zener” diodlarda asosan ko‘chkisimon teshilish bo‘ladi."),
           ("“Tunnel diod teskari yo‘nalishda yomon o‘tkazadi.”", "Aynigan o‘tish teskari yo‘nalishda ham yaxshi o‘tkazadi (teskari diodlar shunga asoslangan).")],
 ai="""Sen quvvat elektronikasi muhandisisan. Menga 5 V, 50 mA yuklama uchun stabilitronli stabilizator kerak (kirish 9–15 V).
1) R, stabilitron quvvati va tavsiya etiladigan stabilitron seriyasini tanla (datasheet parametrlarini men tekshiraman — taxmin bo‘lsa, aytib qo‘y).
2) Nima uchun 5,1–5,6 V atrofida KHK nolga yaqinligini zarbali ionlanish va tunnel mexanizmlari orqali tushuntir.
3) ngspice’da .dc V_kir 9 15 0.1 tahlilini yozib, chiqishning beqarorlik koeffitsiyentini hisobla.""",
 quiz=[("Ko‘chkisimon teshilishda KHK ishorasi:", ["manfiy", "musbat", "nol", "kuchlanishga bog‘liq emas"], 1, "Fonon sochilishi kuchaygani uchun \\(V_{BR}\\) ortadi."),
       ("Tunnel teshilishi uchun zarur shart:", ["kuchsiz legirlash", "ikkala sohaning kuchli legirlanishi va yupqa o‘tish", "yuqori harorat", "keng i-qatlam"], 1, "Barer kengligi bir necha nm bo‘lishi kerak."),
       ("\\(V_{kir}=12\\) V, \\(V_Z=5{,}6\\) V, \\(I_{Zmin}+I_{yuk}=25\\) mA. R = ?", ["224 Ω", "256 Ω", "480 Ω", "56 Ω"], 1, "6,4 V / 25 mA."),
       ("Tunnel diodning asosiy xususiyati:", ["juda katta teskari kuchlanish", "manfiy differensial qarshilik sohasi", "faqat bir yo‘nalishda o‘tkazish", "yorug‘lik chiqarish"], 1, "Cho‘qqi va botiq orasida \\(dI/dV<0\\).")],
 blits=["Kritik maydon nima?", "Issiqlik teshilishini qanday oldini olish mumkin?", "TVS-diod stabilitrondan nimasi bilan farq qiladi?", "ESD-himoyada qaysi teshilish ishlatiladi?", "Teskari (backward) diod nima?"]
))

L.append(dict(
 n=6, short="Bipolyar tranzistor prinsipi", sim="bjt", refs=[2, 3, 4], intl=["sze", "neamen", "sedra"], tn=["TN3", "TN4", "TN11", "TN14"],
 title="Bipolyar tranzistorlarning ishlash prinsipi va statik xarakteristikalari",
 goal="Bipolyar tranzistorning zonaviy diagrammasi, emitter, baza va kollektor toklarining tashkil topishi, tok bo‘yicha kuchaytirish koeffitsiyentini fizik parametrlar orqali hisoblash hamda kichik signal (g‘alayonlanish) nazariyasi asosida parametrlarni aniqlashni o‘rganish.",
 outcomes=["aktiv rejimdagi n-p-n tranzistor zonaviy diagrammasini chizadi;", "emitter samaradorligi \\(\\gamma\\), ko‘chish koeffitsiyenti \\(\\alpha_T\\), \\(\\alpha\\) va \\(\\beta\\) ni hisoblaydi;", "kirish va chiqish statik xarakteristikalarini, Erli effektini tahlil qiladi;", "h-parametrlar va gibrid-π modeli parametrlarini ishchi nuqtadan topadi."],
 plan=["Tuzilishi va ishlash rejimlari", "Zonaviy diagramma, toklar komponentlari", "\\(\\gamma\\), \\(\\alpha_T\\), \\(\\alpha\\), \\(\\beta\\)", "Statik xarakteristikalar, Erli effekti, Ebers–Moll modeli", "Kichik signal parametrlari (h-parametrlar)"],
 terms=["emitter samaradorligi", "baza orqali ko‘chish koeffitsiyenti", "Erli kuchlanishi", "aktiv / to‘yinish / berk rejim", "Ebers–Moll modeli", "h-parametrlar", "ishchi nuqta (Q)"],
 theory=[
  ("Tuzilishi va rejimlari", r"""<p>Bipolyar tranzistor (BT) ikki yaqin joylashgan p-n o‘tishdan iborat: emitter (kuchli legirlangan), yupqa baza va kollektor. Rejimlar o‘tishlarning siljishiga qarab aniqlanadi: <b>aktiv</b> (EO‘ — to‘g‘ri, KO‘ — teskari), <b>to‘yinish</b> (ikkalasi to‘g‘ri), <b>berk</b> (ikkalasi teskari), <b>invers</b>. Kuchaytirish aktiv rejimda bo‘ladi: emitterdan injeksiyalangan elektronlar bazadan diffuziyalanib o‘tib, kollektor o‘tishi maydoni tomonidan tortib olinadi.</p>"""),
  ("Toklar va kuchaytirish koeffitsiyentlari", r"""<p>Emitter toki \(I_E=I_{nE}+I_{pE}\), kollektor toki \(I_C=\alpha_TI_{nE}+I_{CB0}\). Qisqa baza (\(W_B\ll L_B\)) uchun:</p>
$$\gamma=\frac{I_{nE}}{I_E}\approx\left(1+\frac{D_EN_BW_B}{D_BN_EW_E}\right)^{-1},\qquad \alpha_T\approx1-\frac{W_B^2}{2L_B^2}$$
$$\alpha=\gamma\,\alpha_T\,M,\qquad \beta=\frac{\alpha}{1-\alpha}$$
<p>Yuqori \(\beta\) uchun emitter bazadan ancha kuchli legirlanadi va baza juda yupqa qilinadi.</p>"""),
  ("Statik xarakteristikalar va Erli effekti", r"""<p>UE sxemada kirish xarakteristikasi \(I_B(V_{BE})\) diodnikiga o‘xshash, chiqish xarakteristikalari \(I_C(V_{CE})\) esa \(I_B\) parametrli egri chiziqlar oilasi. Kollektor kuchlanishi ortganda KO‘ kengayib, effektiv baza kengligi kamayadi (bazaning modulyatsiyasi), natijada \(I_C\) sekin o‘sadi:</p>
$$I_C=I_S\,e^{V_{BE}/V_T}\left(1+\frac{V_{CE}}{V_A}\right),\qquad r_o=\frac{V_A}{I_C}$$
<p>Ebers–Moll modeli BTni ikki diod va ikki boshqariladigan tok manbai orqali barcha rejimlar uchun tavsiflaydi: \(I_E=I_{ES}(e^{V_{BE}/V_T}-1)-\alpha_RI_{CS}(e^{V_{BC}/V_T}-1)\), \(I_C=\alpha_FI_{ES}(e^{V_{BE}/V_T}-1)-I_{CS}(e^{V_{BC}/V_T}-1)\), \(\alpha_FI_{ES}=\alpha_RI_{CS}\).</p>"""),
  ("Kichik signal (g‘alayonlanish) nazariyasi", r"""<p>Ishchi nuqta atrofida kichik o‘zgarishlar uchun tenglamalarni chiziqlashtirsak, gibrid-π modeli parametrlari olinadi:</p>
$$g_m=\frac{I_C}{V_T},\quad r_\pi=\frac{\beta}{g_m},\quad r_o=\frac{V_A}{I_C}$$
<p>h-parametrlar (UE): \(h_{11e}=r_\pi\) (kirish qarshiligi), \(h_{21e}=\beta\), \(h_{12e}\approx r_\pi/r_\mu\), \(h_{22e}=1/r_o\). Ishchi nuqta yuklama chizig‘i \(V_{CE}=V_{CC}-I_CR_C\) bilan chiqish xarakteristikasining kesishishida topiladi.</p>""")],
 example=("\\(\\beta\\) ni tuzilma parametrlaridan hisoblash",
  r"n-p-n Si BT: \(N_E=10^{19}\), \(N_B=10^{17}\) sm⁻³, \(W_E=W_B=0{,}5\) mkm, \(D_E=2\) sm²/s (emitterdagi teshiklar), \(D_B=20\) sm²/s, bazadagi umr \(\tau_B=0{,}1\) mks. \(\gamma, \alpha_T, \alpha, \beta\) ni toping (\(M=1\)).",
  r"\(\frac{D_EN_BW_B}{D_BN_EW_E}=\frac{2\cdot10^{17}}{20\cdot10^{19}}=10^{-3}\) ⇒ \(\gamma=0{,}9990\). \(L_B=\sqrt{20\cdot10^{-7}}=14{,}1\) mkm ⇒ \(\alpha_T=1-\frac{0{,}25}{2\cdot200}=0{,}99938\). \(\alpha=0{,}99838\), \(\beta=\alpha/(1-\alpha)\approx615\). Real tranzistorlarda emitterdagi kuchli legirlash zonasining torayishi va sirt rekombinatsiyasi \(\beta\) ni 100–300 gacha kamaytiradi."),
 simtask=["\\(V_{CC}=12\\) V, \\(R_C=1{,}5\\) kΩ da \\(I_B\\) ni o‘zgartirib Q-nuqtani chiqish xarakteristikalarining o‘rtasiga (\\(V_{CE}\\approx V_{CC}/2\\)) joylashtiring.",
          "\\(V_A\\) ni 20 va 200 V qilib, \\(r_o\\) va kuchaytirish koeffitsiyenti \\(A_v=-g_m(R_C\\parallel r_o)\\) o‘zgarishini baholang.",
          "Tranzistorni to‘yinishga olib kiring va \\(I_C<\\beta I_B\\) shartini tekshiring."],
 mistakes=[("“Kollektor toki bazadan keladi.”", "Kollektor toki emitterdan injeksiyalangan va bazani diffuziya bilan kesib o‘tgan elektronlardan iborat; baza toki — kichik rekombinatsiya va teskari injeksiya toki."),
           ("“BT — ikkita ketma-ket ulangan diod.”", "Ikki diod modeli tranzistor effektini bermaydi: baza diffuziya uzunligidan ancha yupqa bo‘lishi shart."),
           ("“\\(\\beta\\) doimiy kattalik.”", "\\(\\beta\\) tok, harorat va \\(V_{CE}\\) ga bog‘liq; kichik toklarda rekombinatsiya, katta toklarda yuqori injeksiya (Kirk effekti) uni kamaytiradi.")],
 ai="""Sen analog sxemotexnika o‘qituvchisisan. Menda BC547 tranzistori va V_CC = 12 V, R_C = 2,2 kΩ bor.
1) Kuchlanish bo‘luvchi bilan baza siljitish sxemasini Q-nuqta V_CE ≈ 6 V uchun hisobla; β ning tarqalishi (110–450) Q-nuqtaga qanday ta’sir qilishini ko‘rsat.
2) g_m, r_π, r_o va UE kaskad kuchaytirish koeffitsiyentini hisobla.
3) ngspice uchun sxemani (.op va .ac) yoz; natijalarni qo‘lda hisob bilan solishtirish jadvalini tuz.
Datasheet qiymatlarini men tekshiraman — har birini “datasheet’dan tekshiring” deb belgilab qo‘y.""",
 quiz=[("Aktiv rejimda o‘tishlar qanday siljigan?", ["ikkalasi to‘g‘ri", "EO‘ to‘g‘ri, KO‘ teskari", "ikkalasi teskari", "EO‘ teskari, KO‘ to‘g‘ri"], 1, "Kuchaytirish rejimi."),
       ("\\(\\beta\\) ni oshirish uchun:", ["bazani qalinlashtirish", "emitterni bazadan kuchli legirlash va bazani yupqalash", "kollektorni kuchli legirlash", "haroratni pasaytirish"], 1, "\\(\\gamma\\to1\\) va \\(\\alpha_T\\to1\\)."),
       ("\\(\\alpha=0{,}995\\) bo‘lsa, \\(\\beta\\) = ?", ["99", "199", "995", "0,995"], 1, "\\(0{,}995/0{,}005=199\\)."),
       ("\\(I_C=1\\) mA da \\(g_m\\) ≈ ? (300 K)", ["1 mS", "38,7 mS", "25,9 mS", "100 mS"], 1, "\\(g_m=I_C/V_T=1/0{,}02585\\).")],
 blits=["Kirk effekti nima?", "Invers rejimda \\(\\beta\\) nega kichik?", "Erli kuchlanishi grafikdan qanday topiladi?", "UB, UE, UK sxemalarning farqi?", "Ishchi nuqtaning termik barqarorligi qanday ta’minlanadi?"]
))

L.append(dict(
 n=7, short="BT turlari va chastotaviy xususiyatlar", sim="bjtfreq", refs=[1, 3, 5], intl=["sze", "sedra", "hu"], tn=["TN3", "TN4", "TN9", "TN18"],
 title="Bipolyar tranzistorlar turlari. Chastotaviy xususiyatlar, YuCh tranzistorlar",
 goal="Bipolyar tranzistorlarning chastotaviy cheklovlari (bazadan uchib o‘tish vaqti, sig‘imlar), past chastotali parametrlari va yuqori chastotali tranzistorlar (HBT, SiGe) konstruksiyasini o‘rganish.",
 outcomes=["\\(f_\\beta\\), \\(f_\\alpha\\), \\(f_T\\), \\(f_{max}\\) chastotalarini farqlaydi va hisoblaydi;", "bazadan uchib o‘tish vaqtini tuzilma parametrlaridan baholaydi;", "Miller effekti kaskad o‘tkazish polosasini qanday cheklashini tushuntiradi;", "geteroo‘tishli tranzistorlarning afzalligini zonaviy diagramma bilan asoslaydi."],
 plan=["BT turlari (quvvat, kichik signal, YuCh, HBT)", "Past chastotali parametrlar", "Chastotaviy bog‘liqlik: \\(\\beta(f)\\), \\(f_T\\)", "Kechikish vaqtlari: emitter, baza, kollektor", "YuCh tranzistorlar: SiGe HBT, Miller effekti"],
 terms=["chegaraviy chastota \\(f_T\\)", "\\(\\beta\\)-kesish chastotasi", "maksimal generatsiya chastotasi \\(f_{max}\\)", "bazadan uchib o‘tish vaqti", "Miller sig‘imi", "geteroo‘tishli BT (HBT)", "SiGe"],
 theory=[
  ("Bipolyar tranzistorlar turlari", r"""<p>Vazifasiga ko‘ra: kichik signalli past chastotali, YuCh, impulsli (kalit), quvvat tranzistorlari; tuzilishiga ko‘ra: diffuzion va drift (bazada kirishmaning notekis taqsimoti ichki maydon yaratadi), planar-epitaksial, geteroo‘tishli (HBT). Quvvat BTlarda emitter tarmoqlangan (interdigital) qilinadi — tok siqilishi (current crowding) kamayadi.</p>"""),
  ("\\(\\beta\\) ning chastotaga bog‘liqligi", r"""<p>Tok kuchaytirish koeffitsiyenti bir qutbli past chastotali filtr kabi o‘zgaradi:</p>
$$\beta(f)=\frac{\beta_0}{1+j f/f_\beta},\qquad f_T\approx\beta_0f_\beta,\qquad f_\alpha\approx(\beta_0+1)f_\beta$$
<p>\(f_T\) — \(|\beta|=1\) bo‘ladigan chastota; gibrid-π modeli bo‘yicha \(f_T=\dfrac{g_m}{2\pi(C_\pi+C_\mu)}\).</p>"""),
  ("Kechikish vaqtlari", r"""<p>Umumiy emitter–kollektor kechikishi \(\tau_{ec}=1/(2\pi f_T)\) bir necha qismdan iborat:</p>
$$\tau_{ec}=\tau_E+\tau_B+\tau_{C}+\tau_{d},\qquad \tau_B=\frac{W_B^2}{\eta D_B}$$
<p>bu yerda \(\eta=2\) bir jinsli baza uchun, drift bazada \(\eta>2\). \(\tau_E=C_{je}V_T/I_C\) — emitter o‘tishini qayta zaryadlash, \(\tau_d=W_{C}/(2v_s)\) — kollektor qatlamidan to‘yingan tezlikda uchib o‘tish. Quvvat kuchaytirish birga teng bo‘ladigan chastota: \(f_{max}=\sqrt{\dfrac{f_T}{8\pi r_bC_\mu}}\).</p>"""),
  ("Miller effekti va YuCh tranzistorlar", r"""<p>UE kaskadda kollektor–baza sig‘imi kirishga \((1+|A_v|)\) marta kattalashib o‘tadi: \(C_M=C_\mu(1+g_mR_L)\). Shuning uchun keng polosali kuchaytirgichlarda kaskod (UE+UB) sxemasi ishlatiladi. <b>SiGe HBT</b>da bazaga Ge qo‘shilib \(E_g\) kamaytiriladi: emitter samaradorligi bazani kuchli legirlashga qaramay yuqori qoladi (\(\beta\propto e^{\Delta E_g/kT}\)), Ge ning gradiyent taqsimoti esa bazada tortuvchi maydon hosil qiladi. Zamonaviy SiGe HBT \(f_T\) 300 GGs dan yuqori.</p>""")],
 example=("Bazadan uchib o‘tish vaqti va \\(f_T\\) bahosi",
  r"Bir jinsli baza: \(W_B=0{,}1\) mkm, \(D_B=20\) sm²/s. \(I_C=1\) mA da \(C_\pi+C_\mu=1\) pF. \(\tau_B\), faqat bazaga bog‘liq \(f_T\) chegarasi va gibrid-π bo‘yicha \(f_T\) ni toping.",
  r"\(\tau_B=W_B^2/(2D_B)=(10^{-5})^2/40=2{,}5\) ps ⇒ \(f_T\le1/(2\pi\tau_B)\approx64\) GGs. Gibrid-π: \(g_m=38{,}7\) mS, \(f_T=0{,}0387/(2\pi\cdot10^{-12})\approx6{,}2\) GGs — demak bu holatda sig‘imlarni zaryadlash vaqti asosiy cheklovchi."),
 simtask=["\\(\\beta_0=150\\), \\(f_T=300\\) MGs da \\(f_\\beta\\) ni toping va grafikdagi −3 dB nuqta bilan solishtiring.",
          "\\(f_T\\) ni 10 MGs dan 5 GGs gacha o‘zgartirib, \\(\\tau=1/(2\\pi f_T)\\) ni jadvalga yozing.",
          "Kuchaytirish × polosa (GBW) mahsuloti nima uchun deyarli o‘zgarmasligini tushuntiring."],
 mistakes=[("“\\(f_T\\) — tranzistor ishlay oladigan maksimal chastota.”", "\\(f_T\\) da tok kuchaytirish 1 ga teng; quvvat kuchaytirish uchun \\(f_{max}\\) muhim, u \\(f_T\\) dan katta yoki kichik bo‘lishi mumkin."),
           ("“\\(f_T\\) tokka bog‘liq emas.”", "Kichik toklarda \\(\\tau_E\\propto1/I_C\\) ustun, katta toklarda Kirk effekti \\(f_T\\) ni kamaytiradi — maksimum mavjud."),
           ("“Bazani yupqalash har doim foydali.”", "Juda yupqa bazada baza qarshiligi \\(r_b\\) ortadi va o‘tib ketish (punch-through) xavfi paydo bo‘ladi.")],
 ai="""Sen RF IC muhandisisan. Menga 2,4 GGs kam shovqinli kuchaytirgich uchun tranzistor tanlash kerak.
1) SiGe HBT va GaAs pHEMT ning f_T, f_max, NF_min bo‘yicha farqini jadvalda ber (qiymatlar uchun manba ko‘rsat yoki “tipik” deb belgila).
2) Miller effektini UE kaskadda hisobla: C_μ = 0,2 pF, g_m = 40 mS, R_L = 1 kΩ.
3) ngspice’da .ac tahlil bilan UE va kaskod kaskadlarning o‘tkazish polosasini solishtiruvchi netlist yoz.""",
 quiz=[("\\(f_T\\) ta’rifi:", ["\\(|\\beta|=\\beta_0/\\sqrt2\\)", "\\(|\\beta|=1\\)", "quvvat kuchaytirish = 1", "\\(\\alpha=0{,}5\\)"], 1, "Tok kuchaytirish birga teng chastota."),
       ("\\(\\beta_0=200\\), \\(f_T=400\\) MGs bo‘lsa, \\(f_\\beta\\) = ?", ["2 MGs", "80 GGs", "400 MGs", "200 kGs"], 0, "\\(f_\\beta=f_T/\\beta_0\\)."),
       ("Bazadan uchib o‘tish vaqti baza kengligiga qanday bog‘liq?", ["\\(\\propto W_B\\)", "\\(\\propto W_B^2\\)", "\\(\\propto1/W_B\\)", "bog‘liq emas"], 1, "\\(\\tau_B=W_B^2/(2D_B)\\)."),
       ("SiGe HBT ning asosiy afzalligi:", ["arzon metallizatsiya", "bazada \\(E_g\\) kichikligi tufayli yuqori \\(\\gamma\\) va tortuvchi maydon", "katta teskari kuchlanish", "yorug‘lik chiqarish"], 1, "Geteroo‘tish emitter samaradorligini oshiradi.")],
 blits=["Kaskod sxemasi Miller effektini qanday kamaytiradi?", "\\(f_{max}\\) ni oshirish uchun \\(r_b\\) ni qanday kamaytirish mumkin?", "Drift tranzistor nima?", "Quvvat BT da tok siqilishi nima?", "Datasheet’da \\(f_T\\) qaysi sharoitda beriladi?"]
))

L.append(dict(
 n=8, short="To‘rt qatlamli strukturalar", sim="thyristor", refs=[1, 2, 3], intl=["baliga", "sze"], tn=["TN3", "TN4", "TN7", "TN15"],
 title="To‘rt qatlamli strukturalar: dinistorlar, tiristorlar, simistorlar",
 goal="p-n-p-n strukturalarning ishlash prinsipini ikki tranzistorli analog orqali tushuntirish, VAXni hisoblash, tiristorlarning tayyorlash usullari va kuch elektronikasidagi qo‘llanilishini o‘rganish.",
 outcomes=["to‘rt qatlamli strukturaning ochilish shartini \\(\\alpha_1+\\alpha_2\\to1\\) orqali tushuntiradi;", "VAXning yopiq, manfiy qarshilik va ochiq sohalarini izohlaydi;", "boshqaruv toki, ushlab turish toki va \\(dV/dt\\), \\(dI/dt\\) cheklovlarini hisobga oladi;", "faza boshqaruvli rostlagichni hisoblaydi."],
 plan=["Dinistor: tuzilish va ishlash", "Ikki tranzistorli analog, ochilish sharti", "Tiristor VAX va boshqaruv elektrodi", "Simistor (triak), GTO, IGBT bilan solishtirish", "Tayyorlash usullari va qo‘llanilishi"],
 terms=["dinistor", "tiristor (SCR)", "simistor (triak)", "ochilish kuchlanishi \\(V_{BO}\\)", "ushlab turish toki \\(I_H\\)", "boshqaruv toki \\(I_{GT}\\)", "faza boshqaruvi"],
 theory=[
  ("Ikki tranzistorli analog", r"""<p>p-n-p-n struktura uchta o‘tishga ega (J1, J2, J3). Uni o‘zaro bog‘langan p-n-p (\(\alpha_1\)) va n-p-n (\(\alpha_2\)) tranzistorlar sifatida ko‘rish mumkin. Anod toki:</p>
$$I_A=\frac{\alpha_2I_G+I_{CO}}{1-(\alpha_1+\alpha_2)}$$
<p>\(\alpha\) koeffitsiyentlari tok ortishi bilan o‘sadi. \(\alpha_1+\alpha_2\to1\) bo‘lganda musbat teskari aloqa tufayli tok keskin ortadi — struktura ochiladi, uchala o‘tish to‘g‘ri siljiydi va kuchlanish 1–2 V gacha tushadi.</p>"""),
  ("VAX va asosiy parametrlar", r"""<p>VAX sohalari: (1) to‘g‘ri yopiq holat — J2 teskari siljigan, kichik oqish toki; (2) ochilish nuqtasi \(V_{BO}\) — J2 da ko‘chkisimon ko‘paytirish \(\alpha\) larni oshiradi; (3) manfiy differensial qarshilik sohasi; (4) ochiq holat — diod kabi VAX; (5) teskari yopiq holat. Struktura ochiq qolishi uchun anod toki <b>ushlab turish toki</b> \(I_H\) dan katta bo‘lishi kerak. Boshqaruv toki \(I_G\) \(V_{BO}\) ni kamaytiradi; \(I_G\ge I_{GT}\) da tiristor deyarli darhol ochiladi.</p>"""),
  ("Dinamik cheklovlar", r"""<p>Anod kuchlanishining tez o‘sishi J2 sig‘imini zaryadlovchi siljish tokini hosil qiladi \(i=C_{J2}\,dV/dt\) — u boshqaruv toki kabi ta’sir qilib, soxta ochilishga sabab bo‘ladi. Ochilish boshida tok kichik sohada oqadi, shuning uchun \(dI/dt\) cheklanadi. Snubber RC-zanjirlar va ketma-ket induktivlik shu cheklovlar uchun ishlatiladi.</p>"""),
  ("Simistor, tayyorlash va qo‘llanilishi", r"""<p><b>Simistor (triak)</b> — ikki qarama-qarshi parallel tiristor bitta kristallda; o‘zgaruvchan tokni ikkala yarim davrda boshqaradi. <b>GTO</b> boshqaruv elektrodi orqali yopiladi. Tiristorlar diffuziya (Ga, Al, B) va qotishma usullari bilan katta diametrli kremniy plastinalarda tayyorlanadi; anod va katod tomonlari shunt (emitter shorts) bilan \(dV/dt\) chidamliligi oshiriladi. Qo‘llanilishi: faza boshqaruvli rostlagichlar (yoritish, isitish, motor), YuKO‘ tok uzatish (HVDC — kV, kA darajalari), payvandlash va yumshoq ishga tushirish qurilmalari. O‘rtacha quvvatda o‘rnini IGBT va MOSFETlar egallamoqda.</p>
$$U_{o'rt}=\frac{U_m}{\pi}\cdot\frac{1+\cos\alpha}{2}\ \ (\text{bir yarim davrli}),\qquad P(\alpha)=P_0\left(1-\frac{\alpha}{\pi}+\frac{\sin2\alpha}{2\pi}\right)$$""")],
 example=("Tiristor ochilishi va faza boshqaruvi",
  r"(a) \(\alpha_1=0{,}4\), \(\alpha_2=0{,}5\), \(I_G=10\) mA, \(I_{CO}=10\) mkA bo‘lsa, yopiq holatdagi anod toki qancha? (b) 220 V, 50 Gs tarmoqda triak bilan rezistiv yuklama (\(P_0=1\) kVt) boshqariladi, ochilish burchagi \(\alpha=90^\circ\). Yuklamadagi quvvat qancha?",
  r"(a) \(I_A=(0{,}5\cdot0{,}01+10^{-5})/(1-0{,}9)=50{,}1\) mA — \(\alpha\) yig‘indisi 1 ga yaqinlashsa, tok cheksiz o‘sishga intiladi (ochilish). (b) \(P=P_0\left(1-\frac12+\frac{\sin\pi}{2\pi}\right)=0{,}5\) kVt."),
 simtask=["\\(I_G\\) ni 0 dan \\(I_{GT}\\) gacha oshirib, \\(V_{BO}(I_G)\\) bog‘liqligini 5 nuqtada yozing.",
          "\\(I_H\\) ni o‘zgartirib, tiristor yopilishi uchun yuklama toki qanday bo‘lishi kerakligini aniqlang.",
          "Teskari yo‘nalishdagi xarakteristika nima uchun boshqaruv tokiga bog‘liq emasligini tushuntiring."],
 mistakes=[("“Tiristorni boshqaruv toki bilan yopish mumkin.”", "Oddiy tiristor faqat anod toki \\(I_H\\) dan kamayganda yopiladi; boshqaruv bilan yopish faqat GTO da mumkin."),
           ("“Tiristor ochiq holatda kuchaytiradi.”", "U kalit sifatida ishlaydi: yo ochiq, yo yopiq."),
           ("“\\(dV/dt\\) faqat qizish bilan bog‘liq.”", "\\(dV/dt\\) sig‘im orqali siljish toki hosil qiladi va soxta ochilishga olib keladi.")],
 ai="""Sen quvvat elektronikasi bo‘yicha laboratoriya rahbarisan.
1) Triakli faza rostlagichi (220 V, 50 Gs, 500 Vt rezistiv yuklama) uchun ochilish burchagi α = 0…180° da P(α) grafigini Python’da chiz.
2) Snubber RC zanjirini dV/dt ≤ 50 V/mks shartidan hisobla (yuklama induktivligi berilmagan bo‘lsa, taxminni ochiq ayt).
3) Triak va IGBT asosidagi rostlagichni FIK, garmonikalar va narx bo‘yicha taqqosla.""",
 quiz=[("Ikki tranzistorli modelda ochilish sharti:", ["\\(\\alpha_1\\alpha_2=1\\)", "\\(\\alpha_1+\\alpha_2\\to1\\)", "\\(\\alpha_1=\\alpha_2\\)", "\\(\\beta_1=\\beta_2\\)"], 1, "Maxraj nolga intiladi."),
       ("Oddiy tiristor qanday yopiladi?", ["boshqaruv elektrodiga manfiy impuls", "anod tokini \\(I_H\\) dan kamaytirish", "\\(V_{BO}\\) ni oshirish", "haroratni pasaytirish"], 1, "Tabiiy kommutatsiya."),
       ("Simistor nima?", ["ikki qarama-qarshi parallel tiristor", "tiristor + diod", "MOSFET + BT", "ikki dinistor ketma-ket"], 0, "O‘zgaruvchan tok kaliti."),
       ("\\(\\alpha=90^\\circ\\) da rezistiv yuklamadagi quvvat:", ["25 %", "50 %", "75 %", "100 %"], 1, "\\(1-1/2+0\\).")],
 blits=["Dinistor tiristordan nimasi bilan farq qiladi?", "Emitter shuntlari nima uchun kerak?", "HVDC da nega tiristorlar ishlatiladi?", "Triakning to‘rt kvadranti nima?", "IGBT tiristor o‘rnini qayerda egalladi?"]
))
