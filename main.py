
from modules.management import *

print("User Management")
print("Version 1.0")
print("FB")
print("----------------------------------------")

while True:
    option = show_menu()

    match option:
        case "1":
            get_user()
        case "2":
            login_check()
        case "3":
            show_result()
        case "4":
            break
        case _:
            print("Error : Invalid option")

    print("----------------------------------------")