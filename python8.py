from datetime import datetime
def vypocetVstupenek(kolikLidi,kdy):
  # Datum převedu na python datum
  kdy=datetime.strptime(kdy,"%d.%m.%Y")
  #vytvořím hranice
  start=datetime(2021,7,1)
  stop=datetime(2021,8,31)
  levnejsiVstupenky = datetime(2021,8,11)
  if start <= kdy <= stop:
    valid = True
  else: 
    valid = False
  
  if valid and (kdy >= levnejsiVstupenky):
    cenaVstupenky = 180
  elif valid and (kdy < levnejsiVstupenky):
    cenaVstupenky = 250
  else:
    print("V tomhle termínu nehrajem, sorry.")
    exit()
  cena = int(kolikLidi) * cenaVstupenky
  return f"Zaplať {cena} Kč."

kolikLidi=input("Pro kolik osob chcete koupit vstupenku? ")
kdy = input("Na který den chcete vstupenky? ")

cena = vypocetVstupenek(kolikLidi, kdy)
print(cena)