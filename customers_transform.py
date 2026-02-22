import pandas as pd

df = pd.read_csv("data/raw/customers.csv")

print(f"\nOld data type\n{df.dtypes}\n")
df["signup_date"] = df["signup_date"].astype("datetime64[ns]")
print(f"New data type datetime62 ns\n{df.dtypes}\n")

