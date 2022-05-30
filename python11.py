import requests
import pandas
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(r.content)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(r.content)

praha = pandas.read_csv('zam_praha.csv')
plzen = pandas.read_csv('zam_plzeň.csv')
liberec = pandas.read_csv('zam_liberec.csv')

platy = pandas.read_csv("platy_2021_02.csv")

# Tady jsem se pokusila zkrátit si práci a přidělit název města v cyklu, ale podle googlu v pythonu nejde změnit název proměnné na string..?
# mesta = [praha, plzen, liberec]
# for mesto in mesta:
#   mesto["mesto"] = str(mesto)
praha["mesto"] = "Praha"
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"

# Spojení tabulek
mestaVse = pandas.concat([praha,plzen,liberec], ignore_index = True)
# print(mestaVse.shape)
# Připojení platu
mestaPlat = pandas.merge(mestaVse, platy, on=["cislo_zamestnance"], how="outer")
# print(mestaPlat.shape)
# print(mestaPlat)
# Průměrný plat
# print(mestaPlat.groupby("mesto")["plat"].mean())

nepracuji = mestaPlat[mestaPlat["plat"].isnull()]
nepracuji.to_csv("nepracujici.csv",index=False, sep=";", columns = ["jmeno", "prijimeni"])

pocetNepracujicich = str(nepracuji.shape[0])
# print(f"Nepracuje tu " + pocetNepracujicich + " zaměstnanců")

# Projekty

import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(r.content)
vykazy = pandas.read_csv("vykazy.csv")
print(vykazy)
# Agregace a počet hodin
print(vykazy.groupby("project")["hours"].sum())
# Přejmenování sloupce
vykazy.rename(columns = {'emloyee_id':'cislo_zamestnance'}, inplace = True)
# print(vykazy)
# Spojení výkazů se všemi zaměstnanci
mestaVykazy = pandas.merge(mestaPlat, vykazy, on=["cislo_zamestnance"], how="outer")
print(mestaVykazy)

# Kolik hodin na kterém projektu ve které kanceláři
print(mestaVykazy.groupby(["mesto", "project"])["hours"].sum())