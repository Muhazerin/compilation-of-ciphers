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

        cipherKey.reverse()     #create a 2nd cipher key by reversing the first cipher key

        cipherKey2 = []

        for c in cipherKey:

            cipherKey2.append(c)

        cipherKey.reverse()     #reverse back the first cipher key

        cipherKeyStr = '"' + '", "'.join(cipherKey) + '"'

        cipherKey2Str = '"' + '", "'.join(cipherKey2) + '"'

        key = "{\n\t\"plaintextKey\": [" + tempKeyStr+ "],\n\t\"cipherKey\": [" + cipherKeyStr + "],\n\t\"cipherKey2\": [" + cipherKey2Str + "]\n}"

        secretKeyFile.write(key)
        
    with open("secretKey.json", "r") as secretKeyFile:
        
        keys = json.load(secretKeyFile)
        
def encode(data, key=keys):

    print("encoding\n")

    es = ""

    count = 1

    for c in data:      #iterate each char in the string
    
    i = key["plaintextKey"].index(c)
    
    if count % 2 == 0:
    
        es = es + key["cipherKey"][i]

        else:

            es = es + key["cipherKey2"][i]

        count += 1

    return es                                                                

def decode(data, key=keys):

    print("decoding\n")

    ds = ""
    
    count = 1

    for c in data:      #iterate each char in the string

        if count % 2 == 0:

            i = key["cipherKey"].index(c)

        else:

            i = key["cipherKey2"].index(c)

        ds = ds + key["plaintextKey"][i]

        count += 1

    return ds
