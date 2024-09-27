# def prepare_input(text):
#     # Convert the text to uppercase
#     text = text.upper()
#     # Replace 'J' with 'I' in the text
#     text = text.replace("J", "I")
#     # Remove any non-alphabetic characters from the text
#     text = ''.join(filter(str.isalpha, text))
#     return text

# def generate_key_matrix(key):
#     # Convert the key to uppercase
#     key = key.upper()
#     # Remove any duplicates from the key
#     key = "".join(dict.fromkeys(key))
#     # Replace 'J' with 'I' in the key
#     key = key.replace("J", "I")
#     # Create the key matrix (5x5) with the key
#     key_matrix = []
#     for char in key:
#         if char not in key_matrix and char != " ":
#             key_matrix.append(char)
#     # Fill the remaining cells with the alphabet
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
#     for char in alphabet:
#         if char not in key_matrix:
#             key_matrix.append(char)
#     # Reshape the list into a 5x5 matrix
#     key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
#     return key_matrix

# def find_position(matrix, char):
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == char:
#                 return i, j

# def encrypt_playfair(plaintext, key):
#     plaintext = prepare_input(plaintext)
#     key_matrix = generate_key_matrix(key)
#     ciphertext = ""
#     for i in range(0, len(plaintext), 2):
#         char1 = plaintext[i]
#         char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
#         row1, col1 = find_position(key_matrix, char1)
#         row2, col2 = find_position(key_matrix, char2)
#         if row1 == row2:
#             ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
#         elif col1 == col2:
#             ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
#         else:
#             ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
#     return ciphertext

# def decrypt_playfair(ciphertext, key):
#     key_matrix = generate_key_matrix(key)
#     plaintext = ""
#     for i in range(0, len(ciphertext), 2):
#         char1 = ciphertext[i]
#         char2 = ciphertext[i + 1]
#         row1, col1 = find_position(key_matrix, char1)
#         row2, col2 = find_position(key_matrix, char2)
#         if row1 == row2:
#             plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
#         elif col1 == col2:
#             plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
#         else:
#             plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
#     return plaintext

# # Example usage
# plaintext = "HELLO"
# key = "KEYWORD"
# encrypted_text = encrypt_playfair(plaintext, key)
# decrypted_text = decrypt_playfair(encrypted_text, key)

# print("Plaintext:", plaintext)
# print("Key:", key)
# print("Encrypted text:", encrypted_text)
# print("Decrypted text:", decrypted_text)




def generate_playfair_matrix(key):
    key = key.replace("J", "I")
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(dict.fromkeys(key))
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    print("Playfair Matrix:")
    for row in matrix:
        print(row)
    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    print("Processed Plaintext:", plaintext)
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        print("Pair:", pair)
        try:
            row1, col1 = next((i, row.index(pair[0])) for i, row in enumerate(matrix) if pair[0] in row)
            row2, col2 = next((i, row.index(pair[1])) for i, row in enumerate(matrix) if pair[1] in row)
            print("Indices:", (row1, col1), (row2, col2))
        except ValueError as e:
            print("Error:", e)
            continue
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        try:
            row1, col1 = next((i, row.index(pair[0])) for i, row in enumerate(matrix) if pair[0] in row)
            row2, col2 = next((i, row.index(pair[1])) for i, row in enumerate(matrix) if pair[1] in row)
        except ValueError as e:
            print("Error:", e)
            continue
        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

# Example usage
plaintext = "HELLO WORLD"
key = "KEYWORD"
print("Plaintext:", plaintext)
print("Key:", key)
encrypted_text = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)


# This code should correctly encrypt and decrypt the plaintext "HELLO WORLD" using the Playfair Cipher with the key "KEYWORD". Let me know if you encounter any issues!