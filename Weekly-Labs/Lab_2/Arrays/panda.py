import pandas as pd

mydictionary = {
    "name": ["Alice", "Bob", "Charlie", "David", "Edward"],
    "age": [25, 26, 27, 28, 29],
}


df = pd.DataFrame(mydictionary)
# print(df)
print(df.head())