import csv
import pandas

df = pandas.read_csv("Squirrel_Data.csv")


gray_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])

data = pandas.DataFrame(
    {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [
            gray_squirrels_count,
            cinnamon_squirrels_count,
            black_squirrels_count,
        ],
    }
)

print(data)
