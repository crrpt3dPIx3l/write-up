# Bit-O-Asm 4
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.

### Hints
1. Don't tell anyone I told you this, but you can solve this problem without understanding the compare/jump relationship.
2. Of course, if you're really good, you'll only need one attempt to solve this problem.

## Solution
Starting by downloading the assembly file and examining the content;
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

its better to have some common understading of assembly language before solving for later use, the instruction in code compare the value `0x9fe1a` and `0x2710`, if teh value 1 is less than valu 2 then 0x65 will be deducted from value one which is the right condition. 
using the below python script getting the decimal value for the hex value
```
val1 = 0x9fe1a
val2 = 0x65
val3 = val1-val2
print("picoCTF{" + f"{val3}" +"}")
```
so I've got `654773` and wrapping it in pico format `picoCTF{654773}`