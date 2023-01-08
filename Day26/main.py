numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_name = [namen for namen in name]
new_double = [n*2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"]
cap_name = [name.upper() for name in names if len(name) > 4]