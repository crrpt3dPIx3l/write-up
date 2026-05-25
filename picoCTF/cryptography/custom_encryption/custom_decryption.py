# key generation
def generator(g, x, p):
    return pow(g, x) % p

# this will be the inverser of the process 
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text



p = 97
g = 31
a = 88  # not needed in this equation this will be the opposite if u has been used
b = 26
v = generator(g, b, p)
key = generator(v, a, p)
cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

print(f"The key is: {key}") # key = 35 from debugging

cipher_text = ""
for char in cipher:
    cipher_text += chr(char // 311 // 35) # used chr because opposite of ord and 35 for key
print(f"Cipher text: {cipher_text}")

plaintext = dynamic_xor_encrypt(cipher_text, "aedurtu")
print(f"Plaintext: {plaintext}")