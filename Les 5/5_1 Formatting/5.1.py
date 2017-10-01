def convert(gradenCelcius):
    result = int(gradenCelcius*1.8+32)
    print(result)

def table():
    for temp in range(-30,50,10):
        convert(temp)

table()
