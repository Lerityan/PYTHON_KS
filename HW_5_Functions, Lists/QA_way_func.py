import random as rnd
import time
import math


class QAWay():

    def by_year_money_save(age):
        live = True
        married = False
        haveChild = False
        childAge = 0
        speed = 0.15

        if age < 18:
            bank = 0
        elif age > 75:
            live = False
        else:
            bank = int(age) * 200

        while live:
            print("your age = ", age, ",your bank =", '%.1f' % bank)
            if (rnd.randint(0, 1000) >= 900) and (married is False):
                married = True
                bank -= 1000
                speed *= 1.5
                print("You married")
            if (rnd.randint(0, 1000) >= 950) and (married is True):
                married = False
                bank = bank * 0.5
                speed *= 0.7
                print("You divorced")

            if rnd.randint(0, 10000) >= 9900:
                live = False

            if age % 10 == 0:
                speed *= 1.1

            if age > 65:
                speed = -0.2

            if age > 90:
                live = False

            if (rnd.randint(0, 10000) >= 7000) and (haveChild is False):
                haveChild = True
                speed *= 0.2
                bank -= 2000
                print("You have child")

            if haveChild:
                childAge += 1

            if childAge == 18:
                print("Child is grow up")
                haveChild = False
                childAge = 0
                speed *= 2

            bank = bank + math.fabs(bank * speed)
            age += 1
            time.sleep(1)

        print("You died")

    def by_exp_and_start_salary(exp_age, start_salary):
        auto = 1
        perf = 1
        web = 1
        mobile = 1
        english = 1
        grade = 1
        salary = start_salary
        for year in range(exp_age):
            print(year, " year of work, salary ", '%.1f' % salary)
            auto += rnd.randint(0, 2)
            perf += rnd.randint(0, 2)
            web += rnd.randint(0, 2)
            mobile += rnd.randint(0, 2)
            english += rnd.randint(0, 2)
            sm = (auto + perf + web + mobile + english) / 5
            salary = start_salary * grade * sm

            if (sm > 3) and (sm <= 6):
                grade = 1.5
            elif sm > 6:
                grade = 2.5
