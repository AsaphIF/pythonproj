import pyperclip
import pyautogui as p
import pandas as pd
import time



site = r"https://drive.google.com/drive/u/0/folders/1Iaaghdjs9EIqOH63LBnwGL5v6dvldN"
p.PAUSE = 2

p.hotkey('ctrl','t')
time.sleep(6)
pyperclip.copy(site)
p.hotkey('ctrl','v')
p.press('enter')
time.sleep(8)
p.rightClick(468,340)
time.sleep(1)
p.click(550,639)
time.sleep(10)

df = pd.read_excel(r'C:\Users\name\Downloads\Vendas10.xlsx')


faturamento = df['Valor Final'].sum()
qtde_produto = df['Quantidade'].sum()


p.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
p.hotkey("ctrl", "v")

p.press("enter")
time.sleep(10)
p.click(x=150, y=172)
time.sleep(10)
p.write("email.deteste@gmail.com")
p.press("tab") 

p.press("tab") 
pyperclip.copy("Relatório de Vendas")
p.hotkey("ctrl", "v")

p.press("tab") 

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtde_produto:,}

Qualquer dúvida estou à disposição.
Att.,
Lira do Python
"""



pyperclip.copy(texto)
p.hotkey("ctrl", "v")


p.hotkey("ctrl", "enter")
