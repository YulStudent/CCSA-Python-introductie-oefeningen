aantalAppels = int(input())
aantalPalletten = aantalAppels // (35*20)
aantalAppels = aantalAppels % (35*20)
aantalKisten = aantalAppels // 20
aantalAppels = aantalAppels % 20
print(aantalPalletten)
print(aantalKisten)
print(aantalAppels)