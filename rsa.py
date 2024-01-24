import random
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_coprime(phi)
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_coprime(phi):
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    n, d = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

if __name__ == "__main__":
    bits = 16  # You can adjust the number of bits for the key size

    # Generate key pair
    public_key, private_key = generate_keypair(bits)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Input message
    message = "Hello, RSA!"

    # Encrypt the message
    ciphertext = encrypt(message, public_key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the message
    decrypted_message = decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")
