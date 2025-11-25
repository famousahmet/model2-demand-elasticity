import pandas as pd
import numpy as np
import statsmodels.api as sm


class DemandModel:
    """
    Log-Elasticity Demand Model
    Sales ~ Price + Promo + Footfall
    """

    def __init__(self):
        self.model = None

    def prepare(self, df):
        df = df.copy()

        # Required columns
        required = ["Sales", "Price", "Promo", "Footfall", "Date", "Store"]
        for c in required:
            if c not in df.columns:
                raise ValueError(f"Missing column: {c}")

        # Handle ABV if exists, else create proxy
        if "ABV" not in df.columns:
            df["ABV"] = df["Sales"] / np.maximum(df["Footfall"], 1)

        df["Median_ABV"] = df["ABV"].replace(0, np.nan)
        df["Median_ABV"] = df["Median_ABV"].fillna(df["Median_ABV"].median())

        # Log transforms
        df["Log_Sales"] = np.log(df["Sales"] + 1)
        df["Log_Price"] = np.log(df["Price"] + 1)
        df["Log_Footfall"] = np.log(df["Footfall"] + 1)

        return df

    def fit(self, df):
        df_prep = self.prepare(df)

        X = df_prep[["Log_Price", "Promo", "Log_Footfall"]]
        X = sm.add_constant(X)
        y = df_prep["Log_Sales"]

        model = sm.OLS(y, X).fit()
        self.model = model

        return df_prep, model

    def predict(self, df_prep):
        X = df_prep[["Log_Price", "Promo", "Log_Footfall"]]
        X = sm.add_constant(X)
        return self.model.predict(X)
