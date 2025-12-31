# Level 3 - Task 2
# File Encryption and Decryption (Loop Based)
# Codveda Python Internship

from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)


def load_key():
    try:
        key = open(KEY_FILE, "rb").read()
        Fernet(key)  # validate key
        return key
    except Exception:
        print("⚠ Invalid or missing key. Generating a new key...")
        generate_key()
        return open(KEY_FILE, "rb").read()


def encrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")


def decrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")


def main():
    while True:
        print("\n===== File Encryption / Decryption =====")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            input_file = input("Enter file to encrypt: ")
            encrypt_file(input_file, "encrypted.txt")

        elif choice == "2":
            input_file = input("Enter file to decrypt: ")
            decrypt_file(input_file, "decrypted.txt")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

main()
