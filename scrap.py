import pandas as pd
from selenium import webdriver #lembre-se de configurar antes
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# pega o valor atual do dolar
navegador = webdriver.Chrome()
navegador.get("https://google.com/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = navegador.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pega o valor atual do euro
navegador.get("https://google.com/")
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = navegador.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pega o valor atual do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
ouro = navegador.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')
ouro =ouro.replace(',','.')

# vejo se está tudo certo e fecho o navegador
print("R$ "+ dolar)
print("R$ " + euro)
print("R$ " + ouro + " a grama")
navegador.quit()


df = pd.read_excel("Produtos.xlsx")


df.loc[df["Moeda"] == "Dólar","Cotação"] = float(dolar)
df.loc[df["Moeda"] == "Euro","Cotação"] = float(euro)
df.loc[df["Moeda"] == "Ouro","Cotação"] = float(ouro)


df["Preço de Compra"] = df["Preço Original"] * df["Cotação"] 
df["Preço de Venda"] = df["Preço de Compra"] * df["Margem"] 


df.to_excel("Produtos Novo1.xlsx",index=False)


df1 = pd.read_excel("Produtos Novo1.xlsx")

display(df1)
