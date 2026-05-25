import string

# Constants
enc_flag = "fegdeogdgecoeocgcgchcfcffccfca"
ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

def b16_decoder(cipher):
    decoded = ""
    listed_4b = []
    listed_8b = []
    for i in cipher:
        for k, j in enumerate(ALPHABET):
            if i == j:
                listed_4b.append(format(k,'04b'))

    for i in range(0, len(listed_4b),2):
        listed_8b.append(listed_4b[i] + listed_4b[i+1])

    for i in listed_8b:
        bin = int(i,2)
        decoded+= chr(bin)

    return decoded

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def decrypt(enc, key):
    dec = ""
    for i, c in enumerate(enc):
        dec += unshift(c, key[i % len(key)])
    return dec

for k in ALPHABET:
    decrypted = decrypt(enc_flag, k)
    if all([c in ALPHABET for c in decrypted]):
        decoded = b16_decoder(decrypted)
        if all([c in string.printable for c in decoded]):
            print(f"Key: {k}, Plaintext: {decoded}")