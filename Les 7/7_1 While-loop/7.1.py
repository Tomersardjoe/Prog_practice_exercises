getal = ''
list = []

while getal != 0:
    getal = eval(input('Geef een getal: '))
    if getal == 0:
        break
    else:
        list.append(getal)

length = len(list)
som = sum(list)

print('Er zijn %d getallen ingevoerd, de som is: %d' % (length, som))
