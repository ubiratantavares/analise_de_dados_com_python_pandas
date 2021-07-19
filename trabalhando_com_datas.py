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

# Transformando a coluna de data para o tipop datetime
# df['Data'] = pd.to_datetime(df['Data'])

# agrupamento por ano
print(df.groupby(df['Data'].dt.year)['Receita'].sum())

# criando uma coluna com o ano
df['Ano_Venda'] = df['Data'].dt.year
print(df.sample(5))

# criando uma coluna com o ano
df['Mes_Venda'] = df['Data'].dt.month
print(df.sample(5))

# criando uma coluna com o dia
df['Dia_Venda'] = df['Data'].dt.day
print(df.sample(5))

# criando uma coluna com o trimestre
df['Trimestre_Venda'] = df['Data'].dt.quarter
print(df.sample(5))

# retornando a data mais antiga
print(df['Data'].min())

# Calculando a diferença de dias entre duas datas
df['Diferenca_dias'] = df['Data'] - df['Data'].min()
print(df.sample(5))

# filtrando as vendas de 2019 do mês de março
vendas_marco_2019 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]
print(vendas_marco_2019.sample(5))

vendas_marco_2019 = df.loc[(df['Ano_Venda'] == 2019) & (df['Mes_Venda'] == 3)]
print(vendas_marco_2019.sample(5))


