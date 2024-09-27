import math

def columnar_transposition_encrypt(plaintext, key):
    
    key = ''.join(filter(str.isalpha, key.upper()))
    
    columns = len(key)
    
    rows = math.ceil(len(plaintext) / columns)
    
    plaintext += ' ' * (rows * columns - len(plaintext))
    
    matrix = [list(plaintext[i:i+columns]) for i in range(0, len(plaintext), columns)]
    
    column_order = {char: i for i, char in enumerate(key)}
    
    sorted_columns = sorted(column_order, key=column_order.get)
    
    ciphertext = ''.join(''.join(matrix[row][column_order[char]] for char in sorted_columns) for row in range(rows))
    return ciphertext

def columnar_transposition_decrypt(ciphertext, key):
    key = ''.join(filter(str.isalpha, key.upper()))
    
    columns = len(key)
    rows = math.ceil(len(ciphertext) / columns)
    
    column_order = {char: i for i, char in enumerate(key)}
    
    sorted_columns = sorted(column_order, key=column_order.get)
    
    last_column_length = len(ciphertext) % columns
    
    matrix = [[''] * columns for _ in range(rows)]
    index = 0
    
    for col in sorted_columns:
        col_index = column_order[col]
        for row in range(rows):
            if row < rows - 1 or col_index < last_column_length:
                matrix[row][col_index] = ciphertext[index]
                index += 1
    
    
    plaintext = ''.join(''.join(matrix[row]) for row in range(rows))
    return plaintext

# Example usage
plaintext = "ZIA ALI"
key = "FAYYAZ"
print("Plaintext:", plaintext)
print("Key:", key)
encrypted_text = columnar_transposition_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = columnar_transposition_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
