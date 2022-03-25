def kontrolaCisla(telefonni_cislo):
  #zjistím platnost čísla, tj. obsahuje +420 nebo je dlouhé 9 znaků
  if (telefonni_cislo[0:4] == "+420" and len(telefonni_cislo) == 13) or len(telefonni_cislo) == 9:
    zprava = input("Jakou zprávu chcete poslat? ")
    return zprava
  else:
    print("Špatný formát čísla")
    exit()

def vypocetCeny(zprava):
  #zjistím délku zprávy
  delkaZpravy = len(zprava)
  cenaZpravy = (delkaZpravy//180 + 1) * 3
  return f"Zaplatíš {cenaZpravy} Kč za zprávu"
cislo = input("Na jaké číslo chce poslat zprávu? ")

cisloBezMezer = cislo.replace(" ", "")
zprava = kontrolaCisla(cisloBezMezer)
cena = vypocetCeny(zprava)
print(cena)
