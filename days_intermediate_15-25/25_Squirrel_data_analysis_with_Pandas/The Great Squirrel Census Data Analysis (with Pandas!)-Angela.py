import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrel_colors = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_colors = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_colors = len(data[data["Primary Fur Color"] == "Black"])

squirrel_colors_count = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrel_colors, cinnamon_squirrel_colors, black_squirrel_colors]
}

squirrel_colors_pd = pandas.DataFrame(squirrel_colors_count)
print(squirrel_colors_pd)