# Analise basica de vendas 
import numpy as np

rng = np.random.default_rng(seed=0)

dados_vendas = rng.integers(low=50, high=200, size=30)

maior_venda = np.argmax(dados_vendas) + 1
menor_venda = np.argmin(dados_vendas) + 1

print(f'Dia com a maior venda: {maior_venda}')
print(f'Dia com a menor venda: {menor_venda}')
