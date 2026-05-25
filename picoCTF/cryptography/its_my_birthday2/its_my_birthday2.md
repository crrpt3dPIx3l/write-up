# Its my birthday 2 (Cryptogrpahy)
## Description
My birthday is coming up again, but I want to have a very exclusive party for only the best cryptologists. See if you can solve my challenge, upload 2 valid PDFs that are different but have the same SHA1 hash. They should both have the same 1000 bytes at the end as the original invite. http://wily-courier.picoctf.net:port/ invite.pdf
### Hints
1. This isn't REALLY a birthday attack problem
2. https://shattered.io/
3. The PDFs cannot be the same
4. The PDFs must be valid
5. The last 1000 bytes of each PDF must match the last 1000 bytes of the original

## Solution
So I started by launcing the machine and downloading the pdf birthday file, and after reading the question again I think we have to exploit the website using an attack similar to md5 collision attack but this time using the SHA1-hash collision attack, I downloaded the 2 file for the testing in the link in Hint 2 I donwloaded the 2 files and appended the hex bytes of the file I donwloaded from the challenge because the server accepts the pdf that has same last 1000 bytes of the original one. so I i did all the step and crafted 2 pdf payloads `payload1.pdf` and `payload2.pdf` and submitted it into the website and got the flag.
Before solving this challenge I'd to see some writeup for better understanding. "[Writeup](https://vivian-dai.github.io/PicoCTF2021-Writeup/Cryptography/It%20is%20my%20Birthday%202/)"
PWNED!