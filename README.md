# Library App
## Logika:
- Csak elérhető (nem kölcsönzött) könyvek kölcsönözhetők.
- Adminok kezelhetik a könyvek és szerzők adatait.
- Felhasználók csak saját kölcsönzéseiket és értékeléseiket láthatják/módosíthatják.
- Egy felhasználó nem értékelhet egy könyvet többször.
- Minden könyvhöz automatikusan számítsd ki az átlagos értékelést.
- Az értékelési átlag frissüljön minden új értékelés után.
- Az adminok felhasználói statisztikákat tekinthetnek meg (pl. melyik könyvet kölcsönözték a legtöbben, legaktívabb felhasználók).

## Késedelmi díjak
- Minden kölcsönzéshez automatikusan számíts ki késedelmi díjat, ha a visszaadási dátum meghaladja az előírt kölcsönzési időszakot.
- A késedelmi díj alapja legyen napi összeg, amely admin által állítható be.
- Csak azok a felhasználók kölcsönözhetnek újra, akiknek nincs tartozásuk.

## Könyv Keresés és Szűrés
### Keresés
- A felhasználók kereshetnek könyveket:
    - cím, 
    - szerző, 
    - kategória
    - kiadási év alapján.

### Szűrés
- Csak elérhető könyvek
- Legmagasabb értékelésű könyvek
- Legújabb könyvek

## Felhasználói Kölcsönzési Limit
- Minden felhasználónak legyen maximális kölcsönzési limitje (pl. 5 könyv egyszerre).
- Az adminisztrátorok növelhetik vagy csökkenthetik a kölcsönzési limitet egyénileg.

## Könyv Példányszámok Kezelése
- A könyvekhez add hozzá a "példányszám" mezőt, amely jelzi, hogy hány példány van egy adott könyvből a könyvtárban.
- Kölcsönzéskor csökken a példányszám, visszaadáskor növekszik.
- Csak akkor engedélyezett a kölcsönzés, ha van elérhető példány.

# Extra

## Értesítési Rendszer
- Ha egy kölcsönzés lejárt, a felhasználó kapjon e-mail értesítést.
- Ha egy könyv, amelyre a felhasználó vár, elérhetővé válik, értesítést kapjon.

## Könyvek Importálása CSV Fájlból
- Az adminok egy CSV fájl feltöltésével tömegesen adhatnak hozzá új könyveket a rendszerhez.
- A CSV fájl tartalmazza a következő mezőket: Cím, Szerzők, Kiadó, ISBN, Kiadási év, Kategória, Példányszám.