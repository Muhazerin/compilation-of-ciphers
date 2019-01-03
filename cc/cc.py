import json, secrets                                                         
try:
    # if file exist, load and use the key
    with open("secretKey.json", "r") as secretKeyFile:
        key = json.load(secretKeyFile)

except OSError:
    # if the file does not exist,
    # create the key and write to the file
    # then, load the key from the file
    nkey = 0
    while nkey <= 0:
        nkey = secrets.randbelow(25)

    i = 33
    plainTextList = []
    while i < 127:
        if i == 34:
            plainTextList.append("\\\"")
        elif i == 92:
            plainTextList.append("\\\\")
        else:
            plainTextList.append(chr(i))
        i += 1
    plainTextList.append(" ")
    
    cipherTextList = []
    for c in plainTextList:
        cipherTextList.append(c)
    
    i = 0
    while i < nkey:
        cipherTextList.append(cipherTextList.pop(0))
        i += 1

    plainTextStr = '"' + '", "'.join(plainTextList) + '"'
    cipherTextStr = '"' + '", "'.join(cipherTextList) + '"'
    jsonKey = '{\n\t"key": "' + str(nkey) + '",\n\t"plainTextList": ['+plainTextStr+'],\n\t"cipherTextList": ['+cipherTextStr+']\n}'                      
    with open("secretKey.json", "w") as secretKeyFile:
        secretKeyFile.write(jsonKey)

    with open("secretKey.json", "r") as secretKeyFile:
        key = json.load(secretKeyFile)

# iterate every char in the plaintext
# and encrypt it
def encrypt(plaintext):
    es = ""
    for c in plaintext:
        es += key["cipherTextList"][key["plainTextList"].index(c)]

    return es

# iterate every char in the ciphertext
# and decrypt it
def decrypt(ciphertext):
    ds = ""
    for c in ciphertext:
        ds += key["plainTextList"][key["cipherTextList"].index(c)]

    return ds
