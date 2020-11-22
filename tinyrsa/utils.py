#!/usr/local/bin python
import gmpy2
import random
from math import lcm

def generate_keys(num_bytes=1):
    p = gmpy2.next_prime(int.from_bytes(random.randbytes(num_bytes), "little"))
    q = gmpy2.next_prime(int.from_bytes(random.randbytes(num_bytes), "little"))
    n = p * q
    phi = lcm((p - 1), (q - 1))
    for e in range(phi):
        if (e > 1 and phi % e == 0):
            e = gmpy2.next_prime(e)
            break
    print(e)
    print(n)
    print(p,q)


#p = 61#
#q = 53#

#e = 17
#d = 413

#TODO: Remove phi function 
def phi():
    return lcm(p - 1, q - 1)

def modinv(a, b):
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b
    
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0

    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def rsa_encryption(message):
    return message ** e % 3233

def rsa_decryption(message):
    p = phi()
    d = modinv(e, p)
    return message ** d % 3233
