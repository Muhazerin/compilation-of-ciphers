import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    with open("secretKey.json", 'w') as secretKeyFile:
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
        # cipher key
        random.shuffle(plaintextKey)    # create a cipher key by shuffling the plaintext key
        cipherKeyStr = '"' + '", "'.join(plaintextKey) + '"'
        key = "{\n\t\"plaintextKey\": [" + plaintextKeyStr + "],\n\t\"cipherKey\": [" + cipherKeyStr + "]\n}"

        secretKeyFile.write(key)
        with open("secretKey.json", "r") as secretKeyFile:
            keys = json.load(secretKeyFile)

def encode(data):
    es = ""

    for c in data:      #iterate each char in the string
        i = keys["plaintextKey"].index(c)
        es = es + keys["cipherKey"][i]

    return es

def decode(data):
    ds = ""

    for c in data:      #iterate each char in the string
        i = keys["cipherKey"].index(c)
        ds = ds + keys["plaintextKey"][i]

    return ds
