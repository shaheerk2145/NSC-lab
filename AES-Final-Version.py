import math
# AES S-box
S_BOX = [
    # 0    1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
    '63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76',  # 0
    'ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0',  # 1
    'b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15',  # 2
    '04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75',  # 3
    '09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84',  # 4
    '53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf',  # 5
    'd0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8',  # 6
    '51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2',  # 7
    'cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73',  # 8
    '60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db',  # 9
    'e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79',  # A
    'e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08',  # B
    'ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a',  # C
    '70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e',  # D
    'e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df',  # E
    '8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16'   # F
]

inv_S_BOX = [
    # 0    1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
    '52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb',  # 0
    '7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb',  # 1
    '54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e',  # 2
    '08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25',  # 3
    '72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92',  # 4
    '6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84',  # 5
    '90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06',  # 6
    'd0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b',  # 7
    '3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73',  # 8
    '96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e',  # 9
    '47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b',  # A
    'fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4',  # B
    '1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f',  # C
    '60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef',  # D
    'a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61',  # E
    '17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d'   # F
]

Rcon = [['01','00','00','00'],
        ['02','00','00','00'],
        ['04','00','00','00'],
        ['08','00','00','00'],
        ['10','00','00','00'],
        ['20','00','00','00'],
        ['40','00','00','00'],
        ['80','00','00','00'],
        ['1b','00','00','00'],
        ['36','00','00','00'],]


def ascii_to_hex(text):
    hex_values = []
    for char in text:
        hex_value = hex(ord(char))[2:]  # Remove '0x' prefix
        hex_values.append(hex_value)
    return hex_values

def hex_to_ascii(hex_list):
    # Convert hexadecimal strings to integers
    int_list = [int(x, 16) for x in hex_list]
    # Convert integers to ASCII characters
    ascii_text = ''.join([chr(x) for x in int_list])
    return ascii_text

def fill_state_matrix(hex_values):
    state_matrix = [['00' for _ in range(4)] for _ in range(4)]
    index = 0
    for i in range(4):
        for j in range(4):
            if index < len(hex_values):
                state_matrix[j][i] = hex_values[index]
                index += 1
            else:
                pass
    return state_matrix


def circular_left_shift(arr, n):
    n = n % len(arr)  # Ensure n is within the range of array length
    return arr[n:] + arr[:n]

def circular_right_shift(arr, n):
    n = n % len(arr)  # Ensure n is within the range of array length
    return arr[len(arr)-n:] + arr[:len(arr)-n]

def byte_substitution_array(array):
    for i in range(4):
        hex_value = array[i]
        row = int(hex_value[0], 16)
        col = int(hex_value[1], 16)
        array[i] = S_BOX[row * 16 + col]
    return array

def xorTwoArrays(array, constant):
    result = ['{:02x}'.format(int(a, 16) ^ int(b, 16)) for a, b in zip(array, constant)]
    return result

def convertFrom2DTo1D(array):
    arr = [element for i in array for element in i]
    return arr

def stateMatrixToHexList(stateMatrix):
    arr = []
    for i in range(4):
        for j in range(4):
            arr.append(stateMatrix[j][i]) 
    return arr   

def generate_round_keys(hex_value,round_number):
    stage_matrix = fill_state_matrix(hex_value)
    # 1 byte circular left shift for w[3]
    g_matrix = circular_left_shift(stage_matrix[3],1)
    # byte substitution of w[3]
    g_matrix = byte_substitution_array(g_matrix)
    # adding round constant in w[3]
    g_matrix = xorTwoArrays(g_matrix,Rcon[round_number])
    # The next step is
    # w[4]=w[3]⊕w[0]
    stage_matrix[0] = xorTwoArrays(stage_matrix[0],g_matrix)
    # w[5]=w[4]⊕w[1]
    # w[6]=w[5]⊕w[2]
    # w[7]=w[6]⊕w[3]
    j = 0   
    for i in range(3):
        stage_matrix[j+1] = xorTwoArrays(stage_matrix[j],stage_matrix[j+1])
        j+=1
    #convert state matrix to 1 dimensional array and return it
    roundKey = convertFrom2DTo1D(stage_matrix)
    return roundKey
        
def addRoundKey(stateMatrix1,stateMatrix2):
    for i in range(4):
        stateMatrix1[i] = xorTwoArrays(stateMatrix1[i],stateMatrix2[i])
    return stateMatrix1    

def substitute_bytes(state_matrix):
    for i in range(4):
        for j in range(4):
            hex_value = state_matrix[i][j]
            row = int(hex_value[0], 16)
            col = int(hex_value[1], 16)
            state_matrix[i][j] = S_BOX[row * 16 + col]
    return state_matrix
def inverseSubstitute_bytes(state_matrix):
    for i in range(4):
        for j in range(4):
            hex_value = state_matrix[i][j]
            row = int(hex_value[0], 16)
            col = int(hex_value[1], 16)
            state_matrix[i][j] = inv_S_BOX[row * 16 + col]
    return state_matrix
def shiftRows(state_matrix):
    for i in range(1,4):
        state_matrix[i] = circular_left_shift(state_matrix[i],i)
    return state_matrix
def inverseShiftRows(state_matrix):
    for i in range(1,4):
        state_matrix[i] = circular_right_shift(state_matrix[i],i)
    return state_matrix

def multiply_GF(x, y):
    result = 0
    while y:
        if y & 1:
            result ^= x
        if x & 0x80:
            x = (x << 1) ^ 0x11b  # XOR with AES polynomial
        else:
            x <<= 1
        y >>= 1
    return result
