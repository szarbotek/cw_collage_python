dic= {0:"zero", 1:"jeden", 2:"dwa", 3:"trzy",4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięć"}

v = input("Podaj liczbę: ")

for znak in v:
    print( dic[int(znak)], end="-" )

# print(dic[int(input("Podaj liczbę: "))])
# print(dic[int(input("Podaj liczbę: "))])
# print(dic[int(input("Podaj liczbę: "))])
# print(dic[int(input("Podaj liczbę: "))])