def kwadraten_som(grondgetallen):

    kwadratenlist = []
    for positief in grondgetallen:
        if positief > 0:
            kwadratenlist.append((positief**2))

    som = sum(kwadratenlist)
    return som

print(kwadraten_som([3, 7, -5, 6]))
