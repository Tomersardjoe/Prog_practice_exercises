word = ''

while True:
    word = str(input('Geef een string van vier letters: '))
    if len(word) == 4:
        print('Inlezen van correcte string: %s is geslaagd' % word)
        break
    else:
        length = len(word)
        print('%s heeft %d letters' % (word, length))
