import sys

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
    usd.to_self_output(eur.to_usd(amount))
    eur.to_self_output(eur.to_usd(amount))
    chf.to_self_output(eur.to_usd(amount))
    gbp.to_self_output(eur.to_usd(amount))
    cny.to_self_output(eur.to_usd(amount))
    buried()
except ValueError:
    print("You failed Task 2")

# 3.1
try:
    buf_inp = input("Start task 3: input int\n")
    amount = int(buf_inp)
    if amount >= 0:
        print("Ты ввел", amount, eur.name)
        usd.to_self_output(eur.to_usd(amount))
        eur.to_self_output(eur.to_usd(amount))
        chf.to_self_output(eur.to_usd(amount))
        gbp.to_self_output(eur.to_usd(amount))
        cny.to_self_output(eur.to_usd(amount))
    else:
        print("Введите положительное число.")
except ValueError:
    if buf_inp == "":
        print("Вы ввели пустое поле. Введите число.")
    else:
        print("Вы ввели не число. Введите число.")
buried()

# 4.1
print("Start task 4")
flag = True


def keybreake():
    global flag
    flag = False
    print("Stop_run")
    # sys.exit()


keyboard.add_hotkey("Ctrl + c", keybreake)
while flag:
    try:
        buf_inp1 = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']\n")
        buf_inp2 = input("Введите сумму\n")
        amount = int(buf_inp2)
        if amount >= 0:
            print("Вы ввели сумму", amount, "и валюту", buf_inp1)
            if str.lower(buf_inp1) == "usd":
                usd.to_self_output(eur.to_usd(amount))
            elif str.lower(buf_inp1) == "eur":
                eur.to_self_output(eur.to_usd(amount))
            elif str.lower(buf_inp1) == "chf":
                chf.to_self_output(eur.to_usd(amount))
            elif str.lower(buf_inp1) == "gbp":
                gbp.to_self_output(eur.to_usd(amount))
            elif str.lower(buf_inp1) == "cny":
                cny.to_self_output(eur.to_usd(amount))
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

# 3.2
nf_gbp_c = 0.74
nf_usd_c = 1
nf_cny_c = 6.34
nf_eur_c = 0.86
nf_chf_c = 0.91

nf_gbp_n = "GBP"
nf_eur_n = "EUR"
nf_usd_n = "USD"
nf_cny_n = "CNY"
nf_chf_n = "CHF"

try:
    buf_inp = input("Start task 3: input int\n")
    amount = int(buf_inp)
    if amount >= 0:
        print("Ты ввел", amount, nf_eur_n)
        print("Конвертированная сумма в", nf_gbp_n, "=", "%.2f" % (amount / nf_eur_c * nf_gbp_c))
        print("Конвертированная сумма в", nf_eur_n, "=", "%.2f" % (amount / nf_eur_c * nf_eur_c))
        print("Конвертированная сумма в", nf_usd_n, "=", "%.2f" % (amount / nf_eur_c * nf_usd_c))
        print("Конвертированная сумма в", nf_cny_n, "=", "%.2f" % (amount / nf_eur_c * nf_cny_c))
        print("Конвертированная сумма в", nf_chf_n, "=", "%.2f" % (amount / nf_eur_c * nf_chf_c))

    else:
        print("Введите положительное число.")
except ValueError:
    if buf_inp == "":
        print("Вы ввели пустое поле. Введите число.")
    else:
        print("Вы ввели не число. Введите число.")
buried()

# 4.2

flag = True

while flag:
    try:
        buf_inp1 = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']\n")
        buf_inp2 = input("Введите сумму\n")
        amount = int(buf_inp2)
        if amount >= 0:
            print("Вы ввели сумму", amount, "и валюту", buf_inp1)
            if str.lower(buf_inp1) == "usd":
                print("Конвертированная сумма в", nf_usd_n, "=", "%.2f" % (amount / nf_eur_c * nf_usd_c))
            elif str.lower(buf_inp1) == "eur":
                print("Конвертированная сумма в", nf_eur_n, "=", "%.2f" % (amount / nf_eur_c * nf_eur_c))
            elif str.lower(buf_inp1) == "chf":
                print("Конвертированная сумма в", nf_chf_n, "=", "%.2f" % (amount / nf_eur_c * nf_chf_c))
            elif str.lower(buf_inp1) == "gbp":
                print("Конвертированная сумма в", nf_gbp_n, "=", "%.2f" % (amount / nf_eur_c * nf_gbp_c))
            elif str.lower(buf_inp1) == "cny":
                print("Конвертированная сумма в", nf_cny_n, "=", "%.2f" % (amount / nf_eur_c * nf_cny_c))
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
