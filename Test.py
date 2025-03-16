d=5912021149162244363755593172
s=4833238097010702717751415
from random import randint
def find_e(d,s):
    e=0
    while (e*s)%d!=1:
        e=randint(2,d)
    return e
        
print(find_e(d,s))