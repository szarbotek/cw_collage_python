import math

c = lambda a, b: int(math.sqrt( a**2+b**2))
d = c(9, 12) + c(9, 12) 

print( "{}{}".format(d, d*'-') )