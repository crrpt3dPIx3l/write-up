# Unpackme
## Description
Can you get the flag? Reverse engineer this binary.

### Hints
1. What is UPX?

## Solution
starting by dowloading the binary using the command `wget`, using the `file unpackme-upx` to check the file characteristics
```
unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```
giving the file the permission to execute usign the command `chmod +x unpackme-upx` and running the program using `./unpackme-upx`
```
What's my favorite number? 442
Sorry, that's not it!
```
using "Ghidra" I decompiled the file to check if I can get anything, and I didn't find anything useful so I read the hint and it says What is "UPX"? After a small research; UPX (Ultimate Packer for eXecutables)
is a free, open-source, and portable executable packer that reduces the file size of programs (EXE, DLL, Linux/macOS binaries) by 50%-70%. It enables self-contained, compressed files that automatically decompress in memory upon execution, with minimal overhead and no need for intermediate disk files. 

dowloading the tool to unpack the binary
```
sudo apt update
sudo apt install upx-ucl
```
and after reading the manual for decompressing use the command `upx -d unpackme-upx -o unpackedme-upx`
```
upx -d unpackme-upx -o unpackedme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1006445 <-    379188   37.68%   linux/amd64   unpackedme-upx

Unpacked 1 file.
```
I've got an extra file which is the ouput of the previous command, and again I opened ghidra to find anything interesting, this time the program has more information that before.
```
  if (local_44 == 0xb83cb) {
    local_40 = (char *)rotate_encrypt(0,&local_38);
    fputs(local_40,(FILE *)stdout);
    putchar(10);
    free(local_40);
  }
```
and got something here the password or the number is been comapared to this hex value `0xb83cb`, by using python to get the deecimal number;
```
Python 3.13.11 (main, Dec  8 2025, 11:43:54) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> 0xb83cb
754635
>>>
```
the favourite number is `754635`. 
```
./unpackedme-upx 2                   
What's my favorite number? 754635
picoCTF{up><_m3_f7w_77ad107e}
```

PWNED!