# Shop 
## Description
Best Stuff - Cheap Stuff, Buy Buy Buy...

Additional details will be available after launching your challenge instance.

### Hints
1. Always check edge cases when programming

## Solution
Starting with launching the instance and downloading the source code, and checked the file type using the command `file source`
```
source: ELF 32-bit LSB executable, Intel i386, version 1 (SYSV), statically linked, Go BuildID=4B889tc1TRgpS9czhvct/FgQ1iPCpaksezCsvmIRb/JEuIrSM0u7bsenZgEPQP/pVFuNtB-YiGf_M2pZFLj, with debug_info, not stripped
```
Its an executable, usign the command `chmod +x source` give the program the permission to be an executable then `./source` to run the program
```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
```
the aim is to get the "Fruitful Flag" but it worth 100 and I got 40 so I got see the option sell items
```
Your inventory
(0) Quiet Quiches       10      0
(1) Average Apple       15      0
(2) Fruitful Flag       100     0
What do you want to sell?
```
unfortunately we don't have anything to sell, but using the simple trick, some of the challenges like this use the "-" arithmetic operation to deduct frombalance, so by reversing this operation by adding another minus operation "-" to the input so instead of deducting it increases the balance (eg. 40 -- 100 =140) simple math!

I launched the instance and did the same approach to get the flag encoded `Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 48 99 101 99 54 51 49 55 98 125 10]` so I used CyberChef to get the plaintext flag `picoCTF{b4d_brogrammer_0cec6317b}`

PWNED!