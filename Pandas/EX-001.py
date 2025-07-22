import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Leitura dos arquivos
vendas_df = pd.read_csv(r'Pandas/Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Pandas/Contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
lojas_df = pd.read_csv(r'Pandas/Contoso - Lojas.csv', sep=';', encoding='latin1')
clientes_df = pd.read_csv(r'Pandas/Contoso - Clientes.csv', sep=';', encoding='latin1')

# Limpeza de caracteres indesejados nos nomes das colunas
produtos_df.columns = produtos_df.columns.str.strip().str.replace('ÿ', '')
lojas_df.columns = lojas_df.columns.str.strip().str.replace('ÿ', '')
clientes_df.columns = clientes_df.columns.str.strip().str.replace('ÿ', '')

# Seleção das colunas necessárias nos DataFrames auxiliares
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]
clientes_df = clientes_df[['ID Cliente', 'E-mail']]

# Realizando os merges
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')


# Renomeia a coluna.
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})


frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()


# Exibição
display(frequencia_clientes)
frequencia_clientes[:5].plot(figsize=(15, 5))
plt.show()
