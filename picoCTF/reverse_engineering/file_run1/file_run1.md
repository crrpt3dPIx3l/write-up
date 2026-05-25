# File run 1
## Description
A program has been provided to you, what happens if you try to run it on the command line? Download the program here.

### Hints
1. To run the program at all, you must make it executable (i.e. $ chmod +x run)
2. Try running it by adding a '.' in front of the path to the file (i.e. $ ./run) 

## Solution
Starting by downloading the file using `wget` then using the command `file run` to check the characterisitics of the file
```
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6e8c618e35e1676dcfc1528b849d349e82f127f1, for GNU/Linux 3.2.0, not stripped
```
It is an binary executable, so I'll give it a permission to execute with the command `chmod +x run` and run it using the command `./run`
```
chmod +x run; ./run
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
```
And got the flag immediately.
PWNED!