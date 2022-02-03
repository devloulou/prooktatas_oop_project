# 4. feladat: Írjatok egy olyan programot, amely megmondja egy megadott szóról, hogy 
# palindrome- e.
# A pilindrome azt jelenti, hogy a szó  visszafelé olvasva ugyan azt a szót adja
# pl. görög ->ez visszafelé olvasva is görög;

def is_palindrome(my_str):
    my_string = "".join([item for item in my_str if ' ' != item])
    return my_string == my_string[::-1]

#print(is_palindrome('egy'))


# 5. feladat: írjatok egy olyan programot, 
# amely paraméterben megadott adatot kiírja egy megadott helyre
# json-ben
# példa hívásra: my_func(json_path, data)

def json_write(json_path, data):
    import os    
    import json

    with open(json_path, "w") as f:
        json.dump(data, f)

my_data = {'key': "value"}

json_write('test_json_27.json', my_data)


# 6. feladat: Írjatok egy olyan programot, amely a 4 matematikai alapműveletet
# összeadás, kivonás, szorzás, osztás elvégzi
# a megoldás állhat több függvényből
# törekedjetek a matematika szabályainak betartására

# a futtatás meghívása a következő legyen:
# pl. my_func(2, 3, "+") -> a művelet minden esetben string legyen

# nem szükséges ennél komplexebb megvalósítás- több szám, kombinált műveletek


def calculator(num1, num2, muvelet):

    def osszead():
        return float(num1) + float(num2)
    
    def kivonas():
        return float(num1) - float(num2)

    def szorzas():
        return float(num1) * float(num2)

    def osztas():
        return float(num1) / float(num2)

    if muvelet not in ('+', '-', '*', '/'):
        raise Exception("Nem adtál meg valid műveletet")
    
    else:

        # try:
        #     float(num1)
        #     float(num2)
        # except:
        #     raise Exception("Nem számot adtál meg")


        validation_error = []

        print(isinstance(num1, (float, int)))

        if not isinstance(num1, (float, int)):
            validation_error.append(num1)
        if not isinstance(num2, (float, int)):
            validation_error.append(num2)

        if len(validation_error) > 0:
            raise Exception("Nem számot adtál meg paraméternek")

        if muvelet == '+':
            return osszead()
        if muvelet == '-':
            return kivonas()
        if muvelet == '*':
            return szorzas()
        if muvelet == '/':
            if int(num2) == 0:
                raise Exception("0-val probáltál meg osztani")
            return osztas()

print(calculator(1,4, '*'))