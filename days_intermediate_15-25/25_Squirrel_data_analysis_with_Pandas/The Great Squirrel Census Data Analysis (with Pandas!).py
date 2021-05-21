import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"].to_list()
gray = []
cinnamon = []
black = []

for color in colors:
    if color == "Gray":
        gray.append(color)
    elif color == "Cinnamon":
        cinnamon.append(color)
    elif color == "Black":
        black.append(color)

squirrel_colors_count = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}

squirrel_colors_pd = pandas.DataFrame(squirrel_colors_count)
squirrel_colors_pd.to_csv("squirrel_count.csv")
