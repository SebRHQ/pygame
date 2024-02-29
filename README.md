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
