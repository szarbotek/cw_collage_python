
def exponential(a, n):
    sum = 1
    for _ in range(n): sum *= a
    return sum

dom = [ (int(input("Podaj liczbe: ")), int(input("Podaj potęge: ")) ) for _ in range(1)]

print( [ exponential(*oper) for oper in dom] )

