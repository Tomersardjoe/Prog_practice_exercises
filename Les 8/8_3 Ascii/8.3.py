def code(invoerstring):

    list= []
    for char in invoerstring:
        intwaarde = ord(char)
        intwaarde += 3
        tekenwaarde = chr(intwaarde)
        list.append(tekenwaarde)
    output = ''.join(list)
    return output

print(code('RutteAlkmaarDen Helder'))
