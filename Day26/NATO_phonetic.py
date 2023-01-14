student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key)
    print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#ODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
phonetic_file = pandas.read_csv("./nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_file.iterrows()}

#ODO 2. Create a list of the phonetic code words from a word that the user inputs.
code = input("Enter a word: ").upper()

#code_list = [value for (key, value) in phonetic_dict.items() if key in code]
output_list = [phonetic_dict[letter] for letter in code]
print(output_list)

