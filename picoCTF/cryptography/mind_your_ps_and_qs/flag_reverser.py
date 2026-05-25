flag = " }19ea7cd1_do0g_0n_N_11ams{FTCocip"

# Technique 1
reversed_flag = "".join(reversed(flag))
print(reversed_flag)

# Technique 2
rev_flag = ""
for i in range(1,len(flag)):
    rev_flag += flag[-i]

print(rev_flag)