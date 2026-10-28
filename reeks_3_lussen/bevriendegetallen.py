a = int(input())
b = int(input())
grootste = max(a,b)
somDelersA = 0
somDelersB = 0

for i in range(1, grootste//2+1):
  if(a%i == 0):
    somDelersA += i
  if(b%i == 0):
    somDelersB += i

print(f"{a} en {b} zijn {'geen 'if somDelersA != b and somDelersB != a else ''}bevriende getallen")