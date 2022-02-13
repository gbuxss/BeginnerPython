# write a program to find largest number in a list
import random

list_number = [2, 3, 4, 0, 5, 7, 5, 10]
for num in list_number:
    max_num = 0
    if num > max_num:
        max_num = num
print(f"Max number: {max_num}")

# write a program to remove duplicates in a list

num_list = [5, 3, 4, 5, 7, 8, 9, 7]
for num in num_list:
    if num_list.count(num) > 1:
        num_list.remove(num)
print(num_list)

