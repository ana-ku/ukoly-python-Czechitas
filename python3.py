cislo = input("Na jaké číslo chce poslat zprávu? ")
zprava = input("Jakou zprávu chcete poslat?")
cisloBezMezer = cislo.replace(" ", "")
def posilaniZprav(nr, mess):
  #zjistím platnost čísla, tj. obsahuje +420 nebo je dlouhé 9 znaků
  if (nr[0:4] == "+420" and len(nr) == 13) or len(nr) == 9:
    pass
  else:
    print("Špatný formát čísla")
    exit()
  
  #zjistím délku zprávy s
  delkaZpravy = len(mess)
  cenaZpravy = (delkaZpravy//180 + 1) * 3
  return f"Správně zadané číslo a zaplatíš {cenaZpravy} Kč za zprávu"

print(posilaniZprav(cisloBezMezer,zprava))
