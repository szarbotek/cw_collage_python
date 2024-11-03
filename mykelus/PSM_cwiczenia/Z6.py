K=input("Podaj początkową wartość: ")
p=input("Podaj oprocentowanie: ")
n=input("Podaj czas trwania w latach: ")

wartosc=int(K)*((1+(int(p)/100)))**int(n)
print(wartosc)