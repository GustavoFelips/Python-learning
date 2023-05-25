import pandas

#Funciona essencialmente no colab
#Leitura de arquivos
df = pandas.read_csv("http://pycourse.s3.amazonaws.com/temperature.csv")
print(df)

#Visualizas as 3 primeiras linhas
df.head(3)

#As últimas n linhas
df.tail(3)

#Mostra os tipos de dados das colunas
df.dtypes

#Estatísticas básicas
df.describe()

#dataframe info
df.info()

#INDEXAÇÃO
#Nome das colunas
df.columns

#pode renomear dessa forma
df.columns = ['col1', 'col2', 'col3']

#Indexação direta
print(df['classification'])

#Mais de uma coluna
df[['date','temperatura']]

#Indexação por índice
#Metódo .iloc[ , ]
df.iloc[:,0]

#indexação por nome
df.loc[0:2,'classification']

#Transformando o tipo da coluna date para datetime
df['date'] = pandas.to_datetime(df['date'])
df.dtypes

#Setando o índice
df = df.set_index('date')

#Indexação booleana
cond = df['temperatura'] >= 25
df[cond]

df.loc[df.index >= '2020-03-01', ['classification']]

#Método de ordenação
df.sort_values(by='temperatura') #Ordena pelos valores da coluna temperatura

df.sort_values(by='temperatura', ascending=False) #Ordena de forma descrescente

df.sort_values(by=['classification','temperatura']) #Ordena primeiro pela classificação depois, temperatura

df.sort_index(ascending=False) #Ordena pelo índice

#Agrupar uma coluna
df.groupby(by="classification")

#Operação com o agrupamento; fará as operação com as otras colunas
df.groupby(by="classification").mean() #media das colunas

#Drop - remoção de uma coluna
df.drop("classification", axis=1) #Não altera o original

#Apagando no original
df2 = df.copy()
df2.drop('temperatura', axis=1, inplace=True)
df2

