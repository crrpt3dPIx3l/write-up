# Morse-Code (Cryptography)
## Description
Morse code is well known. Can you decrypt this? Download the file here. Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

### Hints
1. Audacity is a really good program to analyze morse code audio.

## Solution
After reading the quesiton and downloading the audio file,
I used the website "https://morsecode.world/international/translator.html" for reading the morse code from the audio. 
`WH47 H47H 90D W20U9H7` This was the output from the website decoding for the sound wrapping it to satisfy the flag shape using the following python script
```
undefined_flag = "WH47 H47H 90D W20U9H7"
lowercase_flag = undefined_flag.lower()
no_space_flag = lowercase_flag.replace(" ", "_")
print("picoCTF{" + no_space_flag + "}")
```
Output: `picoCTF{wh47_h47h_90d_w20u9h7}`
