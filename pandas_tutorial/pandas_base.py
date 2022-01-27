import pandas as pd

# Series: olyan mint az egycelben 1 oszlop -> 1 dimenziós tömb
# DataFrame: adatrbázis tábla -> 2 dimenziós tömb
# Panel: 3 dimenziós adatok tárolására van kialakítva

my_list = [1, 2, 3, 4, 5, 6]
my_cols = ['a', 'b', 'c', 'd', 'e', 'f']

s = pd.Series(my_list, index=my_cols)

# print(s)
# print(s.index)

# print(s[::2])


# print(s['b'])
# print(s[['a', 'd', 'f']])


# törölni adatot


# print(s)

del s['e']

# print()
# print(s)


s.pop('f')
# print()
# print(s)


# hozzá adni elemet

s["f"] = "Ricsi"

# print()
# print(s)

# megváltoztatni

s["f"] = "Norbi"

# print()
# print(s)

################################################################

# dataFrame

my_list = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(my_list)

#print(df)

# print()
# print(df.info())

# print(df.head(3))

# print()
# print(df.tail(2))

#print(df.info())

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)

print(df)
print(df.groupby("Team").groups)



print(df['Points'].sum())
print(df['Points'].median())
print(df['Points'].mode())


del df['Team']


df.pop('Year')


df['Team'] = None
print(df)