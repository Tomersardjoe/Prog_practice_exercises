import csv

with open('producten.csv', 'r') as bestand:

    reader = csv.DictReader(bestand, delimiter=';')

    maxprijs = None
    Artnaam = None
    minvoorraad = None
    Artnum = None
    Null = None
    list = []

    for row in reader:
        prijs = float(row['Prijs'])
        if maxprijs == None or maxprijs < prijs:
            maxprijs = prijs
            Artnaam = row['Naam']

        voorraad = int(row['Voorraad'])
        if minvoorraad == None or minvoorraad > voorraad:
            minvoorraad = voorraad
            Artnum = row['Artikelnummer']

        totvoorraad = int(row['Voorraad'])
        if Null == None:
            list.append(totvoorraad)

    totaalvoorraad = sum(list)

    print('Het duurste artikel is %s en die kost %.2f' % (Artnaam, maxprijs))
    print('Er zijn slechts %s exemplaren in voorraad van het product met nummer %s' % (minvoorraad, Artnum))
    print('In totaal hebben wij %d producten in ons magazijn liggen' % (totaalvoorraad))


