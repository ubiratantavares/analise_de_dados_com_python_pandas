import pandas as pd

df1 = pd.read_excel('datasets/Aracaju.xlsx')
df2 = pd.read_excel('datasets/Fortaleza.xlsx')
df3 = pd.read_excel('datasets/Natal.xlsx')
df4 = pd.read_excel('datasets/Recife.xlsx')
df5 = pd.read_excel('datasets/Salvador.xlsx')

df = pd.concat([df1, df2, df3, df4, df5])

print(df.head())

print(df.tail())

# cinco amostras do dataframe
print(df.sample(5))

print(df.dtypes)


df['LojaID'] = df['LojaID'].astype('object')

# verificando a existência de valores faltantes
print(df.isnull().sum())

# substituindo os valores nulos pela média
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)

# verificando a existência de valores faltantes
print(df.isnull().sum())

# apagando linhas com valores nulos
df.dropna(inplace=True)

# apagando as linhas com valores nulos com base apenas em uma coluna
df.dropna(subset=['Vendas'], inplace=True)

# apagando as linhas com valores nulos em todas as colunas
df.dropna(how='all', inplace=True)

# criando novas colunas
df['Receita'] = df['Vendas'].mul(df['Qtde'])

print(df.head())

df['Qtde_Novo'] = df['Receita'] / df['Vendas']

print(df.head())

print(df['Receita'].min())
print(df['Receita'].mean())
print(df['Receita'].max())
print(df['Receita'].sum())

# retorna as top 10 com as maiores receitas
print(df.nlargest(10, "Receita"))

# retorna as top 10 com as menores receitas
print(df.nsmallest(10, "Receita"))

# agrupamento por cidade
print(df.groupby('Cidade')['Receita'].sum())

print(df.sort_values('Receita', ascending=False).head(10))

