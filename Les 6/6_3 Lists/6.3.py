invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
listinvoer = invoer.split('-')

listint = list(map(int, listinvoer))

listint.sort()

highestnumber = max(listint)
lowestnumber = min(listint)
length = len(listint)
som = sum(listint)
average = int(som) / int(length)

print('Gesorteerde list van ints: ' + str(listint))
print('Grootste getal: %d en Kleinste getal: %d' % (highestnumber, lowestnumber))
print('Aantal getallen: %d en Som van de getallen: %d' % (length, som))
print('Gemiddelde: %f' % average)
