# Ready Gladiator 2
## Description
Can you make a CoreWars warrior that wins every single round? Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: nc saturn.picoctf.net 57446 < imp.red To get the flag, you must beat the Imp all 100 rounds.

### Hints
If your warrior is close, try again, it may work on subsequent tries... why is that?

## Solution
Starting by downloading the source code of my warrior and examining the content,
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```
asserted 1 as usual, but this time we have to beat the machine  all the 100 time, I tried the code from [ready_gladiator1](/reverse_engineering/ready_gladiator1/imp.red) to see if it can do something, but nothing in return, after a long search nothing was found so I needed for some help in [youtube](https://www.youtube.com/watch?v=l3nJnun_nbo). and after getting the imgate code appended it to the file and connected to the server
```
;redcode
;name Imp Ex
;assert 1
mov 1, 1

gate equ wait-10
wait JMP wait,<gate
end wait
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 1, 1

gate equ wait-10
wait JMP wait,<gate
end wait
end

Rounds: 100
Warrior 1 wins: 100
Warrior 2 wins: 0
Ties: 0
You did it!
picoCTF{d3m0n_3xpung3r_47037b25}
```
PWNED!