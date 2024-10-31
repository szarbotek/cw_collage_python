from random import randint

class Informator:
    INPUT = None

    @staticmethod
    def set(r1, r2):
        Informator.INPUT = lambda : int(input( 'Ile to jest liczba {} razy {}?\n >> '.format(r1, r2) ))

def GetRandom(rs:int= 1, rf: int = 10, n:int = 1 ) -> int:
    return [randint(rs, rf) for _ in range(0,n)]

def CheckMYEQ(eq: int, myeq: int):
    print(f'Użytkownik: {myeq}')
    print(f'Komputer: {eq}')

def GetInpuntEQ():
    try:
        return Informator.INPUT()
    except:
        GetInpuntEQ()

class main:
    index:int = 0
    indexMAX:int = 5
    def __init__(self) -> None:
        main.run()
    
    @staticmethod
    def run():
        r1, r2 = GetRandom(1, 10, 2)
        Informator.set(r1, r2)
        eq = r1 * r2
        myeq = GetInpuntEQ()
        CheckMYEQ(eq, myeq)

    @staticmethod 
    def checkRUN_break():
        pass

if __name__ == '__main__':
    main()
