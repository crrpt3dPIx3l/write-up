# File run 2
## Description
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program here.

### Hints
1. Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")

## Solution
Starting by downloading the file provided in the quesiton usign the command `wget` then using the command `file run` to check the characteristics of the binary
```
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=303d7c50cf258e07aa508de37a50e4d85d5e475f, for GNU/Linux 3.2.0, not stripped
```
Next, give it the permission to execute using the command `chmod +x run`, and run it using the command `./run`.
```
chmod +x run; ./run
Run this file with only one argument.
```
It says the program only runs with one argument, so we will pass one by using the command `./run Hello! ` as prompted `Won't you say 'Hello!' to me first?`
```
./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_96f2195f}
```
PWNED!