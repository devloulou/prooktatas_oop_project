import re

my_str = 'Kedves kovács richárd az ön email címe az : dev.kovacs. az richard1990@gmail.edu.com'

    


# x = re.findall("^\D{4}ény", my_str)

# x = re.search("\w+@\w+", my_str)

#x = re.search(r"^\w+", my_str)

x = re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', my_str)

x = re.search(r"([A-z0-9]+[.-_])*[A-z0-9]+@[A-z0-9-]+(\.[A-Z|a-z]{2,})+", my_str)

y = re.split(r"@", my_str)

z = re.sub(r"@", "$", my_str)

print(z)

# if x:

#     position = x.span()

#     print(my_str[position[0]:position[1]])