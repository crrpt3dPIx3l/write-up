# GDB Baby Step 3
## Description
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}. Debug this.

### Hints
1. You'll need to breakpoint the instruction after the memory load.
2. Use the gdb command x/4xb addr with the memory location as the address addr to examine. GDB manual page.
3. Any registers in addr should be prepended with $ like $rbp.
4. Don't use square brackets for addr
5. What is endianness?

## Solution
Starting by downloading the file and viewing the characteristics using the command `file debugger0_c`, 
```
debugger0_c: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a10a8fa896351748020d158a4e18bb4be15cd3aa, for GNU/Linux 3.2.0, not stripped
```
using the command `chmod +x debugger0_c` and `./debugger0_c`, and no output is appearing. Switching to the `gdb` debugger to check for any useful information. 
`info functions`
```
Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  main
0x0000000000401130  __libc_csu_init
0x00000000004011a0  __libc_csu_fini
0x00000000004011a8  _fini
(gdb) 
```
now going through the disassembled 
```
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   %rbp
   0x000000000040110b <+5>:     mov    %rsp,%rbp
   0x000000000040110e <+8>:     mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:    mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:    movl   $0x2262c96b,-0x4(%rbp)
   0x000000000040111c <+22>:    mov    -0x4(%rbp),%eax
   0x000000000040111f <+25>:    pop    %rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
```
I noticed the value `0x2262c96b` value and I think it is the flag I tried to enter it as it is (LSB), and the second time in (MSB) `0x6bc96222` this was the flag. I used this approach because I read the hint number 5 after asking what is endianness? 

But I asked if there is any other approach because the hints was talking about something else, so I run "gdb" again and this time in INTEL flavour usign the command `set disassembly-flavor intel`

so I run gdb again and this time putting a break after the instruction storing the `0x2262c96b`, by the command `break *0x000000000040111c` and then `run`


after reaching the breakpoint I used the command given in the hind number to get the desired value `x/4xb $rbp-0x4`

```
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
(gdb) break *0x000000000040111c
Breakpoint 1 at 0x40111c
(gdb) x/4xb $rbp-0x4
❌️ No registers.
(gdb) run
Starting program: /home/user/Documents/picoCTF/reverse_engineering/gdb_baby_step3/debugger0_c 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000000000040111c in main ()
(gdb) x/4xb $rbp-0x4
0x7fffffffdc8c: 0x6b    0xc9    0x62    0x22
(gdb)
```
 and got the values in the right way!
 PWNED!