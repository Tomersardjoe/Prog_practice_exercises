kosten = 4356
while True:
    try:
        entry = eval(input('Hoeveel personen gaan mee op reis: '))
        if entry > 0:
            ans = kosten / entry
            print('Dit kost %d euro per persoon' % ans)
            break

        if entry == 0:
            raise ZeroDivisionError

        if entry < 0:
            raise ValueError

    except ZeroDivisionError:
        print('Delen door nul kan niet!')

    except ValueError:
        print('Negatieve getallen zijn niet toegestaan!')

    except NameError:
        print('Gebruik cijfers voor het invoeren van het aantal!')

    except:
        print('Onjuiste invoer!')

