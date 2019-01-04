import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    with open("secretKey.json", 'w') as secretKeyFile:
        #plaintext key
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
        #cipher key
        random.shuffle(plaintextKey)    # create a cipher key by shuffling the plaintextKey
        cipherKeyStr = '"' + '", "'.join(plaintextKey) + '"'

        plaintextKey.reverse()     #create a 2nd cipher key by reversing the first cipher key
        cipherKey2Str = '"' + '", "'.join(plaintextKey) + '"'

        key = "{\n\t\"plaintextKey\": [" + plaintextKeyStr+ "],\n\t\"cipherKey\": [" + cipherKeyStr + "],\n\t\"cipherKey2\": [" + cipherKey2Str + "]\n}"
        secretKeyFile.write(key)

    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)     #initialize keys to start using the cipher

def encode(data):
    print("encoding\n")

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

def decode(data):
    print("decoding\n")

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
