# importar as bibliotecas
#from string import Formatter

'''
link com informações a respeito da leitura de tabelas no Excel.
https://www.hashtagtreinamentos.com/ler-arquivo-excel-varias-abas-no-python
'''
import pandas as pd

# importar a base de dados
# sheet_name = 'nome_da_aba_desejada(caso tenha mais de 1)'
# ou
# sheet_name = 2
#              indice da aba
x=2
tabela_vendas = pd.read_excel('tabela.xlsx', sheet_name=x)

# visualizar a base de dados
#pd.set_option('display.max_columns', None)
#print(tabela_vendas)

# tabela parcial, agrupada por 'Coluna1', somando os termos da 'Coluna2'
faturamento = tabela_vendas[['Coluna1', 'Coluna2']].groupby('Coluna1').sum()
#print(faturamento)
#print('\n'+'*'*44+'\n')

# quantidade de produtos vendidos por loja
produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(produtos)
#print('\n'+'*'*44+'\n')

# ticket medio por loja (faturamento/quantidade)
ticket = (faturamento['Valor Final'] / produtos['Quantidade']).to_frame()
ticket = ticket.rename(columns={0: 'Ticket Médio'})
#print(ticket)
#print('\n')