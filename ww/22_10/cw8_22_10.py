#cw 
sum = 0
n = 4
for i in range(0,n):
    sum += int( input("podaj {} liczbe: ".format(i+1) ) )
else:
    print( 'Średnia artmetyczna: {}'.format(sum/n ))