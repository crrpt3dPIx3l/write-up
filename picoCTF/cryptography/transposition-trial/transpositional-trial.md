# transposition-trial (Cryptography)
## Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message here.

### Hints
1. Split the message up into blocks of 3 and see how the first block is scrambled

## Solution
Started with reading the question and downloading the file, I saw the content of the message and I can see the flag but it is shuffled in 3 to 3 letters, so I came up with an idea to decrypt the flag using a python program.

```
message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
flag = ""

for i in range(0, len(message),3):
    flag += message[i+2] + message[i] + message[i+1]
    
    
print(flag)
```

and got the flag `The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}`

PWNED!