import random

def public_key_private_key():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p-1) * (q-1)
    e= random.randrange(1,phi)
    while gcd(e,phi) != 1:
        e= random.randrange(1,phi)
        
    d = modular_inverse(e,phi)
    
    public_key =(e,n)
    private_key = (d,n)
    
    return public_key , private_key

def generate_prime_number():
    while True:
        num = random.randrange(2,100)
        if is_prime(num):
            return num
        
#     # Example usage:
# prime_number = generate_prime_number()
# print("Generated prime number:", prime_number)

def is_prime(num):
    if num <=1:
        return False
    if num <= 3 :
        return True
    if num % 2 == 0 or  num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i== 0 or num % (i+2) == 0:
            return False
        i += 6
    return True 
def gcd(a,b):
    while b!= 0:
        a,b = b,a%b 
    return a
def modular_inverse(a,m):
    m0 = m
    x0 = 0
    x1 = 1
    while a > 1:
        q = a // m
        m , a = a % m , m
        x0 ,x1 = x1 -q * x0,x0
    return x1 + m0 if x1 < 0 else x1
 
def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(encrypted_msg, private_key):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg


private_key ,public_key = public_key_private_key()
message = input("Enter the message to be encrypted :")
encrypted_message  = encrypt(message , public_key)
print("\n\nThe encoded message(encrypted by public key)\n")
print("Encrypted message " , encrypted_message)
print("\n\nThe decoded message(decrypted by public key)\n")
decrypted_message  = decrypt(encrypted_message , private_key)
print("Decrypted message " , decrypted_message)