
from Users import Users
from DataBase import Database
import time
import os
import re


def read_int(string, num):
    while True:
        buf_input = input(string)
        if re.findall(r'\D', buf_input) == [] and buf_input != "":
            if int(buf_input) <= num and int(buf_input) != 0:
                return int(buf_input)
                break
            else:
                print("Wrong input, try again")
                time.sleep(1)
                cls()
                continue
        else:
            print("Wrong input, try again")
            time.sleep(1)
            cls()
            continue


def read_index(string, num):
    while True:
        buf_input = input(string)
        if re.findall(r'\D', buf_input) == [] and buf_input != "":
            if int(buf_input) <= num:
                return int(buf_input)
                break
            else:
                print("Wrong input, try again")
                time.sleep(1)
                cls()
                continue
        else:
            print("Wrong input, try again")
            time.sleep(1)
            cls()
            continue


def cls():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text


print("===========init database ==========")
time.sleep(1)
db = Database()
# потонуло
# while True:
#     buf_input = input("1. Create new user\n2. Find user\n3. Show database\n4. Exit\n")
#     if re.findall(r'\D', buf_input) == [] and buf_input != "":
#
#         # 1. CREATE USER
#         if int(buf_input) == 1:
#             time.sleep(0.5)
#             cls()
#             print("New User Creating")
#             create_email = input("Input email\n")
#             create_name = input("Input name\n")
#             create_password = input("Input password\n")
#             create_phone = input("Input phone\n")
#             buf_user = Users(create_email, create_name, create_password, create_phone)
#             db.add_user(buf_user)
#             print("...... wait ....")
#             time.sleep(1)
#             cls()
#
#         # 2. FIND USER
#         elif int(buf_input) == 2:
#             time.sleep(0.1)
#             while True:
#                 buf_input = input("1. By index\n2. By email\n")
#                 if re.findall(r'\D', buf_input) == [] and buf_input != "":
#
#                     # 2.1 BY INDEX
#                     if int(buf_input) == 1:
#                         time.sleep(0.1)
#                         cls()
#                         while True:
#                             buf_input = input("Input Index\n")
#                             if re.findall(r'\D', buf_input) == [] and buf_input != "":
#                                 if int(buf_input) > len(db.user) - 1:
#                                     print("User not exist")
#                                     continue
#                                 print(db.find_user_by_index(int(buf_input)))
#                                 index = db.find_user_by_index(int(buf_input))[0]
#                                 # USER OPERATIONS
#                                 while True:
#                                     buf_input = input("1. Update user\n2. Delete user\n")
#                                     if re.findall(r'\D', buf_input) == [] and buf_input != "":
#                                         if int(buf_input) == 1:
#                                             time.sleep(0.1)
#                                         elif int(buf_input) == 2:
#                                             db.remove_user_by_index(index)
#                                             break
#                                         else:
#                                             print("Wrong input, try again")
#                                             time.sleep(1)
#                                             cls()
#                                             continue
#                                     else:
#                                         print("Wrong input, try again")
#                                         time.sleep(1)
#                                         cls()
#                                         continue
#
#                             else:
#                                 print("Wrong input, try again")
#                                 time.sleep(1)
#                                 cls()
#                                 continue
#                             break
#
#
#                     # 2.2 BY EMAIL
#                     elif int(buf_input) == 2:
#                         time.sleep(0.1)
#                     else:
#                         print("Wrong input, try again")
#                         time.sleep(1)
#                         cls()
#                         continue
#                 else:
#                     print("Wrong input, try again")
#                     time.sleep(1)
#                     cls()
#                     continue
#                 break
#
#
#         # 3. SHOW DB
#         elif int(buf_input) == 3:
#             db.show_database()
#
#         # 4. EXIT
#         elif int(buf_input) == 4:
#             break
#         else:
#             print("Wrong input, try again")
#             time.sleep(1)
#             cls()
#             continue
#     else:
#         print("Wrong input, try again")
#         time.sleep(1)
#         cls()
#         continue
#
# cls()
# time.sleep(1)
# print("=======database deleted=======")
# time.sleep(1)

while True:
    time.sleep(0.5)
    cls()
    read = read_int("1. Create new user\n2. Find user\n3. Show database\n4. Exit\n", 4)
    if read == 1:
        time.sleep(0.5)
        cls()
        print("New User Creating")
        create_email = input("Input email\n")
        create_name = input("Input name\n")
        create_password = input("Input password\n")
        create_phone = input("Input phone\n")
        buf_user = Users(create_email, create_name, create_password, create_phone)
        db.add_user(buf_user)
        print("...... wait ....")
        time.sleep(0.5)


    elif read == 2:
        if len(db.user) != 0:
            while True:
                cls()
                print("FIND USER")
                read = read_int("1. By index\n2. By email\n3. Back\n", 3)
                if read == 1:
                    while True:
                        time.sleep(0.5)
                        cls()
                        print("FIND USER BY INDEX")
                        read = read_index("Input Index\n", len(db.user) - 1)
                        print(db.find_user_by_index(int(read)))
                        index = db.find_user_by_index(int(read))[0]
                        while True:
                            read = read_int("1. Update user\n2. Delete user\n3. Back\n", 3)
                            if read == 1:
                                time.sleep(0.5)
                                cls()
                                print(db.find_user_by_index(int(index)))
                                print("UPDATE USER")
                                edit_name = input("Input name\n")
                                db.user[index].set_name(edit_name)
                                edit_password = input("Input password\n")
                                db.user[index].set_password(edit_password)
                                edit_phone = input("Input phone\n")
                                db.user[index].set_phone(edit_phone)
                                print("USER UPDATED")
                                time.sleep(0.5)
                                break
                            elif read == 2:
                                db.remove_user_by_index(index)
                                print("USER REMOVED")
                                time.sleep(0.5)
                                break
                            elif read == 3:
                                time.sleep(0.5)
                                break
                        time.sleep(0.5)
                        break
                elif read == 2:
                    time.sleep(0.5)
                    cls()
                    print("FIND USER BY EMAIL")
                    buff_inp = input("Input email\n")

                    for item in db.user:
                        if buff_inp == item.email:
                            flag = True
                            break
                        else:
                            flag = False

                    if flag == True:
                        print(db.find_user_by_email(buff_inp))
                        index = db.find_user_by_email(buff_inp)[0]
                        while True:
                            read = read_int("1. Update user\n2. Delete user\n3. Back\n", 3)
                            if read == 1:
                                cls()
                                print(db.find_user_by_index(int(index)))
                                print("UPDATE USER")
                                edit_name = input("Input name\n")
                                db.user[index].set_name(edit_name)
                                edit_password = input("Input password\n")
                                db.user[index].set_password(edit_password)
                                edit_phone = input("Input phone\n")
                                db.user[index].set_phone(edit_phone)
                                print("USER UPDATED")
                                time.sleep(0.5)
                                break
                            elif read == 2:
                                db.remove_user_by_index(index)
                                print("USER REMOVED")
                                time.sleep(0.5)
                                break
                            elif read == 3:
                                break
                        break
                    else:
                        print("User not exist")
                        time.sleep(0.5)
                elif read == 3:
                    time.sleep(0.5)
                    break
                time.sleep(0.5)
                break
        else:
            print("Database is empty")

    elif read == 3:
        time.sleep(0.5)
        cls()
        print("DATABASE")
        db.show_database()
        foo = input("Press Enter to continue")
        time.sleep(0.5)

    elif read == 4:
        time.sleep(0.5)
        break

cls()
time.sleep(1)
print("=======database deleted=======")
