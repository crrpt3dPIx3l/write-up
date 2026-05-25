# Basic-mod2 (Cryptography)
## Description
A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Hints
1. Do you know what the modular inverse is?
2. The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
3. It's recommended to use a tool to find the modular inverses

## Solution
While reading the question the concept of modular inverse which I didn't hear about so before doing anything I gave it a quick search, 

***Modular Inverse*** is by taking module of a negativly powered value (eg. formula for private key in RSA: ***d = e<sup>-1</sup> mod(r)*** )

I crafted a python program to do the task;

```
mapping_list = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
message = "432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"
listed_message = message.split(" ")
flag = ""

for i in listed_message:
    val = pow(int(i), -1, 41)

    flag += mapping_list[val]

print("picoCTF{" + flag + "}")
```
Output
```
picoCTF{1NV3R53LY_H4RD_C680BDC1}
```
PWNED!