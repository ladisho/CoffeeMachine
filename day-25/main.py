# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

print(monday.condition)

monday_temp = monday.temp[0]

print(monday_temp)
#
# fahrenheit = (1.8 * monday.temp) + 32
#
# print(fahrenheit)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240807.csv")
#
# grey_squirrel_count = (data["Primary Fur Color"] == "Gray").sum()
# red_squirrel_count = (data["Primary Fur Color"] == "Cinnamon").sum()
# black_squirrel_count = (data["Primary Fur Color"] == "Black").sum()
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
#





