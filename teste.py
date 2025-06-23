
vendedores = {}

while True:
    
    vendedor = input('Informe o nome do vendedor: ')
    vendas = float(input('Innforme a quantia de vendas: '))

    vendedores [vendedor] = vendas

    opc = input('Deseja sair? ')

    if opc == 'nao':
        break
    else:
        continue

print(vendedores)