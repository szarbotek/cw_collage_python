
print( (lambda x, y, func: func(x) if x > y else func(y))(
    int(input("Podaj 1 cyfre: ")), 
    int(input("Podaj 2 cyfre: ")),
    lambda w: f' Wieksze jest {w}',))



[5, 6, 7]

lambda tab, max_val, end_val: [ (lambda x, y: x if x > y else y)(tab[i], tab[i+1]) for i in range(0, tab.__len__()-1 ) ]

[ tab[i] for i in range(0,3)]