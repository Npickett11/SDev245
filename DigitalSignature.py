#The purpose of this program is to demonstrate digital signatures using RSA asymmetric cryptography.
# It includes key generation, message signing, and signature verification.
# as with previous files there are more comments than usual to explain steps because I am trying to get better at leaving useful comments in code. as I am in the habit of not leaving any.

import cryptography  #may have to pip install cryptography in your environment/bash
from cryptography.hazmat.primitives.asymmetric import rsa, padding #for RSA key generation and padding
from cryptography.hazmat.primitives import hashes #for hashing algorithms
from cryptography.exceptions import InvalidSignature #for handling invalid signatures

# generate RSA public and private keys
def keys():
    private_key = rsa.generate_private_key( # generate RSA private key
        public_exponent=65537, # standard value for public exponent According to research this is the most commonly used value)
        key_size=2048 # key size in bits
    )
    public_key = private_key.public_key() #get public key from private key
    return private_key, public_key #return both keys

# sign a message with the private key
def message(private_key, message: bytes):
    signature = private_key.sign( #signs the message using the private key
        message,
        padding.PSS( #Padding for RSA signature
            mgf=padding.MGF1(hashes.SHA256()), #mask generation function using SHA256
            salt_length=padding.PSS.MAX_LENGTH #maximum salt length
        ),
        hashes.SHA256() #hashing algorithm used
    )
    return signature #return the generated signature

# verify the digital signature
def verify_signature(public_key, message: bytes, signature: bytes): #verify using public key
    try:
        public_key.verify( # verify the signature
            signature,
            message,
            padding.PSS( #Padding for RSA signature
                mgf=padding.MGF1(hashes.SHA256()), #mask generation function using SHA256
                salt_length=padding.PSS.MAX_LENGTH #maximum salt length
            ),
            hashes.SHA256() #hashing algorithm used
        )
        return True # if verification is successful
    except InvalidSignature: # if signature is invalid
        return False 

# demonstrate digital signature
def main():
    print("Digital Signature")

    private_key, public_key = keys()

    message = input("Enter message to sign: ").encode("utf-8")

    signature = message(private_key, message)
    print("\nMessage signed successfully.")

    print("\nVerifying signature...")
    valid = verify_signature(public_key, message, signature)

    if valid:
        print("Signature is VALID")
    else:
        print("Signature is INVALID")

    print("\nTampering test...")
    fake_message = b"tampered message"
    valid = verify_signature(public_key, fake_message, signature)

    print("Valid after tampering?", valid)

if __name__ == "__main__":
    main()
