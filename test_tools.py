from tools import load_dataset

df = load_dataset(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

print(df.head())