import pandas
zvirata = pandas.read_csv("adopce-zvirat.txt", sep=";", index_col="nazev_cz")

print(zvirata.index.is_unique)
zvirata = zvirata.sort_index(ascending=True)
print(zvirata)
outlon = zvirata.loc["Outloň váhavý"]
print(outlon)
zelvy = zvirata.loc["Želva černavá":"Žluva hajní"]
print(zelvy)