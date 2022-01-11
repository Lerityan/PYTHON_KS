import math

# Arithmetic

# 1
item_1 = 9
# 2
item_2 = 4
# 3
result_sum = item_1 + item_2
# 4
print(result_sum)
# 5
result_subtr = max(item_1, item_2) - min(item_1, item_2)
# 6
print(result_subtr)
# 7
result_multi = item_1 * item_2
# 8
print(result_multi)
# 9
result_exp = item_1 ** item_2
# 10
print(result_exp)
# 11
result_m_exp = math.pow(item_1, item_2)
# 12
print(result_m_exp)
# 13
result_s_root = item_1 ** (0.5)
# 14
print(result_s_root)
# 15
result_m_s_root = math.sqrt(item_1)
# 16
print(result_m_s_root)
# 17
result_mp_s_root = math.pow(item_1, 0.5)
# 18
print(result_mp_s_root)
# 19
item_1 = item_1 // 2 * 2 + 1
# print(item_1)
# 20
item_2 = item_2 // 2 * 2
# print(item_2)
# 21
result_division = item_1 / item_2
# 22
print(result_division)
# 23
result_m_floor = math.floor(result_division)
# 24
print(result_m_floor)
# 25
result_m_ceil = math.ceil(result_division)
# 26
print(result_m_ceil)
# 27
result_int = int(result_division + (0.5 if result_division > 0 else -0.5));
# 28
print(result_int)
# 29
result_no_division_loss = item_1 // item_2;
# 30
print(result_no_division_loss)
# 31
result_division_loss = item_1 % item_2;
# 32
print(result_division_loss)

# Arithmetic =

# 33
item_3 = 20
# 34
item_3 += 10;
# 35
print(item_3)
# 36
item_3 -= 5;
# 37
print(item_3)
# 38
item_3 *= 3;
# 39
print(item_3)
# 40
item_3 /= 2;
# 41
print(item_3)
# 42
item_3 **= 2;
# 43
print(item_3)
# 44
item_3 **= 0.5;
# 45
print(item_3)
# 46
item_3 %= 6;
# 47
print(item_3)

# Boolean

# 48
b_item_t = True
# 49
b_item_f = False
# 50
b_item_relult_sum = b_item_f + b_item_t
# maybe result?
# 51
print(b_item_relult_sum)
# 52
b_item_relult_subtr = b_item_t-b_item_f
# 53
print(b_item_relult_subtr)
# 54
b_item_relult_multi = b_item_f*b_item_f
# 55
print(b_item_relult_multi)
# 56
try:
    b_item_relult_division = b_item_t / b_item_f
    # 57
    print(b_item_relult_division)
except ZeroDivisionError:
    print("Division by zero")

#58
b_item_1_int = int(b_item_t)
#59
print(b_item_1_int)
#60
b_item_2_int = int(b_item_f)
#in task recursion
#61
print(b_item_2_int)