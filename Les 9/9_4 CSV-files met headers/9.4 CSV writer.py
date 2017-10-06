import csv

with open('producten.csv', 'w', newline='') as bestand:
    writer = csv.writer(bestand, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))

    with open('data.txt', 'r') as data:
        for line in data:
            stripped = line.rstrip('\n')
            split = stripped.split(' ')
            Artikelnummer = split[0]
            Artikelcode = split[1]
            Naam = split[2]
            Voorraad = split[3]
            Prijs = split[4]
            writer.writerow((Artikelnummer, Artikelcode, Naam, Voorraad, Prijs))
