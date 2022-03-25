#Vytvořím třídu Auto s atributy
class Auto:
  def __init__(self, znacka, model, kilometry, volne = True):
    self.znacka = znacka
    self.model = model
    self.kilometry = kilometry
    self.volne = volne
  def pujc_auto(self):
    if self.volne == True:
      self.volne = False
      return f"Potvrzuji zapůjčení auta"
    else:
      return f"Auto je již vypůjčené"
  def vrat_auto(self, tachometr, pocetDni):
    self.kilometry = tachometr
    self.volne = True
    if pocetDni >= 7:
      cenaZaDen = 300
    else:
      cenaZaDen = 400
    vyslednaCena = cenaZaDen * pocetDni
    return f"Vypůjčili jste si auto na {pocetDni} dní a zaplatíte {vyslednaCena} korun"

  def __str__(self):
    return f"Auto má SPZ {self.znacka} a model {self.model}, najeto má {self.kilometry} a je {'k dispozici' if self.volne else 'vypůjčené'}"

def zapujceniVozu(zapujceniZnacka):
  if zapujceniZnacka == "Škoda":
    if auto2.volne == True:
        auto2.pujc_auto()
        return auto2
    else:
      return f"Tohle auto je vypůjčené"
  elif zapujceniZnacka == "Peugeot":
    if auto1.volne == True:
        auto1.pujc_auto()
        return auto1
    else:
      return f"Tohle auto je vypůjčené"
  else:
    return f"Takové auto nemáme"

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

# Dotaz na značku a vypsání informací
zapujceniZnacka = input("Jakou značku auta chcete? Škoda nebo Peugeot? ")
zapujceneAuto = zapujceniVozu(zapujceniZnacka)
print(zapujceneAuto)

# Vypůjčení a vrácení auta s výpočtem ceny
auto1.pujc_auto()
print(auto1.vrat_auto("48000", 8))
print(auto1)


