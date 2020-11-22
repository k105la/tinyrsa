#!/usr/local/bin python
from encrypt import encrypt_cipher
from decrypt import decrypt_cipher

e = encrypt_cipher("Hello world my name is Akil and this is a secret message that was encrypted using RSA!")
d_0 = decrypt_cipher(e)
