# Patchme.py
## Description
Can you get the flag? Run this Python program in the same directory as this encrypted flag.

### Hints
none

## Solution
Starting by downloading the files and examining the content;
```
cat flag.txt.enc  

CR1@    UYX+
6U]WVM 
```
```
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```
By reading the code it seems that the data is encypted in xor technology but when checking the second function `level_1_pw_check()` it reveals the password for decrypting the flag back to plaintext so I modified just one character in the line 19 and changed the `equal` to `not equal`.
```
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw != "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")

```
then I run the program to get;
```
python patchme.flag.py 
Please enter correct password for flag: hello
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```
PWNED!