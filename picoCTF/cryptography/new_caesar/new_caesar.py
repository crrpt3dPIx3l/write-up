import string

LOWERCASE_OFFSET = ord("a")	# 97 HTML number of the letter a
ALPHABET = string.ascii_lowercase[:16] # retrieve a-p list for cipher

def b16_encode(plain):	
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))	# format the first arguement and make it in the 8 bit format
		enc += ALPHABET[int(binary[:4], 2)]	# convert the first 4 bit to letters
		enc += ALPHABET[int(binary[4:], 2)]	# conver the last 4 bits to letters
	return enc	#return the whole encoding

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET	# Deduct the order of the first argument by 97
	t2 = ord(k) - LOWERCASE_OFFSET	# Do the same for k
	return ALPHABET[(t1 + t2) % len(ALPHABET)]	# Retrun the remaining of the division operation between the added t1 and t2 divided by the length of list a-p

flag = "redacted"	# the real value is "radacted"
key = "a"	# the real value is "radacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1	# This ensure that the key is only 1 letter 

'''The assert built in function or keyword here is used for checking the right condition passed into it and as I see
it will produce an error because in the line 21 the loop will check for r which is not in the list of ALPHABET 
and line 22 the key length is no 1 so another error modification is to be done'''

b16 = b16_encode(flag)	
enc = ""
for i, c in enumerate(b16):	# a loop for the index and content of the index
	enc += shift(c, key[i % len(key)])
print(enc)
