# Yarimo‘tkazgich asboblar fizikasi — interaktiv elektron darslik

Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · Magistratura, 70530504 — Yarimo‘tkazgichlar fizikasi · Fan kodi YAAF1206 · 6 ECTS (180 soat)

Muallif: **Eshboltayev Iqbol Mamirjonovich**, professor, PhD
Taqrizchilar: R.Ya. Rasulov (f.-m.f.d., professor, FarDU), M. Qo‘chqorov (PhD, dotsent, QDU)

Darslik 2026/2027 o‘quv yili uchun tasdiqlangan fan dasturi asosida tayyorlangan. Dizayn va tuzilma ILIMZIYO elektron darsligiga asoslangan.

## Tarkibi

| Bo‘lim | Fayllar |
|---|---|
| 15 ta ma’ruza (M1–M15, 30 soat) | `lecture1.html` … `lecture15.html` |
| 15 ta amaliy mashg‘ulot (A1–A15, 30 soat) | `amaliy1.html` … `amaliy15.html` |
| 30 ta mustaqil ta’lim mavzusi + 8 ta keys-stadi (120 soat) | `mustaqil.html` |
| Baholash: JN 30 / ON 20 / YaN 50, TN–nazorat matritsasi, kalkulyator | `baholash.html` |
| Annotatsiya (uz/ru/en), ta’lim natijalari, xalqaro standartlarga muvofiqlik | `annotatsiya.html` |
| O‘qituvchi uchun qo‘llanma, 15 haftalik taqvim | `oqituvchi.html` |
| Atamalar lug‘ati, dasturiy vositalar | `glossariy.html`, `vositalar.html` |
| 16 ta interaktiv asbob modeli | `js/sims.js` |

Har bir ma’ruzada: maqsad va TN, reja, nazariya (formulalar), ishlangan misol, interaktiv model, SI bilan ishlash topshirig‘i, tipik xatolar, o‘z-o‘zini tekshirish testi, blits-savollar, adabiyotlar va o‘qituvchi uchun 80 daqiqalik dars rejasi.

## 2-versiyadagi imkoniyatlar

- **Yangi o‘zbek alifbosi** (O‘RQ-1184, 2026: O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç) — barcha sahifalar avtomatik o‘tkaziladi (`gen/alifbo.py`, `js/alifbo.js`). Manba matnlar eski imloda saqlanadi.
- **Kun / tun rejimi** — tanlov brauzerda eslab qolinadi.
- **UZ / RU / EN** — Google Translate orqali butun sayt, testlar bilan birga; Google paneli yashirilgan. Tarjima sifati uchun matn tarjimadan oldin eski imloga qaytariladi.
- **Tinglash** — har bir mavzuni tanlangan tilda ovozli o‘qish, formulalar so‘z bilan aytiladi.
- **Ovozli namoyish** — har bir interaktiv model parametrlarni o‘zi o‘zgartirib tushuntiradi (`gen/tours.py`), so‘ng boshqaruv talabaga o‘tadi.
- Ovoz brauzerning o‘zidagi **Web Speech API** orqali ishlaydi: API kalit, server va to‘lov talab qilinmaydi. O‘zbekcha tabiiy ovozlar Microsoft Edge brauzerida mavjud.
- Har bir ma’ruzada **10 savolli test** (`gen/quiz_extra.py`).

## O‘zbekcha neyron ovoz (barcha qurilmalarda bir xil)

O‘zbekcha "Tinglash" va modellarning ovozli namoyishi oldindan tayyorlangan MP3 fayllardan (`audio/uz/`) ijro etiladi — qurilmada o‘zbek ovozi bo‘lishi shart emas, telefon, kompyuter va elektron doskada bir xil tabiiy ovoz eshitiladi. Formulalar, darajalar (10¹⁶ → "o‘nning o‘n oltinchi darajasi"), o‘nli kasrlar ("0,77" → "nol butun yuzdan yetmish yetti"), birliklar va qisqartmalar odam o‘qiganidek so‘zga aylantiriladi.

- MP3 lar GitHub Actions (`.github/workflows/ovoz.yml`) orqali avtomatik yaratiladi: sahifa o‘zgarsa, faqat o‘zgargan xatboshilar qayta ovozlanadi (Microsoft Edge neyron ovozi, API kalit talab qilinmaydi).
- Ovozni almashtirish: Actions → "Ovoz (o‘zbekcha MP3)" → Run workflow → `uz-UZ-SardorNeural` (erkak) yoki `uz-UZ-MadinaNeural` (ayol).
- MP3 hali tayyor bo‘lmagan xatbosh uchun brauzerning o‘z ovozi ishlatiladi. Rus va ingliz tillarida brauzer ovozi (Chrome/Edge’da Google va Microsoft ovozlari) ishlatiladi.

## GitHub Pages’da ochish

Settings → Pages → Source: **Deploy from a branch**, Branch: **main**, Folder: **/ (root)** → Save.
Bir necha daqiqadan so‘ng sayt `https://eshboltayev.github.io/Yarimo-tkazgich_asboblar_fizikasi/` manzilida ochiladi.

Sayt statik (HTML/CSS/JS), server va ro‘yxatdan o‘tish talab etilmaydi; formulalar uchun KaTeX `vendor/` papkasida — internetsiz ham ishlaydi.

## Mazmunni tahrirlash

Matnlar `gen/` papkasidagi Python fayllarida:

- `gen/lectures_a.py`, `gen/lectures_b.py` — ma’ruzalar
- `gen/amaliy.py` — amaliy mashg‘ulotlar
- `gen/other.py` — mustaqil ta’lim, keyslar, lug‘at, vositalar, taqvim
- `gen/common.py` — sarlavha, menyu, adabiyotlar ro‘yxati

O‘zgartirgandan so‘ng repozitoriya ildizida:

```bash
python3 gen/build.py .
```

## Eslatma

Fan dasturidagi 2-asosiy adabiyot nomi dastur PDF faylida qisqartirilgan holda keltirilgan (“…optik va fotog…”); to‘liq nomi `gen/common.py` dagi `BASE_LIT` ro‘yxatida yangilanishi mumkin.

Rasmiy topshiriqlar va baholash faqat HEMIS axborot tizimida yuritiladi.

## Litsenziya

Matn va kod: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). KaTeX — MIT litsenziyasi (`vendor/katex/LICENSE`).
