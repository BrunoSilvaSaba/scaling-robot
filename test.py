import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
