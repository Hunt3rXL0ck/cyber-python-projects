# TODO: Encrypt/decrypt files (lab only)
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    # TODO: Implement encryption
    pass

def decrypt_file(file_path, key):
    # TODO: Implement decryption
    pass

if __name__ == "__main__":
    key = Fernet.generate_key()
    print("Key:", key)
