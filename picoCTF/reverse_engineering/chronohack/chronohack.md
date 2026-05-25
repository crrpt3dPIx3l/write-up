# Chronohack
## Description
Can you guess the exact token and unlock the hidden flag? Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important file for token generation. Guess the token to get the flag. The access is granted through nc verbal-sleep.picoctf.net port.

### Hints
1. https://www.epochconverter.com/
2. https://learn.snyk.io/lesson/insecure-randomness/
3. Time tokens generation
4. Generate tokens for a range of seed values very close to the target time

## Solution
Starting by downloading the python file for generating tokens and anlayze it
```
import random
import time

def get_random(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int(time.time() * 1000))  # seeding with current time 
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def flag():
    with open('/flag.txt', 'r') as picoCTF:
        content = picoCTF.read()
        print(content)


def main():
    print("Welcome to the token generation challenge!")
    print("Can you guess the token?")
    token_length = 20  # the token length
    token = get_random(token_length) 

    try:
        n=0
        while n < 50:
            user_guess = input("\nEnter your guess for the token (or exit):").strip()
            n+=1
            if user_guess == "exit":
                print("Exiting the program...")
                break
            
            if user_guess == token:
                print("Congratulations! You found the correct token.")
                flag()
                break
            else:
                print("Sorry, your token does not match. Try again!")
            if n == 50:
                print("\nYou exhausted your attempts, Bye!")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting the program...")

if __name__ == "__main__":
    main()
```
After reading this I understood that I've to guess or bruteforce the token in order to get the flag, but I had no idea where to start from and how even after checking the hints, so I read this document to make a cookie brute forcer [here](https://medium.com/@goldengrisha/when-time-becomes-a-vulnerability-breaking-chronohacks-token-generator-8f1266c0f612) so after reading and document, I crafted this script connects to a remote server and attempts to recover a secret token by exploiting the fact that the server likely generates the token using Python’s `random` module seeded with the current time. It estimates the server’s seed time by recording when the welcome message is received and optionally measuring network delay, then generates a range of possible seeds around that timestamp to account for timing and latency differences. For each candidate seed, it deterministically recreates the token and submits it to the server, checking the response for success. Because the server limits the number of guesses per connection, the script automatically reconnects after reaching the maximum attempts and continues guessing from where it left off. This process repeats until either the correct token is found or all plausible time-based seeds are exhausted.
 
Then I run the program by the command `python decoder.py verbal-sleep.picoctf.net 61920` 
and got the flag ``