"""Interaktiv modellar uchun ovozli avtomatik namoyish ssenariylari.
Har bir qadam: (parametrlar, izoh). Logarifmik parametrlar daraja ko'rsatkichida (masalan 16 → 10^16).
Tanlov (select) uchun qiymat '#indeks' ko'rinishida beriladi."""

T = {
 "fermi": [
  ({"mat": "#0", "Nd": 16, "T": 300}, "Bu model yarimo‘tkazgichdagi elektron va teshiklar konsentratsiyasini ko‘rsatadi. Hozir kremniy, donor konsentratsiyasi o‘n oltinchi darajada, harorat uch yuz kelvin. Elektronlar konsentratsiyasi donorlar soniga teng, Fermi sathi o‘rta sathdan taxminan uch yuz oltmish millielektronvolt yuqorida."),
  ({"Nd": 18}, "Donor konsentratsiyasini yuz marta oshiramiz. Fermi sathi o‘tkazuvchanlik zonasiga yaqinlashdi, o‘tkazuvchanlik ham yuz marta ortdi. Teshiklar esa yuz marta kamaydi, chunki elektron va teshiklar ko‘paytmasi o‘zgarmaydi."),
  ({"Nd": 15, "T": 600}, "Endi legirlashni kamaytirib, haroratni olti yuz kelvingacha ko‘taramiz. Xususiy konsentratsiya keskin o‘sib, donorlar konsentratsiyasidan oshib ketdi. Bu xususiy o‘tkazuvchanlik sohasi: Fermi sathi yana o‘rtaga qaytadi."),
  ({"mat": "#2", "T": 600}, "Galliy arsenidni tanlaymiz. Taqiqlangan zonasi keng bo‘lgani uchun xususiy konsentratsiya ancha kichik. Shu sababli keng zonali materiallar yuqori haroratli elektronikada ishlatiladi."),
  ({"mat": "#0", "Nd": 16, "T": 300}, "Namoyish tugadi. Endi parametrlarni o‘zingiz o‘zgartirib, xususiy o‘tkazuvchanlik qaysi haroratda boshlanishini toping.")],
 "schottky": [
  ({"phiB": 0.72, "n": 1.05, "T": 300, "Nd": 16}, "Bu Shottki diodining volt-amper xarakteristikasi. Ko‘k chiziq Shottki diodi, qizil uzuq chiziq taqqoslash uchun p-n diod. Shottki diodi ancha kichik kuchlanishda ochiladi."),
  ({"phiB": 0.6}, "Barer balandligini nol butun oltidan elektronvoltgacha kamaytiramiz. To‘yinish toki qariyb yuz marta ortdi: har oltmish millielektronvoltga o‘n marta. Ochilish kuchlanishi yana kamaydi."),
  ({"phiB": 0.6, "T": 380}, "Haroratni oshirsak, termoelektron emissiya kuchayadi va tok yanada ortadi. Richardson formulasidagi eksponenta shuni ko‘rsatadi."),
  ({"phiB": 0.72, "T": 300, "Nd": 17.5}, "Legirlashni oshirsak, kambag‘allashgan qatlam torayadi va sig‘im ortadi. Juda kuchli legirlashda tunnel o‘tish boshlanadi — omik kontakt shu tarzda olinadi."),
  ({"Nd": 16}, "Endi o‘zingiz barer balandligini o‘zgartirib, bir milliamper tok uchun zarur kuchlanishni kuzating.")],
 "pn": [
  ({"Na": 17, "Nd": 16, "Va": 0}, "Bu p-n o‘tishning zonaviy diagrammasi va elektr maydoni. Muvozanatda Fermi sathi bir xil, kontakt potensiallar farqi nol butun yetti yuz yetmish to‘rt volt, kambag‘allashgan qatlam kengligi nol butun uch mikrometr."),
  ({"Va": -5}, "Teskari kuchlanish beramiz: minus besh volt. Zonalar egilishi ortdi, qatlam kengaydi, maksimal maydon kuchaydi, sig‘im esa kamaydi. Varikaplar shu xossaga asoslangan."),
  ({"Va": 0.5}, "Endi to‘g‘ri kuchlanish: nol butun besh volt. To‘siq pasaydi, qatlam torayib, kvazi-Fermi sathlari besh yuz millielektronvoltga ajraldi. Asosiy bo‘lmagan tashuvchilar injeksiyasi boshlanadi."),
  ({"Va": 0, "Na": 19}, "P-sohani juda kuchli legirlaymiz. Endi qatlam deyarli butunlay n-sohaga tarqaldi — bu bir tomonlama o‘tish."),
  ({"Na": 17}, "Namoyish tugadi. Kuchlanishni o‘zgartirib, sig‘im kvadrat ildiz qonuniyati bo‘yicha o‘zgarishini o‘zingiz tekshiring.")],
 "diode": [
  ({"Is": -13, "n": 1.2, "Rs": 2, "T": 300, "log": "#0"}, "Bu real diodning volt-amper xarakteristikasi. Kulrang uzuq chiziq ideal diod, ko‘k chiziq ketma-ket qarshilik hisobga olingan real diod. Katta toklarda ular ajraladi."),
  ({"Rs": 15}, "Ketma-ket qarshilikni o‘n besh omgacha oshiramiz. Xarakteristika yotiqlashdi: katta toklarda qo‘shimcha kuchlanish tok va qarshilik ko‘paytmasiga teng."),
  ({"Rs": 2, "log": "#1"}, "Logarifmik shkalaga o‘tamiz. Endi xarakteristika to‘g‘ri chiziq ko‘rinishida, uning qiyaligidan ideallik koeffitsiyenti topiladi."),
  ({"T": 360}, "Haroratni oshiramiz. To‘yinish toki ortgani uchun bir xil tokda kuchlanish kamaydi — taxminan har kelvinga ikki millivolt. Diodli termometrlar shunga asoslangan."),
  ({"T": 300, "log": "#0"}, "Endi o‘zingiz ideallik koeffitsiyentini o‘zgartirib, uning ta’sirini kuzating.")],
 "zener": [
  ({"mode": "#0", "Vz": 5.6, "rz": 10}, "Bu stabilitronning xarakteristikasi. Teskari yo‘nalishda besh butun olti voltda teshilish boshlanadi va tok keng oraliqda o‘zgarganda ham kuchlanish deyarli o‘zgarmaydi."),
  ({"Vz": 3.3}, "Stabilizatsiya kuchlanishini uch butun uch voltga kamaytiramiz. Bu sohada tunnel, ya’ni Zener teshilishi ustun, harorat koeffitsiyenti manfiy."),
  ({"Vz": 12}, "O‘n ikki voltda esa ko‘chkisimon teshilish ustun va harorat koeffitsiyenti musbat. Besh-olti volt atrofida ular bir-birini kompensatsiyalaydi."),
  ({"mode": "#1", "Ip": 10}, "Endi tunnel diodni tanlaymiz. Cho‘qqidan keyin tok kamayadi — bu manfiy differensial qarshilik sohasi. Tunnel diodlar yuqori chastotali generatorlarda ishlatiladi."),
  ({"mode": "#0", "Vz": 5.6}, "Namoyish tugadi. Differensial qarshilikni o‘zgartirib, stabilizatsiya sifatini o‘zingiz baholang.")],
 "bjt": [
  ({"beta": 150, "VA": 80, "Ib": 30, "Vcc": 12, "Rc": 1.5}, "Bu bipolyar tranzistorning chiqish xarakteristikalari. Sariq uzuq chiziq — yuklama chizig‘i, yashil nuqta — ishchi nuqta. Tranzistor aktiv, ya’ni kuchaytirish rejimida."),
  ({"Ib": 55}, "Baza tokini oshiramiz. Kollektor toki beta marta ortdi va ishchi nuqta yuklama chizig‘i bo‘ylab chapga, to‘yinish sohasiga siljidi. Bunday rejimda tranzistor kalit kabi ishlaydi."),
  ({"Ib": 20}, "Baza tokini kamaytirib, ishchi nuqtani o‘rtaga qaytaramiz. Kuchaytirgichda signal buzilmasligi uchun nuqta xarakteristikalar o‘rtasida bo‘lishi kerak."),
  ({"VA": 25}, "Erli kuchlanishini kamaytirsak, xarakteristikalar qiyalashadi: chiqish qarshiligi kamayadi va kuchaytirish koeffitsiyenti pasayadi."),
  ({"VA": 80, "Ib": 30}, "Endi o‘zingiz yuklama qarshiligini o‘zgartirib, ishchi nuqtani kollektor-emitter kuchlanishi olti volt bo‘ladigan joyga keltiring.")],
 "bjtfreq": [
  ({"b0": 150, "fT": 300}, "Bu tok kuchaytirish koeffitsiyentining chastotaga bog‘liqligi. Past chastotada u bir yuz ellikka teng, beta kesish chastotasidan keyin har o‘n marta chastota oshganda o‘n marta kamayadi."),
  ({"fT": 3000}, "Chegaraviy chastotani uch gigagersgacha oshiramiz. Butun egri chiziq o‘ngga siljidi — tranzistor tezroq. Bunday chastotalar uchun yupqa baza va kichik sig‘imlar kerak."),
  ({"b0": 50}, "Past chastotali kuchaytirishni ellikka kamaytirsak, beta kesish chastotasi ortadi, lekin chegaraviy chastota o‘zgarmaydi: kuchaytirish va polosa ko‘paytmasi saqlanadi."),
  ({"b0": 150, "fT": 300}, "Endi o‘zingiz parametrlarni o‘zgartirib, birga teng kuchaytirish nuqtasini toping.")],
 "thyristor": [
  ({"Vbo": 400, "Ig": 0, "Igt": 25, "Ih": 30}, "Bu tiristorning volt-amper xarakteristikasi. Boshqaruv toki nolga teng: tiristor to‘rt yuz voltgacha yopiq, so‘ng keskin ochiladi."),
  ({"Ig": 15}, "Boshqaruv tokini o‘n besh milliamperga oshiramiz. Ochilish kuchlanishi sezilarli kamaydi."),
  ({"Ig": 25}, "Boshqaruv toki ochilish tokiga yetdi — tiristor deyarli darhol ochiladi. Faza boshqaruvli rostlagichlar shunday ishlaydi."),
  ({"Ih": 60}, "Ushlab turish tokini oshirsak, tiristorni ochiq saqlash uchun kattaroq anod toki kerak bo‘ladi. Anod toki undan kamaysa, tiristor yopiladi."),
  ({"Ig": 10, "Ih": 30}, "Endi o‘zingiz boshqaruv tokini o‘zgartirib, ochilish kuchlanishining bog‘liqligini kuzating.")],
 "jfet": [
  ({"Idss": 10, "Vp": -4, "Vgs": 0}, "Chapda JFETning o‘tish xarakteristikasi, o‘ngda chiqish xarakteristikalari. Zatvor kuchlanishi nolga teng — stok toki maksimal, o‘n milliamper."),
  ({"Vgs": -1.5}, "Zatvorga minus bir yarim volt beramiz. Kambag‘allashgan qatlamlar kanalni toraytirdi, tok qariyb to‘rt milliamperga tushdi. Tiklik ham kamaydi."),
  ({"Vgs": -3.6}, "Berkilish kuchlanishiga yaqinlashdik: kanal deyarli yopildi, tok juda kichik."),
  ({"Vgs": -1.5, "Vp": -2}, "Berkilish kuchlanishini minus ikki voltgacha kichraytirsak, xuddi shu zatvor kuchlanishida kanal berkilishga yaqinlashadi: tok va tiklik kamayadi, lekin nol kuchlanishdagi maksimal tiklik ortadi."),
  ({"Vp": -4}, "Endi o‘zingiz zatvor kuchlanishini o‘zgartirib, tiklikning tok kvadrat ildiziga proporsionalligini tekshiring.")],
 "mosc": [
  ({"Na": 17, "tox": 10, "Vfb": -0.9}, "Bu MDYa strukturasining sig‘im-kuchlanish xarakteristikasi. Chapda boyish rejimi, o‘rtada kambag‘allashish, o‘ngda inversiya. Bo‘sag‘a kuchlanishi nol butun to‘rt volt atrofida."),
  ({"tox": 40}, "Oksidni qalinlashtiramiz. Oksid sig‘imi kamaydi, bo‘sag‘a kuchlanishi esa ortdi."),
  ({"tox": 10, "Na": 16}, "Taglik legirlanishini kamaytirsak, kambag‘allashgan qatlam kengayadi va yuqori chastotali minimal sig‘im kamayadi."),
  ({"Na": 17, "Vfb": -0.3}, "Tekis zonalar kuchlanishini o‘zgartirsak, butun egri chiziq siljiydi. Oksiddagi zaryadlar aynan shunday siljish beradi."),
  ({"Vfb": -0.9}, "Endi o‘zingiz parametrlarni o‘zgartirib, past va yuqori chastotali egri chiziqlar farqini kuzating.")],
 "mosfet": [
  ({"Vt": 0.7, "k": 4, "lam": 0.02, "Vgs": 2.5, "T": 300}, "Bu MOSFETning chiqish xarakteristikalari. Ko‘k chiziq tanlangan zatvor kuchlanishi uchun, sariq uzuq chiziq chiziqli va to‘yinish sohalari chegarasi."),
  ({"Vgs": 4}, "Zatvor kuchlanishini to‘rt voltga oshiramiz. To‘yinish toki kuchlanish ortig‘ining kvadratiga proporsional ravishda ortdi."),
  ({"Vgs": 2.5, "T": 420}, "Haroratni to‘rt yuz yigirma kelvingacha oshiramiz. Harakatchanlik kamaygani uchun tok kamaydi. Shu sababli quvvat MOSFETlarni parallel ulash xavfsiz."),
  ({"T": 300, "lam": 0.08}, "Kanal uzunligi modulyatsiyasini oshirsak, to‘yinish sohasida xarakteristika qiyalashadi — chiqish qarshiligi kamayadi."),
  ({"lam": 0.02}, "Endi o‘zingiz haroratni o‘zgartirib, tok deyarli o‘zgarmaydigan zatvor kuchlanishini toping.")],
 "solar": [
  ({"G": 1000, "J0": -12, "n": 1, "T": 300}, "Bu quyosh elementining volt-amper va quvvat xarakteristikasi. Standart yoritilganlikda qisqa tutashuv toki o‘ttiz besh milliamper, salt yurish kuchlanishi nol butun oltmish uch volt, foydali ish koeffitsiyenti o‘n sakkiz foiz atrofida."),
  ({"G": 300}, "Yoritilganlikni uch yuz vattgacha kamaytiramiz. Tok uch marta kamaydi, kuchlanish esa juda oz — logarifmik qonuniyat."),
  ({"G": 1000, "T": 345}, "Panel qizib, harorat yetmish ikki darajaga yetdi. Salt yurish kuchlanishi va quvvat kamaydi. Yozgi issiqda panellar shuning uchun kamroq energiya beradi."),
  ({"T": 300, "J0": -10}, "Qorong‘i tokni yuz marta oshirsak, ya’ni rekombinatsiya kuchaysa, kuchlanish va foydali ish koeffitsiyenti kamayadi. Sifatli material va sirt passivatsiyasi shuning uchun muhim."),
  ({"J0": -12}, "Endi o‘zingiz parametrlarni o‘zgartirib, maksimal quvvat nuqtasining siljishini kuzating.")],
 "led": [
  ({"Eg": 1.9, "T": 300, "Ith": 20, "eta": 0.5}, "Chapda svetodiod spektri, o‘ngda lazerning quvvat-tok xarakteristikasi. Taqiqlangan zona bir butun to‘qqiz elektronvolt — qizil nur, olti yuz ellik nanometr atrofida."),
  ({"Eg": 2.4}, "Taqiqlangan zonani ikki butun to‘rt elektronvoltga oshiramiz. Nur yashil rangga o‘tdi: to‘lqin uzunligi bir ming ikki yuz qirqni taqiqlangan zonaga bo‘lishga teng."),
  ({"Eg": 2.75}, "Ikki butun yetmish besh elektronvoltda ko‘k nur. Oq svetodiodlar ko‘k kristall va sariq fosfordan yasaladi."),
  ({"Eg": 1.9, "Ith": 45}, "Lazerning bo‘sag‘a tokini oshiramiz. Bo‘sag‘agacha nurlanish juda kuchsiz, undan keyin quvvat tokka chiziqli o‘sadi."),
  ({"Ith": 20}, "Endi o‘zingiz haroratni o‘zgartirib, spektr qaysi tomonga siljishini kuzating.")],
 "ccd": [
  ({"cte": 0.9995, "N": 1020, "speed": 1}, "Bu uch fazali zaryad aloqali asbob. Ko‘k elektrodlar faol faza: zaryad paketlari potensial chuqurlar bo‘ylab bir yo‘nalishda siljiydi. Pastdagi grafik har uzatishda qolgan zaryad ulushini ko‘rsatadi."),
  ({"cte": 0.9999}, "Uzatish samaradorligini oshiramiz. Ming uzatishdan keyin ham zaryadning to‘qson foizi saqlanadi."),
  ({"cte": 0.99999, "N": 3000}, "Uch ming uzatish va besh to‘qqizdan keyin to‘qqiz bo‘lgan samaradorlik: yo‘qotish atigi uch foiz. Astronomik kameralarda shunday yuqori samaradorlik talab qilinadi."),
  ({"cte": 0.9995, "N": 1020}, "Endi o‘zingiz samaradorlikni o‘zgartirib, yo‘qotish bir foizdan kam bo‘ladigan qiymatni toping.")],
 "cmos": [
  ({"Vdd": 3.3, "Vtn": 0.5, "Vtp": 0.5, "r": 1, "D": 0}, "Bu KMOP invertorning uzatish xarakteristikasi. Tranzistorlar simmetrik, shuning uchun o‘tish bo‘sag‘asi manba kuchlanishining yarmida."),
  ({"r": 3}, "n-kanalli tranzistorni kuchliroq qilamiz. O‘tish bo‘sag‘asi chapga siljidi, shovqin zahiralari nosimmetrik bo‘ldi."),
  ({"r": 1, "D": 250}, "Endi ikki yuz ellik kilorad nurlanish dozasi. Oksidda tutilgan musbat zaryad bo‘sag‘a kuchlanishlarini siljitdi va xarakteristika chapga surildi. Kosmik elektronikada shuning uchun radiatsiyaga chidamli sxemalar kerak."),
  ({"D": 0, "Vdd": 1.2}, "Manba kuchlanishini bir butun ikki voltga kamaytiramiz. Dinamik quvvat kuchlanish kvadratiga proporsional, ya’ni qariyb yetti yarim marta kamayadi."),
  ({"Vdd": 3.3}, "Endi o‘zingiz nisbat va dozani o‘zgartirib, shovqin zahiralarini kuzating.")],
 "resist": [
  ({"Ns": 19.5, "Ld": 1, "d": 0}, "Chapda diffuziyalangan qatlamning kirishma profili, o‘ngda qatlam qarshiligining olib tashlangan qalinlikka bog‘liqligi."),
  ({"d": 1.2}, "Qatlamning bir butun ikki mikrometrini olib tashlaymiz. Eng kuchli legirlangan sirt qismi ketdi, qatlam qarshiligi keskin ortdi."),
  ({"d": 2.2}, "Yana chuqurroq: qarshilik yanada ortdi. Har bosqichdagi o‘zgarishdan lokal solishtirma qarshilik va konsentratsiya tiklanadi — chiziqli diagramma usuli shunga asoslangan."),
  ({"d": 0, "Ld": 2}, "Diffuziya uzunligini ikki marta oshirsak, o‘tish chuqurligi ham ikki marta ortadi, qatlam qarshiligi esa taxminan ikki marta kamayadi."),
  ({"Ld": 1}, "Endi o‘zingiz sirt konsentratsiyasini o‘zgartirib, to‘rt zondli o‘lchovda kutiladigan kuchlanishni hisoblang.")],
}
