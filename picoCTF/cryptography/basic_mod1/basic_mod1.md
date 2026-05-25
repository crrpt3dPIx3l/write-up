# Basic-mod1 (Cryptography)
## Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Hints
1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Solution
I Downloaded the file and read the content;
`128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140`

Due to the question we are prompted to apply a mod operation for each number and map them to the criteria provided, I used a python program to help me doing this

```
mapping_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
message = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"
listed_message = message.split(" ")
flag = ""

for i in listed_message:
    val = int(i)
    new_val = val % 37
    flag += mapping_list[new_val]

print("picoCTF{"+ flag + "}")
```
which gave me the outhput `picoCTF{R0UND_N_R0UND_79C18FB3}`
PWNED!