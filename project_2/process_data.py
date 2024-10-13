import pandas as pd
df = pd.read_csv('data/data.csv')
print("Data Summary")
print (df.describe())