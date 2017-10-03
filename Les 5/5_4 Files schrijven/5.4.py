naam = str(input('Wat is uw naam? '))

import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a %d %b %Y, %H:%M:%S, ')
print(s + naam)
