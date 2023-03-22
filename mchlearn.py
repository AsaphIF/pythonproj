#importa as bibliotecas de graficos
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importa e define a biblioteca de machine learning
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#le o arquivo
df = pd.read_csv("advertising.csv")

# printa a correlação 
print(df.corr())

# coloca em graficos essa correlação para a visualição
sns.pairplot(df)
plt.show()


# coloca em um grafico de calor essa correlação para a visualição
sns.heatmap(df.corr(),cmap = 'Blues',annot=True)
plt.show()

#define quem é x e quem é y
y = df["Vendas"]
x = df.drop("Vendas", axis=1)

#separa aleatoriamente o x e y de treino e de teste
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3,random_state=1)

#usa um modelo de machine learning 
lin_reg = LinearRegression()
lin_reg.fit(x_treino,y_treino)

#usa um modelo diferente de machine learning
rf_reg = RandomForestRegressor()
rf_reg.fit(x_treino,y_treino)

# testa um valor para os dois modelos
test_lin = lin_reg.predict(x_teste)
test_rf = rf_reg.predict(x_teste)

#usa a metrificação de r2 nos 2 modelos e printa
r2_lin=r2_score(y_teste,test_lin)
r2_rf=r2_score(y_teste,test_rf)
print(r2_lin)
print(r2_rf)

#cria um grafico para mostrar a diferença dos dois modelos
dfr= pd.DataFrame()
dfr["y_teste"] = y_teste
dfr["Arvore de Decisão"] = test_rf
dfr["Regressão Linear"] = test_lin

#define o tamanho do grafico e o tipo do grafico de linha
fig = plt.figure(figsize=(15,5))
sns.lineplot(data=dfr)
plt.show()

#usa uma nova tabela com dados novos
nov = pd.read_csv("novos.csv")
display(nov)

#preve com o melhor modelo de machine learning os dados
prev = rf_reg.predict(nov)
print(prev)
