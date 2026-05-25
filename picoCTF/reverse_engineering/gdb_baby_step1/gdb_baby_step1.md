# GDB baby step 1
## Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Disassemble this.

### Hints
1. gdb is a very good debugger to use for this problem and many others!
2. main is actually a recognized symbol that can be used with gdb commands.

## Solution
Starting with donwnloading file and viewing the characteristics using the command `file debugger0_a`;
```
debugger0_a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15a10290db2cd2ec0c123cf80b88ed7d7f5cf9ff, for GNU/Linux 3.2.0, not stripped
```
giving the exectuable permission to run the binary `chmod +x debugger0_a` then `./debugger0_a`, and nothing appeared so by reading thee quesiton title it says GDB which is gnu debugger for binaries. `gdb ./debbuger0_a`
```
(gdb) disas main
Dump of assembler code for function main:
   0x0000555555555129 <+0>:     endbr64
   0x000055555555512d <+4>:     push   %rbp
   0x000055555555512e <+5>:     mov    %rsp,%rbp
   0x0000555555555131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000555555555134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000555555555138 <+15>:    mov    $0x86342,%eax
   0x000055555555513d <+20>:    pop    %rbp
   0x000055555555513e <+21>:    ret
End of assembler dump.
(gdb)
```
by taking the value stored in eax "0x86342", and using the python script to get the decimal value.
```
Python 3.13.11 (main, Dec  8 2025, 11:43:54) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 0x86342
549698
>>>
```
then wrapping the value with pico format `picoCTF{549698}`
PWNED!