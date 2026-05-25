# Ready Gladiator
## Description
Can you make a CoreWars warrior that always loses, no ties? Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: nc saturn.picoctf.net 61042 < imp.red

### Hints
1. CoreWars is a well-established game with a lot of docs and strategy
2. Experiment with input to the CoreWars handler or create a self-defeating bot

## Solution
Starting with launcing the instance to get more information, I downloaded the source code to see anything interesting.
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```
I read the comment above which is saying assert 1, so I did it instead of 0 and connected to the instance;
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
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57}
```

PWNED!