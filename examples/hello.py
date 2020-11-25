#!/usr/local/bin python
from tinyrsa.encrypt import encrypt_cipher
from tinyrsa.decrypt import decrypt_cipher

e = encrypt_cipher("Hello world!")
d = decrypt_cipher(e)
