c = "apijaczhzgtfnyjgrdvqrjbmcurcmjczsvbwgdelvxxxjkyigy"
p = ['' for _ in c]

for i in range(3):
    for j in range(len(c)):
        v7 = (85 & (j % 255)) + (85 & ((j % 255) >> 1))
        v6 = (v7 & 51) + (51 & (v7 >> 2))
        x = (ord(c[j]) - 97) % 26
        y = (x - ((v6 & 15) + (15 & (v6 >> 4)))) % 26
        p[j] = chr(y + 97)

    c = ''.join(p)

print(c)