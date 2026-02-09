
# used to create the SHA-256 hash of the message
import hashlib

# used to generate random bytes for the AES key and nonce
import os

# used for AES encryption and decryption
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Takes data and turns it into a SHA-256 hash
def sha256_hash(data: bytes):
    return hashlib.sha256(data).digest()

#Creates a SHA-256 hash of the input
def main():
    # Gets user input and encodes it to bytes
    message = input("Enter a message: ").encode()

    # Hashes the message and prints the original hash
    original_hash = sha256_hash(message)
    print("Original SHA-256 hash:", original_hash.hex())

    # Generates AES key and nonce and creates AESGCM object
    key = AESGCM.generate_key(bit_length=128) # used to encrypt and decrypt the message
    aesgcm = AESGCM(key) # AES is the core encryption algorithm, GCM adds encryption and verification
    nonce = os.urandom(12) # number used once, it is a random value that ensures the same text will encrypt to different ciphertexts each time

    # Encrypts the message and prints the ciphertext
    ciphertext = aesgcm.encrypt(nonce, message, None)
    print("Encrypted data:", ciphertext.hex())

    # Decrypts the message and prints the decrypted message
    decrypted_message = aesgcm.decrypt(nonce, ciphertext, None)
    print("Decrypted message:", decrypted_message.decode())

    # Hashes decrypted message and prints the decrypted hash
    decrypted_hash = sha256_hash(decrypted_message) # creates a hash of the decrypted message to compare with the original hash for integrity verification
    print("Decrypted SHA-256 hash:", decrypted_hash.hex())

    # Verifies integrity and prints the result
    if original_hash == decrypted_hash:
        print("Integrity check: PASSED")
    else:
        print("Integrity check: FAILED")

# Run the main function
if __name__ == "__main__":
    main()
