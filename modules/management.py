
from re import match

user_list = []

def show_menu():
    print("1)Add User")
    print("2)Login Check")
    print("3)Show Users")
    print("4)Exit")
    option = input("Enter your choice: ")
    print("----------------------------------------")
    return option

def username_validator(username):
    if match(r"^[a-zA-Z][a-zA-Z._\d]{7,19}$", username):
        return True
    else:
        return False

def nickname_validator(nickname):
    if match(r"^[a-zA-Z][a-zA-Z._\d]{2,29}$", nickname):
        return True
    else:
        return False

def repeat_validator(username):
    for usr in user_list:
        if  username == usr["user name"]:
            return False
        else:
            return True

def get_user():
    username = input("Enter user name: ")
    password = input("Enter password: ")
    nickname = input("Enter nickname: ")
    status = input("Is user Active (Y/N)?")

    if status == "y" or status == "Y":
        status = True
    else:
        status = False

    if username_validator(username) and repeat_validator(username) and nickname_validator(nickname):
        user = {
            "user name": username,
            "password": password,
            "nickname": nickname,
            "status": status
        }
        user_list.append(user)
        print("Info : User added successfully!")
        return user
    else:
        print("Error : Invalid Data !!!")

def login_check():
    user_name = input("Enter user name: ")
    pass_word = input("Enter password: ")
    for usr in user_list:
        if user_name == usr["user name"] and pass_word == usr["password"] and usr["status"] == True:
            print("login OK!")
            break
        elif user_name == usr["user name"] and pass_word == usr["password"] and usr["status"] == False:
            print("Error: User Locked!")
            break
        else:
            print("Error: User Not Found")
            break

def show_result():
    for user in user_list:
        print(
            f"{user["user name"]:12}\t*****\t{user["nickname"]:>12} {user["status"]:>10}")
    print("----------------------------------------")

