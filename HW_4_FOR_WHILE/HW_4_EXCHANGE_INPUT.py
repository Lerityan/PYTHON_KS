import time

from Exchange_tools import Currency, Exchange
import keyboard


def buried():
    for blank in range(10):
        print("\n")
    print("buried")


gbp = Currency("GBP", 0.74)
usd = Currency("USD", 1)
cny = Currency("CNY", 6.34)
eur = Currency("EUR", 0.86)
chf = Currency("CHF", 0.91)

# 1
try:
    amount = int(input("Start task 1: input int\n"))
    print("Ты ввел", amount, eur.name)
    eur.to_usd_output(amount)
    buried()
except ValueError:
    print("You failed Task 1")

2
try:
    amount = int(input("Start task 2: input int\n"))
    print("Ты ввел", amount, eur.name)
    usd.to_self_output(Exchange.convert(eur, usd, amount))
    eur.to_self_output(Exchange.convert(eur, usd, amount))
    chf.to_self_output(Exchange.convert(eur, usd, amount))
    gbp.to_self_output(Exchange.convert(eur, usd, amount))
    cny.to_self_output(Exchange.convert(eur, usd, amount))
    buried()
except ValueError:
    print("You failed Task 2")

# 3.1
try:
    buf_inp = input("Start task 3: input int\n")
    amount = int(buf_inp)
    if amount >= 0:
        print("Ты ввел", amount, eur.name)
        usd.to_self_output(Exchange.convert(eur, usd, amount))
        eur.to_self_output(Exchange.convert(eur, usd, amount))
        chf.to_self_output(Exchange.convert(eur, usd, amount))
        gbp.to_self_output(Exchange.convert(eur, usd, amount))
        cny.to_self_output(Exchange.convert(eur, usd, amount))
    else:
        print("Введите положительное число.")
except ValueError:
    if buf_inp == "":
        print("Вы ввели пустое поле. Введите число.")
    else:
        print("Вы ввели не число. Введите число.")

# 4.1
print("Start task 4")
flag = True


def keybreake():
    global flag
    flag = False
    print("Stop_run")


keyboard.add_hotkey("Ctrl + c", keybreake)
while flag:
    try:
        buf_inp1 = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']\n")
        buf_inp2 = input("Введите сумму\n")
        amount = int(buf_inp2)
        if amount >= 0:
            print("Вы ввели сумму", amount, "и валюту", buf_inp1)
            if str.lower(buf_inp1)=="usd":
                usd.to_self_output(Exchange.convert(eur, usd, amount))
            elif str.lower(buf_inp1)=="eur":
                eur.to_self_output(Exchange.convert(eur, usd, amount))
            elif str.lower(buf_inp1) == "chf":
                chf.to_self_output(Exchange.convert(eur, usd, amount))
            elif str.lower(buf_inp1) == "gbp":
                gbp.to_self_output(Exchange.convert(eur, usd, amount))
            elif str.lower(buf_inp1) == "cny":
                cny.to_self_output(Exchange.convert(eur, usd, amount))
            elif str.lower(buf_inp1) == "":
                print("Но не указали название валюты")
            else:
                print("Мы не можем конвертировать эту валюту")
        else:
            print("Введите положительное число.")
    except ValueError:
        if buf_inp2 == "":
            print("Вы ввели пустое поле. Введите число.")
        else:
            print("Вы ввели не число. Введите число.")
