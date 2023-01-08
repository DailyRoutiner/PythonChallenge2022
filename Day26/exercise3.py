

with open("./file1.txt") as file1:
    numbers = file1.readlines()
    list1 = [int(num) for num in numbers]

with open("./file2.txt") as file2:
    numbers = file2.readlines()
    list2 = [int(num) for num in numbers]

# result = []
# for num in list1:
#     if num in list2:
#         result.append(num)

result = [num for num in list1 if num in list2]

# Write your code above 👆

print(result)


