import pandas as pd
df = pd.read_csv("dados/2019.csv")
print(df.head())
mean_score = df["Score"].mean()
print(mean_score)