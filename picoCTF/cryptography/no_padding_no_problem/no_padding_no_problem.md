# No Padding No Problem (Cryptography)
## Description
Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it?

Additional details will be available after launching your challenge instance.

### Hints
1. What can you do with a different pair of ciphertext and plaintext? What if it is not so different after all...

## Solution
So I started by reading the question and starting the instance and connected to the machine; I've got the following output:
```
Welcome to the Padding Oracle Challenge
This oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!


n: 136861750246254672310201418162596226621730697069921352970719480554043866492660084058606738620775441976711770392929655590114220156093918484038230225729537440614063161926151395636889825856538061872724699909275562057805425544052464435633704514433678329548878370280560745345733491224097681872779387397581928640997
e: 65537
ciphertext: 21343266783163833578554357343018346378464407698282271711048840879167301972862442266545236027857031312484426042473259805041871117828824558930291793958378982375748957112385608656625814767707526639507481099089310621952258182094993323008384472220442504642135330599572214614026837772413504546478885686308417717973


Give me ciphertext to decrypt: 
```

In this challenge the use of 'Homomorphic Encryption', Homomorphic encryption is a type of encryption that allows you to perform computations directly on encrypted data without decrypting it first. When you decrypt the result, you get the same answer as if you had performed the computation on the original plaintext, it usually implemented on untrusted computers to ensure that any unwanted operation won't take place. It is used in the challenge because the serveer doesn't decrypt the ciphrtext but anything else.

So to conclude the homomorphic process will be done again by changing the cipher text into something else with a key to be decrypted later, and the formula of the rsa encryption will be used:
for the ciphertext in the server: ***E(c<sub>1</sub>) = m<sub>1</sub><sup>e</sup> mod n***
for the key which will later restore the flag: ***E(c<sub>2</sub>) = m<sub>2</sub><sup>e</sup> mod n***

Those 2 formulas can be combined together to form a new one:
***E(c<sub>1</sub>) x E(c<sub>2</sub>) = (m<sub>1</sub><sup>e</sup> x  m<sub>2</sub><sup>e</sup>) mod n***
The product of cipher 1 and cipher 2 is the real cipher text encrypted with the key: 
***E(c) = (m<sub>1</sub><sup>e</sup> x  m<sub>2</sub><sup>e</sup>) mod n***

So now applying the concept in python script
```
n=108972254914023584177102380598715576907673914022222689991393300550072378539380371423243578370100819921198770920787803352105136574106883391635826500544696847339376432027356664144641930083693857417071399941060244965153225083001771842649228606865485220651442276463063256616662412564584513624516466990723729082729
e=65537
ciphertext = 46379725137191192141314114838314371858535871817077931449610472636675644929491250544761462107093758963978668380322888163266421694001433510350365707308142209473506343888790880677902805830922058456852191733852394573609874044806264603923723043341076699034300271332840621611037339305479168723464314968835274392594
#print(pow(6,e,n))
key = 3485175559739704366203712937659053082624034678070996373798890384661426784615481257756270696934376763447569774475558575007865293322198948378312777640460818513383872110554377282093624470951801492067427144272975841616607481808782410572815279287353606912833965824207507565624639501187780350386800612812224679973

data_to_decipher = ciphertext * key
#print(data_to_decipher)

flag_with_key = 445862446380825660631229365812412239467467390235563125898358354606136291098728487834607773241552770220110699460686572696326894
hex_flag = hex(flag_with_key // 6) # 6 is the key
hex_flag = str(hex_flag).replace("0x","")
flag = bytes.fromhex(str(hex_flag)).decode('utf-8')
print(flag)
```
output `picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_34eb7018}`

PWNED!