#!/usr/local/bin python
from tinyrsa.utils import rsa_encryption
e_arr = []
def encrypt_cipher(message):
    for i in message:
        ne = ord(i)
        e_arr.append(rsa_encryption(ne))
        print(chr(rsa_encryption(ne)), end='')
    print()
    return e_arr
