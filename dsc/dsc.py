import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    secretKey = {}
    i = 32
    plaintextKey = []
    cipherKey = []
    while i < 127:
        if i == 34:
            plaintextKey.append('\"')
            cipherKey.append('\"')
        elif i == 92:
            plaintextKey.append('\\')
            cipherKey.append('\\')
        else:
            plaintextKey.append(chr(i))
            cipherKey.append(chr(i))
        i += 1

    secretKey['plaintextKey'] = plaintextKey
    random.shuffle(cipherKey)
    secretKey['cipherKey'] = cipherKey
    cipherKey2 = []
    for i in cipherKey:
        cipherKey2.append(i)
    cipherKey2.reverse()
    secretKey['cipherKey2'] = cipherKey2
    
    with open('secretKey.json','w') as secretKeyFile:
        json.dump(secretKey, secretKeyFile)
        
    with open('secretKey.json','r') as secretKeyFile:
        keys = json.load(secretKeyFile)     #initialize keys to start using the cipher
def encrypt(data):
    es = ""
    count = 1

    for c in data:      #iterate each char in the string
        i = keys["plaintextKey"].index(c)
        if count % 2 == 0:
            es = es + keys["cipherKey"][i]
        else:
            es = es + keys["cipherKey2"][i]
        count += 1

    return es

def decrypt(data):
    ds = ""
    count = 1

    for c in data:      #iterate each char in the string
        if count % 2 == 0:
            i = keys["cipherKey"].index(c)
        else:
            i = keys["cipherKey2"].index(c)

        ds = ds + keys["plaintextKey"][i]
        count += 1

    return ds

def newKey():
    random.shuffle(keys['cipherKey'])
    cipherKey2 = []
    for i in keys['cipherKey']:
        cipherKey2.append(i)
    cipherKey2.reverse()
    keys['cipherKey2'] = cipherKey2
    with open('secretKey.json','w') as secretKeyFile:
        json.dump(keys, secretKeyFile)
