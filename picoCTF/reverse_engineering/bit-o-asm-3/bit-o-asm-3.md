# Bit-O-Asm 3
## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.

### Hints
1. Not everything in this disassembly listing is optimal.

## Solution
Starting by downloading the file and examining the conent;
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```
following the instrcution in assebmly language, to conclude what is stored in `eax` = `(0x9fe1a * 0x4) + 0x1f5`, so using the following script to solve the challange
```
val1 = 0x9fe1a
val2 = 0x4
val3 = 0x1f5
val4 = (val1 * val2) + val3
print("Hex_decoded_flag: picoCTF{"+ f"{val4}" + "}") # 2619997 hex value
```
output `Hex_decoded_flag: picoCTF{2619997}`
PWNED!