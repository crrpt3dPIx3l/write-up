# Substitution1 (Cryptography)
## Description
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message here.

### Hints
1. Try a frequency attack
2. Do the punctuation and the individual words help you make any substitutions?

## Solution
Starting by downloading the file and reading the content and a cipher text was provided

```
ZWDg (gejfw djf zacwpfx wex dqar) afx a wscx jd zjicpwxf gxzpfbws zjicxwbwbjv. Zjvwxgwavwg afx cfxgxvwxm hbwe a gxw jd zeaqqxvrxg hebze wxgw wexbf zfxawbybws, wxzevbzaq (avm rjjrqbvr) gnbqqg, avm cfjtqxi-gjqybvr atbqbws. Zeaqqxvrxg pgpaqqs zjyxf a vpitxf jd zawxrjfbxg, avm hexv gjqyxm, xaze sbxqmg a gwfbvr (zaqqxm a dqar) hebze bg gptibwwxm wj av jvqbvx gzjfbvr gxfybzx. ZWDg afx a rfxaw has wj qxafv a hbmx affas jd zjicpwxf gxzpfbws gnbqqg bv a gadx, qxraq xvybfjvixvw, avm afx ejgwxm avm cqasxm ts iavs gxzpfbws rfjpcg afjpvm wex hjfqm djf dpv avm cfazwbzx. Djf webg cfjtqxi, wex dqar bg: cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}
```

I used the previous website from substitute0 to decrypt the message and it worked or that what I thought at the beggining the flag is not correct.

```
CTFs (short for capture the flag) are a type of computer security competition. Contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. Challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. CTFs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. For this problem, the flag is: picoCTF{FR3JU3NCY_4774CK5_4R3_C001_4871E6FB}

```

After giving it a look the hint says try the frequency test, giving it a small research frequency analysis is a test for the letter positioning percentage in the index the highest is the most probable answer to that place, when applying this test to the flag I got after deciphering the text `picoCTF{FR3JU3NCY_4774CK5_4R3_C001_4871E6FB}` every letter was in it right place except for the `J` the percentage of another letter was higher it was `Q` and this was done with the help of "dcode https://www.dcode.fr/monoalphabetic-substitution"

PWNED!

