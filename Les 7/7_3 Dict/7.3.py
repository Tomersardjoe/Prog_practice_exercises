dict = {'Piet': 4.5, 'Jan': 7.3, 'Klaas': 9.6, 'Boris': 7.6, 'Koen':  8.9, 'Hugo': 6.8, 'Mike': 9.0, 'Rutger': 9.2}

for key, value in dict.items():
    if value > 9.0:
        print('%s heeft een %.1f!' % (key,value))
