# The purpose of this program is to demonstrate basic encryption and decryption techniques. Using both symmetric and asymmetric encryption methods.
# The program will show how to encrypt and decrypt messages using - Symmetric encryption using a Caesar Cipher and Asymmetric encryption using a simplified RSA algorithm

#Symmetric Encryption (Caesar Cipher)
def symmetric_encrypt(message, key):
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) + key)
    return encrypted

def symmetric_decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        decrypted += chr(ord(char) - key)
    return decrypted


# Symmetric encryption input
sym_message = "HELLO WORLD" #--------------------------------------------------------------------------------------------------SYMMETRICAL MESSAGE CHANGE HERE FOR DIFFERENT OUTPUT--------------------------------------------------------------------------------------------------------

sym_key = 3

sym_encrypted = symmetric_encrypt(sym_message, sym_key)
sym_decrypted = symmetric_decrypt(sym_encrypted, sym_key)



#Asymmetric Encryption (Simplified RSA)

# Key qeneration
prime1 = 23
prime2 = 31
primeTotal = prime1 * prime2
help = (prime1 - 1) * (prime2 - 1)

# Public and private keys
publicKey = 7      
privateKey = 283     

def asymmetric_encrypt(message, publicKey, primeTotal):
    encrypted = []
    for char in message:
        encrypted.append(pow(ord(char), publicKey, primeTotal))
    return encrypted

def asymmetric_decrypt(ciphertext, privateKey, primeTotal):
    decrypted = ""
    for num in ciphertext:
        decrypted += chr(pow(num, privateKey, primeTotal))
    return decrypted


# Asymmetric encryption input
asym_message = "HELLO WORLD" #--------------------------------------------------------------------------------------------------ASYMMETRICAL MESSAGE CHANGE HERE FOR DIFFERENT OUTPUT--------------------------------------------------------------------------------------------------------

asym_encrypted = asymmetric_encrypt(asym_message, publicKey, primeTotal)
asym_decrypted = asymmetric_decrypt(asym_encrypted, privateKey, primeTotal)


#display results

print("SYMMETRIC ENCRYPTION")
print("Method: Caesar Cipher")
print("Key Used:", sym_key)
print("Input:", sym_message)
print("Encrypted Output:", sym_encrypted)
print("Decrypted Output:", sym_decrypted)

print("\nASYMMETRIC ENCRYPTION")
print("Method: Simplified RSA")
print("Public Key (publicKey, primeTotal):", (publicKey, primeTotal))
print("Private Key (privateKey, primeTotal):", (privateKey, primeTotal))
print("Input:", asym_message)
print("Encrypted Output:", asym_encrypted)
print("Decrypted Output:", asym_decrypted)
