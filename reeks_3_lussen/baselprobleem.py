import math
f100 = 0
for i in range(1, 101):
  f100 += 1/(i**2)
  if f100 - ((math.pi**2)/6) <= 1/100:
    kw = i
print(f100)
print(i)
