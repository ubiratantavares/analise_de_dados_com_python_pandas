import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('datasets/Gapminder.csv', error_bad_lines=False, delimiter=';')

print(df.head())

df.rename(columns={'country': 'País',
                   'continent': 'Continente',
                   'year': 'Ano',
                   'lifeExp': 'Expectativa de vida',
                   'pop': 'Populacao Total',
                   'gdpPercap': 'PIB'}, inplace=True)

print(df.head())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.tail())

print(df.describe())

print(df['Continente'].unique())

oceania = df.loc[df['Continente'] == 'Oceania']
print(df.head())
print(oceania['Continente'].unique())

print(df.groupby('Continente')['País'].nunique())

print(df.groupby('Ano')['Expectativa de vida'].mean())

print(df['PIB'].mean())

print(df['PIB'].sum())
