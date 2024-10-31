
numbers = []

def condit(numbers):
    try:
        n = int(input("Podaj liczbe: "))

        if n == 0:
            return 0
        else:
            numbers.append(n)
            return 1
    except:
        return 0

while condit(numbers): pass
else:
    if numbers: print( "Średnia to {}".format( sum(numbers)/numbers.__len__() ) ) 