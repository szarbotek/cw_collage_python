biedra=input("Jaka cena w Biedronce: ")
lidl=input("Jaka cena w Lidlu: ")
zabka=input("Jaka zena w Żabce: ")

if biedra<=lidl:
    if biedra<=zabka:
        print("Najtańsze kosztują ", biedra)
    else:
        print("Najtańsze kosztują ", zabka)
elif lidl<=biedra:
    if lidl<=zabka:
        print("Najtańsze kosztują ", lidl)
    else:
        print("Najtańsze kosztują ", zabka)