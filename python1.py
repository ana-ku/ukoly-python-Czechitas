baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod = input("Zadejte kód balíku: ")
  
if kod in baliky:
  if baliky[kod] == False:
    print(f"Balík ještě nebyl doručen")
  else:
    print(f"Balík už byl doručen")
