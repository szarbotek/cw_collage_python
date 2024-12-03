"""
    Treeki genarate for base object: (int, str, list, dict, tuple, class) console model readable for human
    Treeki.getPrintBuffor(ojbect) creatr str model can be use for print()

    but  Treeki.display(object) skips that call

    if tree shuld print object True name before use Treeki declarate
    Treeki.setLocals( locals() )
    
exaple:
    list:
    ⟐ nubers1
    ├────›⟐ x= 1
    ├────›⟐ := 2
    └────›⟐ := 3

    ⟐ foo:
    ├────›⟐ ID = 0
    └────›⟐ val = 523
        ├────› ...
        └────› ...

"""

class Treeki:

    EMPTY = " "
    LINE = chr(0x2500)
    ARROW = chr(0x203a)
    L = 5
    EMPTY_ROOT = EMPTY + EMPTY*L
    PLANT_ROOT = chr(0x2502) + EMPTY*L
    NEXT_ROOT  = chr(0x251c)  + LINE*(L-1) + ARROW 
    END_ROOT   = chr(0x2514) + LINE*(L-1) + ARROW
    
    OBJECT_START = chr(0x27d0)

    LOCALS: dict = {}
    FLAG_search_for_name: bool = False

    @classmethod
    def setLocals(cls, loc:dict):
        cls.FLAG_search_for_name =  True
        cls.LOCALS = loc

    @classmethod
    def display(cls, obj:any, FLAG_type:bool = False, ttl:int = 10):
        print( '\n' +cls.getPrintBuffor(obj, FLAG_type=FLAG_type, ttl = ttl))

    @classmethod
    def getValName(cls, value: any ) -> str:

        if cls.FLAG_search_for_name: 
            try:
                globi = {}
                if __name__ == '__main__': globi.update( globals() ) 
                assert len(cls.LOCALS ) != 0, ValueError("<Treeki> Not set locals to search names.")
                globi.update( cls.LOCALS )
                valueName = [ k for k,v in globi.items() if id(v) == id(value)][0]
                return valueName
            except IndexError:
                pass
        
        if value.__class__.__name__ in dir(__builtins__):
            return ':'
        else:
            return value.__class__.__name__

    
    @classmethod
    def getClassType(cls, obj, FLAG) -> str:
        if FLAG:
            return f'<{obj.__class__.__name__}>'
        else:
            return ''

    @classmethod
    def getPrintBuffor(cls, obj: any, objName:str = None, inclusion: str= '', FLAG_type:bool = False, MAXLENGHT:int = 0, ttl:int = 10) -> str:
        if ttl<=0: return '&overload ttl'
        textbuffor:str = ''
        
        if isinstance(objName, str) or objName == None:
            objName = cls.getValName(obj) if objName == None else objName
        else:
            objName = Treeki.getPrintBuffor(obj=objName, objName=objName.__class__.__name__, inclusion= inclusion + "  ")
            objName += "\t\t" 

        if isinstance(obj, (int|str|float) ): 
            setcell = objName + Treeki.getClassType(obj, FLAG_type) + " = "
            if MAXLENGHT == 0: MAXLENGHT = len(objName)
            textbuffor += Treeki.OBJECT_START + ' ' + setcell.ljust(MAXLENGHT+3) + str(obj) 
        elif isinstance(obj, dict): 
            textbuffor += Treeki.OBJECT_START + ' ' + objName + Treeki.getClassType(obj, FLAG_type)
            maxlengh = max([0] + [ len(k) for k in obj.keys() if not isinstance(obj[k], (object| dict| list| tuple)) ])
            for index, (name, elem) in enumerate(obj.items()):
                tree = inclusion + (Treeki.NEXT_ROOT if index+1 != len(obj) else Treeki.END_ROOT)
                incop = (Treeki.PLANT_ROOT if index+1 != len(obj) else Treeki.EMPTY_ROOT)
                textbuffor += '\n' + tree + cls.getPrintBuffor(elem, objName=name, inclusion= inclusion + incop, FLAG_type=FLAG_type, MAXLENGHT=maxlengh, ttl=ttl-1 )
        elif isinstance(obj, (list, tuple)):
            textbuffor += Treeki.OBJECT_START + ' ' + objName + Treeki.getClassType(obj, FLAG_type)
            for index, elem in enumerate(obj):
                tree = inclusion + (Treeki.NEXT_ROOT if index+1 != len(obj) else Treeki.END_ROOT)
                incop = (Treeki.PLANT_ROOT if index+1 != len(obj) else Treeki.EMPTY_ROOT)
                textbuffor += '\n' + tree + cls.getPrintBuffor(elem, inclusion= inclusion + incop, FLAG_type=FLAG_type, ttl=ttl-1 )
        elif isinstance(obj, object):
            try:
                dict_obj = vars(obj)
                textbuffor += cls.getPrintBuffor( dict_obj, objName=objName + ":" + Treeki.getClassType(obj, FLAG_type), inclusion=inclusion, FLAG_type=FLAG_type, ttl=ttl-1)
            except Exception as err:
                print(err, obj.__class__)
                textbuffor += "#not opareted class"
        else:
            textbuffor += r"%unexpected object"
        return textbuffor


if __name__ == "__main__":

    x = 1
    Treeki.display( x, FLAG_type=True )

    hello = "Hello World"
    Treeki.display( hello )

    nubers1  = [1,2,3]
    nubers2 =  [nubers1,5,6]
    nubers3 =  [6,7,nubers2]

    Treeki.display( nubers1 )
    Treeki.display( nubers2, FLAG_type=True )
    Treeki.display( nubers3 )

    dictionary1 = {"name": "Jan", "surname": "Kowalski" }
    dictionary2 = {"name": "Jan", (1,2): "Kowalski" }

    Treeki.display( dictionary1 )
    Treeki.display( dictionary2 )

    class class_dodo:
        def __init__(self) -> None:
            self.val = 132
            self.dictionary1 = dictionary1

    class_instance_dodo = class_dodo()

    class class_kiki:
        def __init__(self) -> None:
            self.parent = class_dodo()
            self.z = 15

    class_instance_kiki = class_kiki()

    Treeki.display( class_instance_dodo )
    Treeki.display( class_instance_kiki )

    class foo():
        inst = []
        ID = 0
        def __init__(self) -> None:
            self.ID = foo.ID 
            foo.ID += 1 
            foo.inst.append(self)
            self.udi = foo.inst

    a = foo()
    b = foo()

    Treeki.display(a, ttl=3)