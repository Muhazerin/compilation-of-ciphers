import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    # plaintext key
    i = 32
    secretKey = {}
    cipherKey = []
    plaintextKey = []
    while i < 127:
        if i == 34:
            cipherKey.append("\"")
            plaintextKey.append("\"")
        elif i == 92:
            cipherKey.append("\\")
            plaintextKey.append("\\")
        else:
            cipherKey.append(chr(i))
            plaintextKey.append(chr(i))
        i += 1

    secretKey['plaintextKey'] = plaintextKey
    random.shuffle(cipherKey)
    secretKey['cipherKey'] = cipherKey                                       
    with open('secretKey.json','w') as secretKeyFile:
        json.dump(secretKey, secretKeyFile)

    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

def encode(data):
    print("encoding\n")

    es = ""

    for c in data:      #iterate each char in the string
        i = keys["plaintextKey"].index(c)
        es = es + keys["cipherKey"][i]

    return es

def decode(data):
    print("decoding\n")

    ds = ""

    for c in data:      #iterate each char in the string
        i = keys["cipherKey"].index(c)
        ds = ds + keys["plaintextKey"][i]

    return ds

def newKey():
    cipherKey = keys['cipherKey']
    random.shuffle(cipherKey)
    keys['cipherKey'] = cipherKey

    with open('secretKey.json','w') as secretKeyFile:
        json.dump(keys, secretKeyFile)
