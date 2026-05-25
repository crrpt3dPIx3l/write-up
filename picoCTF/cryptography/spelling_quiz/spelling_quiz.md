# Spelling_Quiz (Cryptography)
## Description
I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.

### Hints
none

## Solution
I downloaded the file provided in the challenge it was a "public.zip" file, I unzipped it and examined the content, it has a directory and directory contains 3 file `encrypt.py  flag.txt  study-guide.txt` I check the 'study-guide.txt' first to check if there is any thing I've to take care of, I used cat command and throws a long list of unkown text but looked ciphered or something, I headed up to the 'flag.txt' which has `brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm` it is the flag but ciphered and changing every time I run the third file, the last file 'encrypt.py' is a script for encryption and changing the value every time I run the code
!Note: the code is modified with comments only for personal understanding and debugging!
```
import random
import os

# This part checks for the txt files
files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]



alphabet = list('abcdefghijklmnopqrstuvwxyz')   # listing alphabets
random.shuffle(shuffled := alphabet[:])
# assign a copy of the shuffled alphabet into a variable
dictionary = dict(zip(alphabet, shuffled))
# relating the position of the alphabet list and shuffled list and stored in the dictionary

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
```

I was trying to think of a python program to decode the text for me but it took from me a long time and I decided just to look up for a tool breaking the cipher faster and I've found `subbreaker` a tool for breaking this kind of cipher, so by the command  it took a little bit o
```
head -n 50 study-guide.txt> Shortened_study-guide.txt
subbreaker break --lang EN --ciphertext Shortened_study-guide.txt
```

and the output was 

```
Alphabet: abcdefghijklmnopqrstuvwxyz
Key:      xunmrydfwjglstibhcavopezqk
Fitness: 92.78
Nbr keys tried: 4225
Keys per second: 23637
Execution time (seconds): 0.179
Plaintext:
kurchicine
malfeasor
greenheart
baptistry
litorinoid
vindicatory
-----Ommited-----
```

now we know the keys its time to get the flag from the file "flag.txt" using the same method and keys, I used the command
```
subbreaker decode --key xunmrydfwjglstibecavohpkqz --ciphertext flag.txt
```
and the output: `perhaps_the_dog_qumped_over_was_qust_tired` is was good only the q was substituted with the j I did it manually.

final output `perhaps_the_dog_jumped_over_was_just_tired`

PWNED!