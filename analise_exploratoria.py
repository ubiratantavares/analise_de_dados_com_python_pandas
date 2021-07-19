import pandas as pd
from matplotlib import pyplot as plt

# alterando o estilo
plt.style.use('seaborn')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.options.display.float_format = '{:20,.2f}'.format


df = pd.read_excel('datasets/AdventureWorks.xlsx')

print(df.shape)

print(df.dtypes)

print(df.head())

# receita total
print(round(df['Valor Venda'].sum(), 2))

df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
# custo total
print(round(df['Custo'].sum(), 2))

df['Lucro'] = df['Valor Venda'] - df['Custo']
# lucro total
print(round(df['Lucro'].sum(), 2))

# criando uma coluna com total de dias para enviar o produto
df['Tempo_Envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

# verificando tipo da coluna Tempo_Envio
print(df['Tempo_Envio'].dtype)

print(df.groupby('Marca')['Tempo_Envio'].mean())


# missing values
print(df.isnull().sum())

# lucro por ano e por marca
print(df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum())

lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum().reset_index()
print(lucro_ano)

# total de produtos vendidos
print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False))

# grafico do total de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total de produtos vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.savefig('imagens/grafico10.png')
plt.show()

df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title='Total do lucro por ano')
plt.xlabel('Ano')
plt.ylabel('Lucro')
plt.savefig('imagens/grafico11.png')
plt.show()

print(df.groupby(df['Data Venda'].dt.year)['Lucro'].sum())

df_2009 = df[df['Data Venda'].dt.year == 2009]
print(df_2009.head())

df_2009.groupby(df['Data Venda'].dt.month)['Lucro'].sum().plot(title='Total de lucro por mês no ano de 2009', marker='v')
plt.xlabel('Mês')
plt.ylabel('Lucro')
plt.savefig('imagens/grafico12.png')
plt.show()

df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title='Total de lucro por marca no ano de 2009')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.savefig('imagens/grafico13.png')
plt.show()

df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title='Total de lucro por marca no ano de 2009')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.savefig('imagens/grafico14.png')
plt.show()


print(df['Tempo_Envio'].describe())

plt.boxplot(df['Tempo_Envio'])
plt.savefig('imagens/grafico15.png')
plt.show()

plt.hist(df['Tempo_Envio'])
plt.savefig('imagens/grafico16.png')
plt.show()

print(df['Tempo_Envio'].min())

print(df[df['Tempo_Envio'] == 20])

df.to_csv('datasets/VendasNovo.csv', index=False)
