import pandas as pd
print("hello github")

print("Hello VS Code")

# TODO #1@giovannipolimi

df = pd.read_csv('./data/titanic.csv')
df.to_json(r'./data/titanic.json')

print(df.head())