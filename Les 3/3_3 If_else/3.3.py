Age = eval(input("Geef je leeftijd:"))
Paspoort = input("Heb je een Nederlands paspoort?")

if Age >= 18 and Paspoort == 'ja':
    print('Je mag stemmen!')

else:
    print('Je mag niet stemmen')
