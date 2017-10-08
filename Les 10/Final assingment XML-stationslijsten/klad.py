import xmltodict

with open('stations.xml') as bestand:
    filecontentstring = bestand.read()
    xmldictionary = xmltodict.parse(filecontentstring)


    stations = xmldictionary['Stations']['Station']







