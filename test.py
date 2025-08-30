my_list = [{ "user name" : "alireza", "nickname" : "aliali", "status": True},
           { "user name" : "mohseni", "nickname" : "mohsen", "status": False}]

print(type(my_list))
for user in my_list:
    print(user["user name"])