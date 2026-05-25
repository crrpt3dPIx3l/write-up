message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
flag = ""

for i in range(0, len(message),3):
    flag += message[i+2] + message[i] + message[i+1]
    
    
print(flag)