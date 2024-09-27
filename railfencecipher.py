def railfence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    ciphertext = ''.join(''.join(rail) for rail in fence)
    return ciphertext

def railfence_decrypt(ciphertext, rails):
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1
    
    rail = 0
    direction = 1
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += fence[rail][i]
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    return plaintext

# Example usage
plaintext = "HELLO WORLD"
rails = 3

# Encryption
encrypted_text = railfence_encrypt(plaintext, rails)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = railfence_decrypt(encrypted_text, rails)
print("Decrypted text:", decrypted_text)



def encryptRailFence(text, key):
    rail = [["\n" for i in range(len(text))] for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    return "".join(result)


def decryptRailFence(cipher, key):
    rail = [["\n" for i in range(len(cipher))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = "*"
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == "*") and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


if __name__ == "__main__":
    print("Input:")
    print(encryptRailFence("attack at once", 2))
    print("Cipher Text:")
    print(decryptRailFence("atc toctaka ne", 2))
