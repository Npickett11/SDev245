# the purpose of this program is to show practical understadning of cryptographic concepts it shows how to create SHA256 hashes and perform Caesar cipher encryption and decryption. #
# Also includes a simple menu interface for user interaction. There are more comments than usual to expolain steps because I am trying to get better at leaving useful comments in code. as I am in the habit of not leaving any.

import hashlib

#creates a SHA256 hash for a string
def sha256_string(text: str):
    sha = hashlib.sha256()
    sha.update(text.encode("utf-8")) #converts string to bytes
    return sha.hexdigest() # returns the hash in hexadecimal format

#creates a SHA256 hash for a file
def sha256_file(path: str):
    sha = hashlib.sha256() # create sha256 hash object
    with open(path, "rb") as f: # open file in binary mode
        for chunk in iter(lambda: f.read(4096), b""): # read file in 4069-byte chunks
            sha.update(chunk)
    return sha.hexdigest() # return the hash in hexadecimal format

# Caesar cipher encryption
def caesar_encrypt(text: str, shift: int):
    result = "" # to store the encrypted text
    for char in text: # iterate through each character
        if char.isalpha(): # check if character is a letter
            base = ord('A') if char.isupper() else ord('a') # determine base ASCII value
            result += chr((ord(char) - base + shift) % 26 + base) # shift character and wrap around alphabet
        else:
            result += char  # non-alphabetic characters are added unchanged
    return result

def caesar_decrypt(text: str, shift: int):
    return caesar_encrypt(text, -shift) # decryption is just encryption with negative shift

# provides a simple menu interface
def main():
    while True: # main loop for menu
        print("Cryptography Output")
        print("1. SHA-256 hash a string")
        print("2. SHA-256 hash a file")
        print("3. Caesar cipher encrypt text")
        print("4. Caesar cipher decrypt text")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            text = input("Enter text: ")
            print("SHA-256 Hash:", sha256_string(text))

        elif choice == "2":
            path = input("Enter file path: ")
            try:
                print("SHA-256 Hash:", sha256_file(path))
            except FileNotFoundError:
                print("Error: File not found.")

        elif choice == "3":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted text:", caesar_encrypt(text, shift))

        elif choice == "4":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted text:", caesar_decrypt(text, shift))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()