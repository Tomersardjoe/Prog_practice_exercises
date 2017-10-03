def gemiddelde():
    zin = str(input('Schrijf een willekeurige zin: '))
    words = zin.split()
    average = sum(len(word) for word in words) / len(words)
    print('De gemiddelde lengte een woord in deze zin is %d letters' % average)

gemiddelde()
