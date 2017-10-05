def inlezen_beginstation(stations):
    """"
    Deze functie vraagt de gebruiker om een beginstation in te voeren
    en controleert of deze overeenkomt met een station uit de list
    stations. Als dat niet zo is dan wordt er een foutmelding geprint en
    moet de gebruiker opnieuw een station invoeren. Als het
    station wel overeenkomt met een station uit de list dan wordt
    de waarde van het beginstation gereturned.
    """
    while True:
        begin = str(input('Voer het beginstation van uw reis in: '))
        if begin in stations:
            return begin
        else:
            print('%s is geen correct beginstation, probeer het opnieuw' % begin)

def inlezen_eindstation(stations, beginstation):
    """"
    Deze functie vraagt de gebruiker om een eindstation in te voeren
    en controleert of deze overeenkomt met een station uit de list
    stations. Als dat niet zo is dan wordt er een foutmelding geprint en
    moet de gebruiker opnieuw een station invoeren. Als het
    station wel overeenkomt met een station uit de list dan wordt
    er gecontroleert of de index van het eindstation hoger is dan de
    index van het beginstation. Als dat niet zo is dan wordt er
    een foutmelding geprint en moet de gebruiker opnieuw een station
    invoeren. Als dat zo is dan wordt de waarde van het eindstation
    gereturned.
    """
    while True:
        eind = str(input('Voer het eindstation van uw reis in: '))
        if eind in stations:
            start = stations.index(beginstation)
            end = stations.index(eind)
            if end > start:
                return eind
            else:
                print('%s is voor uw beginstation, probeer het opnieuw' % eind)
        else:
            print('%s is geen correct eindstation, probeer het opnieuw' % eind)

def omproepen_reis(stations, beginstation, eindstation):
    """"
    Deze functie vraagt eerst de index van het beginstation op en
    telt daar 1 bij op om van een index naar een rangorde te gaan.
    Dan wordt het beginstation en het bij rangnummer geprint.
    Daarna doet de functie hetzelfde voor het eindstation.
    Het rangnummer van het eindstation wordt van het rangnummer
    van het beginstation afgehaalt om zo de afstand tussen de
    stations te berekenen. De afstand wordt vermenigvuldigd met
    5 om zo de prijs van de reis te berekenen. Daarna wordt het
    beginstation opnieuw geprint gevolgd door een while loop die
    door de indexen vanaf 1 na he beginstation tot 1 voor het
    eindstation loopt en de bijbehorende waarden daarvan print.
    Als laatst wordt het eindstation geprint.
    """
    start = stations.index(beginstation) + 1
    print('Het beginstation %s is het %de station in het traject.' % (beginstation, start))
    end = stations.index(eindstation) + 1
    print('Het eindstation %s is het %de station in het traject.' % (eindstation, end))
    afstand = end - start
    print('De afstand bedraagt %d station(s)' % afstand)
    prijs = afstand * 5
    print('De prijs van het kaartje is %d euro' % prijs)
    print('U stapt in de trein in: %s' % beginstation)
    i = start
    while i < end - 1:
        print('- ' + stations[i])
        i += 1
    print('U stapt uit in: %s' % eindstation)


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond, Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omproepen_reis(stations, beginstation, eindstation)

