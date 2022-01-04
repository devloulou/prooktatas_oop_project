# Egyetemi féléves értékelő: írjatok egy olyan programot - függvények segíségével - ,
# amely az alábbi tanulók féléves jegyét meghatározza.
# Az értékelésnél a következő szabályokat kell betartani:

## a beadando a jegy 10%-át adja
## a vizsga a jegy 70%-át
## a labor gyakorlat pedig a jegy 20%-át

# Az eredmények a következők szerint kell meghatározni
# 90 - 100 => 5
# 80 - 89 => 4
# 70 - 79 => 3
# 60 - 69 => 2
# 0  - 59 => 1

# példa az elvárt eredményre:
#
#
# kriszta = { "tanulo":"Kriszta",
#          "beadando" : [70, 60, 30, 10],
#          "vizsga" : [70, 75],
#          "labor" : [68.20, 77.20]
#        }
# (ez egy lekalkulált eredmény)
# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2

###############################################################################
# KIEGÉSZÍTÉS A FELADATHOZ!!!!!!!!!!
# A feladat megoldásánál erősen törekedjetek a függvények használatára! (természetesen lehet OOP megközelítés, ez ügyben kérem, hogy az
# egyszerűség és átláthatóság legyen a megközelítés központi eleme és ne a túl abstractált utat válasszuk)
# postgresben hozzatok létre táblát / táblákat - nincs megkötésem, hogy hogyan -
# a dict kulcshoz tartozó elemek számossága alkalmakat jelentenek,
# tehát 4 beadandó volt, 2 vizsga, 2 labor dolgozat

# az adatokat töltsétek be ezekbe a táblákba
# az eredmények a legenerálás után legyen betöltve egy általatok létrehozott táblába / táblákba

# a 2. feladatot is adatbázisba valósítsátok meg -> a legenerált eredményeket töltsétek be egy táblába / táblákba
###############################################################################
# 2. feladat: az osztály átlag eredményeit is határozzátok meg:
# példa outputra:
#
# Osztály átlag pontszáma 72.79
# Osztály eredménye 3


karcsi = { "tanulo":"Horváth Károly",
         "beadando" : [80, 50, 40, 20],
         "vizsga" : [75, 75],
         "labor" : [78.20, 77.20]
       }


jani = { "tanulo":"Potter János",
          "beadando" : [82, 56, 44, 30],
          "vizsga" : [80, 80],
          "labor" : [67.90, 78.72]
        }


denes = { "tanulo" : "Neumann Dénes",
          "beadando" : [77, 82, 23, 39],
          "vizsga" : [78, 77],
          "labor" : [80, 80]
        }


emese = { "tanulo" : "Morvai Emese",
         "beadando" : [67, 55, 77, 21],
         "vizsga" : [40, 50],
         "labor" : [69, 44.56]
       }


tomi = { "tanulo" : "Kiss Tamás",
        "beadando" : [29, 89, 60, 56],
        "vizsga" : [65, 56],
        "labor" : [50, 40.6]
      }

import psycopg2 as postgres

def get_connection():
        return postgres.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432,
            database="postgres"
            )

# fel kellene dolgozni a dictionery-ket

def test_type_inserts():
    # ősfeltötése a test_type táblának
    types = ['beadando', 'vizsga', 'labor']

    with get_connection() as con:
        with con.cursor() as cursor:
            for item in types:
                cursor.execute(f"insert into test_types (name)\
                    values ('{item}')")

def insert_students():  
    students = [karcsi, jani, denes, emese, tomi]

    with get_connection() as con:
        with con.cursor() as cursor:
            for item in students:
                cursor.execute(f"insert into students (name)\
                    values ('{item['tanulo']}')")

def base_data_loader():
    with get_connection() as con:
        with con.cursor() as cursor:
            cursor.execute("delete from test_types")
            cursor.execute("delete from students")

    test_type_inserts()
    insert_students()

def insert_test_results(student):
    # fel kell dolgozni a dictet -
    # le kell kérni a test_types táblából az id-t
    # le kell kérni a student id-t

     with get_connection() as con:
        with con.cursor() as cursor:
            cursor.execute(f"select student_id from students where name = '{student['tanulo']}'")

            student_id = cursor.fetchone()[0]

            types = ['beadando', 'vizsga', 'labor']

            for item in types:
                cursor.execute(f"select test_type_id from test_types where name = '{item}'")
                type_id = cursor.fetchone()[0]

                for i in student[item]:
                    cursor.execute(f"insert into test_results \
                        (student_fk_id, test_type_id, test_result_value)\
                            values ({student_id},{type_id},{i})")


if __name__ == '__main__':
    # con = get_connection()
    # cursor = con.cursor()

    # cursor.execute('select 123')
    # print(cursor.fetchone())

    base_data_loader()

    students = [karcsi, jani, denes, emese, tomi]
    for item in students:
        insert_test_results(item)