from random import randint
from sympy import randprime
from math import gcd

def find_NPQ():
    N=0
    while len(str(N))!=28:
        P=randprime(2,(10**randint(2,28)-1))
        Q=randprime(2,(10**randint(2,28)-1))
        N=P*Q
    return N,P,Q

def find_s(d)->int:
    s=randint(2,d-1)
    while gcd(d,s)!=1:
        s=randint(2,d-1)
    return s


#def euclid_method(a,b):
    if b==0:
        return a,1,0
    else:
        d,x,y=euclid_method(b,a%b)
        return d,y,x-y*(a//b)
    

def euclid_method(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = euclid_method(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
