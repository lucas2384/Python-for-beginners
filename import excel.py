import pandas as pd

# passo a passo para solução

# Abrir os 6 arquivos em Excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

tabela_vendas = pd.read_excel('janeiro.xlsx')

print (tabela_vendas)
#para cada arquivo: 