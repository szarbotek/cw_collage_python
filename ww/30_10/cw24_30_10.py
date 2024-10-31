def power(a):
    if a == 0 or a == 1:
        return 1
    else:
        return power(a-1) * a

getval = lambda msg: int(input(msg))

dom = [ getval("Podaj silnie: ") for _ in range(1)]

print( [ power(oper) for oper in dom] )