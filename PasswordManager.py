
# pip install cryptography
from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() # rstrip is use to remove the special character such as "\n". 
            user, passw = data.split("|")
            print(f"Username: {user}\nPassword: {fer.decrypt(passw.encode()).decode()}\n")

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(" Press 'A' to add a new password \n Press 'V' to view existing ones \n Press 'Q' to quit : ").lower()

    if mode == "q":
        break
    if mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid mode.")
        continue