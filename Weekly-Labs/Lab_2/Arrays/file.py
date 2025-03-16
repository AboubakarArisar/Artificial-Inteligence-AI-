import pandas as pd

df = pd.read_csv('/home/aboubakar/Artificial-Inteligence-AI-/Weekly-Labs/Lab_2/Arrays/dirtydata.csv')

df.fillna(df['Calories'].mean(), inplace = True)
print("original data ",df)

print("Missing values ",df.isnull())    