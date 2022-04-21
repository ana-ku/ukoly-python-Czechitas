with open("posta.html", encoding='utf-8') as vstup:
    kodStranky = vstup.read()
kodStranky.replace("\n", " ")
import re
vsechnyMezery = re.compile(r" +")
nahrazeneMezery = vsechnyMezery.sub(" ", kodStranky)

pscMesto = re.compile(r"\d{3} ?\d{2} \w+ ?\d*")
vsechnaPSC = pscMesto.findall(nahrazeneMezery)
for psc in vsechnaPSC:
  print(psc)

