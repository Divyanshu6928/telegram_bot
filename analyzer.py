import pandas as pd


class DataAnalyzer:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary(self):

        return {
            "rows": len(self.df),
            "columns": list(self.df.columns),
            "shape": self.df.shape
        }

    def numeric_columns(self):

        return list(
            self.df.select_dtypes(include="number").columns
        )

    def describe(self):

        return self.df.describe().to_dict()

    def head(self):

        return self.df.head().to_dict()

    def missing(self):

        return self.df.isna().sum().to_dict()

    def max(self):

        result = {}

        for col in self.numeric_columns():
            result[col] = self.df[col].max()

        return result

    def min(self):

        result = {}

        for col in self.numeric_columns():
            result[col] = self.df[col].min()

        return result

    def mean(self):

        result = {}

        for col in self.numeric_columns():
            result[col] = float(self.df[col].mean())

        return result