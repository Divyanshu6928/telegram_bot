from tools import load_dataframe

df = load_dataframe(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

print(df.head())