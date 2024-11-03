x=[]

suma=0
i=0
while i<8:
    x.append(input("Podaj liczbę: "))
    i=i+1

for n in x:
  if int(n)%2!=0:
      print(n)
      suma+=int(n)
print(suma)