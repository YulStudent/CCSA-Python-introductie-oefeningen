aantalWitteEnRodeRozen = int(input())
aantalWitteEnBlauweRozen = int(input())
operator = input().strip()

w = 2
gevonden = False

while w <= min(aantalWitteEnRodeRozen, aantalWitteEnBlauweRozen) and not gevonden:
    r = aantalWitteEnRodeRozen - w
    b = aantalWitteEnBlauweRozen - w
    
    if r >= 2 and b >= 2:
        if operator == "<" and (b + r) < (w + b):
            print(b)
            print(w)
            print(r)
            gevonden = True
        elif operator == ">" and (b + r) > (w + b):
            print(b)
            print(w)
            print(r)
            gevonden = True
            
    w += 1