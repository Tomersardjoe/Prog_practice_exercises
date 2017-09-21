afstandKM = eval(input('Hoeveel kilometer gaat u reizen? '))
leeftijd = eval(input('Wat is uw leeftijd? '))
weekendstr = str(input('Neemt u een weekendrit? '))

weekendrit = weekendstr == 'ja'

def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = afstandKM*0.6 + 15
    elif afstandKM >= 0 and afstandKM <= 50:
        prijs = afstandKM*0.8
    else:
        prijs = 0
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        ritprijs1 = standaardprijs(afstandKM) * 0.7
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        ritprijs1 = standaardprijs(afstandKM) * 0.65
    elif leeftijd >= 12 and leeftijd < 65 and weekendrit == False:
        ritprijs1 = standaardprijs(afstandKM)
    else:
        ritprijs1 = standaardprijs(afstandKM) * 0.4
    return ritprijs1

print('De totale ritprijs is €' +str(ritprijs(leeftijd, weekendrit, afstandKM)))
