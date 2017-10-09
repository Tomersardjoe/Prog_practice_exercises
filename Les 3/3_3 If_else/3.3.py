Age = eval(input("Geef je leeftijd: "))
Paspoort = str(input("Nederlands paspoort: "))

if Age >= 18 and Paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Helaas, je mag niet stemmen')
