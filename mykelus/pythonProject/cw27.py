import random

losowa=random.randint(1,100)
print(losowa)


while True:
    liczba = int(input("Podaj: liczbę "))
    if liczba>losowa:
        print("Za dużo")
    elif losowa>liczba:
        print("Za mało")
    else:
        print("Zgadłeś")
        break
