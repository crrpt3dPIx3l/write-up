# Bit-O-Asm 2
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.

### Hints
1. PTR's or 'pointers', reference a location in memory where values can be stored.

## Solution
Starting by downloading the file provided in the question and reading the file content;
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```
`0x9fe1a` this is the value stored in the eax, using the python ide in terminal printing the value give us the decimal form
```
Python 3.13.11 (main, Dec  8 2025, 11:43:54) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 0x9fe1a
654874
>>>
```
`654874` is the desired value, `picoCTF{654874}`
PWNED!