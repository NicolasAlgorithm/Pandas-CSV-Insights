import pandas as pd

df = pd.read_csv("data/raw/customers.csv")
print(df.info())

print(df.describe(include="all"))

print(df.isna().sum())