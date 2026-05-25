mapping_list = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
message = "432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"
listed_message = message.split(" ")
flag = ""

for i in listed_message:
    val = pow(int(i), -1, 41)

    flag += mapping_list[val]

print("picoCTF{" + flag + "}")
