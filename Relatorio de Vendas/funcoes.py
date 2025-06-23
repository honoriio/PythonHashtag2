# Lugar dedicado as importações
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro():
    vendedor = input('Informe o nome do vendedor: ')
    vendas = input('Informe as vendas: ').replace(",", ".")
    vendas_corrigido = float(vendas)
    return vendedor, vendas_corrigido

def gerenciar_cadastro():
    lista_vendedores = {}

    while True:
        vendedor, vendas = cadastro()
        if vendedor in lista_vendedores:
            lista_vendedores[vendedor].append(vendas)  # Corrigido aqui
        else:
            lista_vendedores[vendedor] = [vendas]     # Corrigido aqui

        opc = input('Deseja continuar? (S/N): ').strip().upper()

        if opc in ['NAO', 'N', 'NÃO']:  # Corrigido aqui
            return lista_vendedores

def imprimir(lista_vendedores):
    print('\nResumo dos cadastros:')
    for nome, vendas in lista_vendedores.items():
        total = sum(vendas)
        media = total / len(vendas)
        print(f'Vendedor: {nome} | Vendas: {vendas}')
        print(f'Total: R$ {total:.2f} | Média: R$ {media:.2f}')
        print('-' * 60)