def mix_columns(state_matrix):
    # Convert hexadecimal strings to integers
    state_matrix = [[int(x, 16) for x in row] for row in state_matrix]
    mix_columns_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    mixed_state = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mixed_state[i][j] = (
                multiply_GF(state_matrix[0][j], mix_columns_matrix[i][0]) ^
                multiply_GF(state_matrix[1][j], mix_columns_matrix[i][1]) ^
                multiply_GF(state_matrix[2][j], mix_columns_matrix[i][2]) ^
                multiply_GF(state_matrix[3][j], mix_columns_matrix[i][3])
            )
    # Convert integers back to hexadecimal strings for printing
    mixed_state_hex = [['{:02x}'.format(x) for x in row] for row in mixed_state]
    return mixed_state_hex
def inverseMixColumns(state_matrix):
    # Create an empty matrix to store the result
    result_matrix = [['00'] * 4 for _ in range(4)]
    # convert state_matrix into a list of integers
    state_matrix = [[int(x, 16) for x in row] for row in state_matrix]
    # Create the pre defined inverse MixColumns matrix
    inv_mix_columns_matrix = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
    ]
    # Perform multiplication of each column with the inverse MixColumns matrix
    for col in range(4):
        for row in range(4):
            # Perform multiplication in GF(2^8)
            result = 0
            for i in range(4):
                result ^= multiply_GF(state_matrix[i][col], inv_mix_columns_matrix[row][i])
            # Store the result in the result matrix
            result_matrix[row][col] = '{:02x}'.format(result)
    
    return result_matrix
def encryption(plaintext_state_matrix,round_keys):
    # Encrpytion 
    #round 0 working
    key_state_matrix = fill_state_matrix(round_keys[0])    
    stateMatrix = addRoundKey(key_state_matrix,plaintext_state_matrix)
    
    #round 1 to 9 working
    for i in range(9):
        key_state_matrix = fill_state_matrix(round_keys[i+1])
        stateMatrix = substitute_bytes(stateMatrix)
        stateMatrix = shiftRows(stateMatrix)
        stateMatrix = mix_columns(stateMatrix)
        stateMatrix = addRoundKey(key_state_matrix,stateMatrix)

    #round 10 working
    key_state_matrix = fill_state_matrix(round_keys[10])
    stateMatrix = substitute_bytes(stateMatrix)
    stateMatrix = shiftRows(stateMatrix)
    stateMatrix = addRoundKey(key_state_matrix,stateMatrix)
    
    # converting stateMatrix to hexadecimal representation
    cipherText = stateMatrixToHexList(stateMatrix)
    
    # converting hexadecimal list back to ascii representation
    cipherText = hex_to_ascii(cipherText)
    
    return cipherText

def decryption(cipher_state_matrix,round_keys):
    # round 0 working
    key_state_matrix = fill_state_matrix(round_keys[10]) 
    decryptMatrix = addRoundKey(key_state_matrix,cipher_state_matrix)
    
    #round 1 to 9 working
    for i in range(9,0,-1):
        key_state_matrix1 = fill_state_matrix(round_keys[i])
        decryptMatrix = inverseShiftRows(decryptMatrix)
        decryptMatrix = inverseSubstitute_bytes(decryptMatrix)
        decryptMatrix = addRoundKey(key_state_matrix1, decryptMatrix)
        decryptMatrix = inverseMixColumns(decryptMatrix)


    #round 10 working
    key_state_matrix1 = fill_state_matrix(round_keys[0])
    decryptMatrix = inverseShiftRows(decryptMatrix)
    decryptMatrix = inverseSubstitute_bytes(decryptMatrix)
    decryptMatrix = addRoundKey(key_state_matrix1, decryptMatrix)
    
    
    # converting stateMatrix to hexadecimal representation
    decryptedText = stateMatrixToHexList(decryptMatrix)
    
    # converting hexadecimal list back to ascii representation
    decryptedText = hex_to_ascii(decryptedText)
    
    return decryptedText
    
def keyExpansion(key):
    round_keys = []
    round_key = ascii_to_hex(key)
    round_keys.append(round_key)
    for i in range(10):
        round_key = generate_round_keys(round_key,i) # function at line no 133
        round_keys.append(round_key)
    return round_keys

def makeKeyAndTextEqual(plaintext,key):
    if len(key) < len(plaintext):
        key = key * math.ceil(len(plaintext)/len(key))
        if len(key) > len(plaintext):
            key = key[0:len(plaintext)]
    elif len(key) > len(plaintext):
        key = key[0:len(plaintext)]
    return key,plaintext

def main():
    # plain text and key input
    plaintext = input("Enter The Plain Text to encrypt :")
    key = input("Enter The Key required for encryption :")

    # if len(key) != len(plaintext) duplicate the key to make length equal
    key,plaintext = makeKeyAndTextEqual(plaintext,key)

    # ENCRYPTION

    plaintext_hex = ascii_to_hex(plaintext)
    completeCipherText = ""
    no_of_state_matrix = math.ceil(len(plaintext)/16)
    for i in range(no_of_state_matrix):
        plaintext_state_matrix = fill_state_matrix(plaintext_hex[i*16:(i+1)*16])
        round_keys = keyExpansion(key[i*16:(i+1)*16])
        cipherText = encryption(plaintext_state_matrix,round_keys)
        completeCipherText+=cipherText
    print("\nThe Cipher text is ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(completeCipherText)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    #DECRYPTION
    
    cipher_text_hex = ascii_to_hex(completeCipherText)
    completeDecryptedText = ""
    for i in range(no_of_state_matrix):
        cipher_state_matrix = fill_state_matrix(cipher_text_hex[i*16:(i+1)*16])
        round_keys = keyExpansion(key[i*16:(i+1)*16])
        decryptedText = decryption(cipher_state_matrix,round_keys)
        completeDecryptedText+=decryptedText
    print("\nThe Decrypted text is ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(completeDecryptedText)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()