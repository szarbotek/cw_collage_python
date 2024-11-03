c=4
a=65
b=20

if a<b:
    if a<c:
        if b<c:
            print(a)
            print(b)
            print(c)
        else:
            print(a)
            print(c)
            print(b)
if b<a:
    if b<c:
        if a<c:
            print(b)
            print(a)
            print(c)
        else:
            print(b)
            print(c)
            print(a)
if c<a:
    if c<b:
        if a<b:
            print(c)
            print(a)
            print(b)
        else:
            print(c)
            print(b)
            print(a)