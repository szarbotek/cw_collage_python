#!/bin/python

def letterOccurrences( word:str, displayFlag:bool=True):

    cl: list[str] = [c for c in word]

    counter = {}
    
    for c in cl:
        if c in counter:
            counter[c] += 1
        else:
            counter.setdefault(c, 1)
    
    def displayINFO():
        print("Your word is:\n ... {}".format(word))
        for key, val in counter.items():
            print( "Liter {} jest: {}".format(key, val) )

    if displayFlag: displayINFO()
    return counter

letterOccurrences('tatarata')