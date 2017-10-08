import xmltodict

with open('producten.xml') as bestand:
    filestring = bestand.read()
    xmldictionary = xmltodict.parse(filestring)

    artikelen = xmldictionary['artikelen']['artikel']

    for artikel in artikelen:
        print(artikel['naam'])
