usernames_path = "./leak/usernames.txt"
passwords_path = "./leak/passwords.txt"
username = input("Enter the username for information:  ")
 

try:
    with open(usernames_path,"r") as f:
        usernames = f.read().split("\n")
except(Exception):
    print(Exception)
try:
    with open(passwords_path, "r") as p:
        passwords = p.read().split("\n")
except(Exception):
    print(Exception)


def find_password(user_index):
    for i in range(0, len(passwords)):
        if i == user_index:
            print(f"The password of the user is {passwords[i]}")
        else:
            continue

def find_user(name):
    for index, username in enumerate(usernames):
        if name == username:
            print(f"The username {username} is found with index {index}")
            find_password(index)
            break
        else:
            continue

find_user(username)