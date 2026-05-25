# GDB Baby Step 4
## Description
main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be picoCTF{4096}. Debug this.

### Hints
1. A function can be referenced by either its name or its starting address in gdb.

##
Starting by downloading the file and giving it the permission to be an executable, then using a gnu debugger "gdb";
```
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  func1
0x000000000040111c  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
(gdb) 
```
I listed the functions to see if anything useful and I found 3 `main`, `func1`, and `frame_dummy`.
```
(gdb) disas main
Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64
   0x0000000000401120 <+4>:     push   %rbp
   0x0000000000401121 <+5>:     mov    %rsp,%rbp
   0x0000000000401124 <+8>:     sub    $0x20,%rsp
   0x0000000000401128 <+12>:    mov    %edi,-0x14(%rbp)
   0x000000000040112b <+15>:    mov    %rsi,-0x20(%rbp)
   0x000000000040112f <+19>:    movl   $0x28e,-0x4(%rbp)
   0x0000000000401136 <+26>:    movl   $0x0,-0x8(%rbp)
   0x000000000040113d <+33>:    mov    -0x4(%rbp),%eax
   0x0000000000401140 <+36>:    mov    %eax,%edi
   0x0000000000401142 <+38>:    call   0x401106 <func1>
   0x0000000000401147 <+43>:    mov    %eax,-0x8(%rbp)
   0x000000000040114a <+46>:    mov    -0x4(%rbp),%eax
   0x000000000040114d <+49>:    leave
   0x000000000040114e <+50>:    ret
End of assembler dump.
(gdb) disas func1
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   %rbp
   0x000000000040110b <+5>:     mov    %rsp,%rbp
   0x000000000040110e <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000401111 <+11>:    mov    -0x4(%rbp),%eax
   0x0000000000401114 <+14>:    imul   $0x3269,%eax,%eax
   0x000000000040111a <+20>:    pop    %rbp
   0x000000000040111b <+21>:    ret
End of assembler dump.
(gdb) disas frame_dummy
Dump of assembler code for function frame_dummy:
   0x0000000000401100 <+0>:     endbr64
   0x0000000000401104 <+4>:     jmp    0x401090 <register_tm_clones>
End of assembler dump.
```
I disassembled the functioned to track the flow of the program. So i read the quesstion again and it says there is a multiplication operation done on the eax so I searched for it and fooun it in the `func1` functinos in the 3rd line from bottom `   0x0000000000401114 <+14>:    imul   $0x3269,%eax,%eax` so I took the value used in the operation and convert it into decimal using python
```
Python 3.13.11 (main, Dec  8 2025, 11:43:54) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 0x3269
12905
>>>
```
and then wrapping the flag in pico format `picoCTF{12905}`
