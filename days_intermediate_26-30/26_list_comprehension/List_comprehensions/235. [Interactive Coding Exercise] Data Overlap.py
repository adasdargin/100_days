with open("235. file1.txt") as file1:
    lst1 = file1.readlines()
stripped_lst1 = [int(num.strip("\n")) for num in lst1]          # [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]


with open("235. file2.txt") as file2:
    lst2 = file2.readlines()
stripped_lst2 = [int(num.strip("\n")) for num in lst2]          # [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

result = [num for num in stripped_lst1 if num in stripped_lst2]
# Write your code above 👆

print(result)                                                   # [3, 6, 5, 33, 12, 7, 42, 13]

#Solution code
solution_code_line = [int(num) for num in lst1 if num in lst2]

