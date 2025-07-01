from collections import Counter

produtos_tecnologia = {
    'Smartphone': 3500.00,
    'Notebook': 5500.00,
    'Tablet': 2000.00,
    'Fone Bluetooth': 500.00,
    'Smartwatch': 1200.00,
    'Monitor 4K': 2500.00,
    'Teclado Mecânico': 450.00,
    'Mouse Gamer': 300.00
}


aux = Counter(produtos_tecnologia)

print(aux)
print('-' * 60)
print('-' * 60)
print('-' * 60)
print(produtos_tecnologia)
