from tools import load_dataframe
from analyzer import DataAnalyzer

df = load_dataframe(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

analysis = DataAnalyzer(df)

print(analysis.summary())
print(analysis.mean())