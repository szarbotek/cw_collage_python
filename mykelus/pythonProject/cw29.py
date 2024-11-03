import random
aalista=[ ]
bblista=[ ]

while len(aalista)<10:
    aalista.append(random.randint(1,50))
    bblista.append(random.randint(1,50))
print(aalista)
print(bblista)

for aa in aalista:
    for bb in bblista:
        if aa == bb:
            print("Liczba", bb, "powtarza się")
