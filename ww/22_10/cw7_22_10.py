#cw 7
while True:
    try:
        a, b = float(input("Podaj dł 1 boku: ")),  float(input("Podaj dł 2 boku: "))
        if not(int(a) == a or int(b) == b) :
            break
        else:
            print("liczby nie moga być naturalne")
    except:
        pass

print('Pole {}'.format( float(a)* float(b) ))   