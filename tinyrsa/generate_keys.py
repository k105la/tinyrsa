import os
import gmpy2
from math import lcm
from tinyrsa.utils import modinv

class TinyKeys:
    def __init__(self): 
        self.p = gmpy2.next_prime(int.from_bytes(os.urandom(1), "little"))
        self.q = gmpy2.next_prime(int.from_bytes(os.urandom(1), "little"))        
        self.n = self.p * self.q
        
    def public_key(self):
        phi = lcm ((self.p - 1), (self.q - 1))
        for e in range(phi):
            if (e > 10 and phi % e == 0):
                e = gmpy2.next_prime(e)
                break

        return (self.n, e)

    def private_key(self):
        _, e = self.public_key()
        d = modinv(e, self.p)
        return (self.n, d)

