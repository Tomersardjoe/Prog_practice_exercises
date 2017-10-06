import datetime
import csv

with open('inloggers.csv', 'w', newline='') as bestand:
    writer = csv.writer(bestand, delimiter=';')
    #writer.writerow(('naam', 'voorl', 'gbdatum', 'email'))

    while True:
        naam = input("Wat is je achternaam? ")

        if naam == 'einde':
            break

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        vandaag = datetime.datetime.today()
        time = vandaag.strftime("%a %d %B %Y at %H:%M")

        writer.writerow((time, voorl, naam, gbdatum, email))
