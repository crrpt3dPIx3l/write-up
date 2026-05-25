v3 = "617B2375F81EA7E1".lower()
v4_0 = "D269DF5B5AFC9DB9".lower()
v4_1 = "F467EDF4ED1BFED2".lower()

def to_LE(h):
    r = bytes.fromhex(h)[::-1].hex()
    return r

t = to_LE(v3)
s = to_LE(v4_0) + to_LE(v4_1)[2:]

full = bytes.fromhex((t+s))

print(full.hex())

a1 = []
v11 = 0
v10 = 0

for i in range(23):
    for j in range(8):
        if v10 == 0:
            v10 = 1
        v6 = 1 << (7 - j)
        v5 = 1 << (7 - v10)
        a1.append(str((v6 & full[i]) >> (7-j)))
        v10 += 1
        if (v10 == 8):
            v10 = 0
            v11 += 1
        if v11 == 27:
            break

a1 = a1 + ["0"] * (7 - (len(a1) % 7)) 
result = []

for i in range(0, len(a1), 7):
    result.append(int("".join(a1[i:i+7]), 2))

password = bytes(result)
print(password)