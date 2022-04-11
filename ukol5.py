class Polozka():
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def vypis_info(self):
    return(f"Název: {self.nazev}\nŽánr: {self.zanr}")

class Film(Polozka):
  def __init__(self, nazev, zanr, delka: int):
    super().__init__(nazev, zanr)
    self.delka = delka
  def vypis_info(self):
      return (super().vypis_info() + f"\nDélka: {self.delka} min.")
  def get_celkova_delka(self):
    return self.delka


class Serial(Polozka):
  def __init__(self, nazev, zanr, pocetEpizod: int, delkaEpizody: int):
    super().__init__(nazev, zanr)
    self.pocetEpizod = pocetEpizod
    self.delkaEpizody = delkaEpizody
  def vypis_info(self):
      return super().vypis_info() + f"\nPočet epizod: {self.pocetEpizod}\nDélka epizody: {self.delkaEpizody}"

  def get_celkova_delka(self):
    celkovaDelka = self.pocetEpizod * self.delkaEpizody
    return celkovaDelka

class Uzivatel():
  def __init__(self, jmeno, delka_sledovani:int = 0):
      self.jmeno = jmeno
      self.delka_sledovani = delka_sledovani
      self.filmy = []
  def pridej_film(self, film):
      self.filmy.append(film)
  def vypis_film(self):
    for f in self.filmy:
      print(f.nazev)

  def pripocti_zhlednuti(self, shlednutychMinut: int):
    self.delka_sledovani += shlednutychMinut
    return f"Uživatel nakoukal {self.delka_sledovani} minut"

film1 = Film("Název", "Žánr", 135)
film2 = Film("Nuda", "STRACH", 122)
prvniShlednutyFilm = film1.get_celkova_delka()
serial1 = Serial("Nemám nápad", "Stres", 20, 13)
uzivatel1 = Uzivatel("Andulka")
prvniShlednutySerial = serial1.get_celkova_delka()
# print(uzivatel1.pripocti_zhlednuti(prvniShlednutySerial))
# print(uzivatel1.pripocti_zhlednuti(prvniShlednutyFilm))
uzivatel1.pridej_film(film2)
uzivatel1.pridej_film(film1)
uzivatel1.vypis_film()
