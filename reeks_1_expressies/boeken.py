verzendingskost = 3.00
verzendingskostPerBoek = 0.75
prijsBoek = 24.95
kortingWinkels = 0.4
aantalBoeken = 60
totaalPrijsAantalBoeken = aantalBoeken * prijsBoek

totaalKost = (totaalPrijsAantalBoeken - totaalPrijsAantalBoeken*kortingWinkels) + verzendingskost + (verzendingskostPerBoek*(aantalBoeken-1))
print(totaalKost)