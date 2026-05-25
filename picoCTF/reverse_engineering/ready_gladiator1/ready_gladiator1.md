# Ready Gladiator 1
## Description
Can you make a CoreWars warrior that wins? Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: nc saturn.picoctf.net 62212 < imp.red To get the flag, you must beat the Imp at least once out of the many rounds.

### Hints
1. You may be able to find a viable warrior in beginner docs

## Solution
Started by downloading the source code and examine the content;
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```
again like "Ready Gladiator 0" it says assert one, so I did instead of 0 `mov 1, 1` then connected to the machine
```
;redcode
;name Imp Ex
;assert 1
mov 1, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 1, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
Try again. Your warrior (warrior 1) must win at least once.
```
not getting the flag, so I hoped directly to the hint which says check the beginner manuall for the corewars "https://www.corewars.org/docs/dummies.html" and in chapter II, I say a peice of code saying
```
;redcode-94
;name Sleepy
;author John Q. Smith
;strategy bombing core

ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33

end
```
so appended this part and connected to the server again,
```
;redcode
;name Imp Ex
;assert 1
mov 1, 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33

end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 1, 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33

end

Rounds: 100
Warrior 1 wins: 19
Warrior 2 wins: 0
Ties: 81
You did it!
picoCTF{1mp_1n_7h3_cr055h41r5_f2ba3220}
```
PWNED!