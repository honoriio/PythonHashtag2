import numpy as np

precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])

preco_maximo = np.max(precos)

preco_minimo = np.min(precos)

variacao_precos = np.std(precos)

print(f'O preço maximo foi de: {preco_maximo}')
print(f'O preço minimo de foi de: {preco_minimo}')
print(f'Ouve uma variação de preços durante a semana de: {variacao_precos:.2f}.%')