sklepy = {"Biedronka": 0, "Lidl": 0, "Żabka":0}

najtanszy = None

for k in sklepy:
    sklepy[k] = input("Ile kosztuja jabłka w {}?\n >> ".format(k))
    if (najtanszy is None): najtanszy = k
    elif (sklepy[k] < sklepy[najtanszy]): najtanszy = k
else:
    print( "Najtaniej jest w {}, jabłka sa w cenie: {}".format(najtanszy, sklepy[najtanszy]))