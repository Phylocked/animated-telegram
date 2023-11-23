from xor import hex_xor
ciphertext='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
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