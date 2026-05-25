try:
    with open("flag",'r') as f:
        content = f.readlines()
except(Exception):
    print(Exception)


formatted_list = []
hex_flag = ""

for i in content:
    formatted_list.append(i.strip().split(','))

for i in formatted_list:
    try:
        hex_flag += (i[1].replace('0x',''))
    except(IndexError): # The error is formed because of the last index not having a value
        print("The indexing is done\n")
        continue

flag = bytes.fromhex(hex_flag).decode('utf-8')
print(flag)