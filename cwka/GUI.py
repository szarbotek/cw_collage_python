import os

class GUI:
    
    @classmethod
    def displayTitle(cls, title:str, r:int=17) -> None:
        if title != '':
            print( "="*r + f"> {title} <" + "="*r  )
        else:
            pass
    
    @classmethod
    def displayMsg(cls, msg:str='' ) -> None:
        print(msg)

    @classmethod
    def inputOption(cls, msgInput:str = "Chose option... ", option:list[str, str] = ['y', 'n'] ) -> str:
        GUI.displayMsg( "[{}]\t(x)".format( "|".join( option ) ) )
        return input( msgInput )
    
    @classmethod
    def waitInput(cls):
        input("\nPress any to continue...")
    
    @classmethod
    def window(cls, title:str, msg:str)->None:
        GUI.displayTitle(title)
        GUI.displayMsg(msg)

    @classmethod
    def windowAlert(cls, title:str = "Alert", msg:str = "Its Allert msg", msgInput:str = "Chose option... ", option:list[str, str] = ['y', 'n'], ErrorMsg:str = "Incorracte option." ) -> str:
        assert len(option) == 2, "Valid options!"

        while True:
            os.system( "cls" )
            GUI.window(title, '\n'+msg)
            GUI.displayMsg()
            opt = GUI.inputOption( msgInput, option )
            if opt in option:
                if opt == 'x': return None
                if opt == option[0]:
                    return True
                elif opt == option[1]:
                    return False
            GUI.displayMsg()
            GUI.displayMsg( ErrorMsg  )
            GUI.waitInput()

    @classmethod
    def windowMenu(cls, title:str = "Menu", msg:str = "Its Menu msg", msgInput:str = "Chose option... ", option:dict[str: any] = {1: "add", 2:"remove"}, ErrorMsg:str = "Incorracte option." ) -> str:
        assert len(option) >= 1, "Valid options!"
        assert isinstance(option, dict), TypeError
        while True:
            os.system( "cls" )
            GUI.window(title, '\n'+msg)
            GUI.displayMsg()
            for index, value in option.items():
                GUI.displayMsg( "\t{}. {}".format( index, value ) )
            GUI.displayMsg()
            optionIndex = [ str(key) for key in option.keys()]
            opt = GUI.inputOption( msgInput, optionIndex )
            if opt == 'x': return None
            if opt in optionIndex:
                return opt
            GUI.displayMsg()
            GUI.displayMsg( ErrorMsg  )
            GUI.waitInput()

# gg.window("menu", "1-add, 2-remove")

# gg.inputOption()

# GUI.windowAlert()

class foo:
    def __init__(self, v) -> None:
        self.val = v
    
    def __str__(self) -> str:
        return 'element'

from Treeki import Treeki

a  = foo(11)
b  = foo(12)
c  = foo(13)

num = [a, b ,c]

# Treeki.setLocals( locals() )
Treeki.display( num )

ret = GUI.windowMenu( msg=Treeki.getPrintBuffor(num) + "\n\nHelko", option={1:'close',2: 'exit'} )
print(ret)