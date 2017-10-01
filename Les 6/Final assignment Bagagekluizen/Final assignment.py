import os
import platform
import time


def toon_aantal_kluizen_vrij():
    """
    Deze functie leest hoeveel regels in gebruik zijn
    en haalt dit van het totaal aantal kluizen af
    om zo het aantal beschikbare kluizen te tellen

    :return: aantal beschikbare kluizen
    """
    num_lines = sum(1 for line in open('Kluizen.txt'))
    beschikbarekluizen = 12 - num_lines
    return beschikbarekluizen


def nieuw_kluis():
    """
    Deze functie kijk eerst of er kluizen beschikbaar zijn.
    Dan wordt er een list aangemaakt van 1 t/m 13.
    Daarna wordt het kluizen.txt bestand afgegaan en worden
    de regels gesplitst op ;, waarvan het eerste gedeelte
    het kluisnummer is. De gevonden kluisnummers worden van de list
    verwijdert. Dan wordt er een wachtwoord aangemaakt en
    samen met het kluisnummer aan het kluizen.txt bestand toegevoegd.
    """
    if toon_aantal_kluizen_vrij() == 0:
        print('Er zijn geen kluizen beschikbaar')
        return

    kluizenlist = list(range(1, 13))  # 13 exclusive
    kluizendata = open('Kluizen.txt', 'r+')
    for line in kluizendata:
        prefix = line.split(';', 1)[0]
        kluizenlist.remove(int(prefix))

    wachtwoord = ''
    print_error = False
    while len(wachtwoord) < 4:
        if print_error:
            print('Het opgegeven wachtwoord voldoet niet aan de eisen, probeer het opnieuw')
        wachtwoord = str(input('Voer een wachtwoord in met minimaal 4 tekens: '))
        print_error = True

    entry = '%d;%s\n' % (kluizenlist[0], wachtwoord)
    kluizendata.write(entry)
    print('Uw toegewezen kluis is kluisnummer %d' % kluizenlist[0])

    kluizendata.close()


def kluis_openen():
    """"
    Deze functie kijk of het opgegeven kluisnummer en kluiscode overeenkomen
    met een regel in het Kluizen.txt bestand. Als dat zo is dan gaat
    de kluis open. Anders krijgt de gebruiker een foutmelding.
    """
    openen = str(input('Voer uw kluisnummer en code in op de volgende manier (kluisnummer;kluiscode): '))
    kluizendata = open('Kluizen.txt', 'r')

    found = False

    for line in kluizendata:
        if openen + '\n' == line:
            print('Uw kluis is geopend')
            found = True
            break

    if not found:
        print('Het opgegeven kluisnummer en kluiscode zijn onjuist')

    kluizendata.close()


# Get full path of current file
abspath = os.path.abspath(__file__)
# Get directory
dname = os.path.dirname(abspath)
# Change current working directory
os.chdir(dname)

while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil mijn kluis openen')
    print('4: Stop')

    try:
        menu = int(input('Maak uw keuze: '))
    except ValueError:
        print('De door uw opgegeven waarde is niet geldig, probeer het opnieuw')
        time.sleep(2)
        if platform.system() == 'Windows':
            os.system('cls')
        if platform.system() == 'Linux:':
            os.system('clear')
        continue

    if menu == 1:
        beschikbaar = toon_aantal_kluizen_vrij()
        print('Er zijn %d kluizen beschikbaar' % beschikbaar)
    elif menu == 2:
        nieuw_kluis()
    elif menu == 3:
        kluis_openen()
    elif menu == 4:
        break
