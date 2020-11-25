import os
import gmpy2
from math import lcm

class TinyKeys:
    def __init__(self): 
        self.p = gmpy2.next_prime(int.from_bytes(os.urandom(1), "little"))
        self.q = gmpy2.next_prime(int.from_bytes(os.urandom(1), "little"))        
        self.n = self.p * self.q

    def phi(self):
        return lcm((self.p - 1), (self.q - 1))
   
    def xgcd(self, a, b): 
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0
    
    def modinv(self, a, b):
        g, x, _ = self.xgcd(a, b)
        if g != 1:
            raise Exception('gcd(a, b) != 1')
        return x % b
    
    def public_key(self):
        phi = self.phi()
        for e in range(phi):
            if (e > 1 and phi % e == 0 and self.n % e == 0):
                e = gmpy2.next_prime(e)
                break
        return (self.n, e)

    def private_key(self):
        _, e = self.public_key()
        d = self.modinv(e, self.phi)
        return (self.n, d)
