# pygame
Az összes eddigi pygame projektem

## 1. IKT-Fizikusok projekt
- Egy adatbáziskezelő szoftver pygame-ben, amely képes olvasni egy JSON fájl tartalmait, majd azokat kiírni a kijelzőre
- A felhasználónak további lehetősége van hogy megnyissa az egyes adatokat, és egy leírást olvasson azokról
- A program egy kidolgozott, kattintható felhasználói felületet nyújt a használónak, amely lehetővé teszi a könnyű navigációt
- A JSON Struktúra kifejezetten erre a projektre íródott, de a programban egyes változók átírásával lehetséges akármilyen adatstruktúrát is hozzácsatolni
- A struktúra amit a program képes olvasni a következő:
  {
    "fizikusok": [
      {adat1}, {adat2}, {adat3}
    ]
  }

  Az adatoknak az olvasható struktúra a következő:
  {
    "Születési idő":<évszám stringben>,
    "Név":<név stringben>,
    "Leírás":<leírás stringben>,
    "Kép":<kép elérési útja stringben>
  }

- A program hibás fájlstruktúra esetén hibára figyelmezteti a felhasználót

## 2. SovietOS - Windows XP SOVIET, MacOS S
- Két operációs rendszer jellegének újraalkozása egy fikcionális formában
- A program szovjet poénokat tartalmaz, de megjegyezném hogy nem támogatom a szovjetúniót, csakis a poén és a szórakoztatás kedvéért készítettem
- A szovjet windows-t egy youtube-ra feltöltött powerpoint bemutató inspirálta, amelyet igyekeztem minél pontosabban újraalkotni
- A szovjet MacOS-t is egy powerpoint bemutató inspirált, de itt megpróbáltam egyedi poénokat, illetve funkciókat is belerakni. Ez a program fejlesztés alatt áll
- Mindkét szoftver kattintható felhasználói felületet biztosít a felhasználónak

## 3. Gravitysim - Gravitáció szimuláció
- Ez egy gravitáció-szimulátor, amely különböző tömegű és átmérőjű égitestek egymásra ható erejét, illetve mozgását szimulálja
- A program lehetővé teszi a felhasználó beavatkozását a szimulációba, az irányítások a következők:
    - D: Pontokat rajzolnak az égitestek, a megtett pályájukat kirajzolva. Ez egy viszonylag erőforrásigényes, ezért nem javasolt a funkció folyamatos használata
    - C: Pontok törlése, ha a szimuláció akadozna
    - R: Szimuláció visszaállítása alapkonfigurációba
    - P: Szimuláció szüneteltetése (BÉTAFUNKCIÓ, nem tökéletes a működése)
 
    - Új bolygó lehelyezésé:
        - E: Bolygó lehelyezése a kurzor helyére
        - A program tartalmaz egy húzás funkciót, amely a balklikk hosszan nyomvatartásával érhető el. Nyomd le a bal egérgombot, majd húzd el a kurzort valahova, majd a balklikk felengedésekor csúzliszerűen kilő            egy bolygó a kurzor elhúzásának irányával ellentétes irányba. A húzás erőssége a képernyő jobb oldalán található lenyitható beállítások fülön érhető el.
     
        - A bolygóra vonatkozó beállítások a következők:
            - Mind a tömeget, az erősséget, és az átmérőt egy százalékos formában lehet megadni. A bolygóállás-alapkonfigurációban lévő "nap" beállításai a következők:
              - Tömeg: 50%
              - Átmérő: 40%
            - a "Föld" bolygó beállításai a következők:
              - Tömeg: 1%
              - Átmérő: 10%
            - a "Hold bolygó beállításai a következők:
              - Tömeg: 0,25%
              - Átmérő: 4%
        
                

