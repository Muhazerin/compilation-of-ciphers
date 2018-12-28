import json, random

try:
    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)

except OSError:
    with open("secretKey.json", 'w') as secretKeyFile:
        #plaintext key
        plaintextKey = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ,, _, -,  "
        tempList = plaintextKey.split(", ")
        tempKeyStr = '"' + '", "'.join(tempList) + '"'
        
        #cipher key
        random.shuffle(tempList)
        cipherKey = tempList   #create a cipher key by shuffling plaintext key
        cipherKeyStr = '"' + '", "'.join(cipherKey) + '"'
        key = "{\n\t\"plaintextKey\": [" + tempKeyStr+ "],\n\t\"cipherKey\": [" + cipherKeyStr + "]\n}"
        secretKeyFile.write(key)                                             

    with open("secretKey.json", "r") as secretKeyFile:
        keys = json.load(secretKeyFile)                                      

def encode(data, key=keys):
    print("encoding\n")

    es = ""

    for c in data:      #iterate each char in the string
    i = key["plaintextKey"].index(c)
        es = es + key["cipherKey"][i]

    return es

def decode(data, key=keys):
    print("decoding\n")

    ds = ""

    for c in data:      #iterate each char in the string
        i = key["cipherKey"].index(c)
        ds = ds + key["plaintextKey"][i]

    return ds
