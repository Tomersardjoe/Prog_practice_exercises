fileWords = open('Kaartnummers.txt','r')
print(fileWords.read().split(','))
#print(fileWords.read())



fileWords.close()
