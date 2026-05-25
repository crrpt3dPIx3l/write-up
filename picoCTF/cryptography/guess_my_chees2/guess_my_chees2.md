# Guess My Chees 2 (Cryptography)
## Description
The imposter was able to fool us last time, so we've strengthened our defenses! Here's our list of cheeses.

Additional details will be available after launching your challenge instance.

### Hints
1. I heard that SHA-256 is the best hash function out there!
2. Remember Squeexy, we enjoy our cheese with exactly 2 nibbles of hexadecimal-character salt!
3. Ever heard of rainbow tables?

## Solution
Starting by reading the quesiton and downloading the list of cheeses:
```
Abbaye du Mont des Cats
Abertam
Ackawi
Acorn
Allgauer Emmentaler
Anejo Enchilado
Anthoriro
Ardi Gasna
--------Omitted Output--------
```
Then I launch the instance to see what is the challenge:
```
*******************************************
***             Part 2                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

DRAT! The evil Dr. Lacktoes Inn Tolerant's clone was able to guess the cheese last time! I guess simple ciphers aren't good hashing methods. But now I've strengthened my encryption scheme so that now ONLY SQUEEXY can guess it...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  233d58268f6cf68575d4a8f9135cdc50ebd92768dd35ee67bb1c3147d8ea5e89

Commands: (g)uess my cheese
What would you like to do?
```
I've got an sha-256 and I knew that by scanning it in the tool "dCode", to solve this question I have to get the hashes of the cheeses in the cheese list and their salt value then compare them to the value given by the server, then I'll be able to the real cheese and give it to 'SQUEEXY'.
Using this python script I've found in another writeup thanks to that person:
```
#!/usr/bin/env python3
import hashlib
import sys

target_hash = "233d58268f6cf68575d4a8f9135cdc50ebd92768dd35ee67bb1c3147d8ea5e89"

# Define the encodings and case variants we want to try.
encodings = ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]
case_variants = {
    "original": lambda s: s,
    "lower": lambda s: s.lower(),
    "upper": lambda s: s.upper(),
}

# Read cheese names from cheese_list.txt (one per line)
try:
    with open("cheese_list.txt", "r") as f:
        cheeses = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("cheese_list.txt not found. Please create it with your list of cheese names.")
    sys.exit(1)

found = False

# Define a helper function that tests a candidate bytes object.
def test_candidate(candidate_bytes, method, extra, cheese, case_name, enc, salt):
    global found
    hash_val = hashlib.sha256(candidate_bytes).hexdigest()
    if hash_val == target_hash:
        print("Match found!")
        print(f"Cheese: {cheese}  (case variant: {case_name}, encoding: {enc})")
        print(f"Salt value: {salt} (0x{salt:02x})")
        print(f"Method: {method}, extra: {extra}")
        try:
            candidate_str = candidate_bytes.decode(enc)
        except Exception:
            candidate_str = repr(candidate_bytes)
        print(f"Candidate (using {enc}): {candidate_str}")
        found = True
        return True
    return False

for cheese in cheeses:
    for case_name, case_func in case_variants.items():
        cheese_variant = case_func(cheese)
        for enc in encodings:
            try:
                cheese_bytes = cheese_variant.encode(enc)
            except Exception:
                continue
            for salt in range(256):
                salt_raw = bytes([salt])
                salt_hex_str = format(salt, "02x")
                try:
                    salt_hex = salt_hex_str.encode(enc)
                except Exception:
                    salt_hex = salt_hex_str.encode("utf-8")  # fallback

                # Option A: Append and prepend raw byte.
                if test_candidate(cheese_bytes + salt_raw, "append_raw", "raw byte appended",
                                  cheese, case_name, enc, salt):
                    break
                if test_candidate(salt_raw + cheese_bytes, "prepend_raw", "raw byte prepended",
                                  cheese, case_name, enc, salt):
                    break

                # Option B: Append and prepend hex string.
                if test_candidate(cheese_bytes + salt_hex, "append_hex", "hex string appended",
                                  cheese, case_name, enc, salt):
                    break
                if test_candidate(salt_hex + cheese_bytes, "prepend_hex", "hex string prepended",
                                  cheese, case_name, enc, salt):
                    break

                # Option C: Insert raw byte at every possible index.
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_raw + cheese_bytes[i:]
                    if test_candidate(candidate, "insert_raw", f"at byte index {i}",
                                      cheese, case_name, enc, salt):
                        break
                else:
                    pass
                if found:
                    break

                # Option D: Insert hex string at every possible index.
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_hex + cheese_bytes[i:]
                    if test_candidate(candidate, "insert_hex", f"at byte index {i}",
                                      cheese, case_name, enc, salt):
                        break
                else:
                    pass
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("No matching cheese and salt combination was found.")
```
I was able to find the cheese and the salt value, now I give the cheese to 'SQUEEXY' and got the flag `picoCTF{cHeEsY5d45bcdd}`
PWNED!
