def ticker(filename):
    dictio = {}
    for line in open(filename):
        line = line.rstrip('\n')
        bedrijfsnaam = line.split(':')[0]
        tickersymbol = line.split(':')[1]
        dictio[bedrijfsnaam] = tickersymbol
    return dictio

dictionary = ticker('ticker symbols.txt')
entry = str(input('Enter Company name: '))
print('Ticker symbol: ' + dictionary[entry])

print()

entry2 = str(input('Enter Ticker symbol: '))
for key, symbol in dictionary.items():
    if symbol == entry2:
        print('Company name: ' + key)

