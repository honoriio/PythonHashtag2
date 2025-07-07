import numpy as np

quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])

valor_total = np.dot(quantidades, precos)

print(f'O total de vendas do dia foi de: R${valor_total:.2f}')
