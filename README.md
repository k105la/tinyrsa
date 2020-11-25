# tinyrsa 

![Unit Tests](https://github.com/akilhylton/tinyrsa/workflows/Unit%20Tests/badge.svg)

This may not be the most secure RSA library but it is a RSA library that is tiny.

### Installation
```
cd ~/tinyrsa
python setup.py install
```

### Hello World example (from example/hello.py)
```python
from tinyrsa.encrypt import encrypt_cipher
from tinyrsa.decrypt import decrypt_cipher

e = encrypt_cipher("Hello world!") # Encrypts message with tinyrsa
d = decrypt_cipher(e)              # Decrypts message with tinyrsa
```

### Only Encryption and Decrpytion?
Yes, tinyrsa is as simple as RSA can get it does: key generation, encryption, and decryption.  
However, tinyrsa doesn't do signing messages or key distribution.

### Running tests

```bash
python -m pytest
```

### TODO
* Increase two prime numbers (p and q) to 1024 bytes 
* Add support for signing messages
