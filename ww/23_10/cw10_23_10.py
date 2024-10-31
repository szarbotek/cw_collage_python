#cw10
msg:str = "5h9n gibn9e j 59n 9h5 nbne0j y9h6 p95j 04040gj0gh0mg"
SPACE:chr = ' '

print(msg.__len__() )
print(msg.count(SPACE)) 

L = msg.__len__()
msg = msg.replace(SPACE, '')

# print(len(msg.split(' '))-1)
print( L - len(msg))

