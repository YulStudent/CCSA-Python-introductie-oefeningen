n = int(input())
aantalBeleefdheden = 0

for i in range(1, n):
  totaal = 0
  for j in range(i, n):
    totaal += j
    if(totaal == n):
      aantalBeleefdheden += 1

print(aantalBeleefdheden)
