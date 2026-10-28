keuzeSoort = str(input())
foutOfJuist = ""
opmerking = ""
if(keuzeSoort == "waarde"):
  getal = int(input())
  if (getal%2 == 0):
    opmerking = f"kaarten met waarde {getal} moeten gedraaid worden."
  else: 
    opmerking = f"kaarten met waarde {getal} moeten niet gedraaid worden."
  keuzeOmdraaien = str(input())
  if((getal%2 == 0 and keuzeOmdraaien == "ja") or (getal%2 == 1 and keuzeOmdraaien == "nee")):
    foutOfJuist = "Juist"
  else:
    foutOfJuist = "Fout"
if(keuzeSoort == "kleur"):
  kleur = str(input())
  if (kleur != "rood"):
    opmerking =f"kaarten met kleur {kleur} moeten gedraaid worden."
  else: 
    opmerking ="kaarten met kleur rood moeten niet gedraaid worden."
  keuzeOmdraaien = str(input())
  if ((kleur != "rood" and keuzeOmdraaien == "ja") or (kleur == "rood" and keuzeOmdraaien == "nee")):
    foutOfJuist = "Juist"
  else:
    foutOfJuist = "Fout"

print(f"{foutOfJuist}: {opmerking}")