# import requests
# import pandas as pd



# # Standardizes currency to USD values so that we can better compare results
# def format_currency(dataset):
#   url = "https://api.exchangerate-api.com/v4/latest/USD"

#   # Requests data from API
#   response = requests.get(url)
#   data = response.json()
  
#   def convert_currency(row):
#     rate = data["rates"][row["Unit Code"]]
#     return row["Value"] / rate

#   for index, row in dataset.iterrows():
#     dataset.at[index,"Unit Code"] = "USD"
#     dataset.at[index,"Value"] = convert_currency(row)
#   return dataset


# # ADD CODE: Pandas dataframes
# wage = pd.read_csv("wage.csv", delimiter=",")
# # print(wage)
# happiness = pd.read_csv("happiness.csv", delimiter=",")
# # print(happiness)
# wage_usd = format_currency(wage)
# # print(wage_usd)
# wage_and_happiness = happiness.merge(wage_usd)
# # print(wage_and_happiness)

import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

arr = np.array([[10, 20], [30, 40]])
df2 = pd.DataFrame(arr, columns=['X', 'Y'], index=list('AB'))
df2['Z'] = df2['X'] + df2['Y']
print(df2)

# np.random.seed(0)
data3 = {
    'Age': np.random.randint(20, 60, size=5),
    'Income': np.random.normal(50000, 10000, size=5)
}
df3 = pd.DataFrame(data3)

# Normalize income using NumPy
df3['Income_norm'] = (df3['Income'] - np.mean(df3['Income'])) / np.std(df3['Income'])

print(df3)
