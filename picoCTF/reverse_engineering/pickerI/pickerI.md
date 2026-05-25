# PickerI
## Description
This service can provide you with a random number, but can it do anything else? Connect to the program with netcat: $ nc saturn.picoctf.net port The program's source code can be downloaded here.

### Hints
1. Can you point the program to a function that does something useful for you?

## Solution
Started by downloading the the source code to understand how the program work [source_code](/reverse_engineering/pickerI/picker-I.py);
After reading the code and I saw the part that is taking the input from the user and passing it true `eval`, eval is method to convert strings into instruction for the program to follow, so I think if I can use it to make the win() method run.
```
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d 
Try entering "getRandomNumber" without the double quotes...
==>
```
by entering the string `win` the program automatically adds the pair of bracket "()" which will make a whole string of `win()` and this is the funciton we want to print the flag. So I got the flag in a hex value encoded for each letter so using the following script I printed the flag immediently.
!Note: an external source can be used to decode the value like "CyberChef" but I prefer python for personal use
```
hex_flag = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d"
listed_hex_flag = hex_flag.replace('0x','').split(' ')
pure_hex = "".join(listed_hex_flag)
flag = bytes.fromhex(pure_hex).decode('utf-8')
print(flag)
```
output `picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`