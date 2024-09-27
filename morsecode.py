# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Reverse Morse code dictionary
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def morse_encrypt(plaintext):
    ciphertext = ""
    for char in plaintext.upper():
        if char in morse_code_dict:
            ciphertext += morse_code_dict[char] + " "
    return ciphertext.strip()

def morse_decrypt(ciphertext):
    plaintext = ""
    for code in ciphertext.split():
        if code in reverse_morse_code_dict:
            plaintext += reverse_morse_code_dict[code]
    return plaintext

# Example usage
plaintext = "shaheer"
encrypted_text = morse_encrypt(plaintext)
decrypted_text = morse_decrypt(encrypted_text)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
