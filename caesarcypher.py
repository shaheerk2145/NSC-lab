def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            result += char

    return result

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Example usage:
plaintext = input("enter the plaintext:")
shift = int(input("enter the number for letter to be shifted:"))
# plaintext = "shaheer"
# shift = 3

# Encrypt the plaintext
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)


"""

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if encrypt else chr((ord(char) - 65 - shift) % 26 + 65)
            result += shifted_char
        # Encrypt lowercase characters
        elif char.islower():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) if encrypt else chr((ord(char) - 97 - shift) % 26 + 97)
            result += shifted_char
        # Non-alphabetic characters remain unchanged
        else:
            result += char
    return result

# Function to detect if the input text is encrypted or decrypted
def detect_input_type(text):
    if all(char.isalpha() for char in text):
        if text.isupper():
            return "encrypted"
        elif text.islower():
            return "decrypted"
    return "mixed"

# Main function
def main():
    user_input = input("Enter text: ").strip()
    input_type = detect_input_type(user_input)

    if input_type == "mixed":
        print("Invalid input: Please provide either fully encrypted or fully decrypted text.")
        return

    if input_type == "encrypted":
        shift = int(input("Enter the shift value used for encryption: "))
        decrypted_text = caesar_cipher(user_input, shift, encrypt=False)
        print("Decrypted text:", decrypted_text)
    else:
        shift = int(input("Enter the shift value for encryption: "))
        encrypted_text = caesar_cipher(user_input, shift, encrypt=True)
        print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
"""