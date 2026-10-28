aantalPiraten = int(input())
aantalKokosnoten = int(input())

for i in range(aantalPiraten):
    aandeelKokosnoten = aantalKokosnoten // aantalPiraten
    rest = aantalKokosnoten % aantalPiraten
    
    if rest == 0:
        aap_tekst = "geen noten voor de aap"
    elif rest == 1:
        aap_tekst = "1 noot voor de aap"
    else:
        aap_tekst = f"{rest} noten voor de aap"
        
    print(f"{aantalKokosnoten} noten = {aandeelKokosnoten} noten voor piraat#{i+1} en {aap_tekst}")
    
    aantalKokosnoten -= aandeelKokosnoten
    aantalKokosnoten -= rest

elke_piraat = aantalKokosnoten // aantalPiraten
slot_rest = aantalKokosnoten % aantalPiraten

if slot_rest == 0:
    slot_aap_tekst = "geen noten voor de aap"
elif slot_rest == 1:
    slot_aap_tekst = "1 noot voor de aap"
else:
    slot_aap_tekst = f"{slot_rest} noten voor de aap"

print(f"elke piraat krijgt {elke_piraat} noten en {slot_aap_tekst}")