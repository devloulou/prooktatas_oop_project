

def my_dict():

    test_dict = {'Jolán' : [1, 4, 5, 6],
        'Ibolya' : [1, 8, 9],
        'Jácint': [10, 22, 4],
        'Karcsi': [5, 11, 22]}


    latott = [j for item in test_dict.values() for j in item ]
    # print(latott)
    # exit()
    for i in test_dict.values():
        for k in latott:
            if k in i:
                i.remove(k)
        latott.extend(i)
    return test_dict





print(my_dict())