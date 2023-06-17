# implicit Data type
# age: int

age = 12
age = "tweleve"

def police_check(age):
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


if police_check(age):
    print("You may Pass")
else:
    print("No!")