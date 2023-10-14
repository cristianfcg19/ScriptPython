import pandas as pd

df = pd.read_csv('amazon_laptop_prices_v01.csv')

print(df)

color = df[df['color']== 'Blue']

print(color)

columna_precio = df['price;']

print(columna_precio)


print(df.columns)



