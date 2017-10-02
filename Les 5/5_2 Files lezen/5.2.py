fileWords = open('Kaartnummers.txt','r')

for line in fileWords:
    nummer = line.split(', ')
    if '\n' in nummer[1]:
        naampersoon = nummer[1].replace('\n','')
    else: continue
    regel = naampersoon + ' heeft kaartnummer: ' + nummer[0]
    print(regel)


fileWords.close()
