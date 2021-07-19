import pandas as pd
from matplotlib import pyplot as plt

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

# criando uma coluna com o ano
df['Ano_Venda'] = df['Data'].dt.year

# criando uma coluna com o ano
df['Mes_Venda'] = df['Data'].dt.month

# criando uma coluna com o dia
df['Dia_Venda'] = df['Data'].dt.day

# criando uma coluna com o trimestre
df['Trimestre_Venda'] = df['Data'].dt.quarter

print(df['LojaID'].value_counts(ascending=False))

df['LojaID'].value_counts(ascending=False).plot.bar()
plt.savefig('imagens/grafico01.png')
plt.show()

df['LojaID'].value_counts(ascending=True).plot.barh()
plt.savefig('imagens/grafico02.png')
plt.show()

df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie()
plt.savefig('imagens/grafico03.png')
plt.show()

print(df['Cidade'].value_counts())

df['Cidade'].value_counts().plot.bar(title="Total de Vendas por Cidade")
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.savefig('imagens/grafico04.png')
plt.show()

df['Cidade'].value_counts().plot.bar(title="Total de Vendas por Cidade", color='red')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.savefig('imagens/grafico05.png')
plt.show()

# alterando o estilo
plt.style.use('ggplot')

df.groupby(df['Mes_Venda'])['Qtde'].sum().plot(title='Total de Produtos Vendidos por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend()
plt.savefig('imagens/grafico06.png')
plt.show()

print(df.groupby(df['Mes_Venda'])['Qtde'].sum())

df_2019 = df[df['Ano_Venda'] == 2019]
df_2019.groupby(df_2019['Mes_Venda'])['Qtde'].sum().plot(title='Total de Produtos Vendidos por Mês - 2019', marker='v')
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend()
plt.savefig('imagens/grafico07.png')
plt.show()

plt.hist(df['Qtde'], color='orangered')
plt.show()

plt.scatter(x=df_2019['Dia_Venda'], y=df_2019['Receita'])
plt.savefig('imagens/grafico08.png')
plt.show()

df_2019.groupby(df_2019['Mes_Venda'])['Qtde'].sum().plot(title='Total de Produtos Vendidos por Mês - 2019', marker='v')
plt.xlabel('Mês')
plt.ylabel('Total de Produtos Vendidos')
plt.legend()
plt.savefig('imagens/grafico09.png')
plt.show()
