list = eval(input('Geef een lijst met minimaal 10 strings: '))

newlist = []

for word in list:
    if len(word) == 4:
        newlist.append(word)
    else:
        continue
print('De nieuw-gemaakte lijst met alle vier-letter strings is: ' + str(newlist))
