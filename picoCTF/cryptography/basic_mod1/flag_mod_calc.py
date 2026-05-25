mapping_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
message = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"
listed_message = message.split(" ")
flag = ""

for i in listed_message:
    val = int(i)
    new_val = val % 37
    flag += mapping_list[new_val]

print("picoCTF{"+ flag + "}")