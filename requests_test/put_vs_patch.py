
my_dict = {

    "name": "Ricsi", 
    "age": 32
}

# hozzáadni egy email címet:

# http put-al:
# 

# PUT
# endpoint/adat

adat = {"email": "test@email.hu", "name": "Ricsi"}

# eredmény:
my_dict = {
    "email": "test@email.hu",
    "name": "Ricsi",    
}

# PATCH - partial update
my_dict = {

    "name": "Ricsi", 
    "age": 32
}

adat = {"email": "test@email.hu", "name": "Ricsi", "age": 40}

eredmeny = {    
    "name": "Ricsi", 
    "age": 40,
    "email": "test@email.hu"
}