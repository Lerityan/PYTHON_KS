import random as rnd


class ArrFunctions():
    # 4
    def odd_from_list(arr):
        for item in arr:
            if item % 2 == 1:
                print(item)

    # 5
    def even_from_list(arr):
        for item in arr:
            if item % 2 == 0:
                print(item)

    # 6
    def mod5_from_list(arr):
        for item in arr:
            if item % 5 == 0:
                print(item)

    # 7
    def mod5_count_from_list(arr):
        count = 0
        for item in arr:
            if item % 5 == 0:
                count += 1
        print(count)

    # 8
    def create_rand_int_list(min_n, max_n, length):
        arr = list()
        for item in range(length):
            arr.append(rnd.randint(min_n, max_n))
        return arr

    # 9

    def group_list_by_five(arr):
        newlist = list()
        counter = 0
        while counter < len(arr):
            newlist.append(arr[counter:counter + 5])
            counter += 5
        return newlist

    # 10

    def sort_list_odd_even(arr):
        odd_list = list()
        even_list = list()
        for item in arr:
            if item % 2 == 0:
                even_list.append(item)
            else:
                odd_list.append(item)
        return odd_list, even_list

    # 12
    def list_of_sum(arr):
        newarr = list()
        for item in arr:
            newarr.append(sum(item))
        return newarr

    # 13
    def compare_sum_group_with_100(arr):
        more_100 = list()
        less_100 = list()
        for item in arr:
            if sum(item) >= 100:
                more_100.append(item)
            else:
                less_100.append(item)
        if len(more_100) == 0:
            more_100 = "No_lists"
        if len(less_100) == 0:
            less_100 = "No_lists"
        return less_100, more_100
