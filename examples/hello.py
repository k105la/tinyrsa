#!/usr/local/bin python
from tinyrsa.encrypt import encrypt_cipher
from tinyrsa.decrypt import decrypt_cipher

e = encrypt_cipher("Hello world my name is Akil and this is a secret message that was encrypted using RSA!")
d = decrypt_cipher(e)