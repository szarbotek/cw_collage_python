import os, sys

product = {
    "mleko": 2.50,
    "chleb": 1.80,
    "jajka": 3.20,
    "ser": 4.50,
    "ziemniaki": 1.00,
    "marchew": 0.80,
    "cukier": 2.00,
    "ryż": 1.50,
    "makaron": 2.20,
    "kurczak": 5.80
}

cart:list = []

def productInShop():
    print("\n === O === ")
    print("Oferta sklepu to:")
    for key, val in product.items():
        print( "> {} w cenie {}zł".format(key.rjust(11, '.'), val) )
    else:
        print("")

def addToCart():
    print("\n === D === ")
    select = input("Podaj produkt do dodania do koszyka: ")
    cart.append( select )

def viewCart():
    print("\n === P === ")
    print(" Twój koszyk: ")
    for p in cart:
        print( "> Kupujesz {} za {}zł".format(p, product[p]) )
    else:
        print("")

def gotoCash():
    print("\n === K === ")
    purchace:int = 0
    for p in cart:
        purchace += product[p]
    else:
        print( "Na wszystko wydałeś {}zł, przynajmniej nie nie będziesz głodować. ".format(purchace) )
        print("")


option = {"O": productInShop, "D": addToCart, "P": viewCart, "K": gotoCash, "X": (lambda: sys.exit(0))}


def menu():
    os.system('cls')
    print(" === menu ===")
    print("O - oferta sklepu")
    print("D - dodaj do koszyka")
    print("P - podgląd koszyka")
    print("K - koniec/kasa")
    print("X - zakończ zakupy")
    print("")

    select = input("Wybierz opcje: ")

    try:
        select  = select.upper()
        option[select]()
        input("\nkontynuj...")
    except KeyError:
        print("[Err] Błedna opcja! ")
    menu()

if __name__ == "__main__":
    menu()