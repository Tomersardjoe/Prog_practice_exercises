num_lines = sum(1 for line in open('Kaartnummers.txt'))
print('Deze file telt %s' % num_lines + ' regels')

nummerlist = []

fileWords = open('Kaartnummers.txt','r')

for line in fileWords:
    nummer = line.split(', ')[0]
    nummerlist.append(nummer)

highestnumber = max(nummerlist)
positie = nummerlist.index(highestnumber)
regel = positie +1

print('Het grootste kaartummer is: %s en dat staat op regel %d' % (highestnumber, regel))
