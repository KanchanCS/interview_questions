# Question 5: File Encryption and Decryption Write a Python program to encrypt and decrypt
# a text file using a simple encryption algorithm. The program should take a text file as input,
# encrypt it, save the encrypted data to another file, and then be able to decrypt the encrypted file back to the original text.

# Example:

# Input (plaintext file): "sample.txt"
# Output (encrypted file): "sample_encrypted.txt"

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        text = file.read()
    encrypted_text = encrypt(text, key)
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
    decrypted_text = decrypt(encrypted_text, key)
    with open(output_file, 'w') as file:
        file.write(decrypted_text)

# Example usage
input_file = "sample.txt"
encrypted_file = "sample_encrypted.txt"
decrypted_file = "sample_decrypted.txt"
key = 3  # Shift key for encryption

# Encrypt the file
encrypt_file(input_file, encrypted_file, key)
print(f"File '{input_file}' encrypted and saved as '{encrypted_file}'")

# Decrypt the encrypted file
# decrypt_file(encrypted_file, decrypted_file, key)
# print(f"File '{encrypted_file}' decrypted and saved as '{decrypted_file}'")
