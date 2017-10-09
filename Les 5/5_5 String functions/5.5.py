def gemiddelde():

    zin = str(input('Schrijf een willekeurige zin: '))
    words = zin.split()
    average = sum(len(word) for word in words) / len(words)

    return 'De gemiddelde lengte een woord in deze zin is %d letters' % average

print(gemiddelde())
