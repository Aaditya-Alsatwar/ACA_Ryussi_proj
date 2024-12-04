import os
import json
import hashlib
import base64
from cryptography.fernet import Fernet
from getpass import getpass

# Function to generate a Fernet-compatible key from the master password
def generate_key(master_password):
    """Generate a 32-byte base64-encoded key from the master password"""
    password_hash = hashlib.sha256(master_password.encode()).digest()  # Get the hash of the master password
    key = base64.urlsafe_b64encode(password_hash)  # Base64 encode the hash to make it Fernet-compatible
    return key

# Function to encrypt passwords
def encrypt_password(password, master_password):
    """Encrypt a password using the master password"""
    key = generate_key(master_password)
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Function to decrypt passwords
def decrypt_password(encrypted_password, master_password):
    """Decrypt a password using the master password"""
    key = generate_key(master_password)
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to create or validate user (based on master password)
def create_or_validate_user():
    """Create or validate the user with a master password"""
    if not os.path.exists('password_manager.json'):
        # If the file does not exist, create the user
        print("Welcome! Let's set up your account.")
        master_password = getpass("Enter a master password: ")
        # Hash the master password for storage
        user_data = {"master_password_hash": hashlib.sha256(master_password.encode()).hexdigest()}
        with open('password_manager.json', 'w') as f:
            json.dump(user_data, f)
        print("Account created successfully!")
    else:
        # If the file exists, validate the master password
        with open('password_manager.json', 'r') as f:
            user_data = json.load(f)
        
        while True:
            master_password = getpass("Enter your master password: ")
            if hashlib.sha256(master_password.encode()).hexdigest() == user_data["master_password_hash"]:
                print("Password validated successfully!")
                break
            else:
                print("Invalid password, try again.")

# Function to add or update passwords in the password manager
def add_password(service_name, password, master_password):
    """Add or update a password for a service"""
    encrypted_password = encrypt_password(password, master_password)
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}

    passwords[service_name] = encrypted_password.decode()

    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

    print(f"Password for {service_name} saved successfully!")

# Function to retrieve passwords
def retrieve_password(service_name, master_password):
    """Retrieve a stored password for a service"""
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
        
        if service_name in passwords:
            encrypted_password = passwords[service_name].encode()
            decrypted_password = decrypt_password(encrypted_password, master_password)
            print(f"Password for {service_name}: {decrypted_password}")
        else:
            print(f"No password found for {service_name}")
    
    except FileNotFoundError:
        print("No passwords have been saved yet.")

# Main function to run the password manager
def main():
    create_or_validate_user()

    while True:
        print("\nPassword Manager:")
        print("1. Add or Update Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            service_name = input("Enter the service name (e.g., Gmail, Facebook): ")
            password = getpass("Enter the password: ")
            add_password(service_name, password, getpass("Enter your master password: "))
        elif choice == '2':
            service_name = input("Enter the service name to retrieve password: ")
            retrieve_password(service_name, getpass("Enter your master password: "))
        elif choice == '3':
            print("Exiting password manager. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
