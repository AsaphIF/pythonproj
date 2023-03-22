#importei as bibliotecas
import pandas as pd 
import plotly.express as px

# a var df recebe os dados do csv
df = pd.read.csv(r'C:\Users\name\Downloads\telecom_users.csv')

#vejo como esta a tabela
display(df)

# pego as informações necessarias para saber se tudo está em ordem
print(df.info())

# .drop apaga a coluna UNNAMED e axis = 1 apaga a coluna axis = 0 apaga a linha
df = df.drop(["Unnamed: 0"],axis=1)

#  
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors = "coerce")

df=df.dropna(how='all',axis=1)

df=df.dropna()


print(df["Churn"].value_counts() )
print(df["Churn"].value_counts(normalize=True).map('{:.1%}'.format) )

for coluna in df:
    if coluna == "MesesComoCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()
 

colu = "Aposentado"
figu = px.histogram(df, x=colu, color="Churn")
figu.show()
