# Feladat: postgres használat
# a 4_jsons mappában lévő json-öket töltsük be egy táblába
# a táblába betöltés után minden 100 lóerőnél - horsepower - kisebb értékű adatot töröljük a táblából

# a 10 legkisebb fogyasztású autóból a következő statisztikát készítsük el, és json-be írjuk ki:
# legrégebbi - Year
# legkisebb fogyasztás
# legnagyobb lóerő
# legkönnyebb - weight_in_lbs

import os
import json
import psycopg2 as postgres
from datetime import datetime


json_path = r"C:\WORK\Prooktatás\oop_project\kethetes_feladatok\4_jsons"

def get_connection():
        return postgres.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432,
            database="postgres"
            )

# előállítja a jsonket tartalmazó listát
def get_jsons():
    return [os.path.join(json_path, file) for file in os.listdir(json_path) if file.endswith('.json')]

# felolvassa a json-file-okat
def read_json(file_path):
    data = None
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
    return data

# létrehozza a táblát
def generate_table_script(json_data):
    cre_table_script = 'create table cars ('

    for key, value in json_data.items():
        cre_table_script += f"{key.lower()} {gen_database_type(value)},"
    
    cre_table_script += " creation_date date default now())"

    print(cre_table_script)

def gen_database_type(data):

    if isinstance(data, str):
        try:
            datetime.strptime(data, '%Y-%m-%d')
            return "date"
        except:
            pass

        return f"varchar({int(len(data)/10)+10})"
    if isinstance(data, int):
        return "int4"
    if isinstance(data, float):
        return "numeric"
    else:
        return None
    

# betölti az adatot a táblába
def insert_data(data):
    insert_statement = """insert into cars (
        name
        ,miles_per_gallon
        ,cylinders
        ,displacement
        ,horsepower
        ,weight_in_lbs
        ,acceleration
        ,year
        ,origin)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    with get_connection() as con:
        with con.cursor() as cursor:
            cursor.execute(insert_statement, tuple(data.values()))

# elvégzi a törlést
def run_script(script):
    with get_connection() as con:
        with con.cursor() as cursor:
            if 'drop' not in script:
                cursor.execute(script)
            # ez veszélyes: sql injection


# statisztikát előállítja

if __name__ == '__main__':
    delete_script = """delete from cars c
                    where c.horsepower < 100;"""
    json_list = get_jsons()

    # for item in json_list:
    #     insert_data(read_json(item))
        # generate_table_script(read_json(item))

    run_script(delete_script)

    # print(gen_database_type(13))
    # print(gen_database_type("ford ltd"))
    # print(gen_database_type('1973-01-01'))
    # print(gen_database_type(8.5))
    # print(gen_database_type(None))

    