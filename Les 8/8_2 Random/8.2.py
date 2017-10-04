import random
def monopolyworp():

    dubbel = 0
    while True:

        dobbel1 = random.randrange(1,7)
        dobbel2 = random.randrange(1,7)
        opgeteld = dobbel1+dobbel2
        if dobbel1 == dobbel2 and dubbel != 2:
            print('%d + %d = %d (dubbel)' % (dobbel1,dobbel2,opgeteld))
            dubbel += 1
        elif dobbel1 == dobbel2 and dubbel == 2:
            print('%d + %d = (direct naar de gevangenis)' % (dobbel1, dobbel2))
            break
        else:
            print('%d + %d = %d' % (dobbel1,dobbel2,opgeteld))
            dubbel = 0

monopolyworp()
