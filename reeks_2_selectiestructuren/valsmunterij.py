standWeegschaal1 = str(input())
standWeegschaal2 = str(input())
nummerMunt = 0
if (standWeegschaal1 == "rechts"):
  if(standWeegschaal2 == "rechts"):
    nummerMunt = 1
  elif(standWeegschaal2 == "links"):
    nummerMunt = 2
  elif(standWeegschaal2 == "evenwicht"):
    nummerMunt = 3
elif (standWeegschaal1 == "links"):
  if(standWeegschaal2 == "rechts"):
    nummerMunt = 4
  elif(standWeegschaal2 == "links"):
    nummerMunt = 5
  elif(standWeegschaal2 == "evenwicht"):
    nummerMunt = 6
elif(standWeegschaal1 == "evenwicht"):
  if(standWeegschaal2 == "rechts"):
    nummerMunt = 7
  elif(standWeegschaal2 == "links"):
    nummerMunt = 8
  elif(standWeegschaal2 == "evenwicht"):
    nummerMunt = 9
print(f'muntstuk #{nummerMunt} is vervalst')