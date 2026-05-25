# RSA Oracle (Cryptography)
## Description
Can you abuse the oracle? An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message (ciphertext) and the password that was used to encrypt the message.

Additional details will be available after launching your challenge instance.

### Hints
1. Crytography Threat models: chosen plaintext attack.
2. OpenSSL can be used to decrypt the message. e.g openssl enc -aes-256-cbc -d ...
3. The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.
4. Minimum requirements for a useful cryptosystem is CPA security.

## Solution
Starting by reading the question and downloading the cipher text and the password files:
```
`secret.enc` : Salted__jX���9V)�pT3Ͼq�$�qEs�5�n\K5=�%c��       �Q�9s�1!quM�0��4��
`password.enc`: 2336150584734702647514724021470643922433811330098144930425575029773908475892259185520495303353109615046654428965662643241365308392679139063000973730368839
```
I launched the instance and got some extra information:
```
After some intensive reconassainance they found out that the bank has an oracle that was used to encrypt the password and can be found here nc titan.picoctf.net 51812. Decrypt the password and use it to decrypt the message. The oracle can decrypt anything except the password.
```
I connected to machine to see how it works, and the same trick is used from another oracle rsa bot which is "Chosen Plaintext Attack (CPA)", 

I will cover the password, multiplying the encrypted value of the encrypted password by an encrypted value of 5 which will become 

refer to "[writeup](https://medium.com/@mr-nakamura/rsa-oracle-picoctf-1682abefe1d0)"
```
enter text to encrypt (encoded length must be less than keysize): 5
5

encoded cleartext as Hex m: 35

ciphertext (m ^ e mod n) 328779559998814913351140854640801391504762517581365098951033961875402256487125183765198160515443022459576165533710527230789639796593595281878338659777623

what should we do for you? 
E --> encrypt D --> decrypt.
```   
using this python script I decoded the flag
```
from subprocess import run, PIPE  
  
# Grab ciphertext
with open("password.enc", "r") as f:  
	c = int(f.read())  
  
print("Phase 1: Get password\n")  
  
print(f"c = {c}\n")  
 
# Get message from user
m1 = input("Enter message (m1): ")  
m1_bytes = bytes(m1, "utf-8")  
m1_int = ord(m1_bytes) 
  
print(f"Have the oracle encrypt this message (m1): {m1}\n")  
c1 = int(input("Enter ciphertext from oracle (c1 = E(m1)): "))  
print("\n")  
 
# Exploit the homomorphic property of RSA
c2 = c * c1  
print(f"Have the oracle decrypt this message (c2 = c * c1): {c2}\n")  
  
m2 = int(input("Enter decrypted ciphertext as HEX (m2 = D(c2): "), 16)  
print("\n")  
 
# Exploit the homomorphic property of RSA some more
m_int = m2 // m1_int  
m = m_int.to_bytes(len(str(m_int)), "big").decode("utf-8").lstrip("\x00")
print(f"Password (m = m2 / m1): {m}\n")  
  
print("-" * 50)  
  
print("Phase 2: Decrypt secret.enc\n")  
 
# Decrypt the secret and print it
res = run(["openssl", "enc", "-aes-256-cbc", "-d", "-in", "secret.enc", "-pass",  
f"pass:{m}"], stdout=PIPE, stderr=PIPE, text=True)  
print(res.stdout)
```
and got the flag `picoCTF{su((3ss_(r@ck1ng_r3@_60f50766}`

PWNED!