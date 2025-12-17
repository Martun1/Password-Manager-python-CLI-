import json
import os
from cryptography.fernet import Fernet

key_file = "key.key"
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

cipher = Fernet(key)
data_file = "passwords.json"


if os.path.exists(data_file):
    with open(data_file, "r") as f:
        passwords = json.load(f)
else:
    passwords = {}

def save_data():
    with open(data_file, "w") as f:
        json.dump(passwords, f)

def add_password():
    account = input("Account name: ")
    pwd = input("Password: ")
    passwords[account] = cipher.encrypt(pwd.encode()).decode()
    save_data()
    print(f"Password for {account} saved.")

def view_passwords():
    for account, pwd in passwords.items():
        print(f"{account}: {cipher.decrypt(pwd.encode()).decode()}")

while True:
    print("\nOptions: add / view / quit")
    action = input("Choose: ").lower()
    if action == "add":
        add_password()
    elif action == "view":
        view_passwords()
    elif action == "quit":
        break
    else:
        print("Invalid choice.")
