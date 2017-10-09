def namen():

    entry = 'niet leeg'
    dictio = {}
    while entry != '':
        entry = str(input('Volgende naam: '))
        if entry in dictio:
            dictio[entry] += 1
        elif entry != '':
            dictio[entry] = 1
    return dictio

dictionary = namen()

for key, value in dictionary.items():
    if value > 1:
        print('Er zijn %s studenten met de naam %s' % (value, key))
    else:
        print('Er is %s student met de naam %s' % (value, key))

