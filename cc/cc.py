import json, secrets

try:
    # if file exist,load and use the key
    with open("secretKey.json", "r") as secretKeyFile:
        key = json.load(secretKeyFile)

except OSError:
    # if the file does not exist,
    # create the key and write to the file
    # then, load the key from the file
    nkey = 0
    while nkey <= 0:
        nkey = secrets.randbelow(94)

    i = 32
    plaintextKey = []
    cipherKey = []
    while i < 127:
        if i == 34:
            cipherKey.append('\"')
            plaintextKey.append("\"")
        elif i == 92:
            cipherKey.append('\\')
            plaintextKey.append("\\")
        else:
            cipherKey.append(chr(i))
            plaintextKey.append(chr(i))
        i += 1

    i = 0
    while i < nkey:
        cipherKey.append(cipherKey.pop(0))
        i += 1

    secretKey = {}
    secretKey['plaintextKey'] = plaintextKey
    secretKey['cipherKey'] = cipherKey

    with open("secretKey.json", "w") as secretKeyFile:
        json.dump(secretKey, secretKeyFile)

    with open("secretKey.json", "r") as secretKeyFile:
        key = json.load(secretKeyFile)

# iterate every char in the plaintext
# and encrypt it
def encrypt(plaintext):
    es = ""
    for c in plaintext:
        es += key["cipherKey"][key["plaintextKey"].index(c)]

    return es

# iterate every char in the ciphertext
# and decrypt it
def decrypt(ciphertext):
    ds = ""
    for c in ciphertext:
        ds += key["plaintextKey"][key["cipherKey"].index(c)]                 
    return ds

def newKey():
    cipherKey = []
    for c in key['plaintextKey']:
        cipherKey.append(c)
    nKey = 0
    while nKey == 0:
        nKey = secrets.randbelow(94)

    i = 0
    while i < nKey:
        cipherKey.append(cipherKey.pop(0))
        i += 1

    key['cipherKey'] = cipherKey

    with open('secretKey.json','w') as secretKeyFile:
        json.dump(key, secretKeyFile)
