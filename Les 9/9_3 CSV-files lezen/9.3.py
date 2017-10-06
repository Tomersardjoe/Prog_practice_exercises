import csv

with open('gamers.csv', 'r') as bestand:

    reader = csv.reader(bestand, delimiter=';')

    scorelist = []
    namelist = []
    datelist = []

    for row in reader:
        name = row[0]
        namelist.append(name)
        date = row[1]
        datelist.append(date)
        score = row[2]
        scorelist.append(score)

maxscore = max(scorelist)
index = scorelist.index(maxscore)
maxname = namelist[index]
maxdate = datelist[index]

print('De hoogste score is: %s op %s behaald door %s' % (maxscore, maxdate, maxname))
