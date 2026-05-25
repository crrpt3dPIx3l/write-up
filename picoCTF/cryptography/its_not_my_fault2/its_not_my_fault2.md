# Its not my fault 2 (Cryptography)
## Description
What do you mean RSA with CRT has an attack that's not a fault attack? Connect with nc wily-courier.picoctf.net port. not_my_fault_again.py

### Hints
none

## Solution
This challenge implements RSA using the Chinese Remainder Theorem (CRT) for faster decryption/signing, but one of the CRT private exponents (`d_p = d mod (p-1)`) is **very small** — at most **20 bits** (i.e., ≤ 1,048,576).

The server:
- Requires solving an MD5 proof-of-work
- Gives you the public modulus `N` and public exponent `e`
- Asks for `p + q` to get the flag

No ciphertext or signature is given — just `N` and `e`.  
The attack exploits the fact that `d_p` is tiny → we can brute-force it.

## The Non-Fault Attack on CRT-RSA with Small d_p

We use the following property:

For any message `m` (chosen randomly, 1 < m < N), if `dp` is the correct value:
m^(e * dp) ≡ m mod p     (because e * dp ≡ 1 mod (p-1))
→ m^(e * dp) - m ≡ 0 mod p
→ p divides (m^(e * dp) - m)
→ p divides gcd( m^(e * dp) - m , N )

```

When `dp` is wrong, the gcd is almost always 1.  
When correct → gcd = p (with very high probability).

This is a well-known attack on CRT-RSA with unbalanced / small exponents (not the famous Bellcore fault injection attack).

## Solution Steps

1. Connect to the remote server (usually `nc mercury.picoctf.net 26695` or similar port)
2. Solve the MD5 proof-of-work:  
   - Given prefix (e.g. "42761") and target suffix (e.g. "8dfce7")  
   - Find string = prefix + digits such that md5(string).hexdigest() ends with target  
   - Brute-force ~0–16M tries (usually finishes in seconds)

3. Receive `N` and `e`

4. Brute-force `dp` from 1 to ~1.1 million:

   python
   import math

   # Example values from your connection:
   n = 82945059216241553159103929776029372433296145024083151095493453019677937131860391296531646081114539579944832436523111836355872684717791948598182638393509129468984412488080911742401684025128085634651035100436682893953318273117318172472387585816624977976254922661076660267396788401013613363279444287851272557193
   e = 76434478442423153178067687501682239001398626476635874429782773028596750591414687879339392763109893948291766885167168320928175442137465813660869855564868188723828381674920230022541588163585963848462146400648892171667934137833337506945124846569299289458397105822747097989455279441158233199228727969896912253413

   m = n // 2 + 1          # large random-ish value < N works well

   for dp in range(1, 1 << 20):
       if dp % 50000 == 0:
           print(f"Progress: {dp:,}")

       powered = pow(m, e * dp, n)
       diff = (powered - m) % n
       g = math.gcd(diff, n)

       if 1 < g < n:
           print("Found!")
           print("dp =", dp)
           p = g
           q = n // g
           print("p =", p)
           print("q =", q)
           print("p + q =", p + q)
           break
```


Once you have p and q, compute p + q Send p + q to the server when prompted.
can't be solved due to my GPU powers as it needs more power and speed. But when running the code will be able to get the flag.