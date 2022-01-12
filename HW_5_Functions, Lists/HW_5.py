from Arr_func import ArrFunctions as arf
from QA_way_func import QAWay as qa
from Data_generation_func import DataGenerate as data
import random as rnd

# 1
arr_int = list()
for item in range(70):
    arr_int.append(rnd.randint(0, 50000))

# 2
arr_even = list()
for item in range(70):
    arr_even.append(rnd.randint(0, 25000) * 2)

# 3
arr_odd = list()
for item in range(70):
    arr_odd.append(rnd.randint(0, 25000) * 2 + 1)
# 4
arf.even_from_list(arr_int)

# 5
arf.odd_from_list(arr_int)

# 6

arf.mod5_from_list(arr_int)

# 7
arf.mod5_count_from_list(arr_int)

# 8
testarr = arf.create_rand_int_list(0, 10, 70)

# 9-10 in arr_func.py

# 11
five_star = arf.group_list_by_five(arf.create_rand_int_list(0, 100, 70))
# 12
print(arf.list_of_sum(five_star))

# 13
arf.compare_sum_group_with_100(five_star)

# 14 (after 30)
qa.by_year_money_save(18)

# 15 (after 30)
qa.by_exp_and_start_salary(5, 1000)

# 16
print(data.create_name_list(70))

# 17

file_arr = data.create_file_name_list(70)
for count in range(len(file_arr)):
    file_arr[count] = str(count) + ". " + file_arr[count]

# 18

login_date_arr = data.create_login_date_list(70)

# 19

Employees = data.create_name_login_pass_email_date(70)

# 20

family = data.create_login_name_married(10)

# 21

gender = data.create_login_name_gender(70)

# 22

salary = data.create_login_name_salary(5)

# 23
namelist = list()
for item in salary:
    if (item[2] > 1500) and (item[2] < 3000):
        namelist.append(item[1])
print(namelist)

# 24

malelist = list()
for item in gender:
    if item[2] == 1:
        malelist.append(item[1])
print(malelist)

# 25

femalelist = list()
for item in gender:
    if item[2] == 0:
        femalelist.append(item[1])
print(femalelist)

# ВСЕ *****, давай по новой. Тк последующие  задания ВНЕЗАПНО требуют реляции между списками
# то самый простой способ это  реализовать -  сгенерить мастерсписок со всеми параметрами
# и попилить его на подсписки
# print("=0.login=1.name=2.gender(1m/0f)=3.married(t/f)=4.pass=5.email=6.date==7.salary===")

master_list = data.create_master_list(70)

gender = list()
for item in master_list:
    gender.append([item[0], item[1], item[2]])

family = list()
for item in master_list:
    family.append([item[0], item[1], item[3]])

salary = list()
for item in master_list:
    salary.append([item[0], item[1], item[7]])

Employees = list()
for item in master_list:
    Employees.append([item[1], item[0], item[4], item[5], item[6]])

# 26
print("==================================")
unmarried_male = list()
for index, item in enumerate(family):
    if (item[2] is False) and (gender[index][2] == 1):
        unmarried_male.append(item[1])

# 27
unmarried_female = list()
for index, item in enumerate(family):
    if (item[2] is False) and (gender[index][2] == 0):
        unmarried_female.append(item[1])

# 28
# not sexism, just a reference to borat
lady_magnet = list()
for index, item in enumerate(family):
    if (item[2] is False) and (gender[index][2] == 1) and (salary[index][2] > 1500):
        lady_magnet.append(Employees[index][0])

# 29
lady_magnet = data.find_lady_magnet(family, salary, gender, Employees)
