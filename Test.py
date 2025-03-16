from random import randint
from sympy import randprime

def give_me_fucking_number():
    N=0
    while len(str(N))!=28:
        P=randprime(2,(10**randint(2,28)-1))
        Q=randprime(2,(10**randint(2,28)-1))
        N=P*Q
    return N,P,Q


print(give_me_fucking_number())