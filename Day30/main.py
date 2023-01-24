# # File Not found
#
# try:
#     file = open("a_file.txt", mode="r")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["asdfadsf"])  # not exist
#
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w+")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")