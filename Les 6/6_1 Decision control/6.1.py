def seizoen(maand):

    if maand > 2 and maand < 6:
        season = 'lente'

    elif maand > 5 and maand < 9:
        season = 'zomer'

    elif maand > 8 and maand < 12:
        season = 'herfst'

    else:
        season = 'winter'

    return 'Het is ' + season

print(seizoen(3))
