import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    # plaintext key
    i = 33
    plaintextKey = []
    while i < 127:
        if i == 34:
            plaintextKey.append("\\\"")
        elif i == 92:
            plaintextKey.append("\\\\")
        else:
            plaintextKey.append(chr(i))
        i += 1
    plaintextKey.append(" ")
    plaintextKeyStr = '"' + '", "'.join(plaintextKey) + '"'

    # cipherkey
    cipherKey = []
    for c in plaintextKey:
        cipherKey.append(c)
    random.shuffle(cipherKey)
    cipherKeyStr = '"' + '", "'.join(cipherKey) + '"'

    keyStr = '{\n\t"plaintextKey": [' + plaintextKeyStr + '],\n\t"cipherKey": [' + cipherKeyStr + ']\n}'

    with open("secretKey.json", "w") as secretKeyFile:
        secretKeyFile.write(keyStr)

    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

def encrypt(data):
    es = ""
    i = 0

    for c in data:
        if i > 94:
            i = 0
        indexToAdd = keys["plaintextKey"].index(keys["cipherKey"][i])
        newIndex = keys["plaintextKey"].index(c) + indexToAdd
        if newIndex > 94:
            newIndex -= 95
        es += keys["plaintextKey"][newIndex]
        i += 1

    return es
    
def decrypt(data):
    ds = ""
    i = 0

    for c in data:
        if i > 94:
            i = 0
        indexToSubtract = keys["plaintextKey"].index(keys["cipherKey"][i])
        newIndex = keys["plaintextKey"].index(c) - indexToSubtract
        if newIndex < 0:
            newIndex += 95
        ds += keys["plaintextKey"][newIndex]
        i += 1

    return ds
