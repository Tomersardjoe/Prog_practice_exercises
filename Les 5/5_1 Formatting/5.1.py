def convert(gradenCelcius):
    result = float(gradenCelcius*1.8+32)
    return result

def table():
    for temp in range(-30,50,10):
        celsius = float(temp)
        fahrenheit = convert(temp)
        print('{:>5}   {:>5}'.format(fahrenheit, celsius))


print('{:>4}   {:>4}'.format('F', 'C'))
table()
