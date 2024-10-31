from random import randint
creatRandList = lambda: [randint(1,50) for i in range(10)]
k1, k2 = creatRandList(), creatRandList()

def checkUnic(a1, a2):
    A = set(a1)
    B = set(a2)
    C = A&B
    return C if C else None

print( k1, k2, checkUnic(k1, k2) )
