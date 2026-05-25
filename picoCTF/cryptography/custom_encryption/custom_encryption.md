# Custom Encryption
## Description
Can you get sense of this code file and write the function that will decode the given encrypted file content. Find the encrypted file here flag_info and code file might be good to analyze and get the flag. 

### Hints
1. Understanding encryption algorithm to come up with decryption algorithm.

## Solution
After reading the question and downloading the content of the challenge, I've got 2 files `custom_encryption.py` and `enc_flag` the content of the enc_flag is:
```
a = 88
b = 26
cipher is: [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]
```

custom_encryption.py:
```
from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
```
When I understood the flow of the code, the flag is been XORed first with a key generatded by the function `generator` then passed to encrypter to complete the second part of encryption which is multiplying the integer form of the text by `311 * key` and store it back in the list.
I crafter a python script to decrypt the flag;
```
# key generation
def generator(g, x, p):
    return pow(g, x) % p

# this will be the inverser of the process 
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text



p = 97
g = 31
a = 88  # not needed in this equation this will be the opposite if u has been used
b = 26
v = generator(g, b, p)
key = generator(v, a, p)
cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

print(f"The key is: {key}") # key = 35 from debugging

cipher_text = ""
for char in cipher:
    cipher_text += chr(char // 311 // 35) # used chr because opposite of ord and 35 for key
print(f"Cipher text: {cipher_text}")

plaintext = dynamic_xor_encrypt(cipher_text, "aedurtu")
print(f"Plaintext: {plaintext}")
```
!Note: When using XOR:
1. plaintext ^ key = ciphertext
2. ciphertext ^ key = plaintext
3. plaintext ^ ciphertext = key

PWNED!