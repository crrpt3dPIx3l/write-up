import binascii

#constants
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e = 65537
p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477
r = (p-1) * (q-1)
d = pow(e, -1, r)

decoded_value = pow(c, d, n)
# Convert to bytes and decode as string (assuming the message is text)

plaintext_bytes = decoded_value.to_bytes((decoded_value.bit_length() + 7) // 8, 'big')
print(plaintext_bytes)
plaintext = plaintext_bytes.decode('utf-8', errors='ignore')

# The flag is reversed, so reverse it
flag = plaintext[::-1]
print(flag)