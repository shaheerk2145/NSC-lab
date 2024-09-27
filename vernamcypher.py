def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = chr((ord(plaintext[i]) + ord(key[i])) % 26 + 65)
        ciphertext += char
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = chr((ord(ciphertext[i]) - ord(key[i])) % 26 + 65)
        plaintext += char
    return plaintext

# Example usage
plaintext = "shaheer"
key = "wqasbxz"
encrypted_text = vernam_encrypt(plaintext, key)
decrypted_text = vernam_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
