from faker import Faker
import random as rnd


class DataGenerate():

    # 16
    def create_name_list(leng):
        f = Faker()
        arr_names = list()
        for item in range(leng):
            arr_names.append(f.name())
        return arr_names

    # 17
    def create_file_name_list(len):
        f = Faker()
        arr_file_names = list()
        for item in range(len):
            arr_file_names.append(f.file_name())
        return arr_file_names

    # 18
    def create_login_date_list(len):
        f = Faker()
        arr_log_date = list()
        for item in range(len):
            arr_log_date.append([f.user_name(), str(f.date_time_this_century())])
        return arr_log_date

    # 19
    def create_name_login_pass_email_date(len):
        f = Faker()
        arr_log_date = list()
        for item in range(len):
            arr_log_date.append([f.name(), f.user_name(), f.password(), f.email(),
                                 str(f.date_time_this_century())])
        return arr_log_date

    # 20
    def create_login_name_married(len):
        f = Faker()
        arr = list()
        for item in range(len):
            arr.append([f.user_name(), f.name(), bool(rnd.randint(0, 1))])
        return arr

    # 21
    def create_login_name_gender(len):
        f = Faker()
        arr = list()
        for item in range(len):
            rand = rnd.randint(0, 1)
            if rand == 1:
                arr.append([f.user_name(), f.name_male(), rand])
            else:
                arr.append([f.user_name(), f.name_female(), rand])
        return arr

    # 22
    def create_login_name_salary(len):
        f = Faker()
        arr = list()
        for item in range(len):
            arr.append([f.user_name(), f.name(), rnd.randint(300, 5000)])
        return arr

    def create_master_list(len):
        f = Faker()
        arr = list()
        for item in range(len):
            rand = rnd.randint(0, 1)
            if rand == 1:
                arr.append(
                    [f.user_name(), f.name_male(), rand, bool(rnd.randint(0, 1)), f.password(), f.email(),
                     str(f.date_time_this_century()), rnd.randint(300, 5000)])
            else:
                arr.append(
                    [f.user_name(), f.name_female(), rand, bool(rnd.randint(0, 1)), f.password(),
                     f.email(),
                     str(f.date_time_this_century()), rnd.randint(300, 5000)])
        return arr

    # not sexism, just a reference to borat
    def find_lady_magnet(family_arr, salary_arr, gender_arr, useless_arr):
        lady_magnet = list()
        for index, item in enumerate(family_arr):
            if (item[2] is False) and (gender_arr[index][2] == 1) and (salary_arr[index][2] > 1500):
                lady_magnet.append(useless_arr[index][0])
        return lady_magnet

