from random import randint


def checkNumber(r):
    u = int(input("Zgaduj dalej: "))
    if r > u:
        print("Cyfra jest większa!\n")
        checkNumber(r)
    elif r < u:
        print("Cyfra jest mniejsz!\n")
        checkNumber(r)
    else:
        print("Zgadłeś")

if __name__ == "__main__":
    print("Witaj w grze za dużo za mało zgadnij moja cyfre od 1 do 100")
    checkNumber(randint(1,100))