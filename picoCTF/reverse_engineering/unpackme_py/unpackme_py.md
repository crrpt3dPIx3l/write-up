# Unpackme.py
## Description
Can you get the flag? Reverse engineer this Python program.

### Hints
none

## Solution
Starting by downlaoding the python file and examining the source code;
```
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

by reading the code and inserting `print(plain)` in the line 12, I was able to see what is the password and flag itself,
```
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_85f5d0ac}')\nelse:\n  print('That password is incorrect.')\n\n"
What's the password? batteryhorse
picoCTF{175_chr157m45_85f5d0ac}
```
PWNED!