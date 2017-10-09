cijferICOR = 6.5
cijferPROG = 8.3
cijferCSN = 7.2

gemiddelde = (cijferICOR + cijferPROG + cijferCSN)/3
beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)

overzicht = ('Mijn cijfers (gemiddeld een {:.1f}) leveren een beloning van €{:.1f},- op!'.format(float(gemiddelde), float(beloning)))

print(overzicht)
