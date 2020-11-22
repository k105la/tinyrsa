from tinyrsa.utils import rsa_decryption
d_m = []
def decrypt_cipher(cipher_m):
    for c in cipher_m:
        d_m.append(chr(rsa_decryption(c)))
    for i in d_m:
        print(i, end='')     
    print()

