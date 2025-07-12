import pandas as pd
from IPython.display import display

vendas_df = pd.read_csv(r'Pandas/Contoso - Vendas - 2017.csv', sep=';')  # OK
produtos_df = pd.read_csv(r'Pandas/Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1') #ok
lojas_df = pd.read_csv(r'Pandas/Contoso - Lojas.csv', sep=';', encoding='latin1') #ok
clientes_df = pd.read_csv(r'Pandas/Contoso - Clientes.csv', sep=';', encoding='latin1') #ok

# Essa parte do codigo retira o caracter indesejado no inicio das colunas
produtos_df.columns = produtos_df.columns.str.strip().str.replace('ÿ', '')
lojas_df.columns = lojas_df.columns.str.strip().str.replace('ÿ', '')
clientes_df.columns = clientes_df.columns.str.strip().str.replace('ÿ', '')


# essa parte do codigo coleta somente as colunas que preciso usar para fazer o marge entre as tabelas. 
vendas_df = vendas_df[['ID Produto']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]
clientes_df = clientes_df[['ID Cliente', 'E-mail']]


# essa parte esta com erro, o mesmo dis que a Key esta incorreta, no caso as keys de Lojas_df e Clientes_df
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')



display(vendas_df)

