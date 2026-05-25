# GDB Test Drive
## Description
Can you get the flag? Download this binary. Here's the test drive instructions:

    $ chmod +x gdbme
    $ gdb gdbme
    (gdb) layout asm
    (gdb) break *(main+99)
    (gdb) run
    (gdb) jump *(main+104)

### Hints
none

## Solution
Starting by downloading the file and giving it the permission to be an executable `chmod +x gdbme` and then follwoing the steps in the description of the challenge. Obtained the flag `picoCTF{d3bugg3r_dr1v3_72bd8355}`