import pandas
zvirata = pandas.read_csv("adopce-zvirat.txt", sep=";")
print(zvirata.columns)
print(zvirata.shape)
czNazev = zvirata.iloc[33, 1]
print(czNazev)
enNazev = zvirata.iloc[33, 2]
print(enNazev)