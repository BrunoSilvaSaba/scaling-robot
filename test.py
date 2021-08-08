import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc51b2719860332b2ab4bd704dd40ce4c"
# Your Auth Token from twilio.com/console
auth_token = "64d22b37dcec208a1f52b61e1e92d1c6"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if(tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #print(f'No mes {mes}, o vendedor {vendedor} encontrou alguem com mais de {vendas}')
        message = client.messages.create(
            to="+5511943272962",
            from_="+14242688405",
            body="Hello from Python!")

        print(message.sid)
