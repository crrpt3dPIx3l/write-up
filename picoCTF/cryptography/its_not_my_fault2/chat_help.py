'''import hashlib

prefix = "42761"
target = "8dfce7"

i = 0
while True:
    candidate = prefix + str(i)
    digest = hashlib.md5(candidate.encode()).hexdigest()
    if digest.endswith(target):
        print("Found it!")
        print("String to send:", candidate)
        print("MD5:", digest)
        break
    i += 1
    if i % 1000000 == 0:
        print(f"Tried {i} ... still searching")'''

import time
import math

n = 82945059216241553159103929776029372433296145024083151095493453019677937131860391296531646081114539579944832436523111836355872684717791948598182638393509129468984412488080911742401684025128085634651035100436682893953318273117318172472387585816624977976254922661076660267396788401013613363279444287851272557193
e = 76434478442423153178067687501682239001398626476635874429782773028596750591414687879339392763109893948291766885167168320928175442137465813660869855564868188723828381674920230022541588163585963848462146400648892171667934137833337506945124846569299289458397105822747097989455279441158233199228727969896912253413

m = n // 2          # good safe choice (large random-like number < n)
# m = 2**500        # also fine
# m = 12345678901234567890   # small also usually works

start = time.time()

for dp in range(1, 1 << 20):           # up to ~1 million
    if dp % 50000 == 0:
        print(f"Progress: {dp / 1048576:.2%}  |  time: {time.time()-start:.1f} s")

    # compute m^(e*dp) mod n
    powered = pow(m, e * dp, n)

    diff = (powered - m) % n            # make sure non-negative
    g = math.gcd(diff, n)

    if 1 < g < n:
        print("\nHIT!")
        print("dp candidate:", dp)
        print("factor:", g)
        p = g
        q = n // g
        print("p  =", p)
        print("q  =", q)
        print("p * q == n?", p * q == n)
        print("p + q =", p + q)
        # usually the server wants p + q
        break

print("Total time:", time.time() - start, "seconds")