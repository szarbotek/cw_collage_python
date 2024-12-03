"""
Bartosz Bieńkowski WMT22AP1S1 30.11.2024
nr. srudenta: 79234
"""
import random

"""
Zadanie 1
Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Produkt, Zamowienie, Jablko i Cebula:
a Produkt: nazwa, nazwa kategorii, cena jednostkowa
b Zamowienie: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
c Jablko: nazwa gatunku, rozmiar, cena za kg
d Cebula: nazwa gatunku, rozmiar, cena za kg

Utwórz kilka obiektów każdej klasy.
Napisz funkcję wypisującą produkt i zamówienie. Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.
Napisz funkcję generującą zamówienie z losową listą produktów, na przykład: Produkt-1, Produkt-2 itd.

"""

class food:
    def __init__(self, nazwa_gatunku: str, rozmiar: int, cena_za_kg:float) -> None:
        assert isinstance(nazwa_gatunku, str), TypeError
        assert isinstance(rozmiar, int), TypeError
        assert isinstance(cena_za_kg, float), TypeError
        self.nazwa_gatunku = nazwa_gatunku
        self.rozmiar = rozmiar
        self.cena_za_kg = cena_za_kg

    def __str__(self) -> str:
        text = ''
        text += '\n' + self.__class__.__name__
        def filter(name):
            if name == "nazwa_gatunku":
                return ''
            elif name == "rozmiar":
                return 'cm'
            elif name == "cena_za_kg":
                return 'zł'
            else:
                return ''
        for name in vars(self):
            text += "\n\t" + name + ":\t" + str(getattr(self, name, None)) + filter(name)
        return text

class Produkt:
    def __init__(self,  nazwa:str, nazwa_kategorii:str, cena_jednostkowa:float) -> None:
        assert isinstance(nazwa, str), TypeError
        assert isinstance(nazwa_kategorii, str), TypeError
        assert isinstance(cena_jednostkowa, float), TypeError
        self.nazwa = nazwa
        self.nazwa_kategorii = nazwa_kategorii
        self.cena_jednostkowa = cena_jednostkowa
        self.lvl: int = 0

    def setLvl(self, val) -> None:
        self.lvl = val

    def __str__(self) -> str:
        text = ''
        text += '\n' + '\t'*self.lvl + self.__class__.__name__

        for name in vars(self):
            if name == 'lvl': continue
            if name == 'cena_jednostkowa':
                text += '\n' + '\t'*(self.lvl+1) + (name + ":").ljust(17) + '\t' + f"{getattr(self, name, None):.2f}zł"
            else:
                text += '\n' + '\t'*(self.lvl+1) + (name + ":").ljust(17) + '\t' + str(getattr(self, name, None))
        return text

class Zamowienie:
    def __init__(self, imie:str, nazwisko:str, lista_prodoktow:list[Produkt]=[], laczna_cena:float=0.0) -> None:
        assert isinstance(imie, str), TypeError
        assert isinstance(nazwisko, str), TypeError
        assert isinstance(lista_prodoktow, list), TypeError
        assert all([isinstance(prod, Produkt) for prod in lista_prodoktow]), TypeError
        assert isinstance(laczna_cena, float), TypeError
        self.imie:str = imie
        self.nazwisko:str = nazwisko
        self.lista_prodoktow:list[Produkt] = lista_prodoktow
        self.laczna_cena:float = sum([ prod.cena_jednostkowa for prod in lista_prodoktow])
        self.lvl = 0
        # zwiększe poziomu wyświetlania
        [ prod.setLvl(self.lvl + 4) for prod in lista_prodoktow]
        

    def __str__(self) -> str:
        text = ''
        text += '\n' + '\t'*self.lvl + self.__class__.__name__
        def filter(name):
            if name == "laczna_cen":
                return 'zł'
            return ''
        for name in vars(self):
            if name == 'lvl': continue
            value = getattr(self, name, None)
            if type(value) == list:
                text += '\n' + '\t'*(self.lvl+1) + (name + ":").ljust(17)
                for elem in value:
                    text += str(elem)
            elif name == 'laczna_cena':
                text += '\n' + '\t'*(self.lvl+1) + (name + ":").ljust(17) + '\t' + f"{getattr(self, name, None):.2f}zł"
            else:
                text += '\n' + '\t'*(self.lvl+1) + (name + ":").ljust(17) + '\t' + str(value) + filter(name)
        return text
    
# dziedziczenie klasy foo do Jabłka i Cebuli
class Jablko(food):  pass
class Cebula(food): pass

def genLosoweZamowienie() -> Zamowienie:
    imiona:list[str] = ["Anna", "Jan", "Katarzyna", "Piotr", "Monika", "Tomasz", "Maria", "Paweł", "Magdalena", "Michał"]
    nazwiska:list[str] = ["Kowalska", "Nowak", "Wiśniewska", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowska", "Dąbrowski", "Zielińska", "Szymański"]
    lista_prodoktow: list[Produkt] = [
        Produkt("Chleb", "Pieczywo", 3.50),
        Produkt("Masło", "Nabiał", 6.00),
        Produkt("Jabłko", "Owoce", 2.20),
        Produkt("Szynka", "Wędliny", 20.00),
        Produkt("Mleko", "Nabiał", 3.20),
        Produkt("Czekolada", "Słodycze", 5.50),
        Produkt("Cukier", "Artykuły spożywcze", 4.00),
        Produkt("Kawa", "Napoje", 18.00),
        Produkt("Ser", "Nabiał", 12.00),
        Produkt("Papryka", "Warzywa", 7.00),
    ]
    
    rl = [ random.choice(lista_prodoktow) for _ in range(random.randint(0, len(lista_prodoktow)-1))]

    return Zamowienie( random.choice(imiona), random.choice(nazwiska), rl )

if __name__ == "__main__":
    cz = Cebula('czerwona', 4, 5.99)
    bi = Cebula('biala', 5, 3.49)
    jz = Jablko("Zielone", 5, 1.99)
    jcz = Jablko("czerwone", 5, 2.29)
    # print(cz, bi, jz, jcz)

    p1 = Produkt("Chleb", "Pieczywo", 3.50)
    p2 = Produkt("Masło", "Nabiał", 6.00)
    p3 = Produkt("Jabłko", "Owoce", 2.20)
    
    z1 = Zamowienie( "Filip", "Karton", [p1, p2, p3])
    z2 = genLosoweZamowienie()
    z3 = genLosoweZamowienie()

    # print(z1)
    # print(z2)
    # print(z3)

    from Treeki import Treeki
    print(Treeki.getPrintBuffor( z1 ))
    print(Treeki.getPrintBuffor( p1 ))
