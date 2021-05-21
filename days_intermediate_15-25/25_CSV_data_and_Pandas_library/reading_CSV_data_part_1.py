# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)     # <_csv.reader object at 0x7fa48808f660>
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)     # [12, 14, 15, 14, 21, 22, 24]


import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

print(data["temp"])
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64







