#!/usr/local/bin python
import gmpy2
import random
from tinyrsa.generate_keys import TinyKeys

k = TinyKeys()

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
    n, e = k.public_key() 
    return message ** int(e) % int(n)

def rsa_decryption(message):
    n, d = k.private_key()
    return message ** int(d) % int(n)
