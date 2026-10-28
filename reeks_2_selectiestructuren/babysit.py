beginUur = int(input())
beginMinuten = int(input())
eindUur = int(input())
eindMinuten = int(input())

begin = beginUur * 60 + beginMinuten
eind = eindUur * 60 + eindMinuten

startTijd = 18 * 60               
grensHogeBetaling = 21 * 60 + 30
uurloonLaag = 2
uurloonHoog = 4

if begin < startTijd or eind <= begin:
    print("ongeldige invoer")
else:
    if eind <= grensHogeBetaling:
        minutenLaag = eind - begin
        minutenHoog = 0
    elif begin >= grensHogeBetaling:
        minutenLaag = 0
        minutenHoog = eind - begin
    else:
        minutenLaag = grensHogeBetaling - begin
        minutenHoog = eind - grensHogeBetaling

    betaling = (minutenLaag * uurloonLaag + minutenHoog * uurloonHoog) / 60
    print(betaling)