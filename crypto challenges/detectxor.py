from xor import hex_xor
from hex2base64 import hex_to_ascii
ciphertext='0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'
ctext=hex_to_ascii(ciphertext)
k1=6^3
k1=hex(k1)[2:]
k2=15^7
k2=hex(k2)[2:]
k=k1+k2
key=''
for i in range(int(len(ciphertext)/2)):
    key=key+k
print('the key is',key)
plaintext=hex_xor(ciphertext,key)
print(plaintext)