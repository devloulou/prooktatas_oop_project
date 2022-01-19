# 1 .feladat: az alább megadott dictionary-ből hozzunk létre JSON stringet

my_dict = {"car": "BMW", "color": "yellow"}

import json

my_json_srting = json.dumps(my_dict, indent=4)

#print(my_json_srting)

# 2. feladat: A Fibonacci sorozatra igaz, hogy minden elem az azt megelőző 2 elem
# összegével egyenlő.
# Írjatok egy olyan függvényt, amely paraméterben kap egy számot.
# A megadott szám a Fibonacci sorozat új elemeinek számát jelenti.
# A függvény szúrja be az új elemeket a lenn megadott listába

# példa függvényhívásra: my_fib(2) -> elvárt eredmény:  [0,1,1,2,3,5,8,13,21,34]


my_list = [0,1,1,2,3,5,8,13]

def my_fib(param):
    for item in range(param):
        my_next_fib = sum(my_list[-2:])
        my_list.append(my_next_fib)

my_fib(1000)
#print(my_list)

# 3. feladat: Írjatok egy olyan függvényt, amely a 2 megadott listából egy dictionary-t
# állít elő

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def my_func():
    my_dict = {}
    for item in range(len(keys)):
        my_dict[keys[item]] = values[item]

    return my_dict

def my_func2():
    return {keys[item]:values[item] for item in range(len(keys))}

my_dict = {keys[item]:values[item] for item in range(len(keys))}

# print(my_func())
# print(my_dict)
# print(my_func2())



# 4. feladat: Írjatok egy olyan függvényt, amely a megadott dictionary-ből
# extractolj a megadott kulcsokat és a hozzá tartozó értékpárokat:

# elvárt output: {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


def my_func(keys):
    my_dict = {}
    for item in keys:
        if sample_dict.get(item):
            my_dict[item] = sample_dict.get(item)

    return my_dict

def my_func2(keys):
    return {item:sample_dict.get(item) for item in keys if sample_dict.get(item)}

print(my_func(keys))
print(my_func2(keys))