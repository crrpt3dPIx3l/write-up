input = 39722847074734820757600524178581224432297292490103995908738058203639164185
output = input * 5
hex_value = hex(output).replace('0x','')
flag = bytes.fromhex(hex_value).decode('utf-8')
print(flag)