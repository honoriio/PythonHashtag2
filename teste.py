import numpy as np

carros = {'BMW': 5000,
          'AUDI': 8000}

juros = 1.9

# Somando os valores dos carros
carros_juros = np.sum([carros['BMW'], carros['AUDI']])

print(carros_juros)
