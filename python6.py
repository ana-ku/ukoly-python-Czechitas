jmenoSouboru = input("Jaký soubor chcete otevřít? ")
with open(jmenoSouboru+".txt") as vstup:
  text = vstup.readlines()

seznamSPZ = [spz.split() for spz in text]
# print(seznamSPZ)

seznamSPZ = [[spz[0], spz[1].replace(",",".")] for spz in seznamSPZ]
print(seznamSPZ)

poctyKm = [float(spz[1]) for spz in seznamSPZ]
vysledekKm = sum(poctyKm) * 1000
print(f"Výsledný součet km za rok je {int(vysledekKm)} kilometrů")
