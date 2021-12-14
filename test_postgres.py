import os
import json
import datetime

file_location = r"C:\WORK\Prooktatás\oop_project\meta_data\Aladdin.json"

# json file stukturájából egy create table utasítást:
# típusosítás

data = None
with open(file_location, "r") as f:
    data = json.load(f)

print(data)
print()


cols = {}
cols_type = None
for key, value in data.items():
    if isinstance(value, float):
        cols_type = 'decimal({precision}, 1)'.format(precision=len(str(value).split(".")[0]))
    elif isinstance(value, int) and (value not in (True, False)):
        cols_type = 'int' # bigint
    elif isinstance(value, datetime.date):
        cols_type = 'date'
    elif value in (True, False):
        cols_type = 'boolean'
    else:
        # genre_id-t refaktor során le kell majd tárolni -> új táblát many-to-many
        cols_type = 'varchar({precision})'.format(precision=len(value))
    
    try:
        dto = datetime.datetime.strptime(value, '%Y-%m-%d').date()
        cols_type = 'date'
    except:
        pass

    cols[key] = cols_type

del cols['genre_ids']

print(cols)
print()

create_table_statment = "create table stage_data ("

for key, val in cols.items():
    create_table_statment += f"{key} {val}, "

create_table_statment += 'creation_date date default now())'

print(create_table_statment)




    