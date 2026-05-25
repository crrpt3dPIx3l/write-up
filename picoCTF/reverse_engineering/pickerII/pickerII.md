# PickerII
## Description
Can you figure out how this program works to get the flag? Connect to the program with netcat: $ nc saturn.picoctf.net port The program's source code can be downloaded here.

### Hints
1. Can you do what win does with your input to the program?

## Solution
Started by downloading the source code and examining the content this is the source [code](picker-II.py);
So the `win` string is being filtered so we have bypass the filter, I think if the fucntion is filtered and eval is used to convert string to instuction, then I could read the file directly from the eval without using the name by passing the instruction `print(open('flag.txt', 'r').read())`
and got the flag
```
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object is not callable
```