# Beadandó feladat

# A feladat több részből áll. Kérlek benneteket, hogy egy újrafuttatható,
# működő megoldást küldjetek vissza tömörített formában, emailben.
# A feladat során bármit használhattok, kódrészleteket.
# Törekedjetek az együtt tanutlak használatára
# Minden esetben a minimum követelmény, hogy legalább függvények implementálásával 
# oldjátok meg a feladatokat.
# Ha egy adott feladatot nem sikerül megoldani, akkor is küldjétek el a próbálkozásokat
# Törekedjetek az átlátható kód írására, ne legyenek kikommentezett részek a beadott munkában

####################################################################################
################################### FELADATOK ######################################
# 1. feladat: a csatolt "data" mappában lévő csv-k betöltése általatok választott
# adatbázisba
# az adatbázis lehet: postgres, oracle, sqlite de aki modernebb megoldást preferálna
# lehetősége van mongodb használatára is

# Aki Postgrest választ következő driverek közül válasszon: psycopg2, SQLAlchemy, pandas
# Oracle esetén a cx_Oracle,
# MongoDb esetéb pymongo libraryt használjátok

# Relációs adatbázis esetén a file-okat külön táblákba töltéstek be
# a betöltés után manuálisan határozzátok meg, hogy mely táblákra milyen constrainteket tesztek
# foreing_key és primary_key -eket értem constraintek alatt
# Mongodb esetében nem szükséges
# Mongodb esetében 1 dokumentumba legyen az 1 emberhez tartozó adatok összessége
# aki szeretné csinálhat külön collection-öket, amelyek logikailag szétdarabolják az adatot

# 2. feladat: adatbázistól függetlenül ugyan ez a feladat
# A HR úgy döntött, hogy szeretné bővíteni a dolgozók számát,
# így csoportos és egyéni feltételt hirdet megannyi pozícióra
# írjatok olyan programot, amely lehetővé teszi, hogy 1 vagy több embert egyidejű
# felvétele során kelettkezett dolgozói adatok betöltésre kerüljenek
# a betöltés során használt tesztadatot magatoknak kell elkészítenetek

# 3. feladat:
# Az 2021-ben 7% felett volt az infláció. Mi egy roppant remek munkahelyen dolgozunk,
# ahol 3-5% közötti fizetésmelést kapnak a dolgozók.
# Írjatok egy olyan programot, amely 
# A % meghatározása a következő legyen: 
# - akinek az emelés után a fizetése meghaladja a maximális fizetés mértékét,
#   neki automatikusan a maximálisan megadható összeg legyen beállítva
# - aki a minimális összeget keresi a pozíciójában, ő automatikusan 5%-ot kapjon
# - mindenki más random %-ot kapjon

# 4. feladat: Statisztika készítés
# Az emelést követően csináljatok statisztikát a következőre
# Mely emberek keresnek a legtöbbet adott pozícióban. 
# Mely emberek keresnek a legkevesebbet az adott pozícióban

#HA több ember van ugyan azzal a bérrel
# akkor mindenkit tegyünk a listába

# Mekkora a különbség a legnagyobb és legkisebb fizetés között

# A kapott eredményeket JSON be írjátok ki
# A JSON struktúrája a következő legyen:
# 
{
    "best_salaries_per_positions": [
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
    ],
    "worst_salaries_per_positions": [
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
        {"employee_name": "name", "salary": 12345, "position": "job name"},
    ],
    "differences": {

        "best_salary": 12345,
        "worst_salary": 1234,
        "difference": 12345 - 1234
    }
} 