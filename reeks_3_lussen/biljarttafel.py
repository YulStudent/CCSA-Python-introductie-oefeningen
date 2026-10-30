hoogte =  int(input())
breedte =  int(input())

x = 0
y = 0

xRichting = 'R'
yRichting = 'B'

while x != breedte or x != 0 and y != hoogte or y != 0:
  if xRichting == 'R':
    x += 1
  if xRichting == 'L':
    xBalLocatie -= 1
  if yRichting == 'O':
    yBalLocatie -= 1
  if yRichting == 'B':
    yBalLocatie += 1
  if xBalLocatie == breedte:
    print(f"rechterband ({xBalLocatie}, {yBalLocatie})")
    xRichting = 'L'
  if xBalLocatie == 0:
    print(f"linkerband ({xBalLocatie}, {yBalLocatie})")
    xRichting = 'R'
  if yBalLocatie == hoogte:
    print(f"bovenband ({xBalLocatie}, {yBalLocatie})")
    yRichting = 'O'
  if yBalLocatie == 0:
    print(f"onderband ({xBalLocatie}, {yBalLocatie})")
    yRichting = 'B'
  
print(f"({xBalLocatie}, {yBalLocatie})")