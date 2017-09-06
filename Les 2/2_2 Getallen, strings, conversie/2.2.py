cijferICOR = 6
cijferPROG = 8
cijferCSN = 7
gemiddelde = (cijferICOR + cijferPROG + cijferCSN)/3
beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)
overzicht = ('Mijn cijfers (gemiddeld een {:d}) leveren een beloning van €{:d},- op!'.format(int(gemiddelde), int(beloning)))
print(overzicht)
