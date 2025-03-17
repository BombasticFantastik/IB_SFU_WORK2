from random import randint
from sympy import randprime
from math import gcd

def find_NPQ()->(int,int,int):
    N=0
    while len(str(N))!=28:
        P=randprime(2,(10**randint(2,28)-1))
        Q=randprime(2,(10**randint(2,28)-1))
        N=P*Q
    return N,P,Q

def find_s(d)->int:
    s=d
    while gcd(d,s)!=1:
        s=randint(2,d)
    return s


def euclid_method(a,b):
    if b==0:
        return a,1,0
    else:
        d,x,y=euclid_method(b,a%b)
        return d,y,x-y*(a//b)
