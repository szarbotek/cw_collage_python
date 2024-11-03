suma=0
i=0
while True:
    liczba=int(input("Podaj liczbę: "))
    if liczba==0:
        break
    suma=suma+liczba
    i+=1
    srednia=suma/i
print(srednia)
