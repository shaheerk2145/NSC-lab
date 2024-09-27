from pyDes import des, CBC, PAD_PKCS5
import binascii

def encrypt(key, data):
    des_obj = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    encrypted_data = des_obj.encrypt(data)
    return encrypted_data

def decrypt(key, encrypted_data):
    des_obj = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    decrypted_data = des_obj.decrypt(encrypted_data)
    return decrypted_data

# Example usage:
if __name__ == "__main__":
    # Key must be 8 bytes long (64 bits)
    key = b"abcdefgh"
    # Data to be encrypted
    data = b"Hello, World!"
    
    # Encryption
    encrypted_data = encrypt(key, data)
    print("Encrypted:", binascii.hexlify(encrypted_data))

    # Decryption
    decrypted_data = decrypt(key, encrypted_data)
    print("Decrypted:", decrypted_data.decode('utf-8'))
