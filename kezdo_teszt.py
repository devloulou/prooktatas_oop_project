# 1. feladat: írj egy olyan függvényt, amely a megadott listából eltávolítja azon  elemek összes előfordulását,
# amelyek duplikálva vannak..
# lehetséges output: my_func(my_list) -> output: ['banana', 'melon', 'tomato', 'plum']

my_list = ['apple', 'banana', 'melon', 'apple', 'orange', 'tomato', 'orange', 'plum']

def my_func(p_list):
    from collections import Counter

    duplicated = dict(Counter(p_list))
    list_set = list(set(my_list))

    for key, value in duplicated.items():
        if value > 1:
            list_set.remove(key)
    
    return list_set

#print(my_func(my_list))


# 2. feladat: Írj egy olyan függvényt, amely az alább létrehozott tuple minden elemének az 1/10-ére
# módosítja.
# példa függvény hivásra és outputra: 
# my_func(my_tuple) -> output. (1, 2, 3, 4, 5). Ügyeljetek, hogy tuple elemei integerek legyenek

my_tuple = (10, 20, 30, 40, 50)

def my_func(p_tuple):
    return tuple(int(item/10) for item in p_tuple if isinstance(item, int))

#print(my_func(my_tuple))

# 3. feladat: Írjatok egy olyan függvényt, amely 
# lehetőséget teremt arra, hogy tetszőleges mennyiségű és típusú email címet hozzá tudjunk adni.
# a feladat során gondoljatok arra, hogy első futás során nincs még email, a többi futásnál pedig már lesz email adat.

# példa függvény hivásra és outputra: Az email_parameter értéke minden esetben dict-nek kell, hogy legyen. 
# (vagy olyen lista - tuple, amelynek elemei dictionaryk)
# my_func(email_parameter) -> lehetséges output: 

# my_dict ={
#     "firstName": "Rack",
#     "lastName": "Jackon",
#     "gender": "man",
#     "age": 24,
#     "address": {
#         "streetAddress": "126",
#         "city": "San Jone",
#         "state": "CA",
#         "postalCode": "394221"
#     },
#     "phoneNumbers": [
#         { "type": "home", "number": "7383627627" }
#     ]
#     "email_addresses": [
#       {"type": "business", "email": "business@email.com"},
#       {"type":  "private", "email": "private@email.com"}    
#   ]
# }

my_dict ={
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "age": 24,
    "address": {
        "streetAddress": "126",
        "city": "San Jone",
        "state": "CA",
        "postalCode": "394221"
    },
    "phoneNumbers": [
        { "type": "home", "number": "7383627627" }
    ]
}


def add_email(email_param):
    # még nem létezik az email_addresses mint kulcs
        # vagy dict-et kapunk
        # vagy valamilyen iterálható objektumot, amiben dict-ek vannak
    # már létezik az email_addresses
        # vagy dict-et kapunk
        # vagy valamilyen iterálható objektumot

    if not my_dict.get("email_addresses"):
        if isinstance(email_param, dict):
            my_dict["email_addresses"] = [email_param]
        elif isinstance(email_param, tuple):
            my_dict["email_addresses"] = list(email_param)
        elif isinstance(email_param, list):
            my_dict["email_addresses"] = email_param
    else:
        if isinstance(email_param, dict):
            my_dict["email_addresses"].append(email_param)
        elif isinstance(email_param, tuple):
            my_dict["email_addresses"].extend(list(email_param))
        elif isinstance(email_param, list):
            my_dict["email_addresses"].extend(email_param)

test_email1 = {"type": "business", "email": "business@email.com"}
test_email2 = [{"type": "business", "email": "business@email.com"},
                {"type": "private", "email": "private@email.com"}
            ]

test_email3 = ({"type": "business", "email": "business@email.com"},
                {"type": "private", "email": "private@email.com"}
)

import pprint
pp = pprint.PrettyPrinter(indent=4)

add_email(test_email3)

add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
add_email(test_email3)
pp.pprint(my_dict)


