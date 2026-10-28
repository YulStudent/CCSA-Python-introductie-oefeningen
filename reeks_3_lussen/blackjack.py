totaal  = 0
gedaan = False
tekstje = ""

while not gedaan:
  kaart = int(input())
  totaal += kaart
  if(totaal == 21):
    tekstje = "Gewonnen!"
  elif(totaal > 21):
    tekstje = f"Verbrand ({totaal})"
  elif(kaart == 0):
    tekstje = f"Voorzichtig gespeeld ({totaal})"
  gedaan = totaal >= 21 or kaart == 0
print(tekstje)