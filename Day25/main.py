# import csv
#
# temperatures = []
# with open("./weather_data.csv") as data_file:
#     #data = data_file.readlines()
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas

# series and dataframe type
data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])
# print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(min(temp_list))
#
# # Average temperature
# def average(list):
#     return sum(list) / len(list)
#
#
# print(round(average(temp_list), 2))
# # Series
# print(data["temp"].mean())
# print(data["temp"].max())

# Compare with temp max
# print(data[data.temp == data["temp"].max()])


def f(x):
    x = x * 1.8 + 32
    return float(x)


# Convert C to F
# monday = data[data.day == "Monday"]
# print(monday.temp.apply(f))
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 80, 49]
# }
#
# data2 = pandas.DataFrame(data_dict)
# #data2.to_csv("new_data.csv")
# print(data2)

data2 = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long
# print(data2["Primary Fur Color"])
squirrel_count_dict = data2["Primary Fur Color"].value_counts().to_dict()
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrel_count_dict["Gray"], squirrel_count_dict["Cinnamon"], squirrel_count_dict["Black"]]
}

# Dataframe 을 만드는 조건이 까다롭네... dictionary 형태로 하려면 "컬럼명":List 형태로 만들어야함
df = pandas.DataFrame(data_dict)
print(df.to_csv())


