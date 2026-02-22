import pandas as pd

df = pd.read_csv("data/raw/customers.csv")

print(f"Duplicates\n{df.duplicated().sum()}\n")
print(f"Nulls Quantity per column\n{df.isna().sum()}")

print(f"Shape count = {df.shape}\n")
df_Without_nulls = df.drop_duplicates()
print(f"Shape count = {df_Without_nulls.shape}\n")