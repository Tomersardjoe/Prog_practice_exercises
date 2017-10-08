import xmltodict

with open('stations.xml') as bestand:
    filecontentstring = bestand.read()
    xmldictionary = xmltodict.parse(filecontentstring)

    stations = xmldictionary['Stations']['Station']

    print("Dit zijn de codes en types van de 4 stations:")

    for station in stations:
        code = station['Code']
        type = station['Type']
        print('{:<4} - {:>6}'.format(code, type))

    print()
    print("Dit zijn alle stations met één of meer synoniemen:")

    for station in stations:
        if station['Synoniemen'] is not None:
         code = station['Code']
         synoniem = station['Synoniemen']['Synoniem']
         print('{:<4} - {}'.format(code, synoniem))

    print()
    print("Dit is de lange naam van elk station:")

    for station in stations:
        code = station['Code']
        naam = station['Namen']['Lang']
        print('{:<4} - {:>6}'.format(code, naam))
