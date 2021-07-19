import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df1 = pd.read_excel('datasets/Aracaju.xlsx')
df2 = pd.read_excel('datasets/Fortaleza.xlsx')
df3 = pd.read_excel('datasets/Natal.xlsx')
df4 = pd.read_excel('datasets/Recife.xlsx')
df5 = pd.read_excel('datasets/Salvador.xlsx')

df = pd.concat([df1, df2, df3, df4, df5])
df['LojaID'] = df['LojaID'].astype('object')

# substituindo os valores nulos pela média
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)

# criando novas colunas
df['Receita'] = df['Vendas'].mul(df['Qtde'])

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
