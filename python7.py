with open("posta.html", encoding='utf-8') as vstup:
    kodStranky = vstup.read()
kodStranky.replace("\n", " ")
import re
nahrazeneMezery = re.sub(" +"," ", kodStranky)

pscMesto = re.compile(r"\d{3} ?\d{2} [\w ]* ?\d*")
print(nahrazeneMezery)
vsechnaPSC = pscMesto.findall(nahrazeneMezery)
for psc in vsechnaPSC:
  print(psc)
