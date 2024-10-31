
lista1 = [ int(input(" Podaj {} liczbę całkowitą: ".format(i+1))) for i in range(0,5)]
print( lista1 )
print( sum(lista1) )
print( sum(lista1)/lista1.__len__() )