import pandas

data = pandas.read_csv("squirrel_data.csv")
data_dict = data.to_dict()
print(data_dict["Primary_Fur_Color"])


grey_sq = len(data[data.Primary_Fur_Color == "Gray"])
cinnamon = len(data[data.Primary_Fur_Color == "Cinnamon"])
black = len(data[data.Primary_Fur_Color == "Black"])
sq_color = {
    "color": ["gray", "cinnamon", "black"],
    "population": [grey_sq, cinnamon, black]
}
all_colors = pandas.DataFrame(sq_color)
all_colors.to_csv("color.csv")

