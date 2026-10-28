import math 
a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if (d < 0):
  print("geen wortels")
if(d == 0):
  print("een wortel")
  x = -b / (2*a)
  print(f"{x:.1f}")
if(d>0):
  print("twee wortels")
  x1 = (-b+ math.sqrt(d))/ (2*a)
  x2 = (-b - math.sqrt(d))/ (2*a)
  if(x1 > x2):
    print(x2)
    print(x1)
  else:
    print(x1)
    print(x2)
  