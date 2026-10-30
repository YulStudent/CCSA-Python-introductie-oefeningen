def maximale_blootstelling(decibel):
  aantalSeconden  = -1
  if (decibel >= 80):
    aantalSeconden =  (8*60*60) // 2**((decibel-80)//3)
  return aantalSeconden

print(maximale_blootstelling(80))