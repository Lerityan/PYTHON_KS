import csv
import names
from datetime import datetime
from faker import Faker
import pandas as pd

# 1
first = open('empty.csv', 'w', newline='')
first.close()

# 2


with open('digits.csv', 'w', newline='') as csvfile2:
    digits = csv.writer(csvfile2)
    for i in range(0, 150):
        digits.writerow({str(i)})

# 3

with open('names.csv', 'w', newline='') as csvfile3:
    name = csv.writer(csvfile3)
    for i in range(0, 100):
        name.writerow({names.get_full_name()})

# 4

with open('email.csv', 'w', newline='') as csvfile4:
    fake = Faker()
    email = csv.writer(csvfile4)
    for i in range(0, 100):
        email.writerow({fake.email(True, "gmail")})

# 5

with open('nne.csv', 'w', newline='') as csvfile5:
    fake = Faker()
    fieldnames = ['Number', 'Name', "Email"]
    nne = csv.DictWriter(csvfile5, fieldnames=fieldnames)
    nne.writeheader()
    for i in range(0, 99):
        name = fake.first_name()
        nne.writerow({'Number': str(i), 'Name': name, "Email": name + "@" + fake.domain_name()})

# 6

with open('digits_2.csv', 'w', newline='') as csvfile6:
    digits_2 = csv.writer(csvfile6)
    numbers = list()
    for i in range(10, 310):
        numbers.append(i)
    for item in numbers:
        digits_2.writerow({item})

# 7

with open('names_2.csv', 'w', newline='') as csvfile7:
    names_2 = csv.writer(csvfile7)
    names = list()
    fake = Faker()
    for i in range(400):
        names.append(fake.name())
    for item in names:
        names_2.writerow({item})

# 8

with open('emals_2.csv', 'w', newline='') as csvfile8:
    emals_2 = csv.writer(csvfile8)
    emails = list()
    fake = Faker()
    for i in range(400):
        emails.append(fake.email(True, "gmail.com"))
    for item in emails:
        emals_2.writerow({item})

# 9

with open('nne_2.csv', 'w', newline='') as csvfile9:
    fake = Faker()
    fieldnames = ['Number', 'Name', "Email"]
    nne_2 = csv.DictWriter(csvfile9, fieldnames=fieldnames)
    nne_2.writeheader()
    emails = list()
    for i in range(0, 449):
        name = fake.first_name()
        emails.append([str(i), name, name + "@" + fake.domain_name()])
    for item in emails:
        nne_2.writerow({'Number': item[0], 'Name': item[1], 'Email': item[2]})

# 10

ten = pd.read_csv("nne_2.csv")
ten["Date"] = ""
for i in range(0, 450):
    fake = Faker()
    if i < 50:
        ten._set_value(i, "Date",
                       fake.date_between_dates(date_start=datetime(1980, 1, 1), date_end=datetime(1990, 12, 31)))
    elif i < 150:
        ten._set_value(i, "Date",
                       fake.date_between_dates(date_start=datetime(1991, 1, 1), date_end=datetime(2000, 12, 31)))
    elif i <300 :
        ten._set_value(i, "Date",
                       fake.date_between_dates(date_start=datetime(2001, 1, 1), date_end=datetime(2010, 12, 31)))
    else :
        ten._set_value(i, "Date",
                       fake.date_between_dates(date_start=datetime(2011, 1, 1), date_end=datetime(2021, 12, 31)))

ten.to_csv("nne_2.csv")
