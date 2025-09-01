# TODO: Implement password strength checker
import re

def check_password_strength(password):
    if len(password) < 8:
        print("Weak: Less than 8 characters")
    # TODO: Add other checks
    pass

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)
