uurloon = eval(input('Wat verdien je per uur?'))
aantal_uur = eval(input('Hoeveel uur heb je gewerkt?'))

salaris = (aantal_uur * uurloon)

print('{:d} uur werken levert {:.1f} Euro op'.format(int(aantal_uur), float(salaris)))
