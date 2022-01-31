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