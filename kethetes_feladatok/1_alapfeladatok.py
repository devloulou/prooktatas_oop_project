# 1. feladat: Írjatok egy olyan függvényt, ami az alább megadott 2 dictionaryből egy harmadikat készít - merge-li őket -

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict3 = {**dict1, **dict2}

dict3 = {}

dict3.update(dict1)
dict3.update(dict2)


#print(dict3)

############################################################################
# 2. feladat: írjatok egy olyan függvényt, amely az alábbi dictionary-ben,
# az értékek közzül csak azokat hagyja meg,
# amelyek semelyik másik listában nem szerepel

# Példa:
# test_dict = {'ricsi': [1], 'norbi': [1,2,3]}
# my_func(test_dict)
# output: {'ricsi': [], 'norbi': [2,3]}
#



test_dict = {'Jolán' : [1, 4, 5, 6],
            'Ibolya' : [1, 8, 9],
            'Jácint': [10, 22, 4],
            'Karcsi': [5, 11, 22]}

temp = [j for item in test_dict.values() for j in item ]
temp2 = []
#print(f"temp: {temp}")
for item in temp:
    #print(f"temp.count(item): {temp.count(item)} - item: {item}")
    if temp.count(item) > 1:
        temp2.append(item)

temp = list(set(temp2))

my_list = [1,2,3]

for key, value in test_dict.items():
    for item in temp:
        if item in value:
            value.remove(item)

#print(test_dict)

####################################################################################

# 3. feladat: írjatok egy olyan függvényt, amely az alábbi példában látható módon alakítka át:

# test_list = [{'tibi': 10, 'fizetes': 123 }, {'tibi': 5, 'fizetes': 456 }]
# my_func(test_list)
# output: [['tibi', 'fizetes'], [10, 123], [5, 456]]

test_list = [{'Robi' : 17, 'Karcsi' : 18, 'Vendel' : 20},
             {'Robi' : 21, 'Karcsi' : 30, 'Vendel' : 10},
             {'Robi' : 31, 'Karcsi' : 12, 'Vendel' : 19}]

my_list = []
for idx in range(len(test_list)):
    my_list.append(list(test_list[idx].keys()))
    my_list.append(list(test_list[idx].values()))

print(list(my_list))


# 4. feladat: az alábbi lista elemeit alakítsuk át a példában megadott módon


test_list = [('Robi', 17), ('Karcsi',18) , ('Vendel', 20)]

# elvárt output: [{'Robi' : 17}, {'Karcsi' : 18}, {'Vendel' : 20}]
my_list = []
for item in test_list:
    my_list.append({item[0]:item[1]})

#print(my_list)


if __name__ == '__main__':
    test_list = [{'Robi' : 17, 'Karcsi' : 18, 'Vendel' : 20},
             {'Robi' : 21, 'Karcsi' : 30, 'Vendel' : 10},
             {'Robi' : 31, 'Karcsi' : 12, 'Vendel' : 19}]
    def my_func(test_list):
        eredmeny = [list(test_list[0].keys())]
        for i in test_list:
            eredmeny.append(list(i.values()))

        return eredmeny

    print(my_func(test_list))