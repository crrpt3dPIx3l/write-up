# FactCheck
## Description
This binary is putting together some important piece of information... Can you uncover that information? Examine this file. Do you understand its inner workings? 

### Hints
none

## Solution
Starting by downloading the binary file and checking the file;
```
└─$ file bin     
bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ba87dd5805704ffe3d15a1e136c290a83fe95dba, for GNU/Linux 3.2.0, not stripped
```
giving it the permission to execute and running it but nothing appeared so means something happened behind, I will check the `strings` commands first to check for anything useful
```
└─$ strings bin
/lib64/ld-linux-x86-64.so.2
libstdc++.so.6
__gmon_start__
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm
_ZNSaIcED1Ev
---------Omitted Output---------
```
 next I used `gdb` to check for something I can use
 ```
 (gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
------------Omitted Output---------
0x00000000000011a0  _start
0x00000000000011d0  deregister_tm_clones
0x0000000000001200  register_tm_clones
0x0000000000001240  __do_global_dtors_aux
0x0000000000001280  frame_dummy
0x0000000000001289  main
0x0000000000001c54  __static_initialization_and_destruction_0(int, int)
0x0000000000001ca1  _GLOBAL__sub_I_main
0x0000000000001cc0  __libc_csu_init
0x0000000000001d30  __libc_csu_fini
0x0000000000001d38  _fini
 ```
after long searching nothing was found useful up to now, so I went to ghidra for deeper analysis
and got the flag but distributed all along the code so I had to collect them one by one. And this is the final flag `picoCTF{wELF_d0N3_mate_05d32aaeedbe6c98}`, but this was wrong to check for something else, and scrolling down using ghidra I've found
```
  pcVar2 = (char *)std::__cxx11::string::operator[]((ulong)local_208);
  if (*pcVar2 < 'B') {
    std::__cxx11::string::operator+=(local_248,local_c8);
  }
  pcVar2 = (char *)std::__cxx11::string::operator[]((ulong)local_a8);
  if (*pcVar2 != 'A') {
    std::__cxx11::string::operator+=(local_248,local_68);
  }
  pcVar2 = (char *)std::__cxx11::string::operator[]((ulong)local_1c8);
  cVar1 = *pcVar2;
  pcVar2 = (char *)std::__cxx11::string::operator[]((ulong)local_148);
  if ((int)cVar1 - (int)*pcVar2 == 3) {
    std::__cxx11::string::operator+=(local_248,local_1c8);
  }
  std::__cxx11::string::operator+=(local_248,local_1e8);
  std::__cxx11::string::operator+=(local_248,local_188);
  pcVar2 = (char *)std::__cxx11::string::operator[]((ulong)local_168);
  if (*pcVar2 == 'G') {
    std::__cxx11::string::operator+=(local_248,local_168);
  }
  std::__cxx11::string::operator+=(local_248,local_1a8);
  std::__cxx11::string::operator+=(local_248,local_88);
  std::__cxx11::string::operator+=(local_248,local_228);
  std::__cxx11::string::operator+=(local_248,local_128);
  std::__cxx11::string::operator+=(local_248,'}');
```
which explains the new flag ordering under some condition, which only the last 4 letter are clear and the rest need some sort of attention;
Conditions:
1. if '5' < 'B' then flag+='e'
2. if '6' != 'A' then flag+='9'
3. if '3' - 'e' == 3 then flag+='3'
4. flag += 'd'
5. flag += 'a'
6. if 'a' == 'G' then flag += 'a'
7. flag += '2'
8. flag += 'c'
9. flag += '0'
10. flag += 'e'
11. flag += '}'
So after following the instruction and filtering the new flag the output will be `picoCTF{wELF_d0N3_mate_e9da2c0e}`

PWNED!