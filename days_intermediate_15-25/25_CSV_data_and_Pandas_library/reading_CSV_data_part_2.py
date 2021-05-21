import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))                  # <class 'pandas.core.frame.DataFrame'>  - it's equivalent of whole table.
# print(type(data["temp"]))          # <class 'pandas.core.series.Series'>   - it's equivalent to a list.

data_dict = data.to_dict()           # creates a dictionary.
# print(data_dict)

temp_list = data["temp"].to_list()    # creates a list for temp column.     [12, 14, 15, 14, 21, 22, 24]


average_temp = sum(temp_list) / len(temp_list)
# or
average_temp_pd = data["temp"].mean()
max_temp_pd = data["temp"].max()


# Get Data in Columns - the same result.
# print(data["condition"])
# print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])               # 0  Monday    12     Sunny

# Print the row of data which had the highest temperature
print(data[data.temp == data.temp.max()])    # 6  Sunday    24     Sunny

monday = data[data.day == "Monday"]          # 0  Monday    12     Sunny
print(monday.condition)                      # 0    Sunny


monday_temp_fahrenheit = (monday.temp * 9/5) + 32
print(monday_temp_fahrenheit)

