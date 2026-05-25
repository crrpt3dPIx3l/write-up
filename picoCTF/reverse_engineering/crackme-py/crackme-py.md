# Crackme-py
## Description
(crackme-gen.py)[https://challenge-files.picoctf.net/c_wily_courier/54afa7be1292e2d89dd7d1b6d0f5a6cede18c17055d3e46682128dc8715b93b3/crackme_gen.py]

### Hints
none

## Solution
Starting by downloading the python file and examining the content;
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`>0c0Abc?FE0g`_47fgaagg6ffN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)



def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program

    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )



choose_greatest()
```
By reading the code qucikly I saw a decode function and a secret and the combination of those 2 will print out the flag
`decode_secret(bezos_cc_secret)` and the flag is `picoCTF{1m_4_p34nut_810cf782288e77}`

PWNED!