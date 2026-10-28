keuzeSpeler1 = str(input())
keuzeSpeler2 = str(input())


if(keuzeSpeler1 == keuzeSpeler2):
  print("gelijkspel")
elif(keuzeSpeler1 == 'schaar'):
  if(keuzeSpeler2 == "blad" or keuzeSpeler2 == "hagedis"):
    print("speler1 wint")
  else:
    print("speler2 wint")
elif(keuzeSpeler1 == 'blad'):
  if(keuzeSpeler2 == "steen" or keuzeSpeler2 == "Spock"):
    print("speler1 wint")
  else:
    print("speler2 wint")
elif(keuzeSpeler1 == 'steen'):
  if(keuzeSpeler2 == "hagedis" or keuzeSpeler2 == "schaar"):
    print("speler1 wint")
  else:
    print("speler2 wint")
elif(keuzeSpeler1 == 'hagedis'):
  if(keuzeSpeler2 == "Spock" or keuzeSpeler2 == "blad"):
    print("speler1 wint")
  else:
    print("speler2 wint")
elif(keuzeSpeler1 == 'Spock'):
  if(keuzeSpeler2 == "schaar" or keuzeSpeler2 == "steen"):
    print("speler1 wint")
  else:
    print("speler2 wint")