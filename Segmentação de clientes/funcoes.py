# Lugar dedicado as importações
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro():
    while True:
        cliente = input('Informe o nome do comprador: ')
        compras = input('Informe o valor das compras: ').replace(",", ".")
        try:
            compras_corrigido = float(compras)
            break
        except ValueError:
            print('Valor informado invalido, Por favor informe um valor valido.')
    return cliente, compras_corrigido


def gerenciar_cadastro():
    lista_clientes = {}

    while True:
        cliente, compras = cadastro()
        if cliente in lista_clientes:
            lista_clientes[cliente].append(compras)  
        else:
            lista_clientes[cliente] = [compras]   

        opc = input('Deseja continuar? (S/N): ').strip().upper()

        if opc in ['NAO', 'N', 'NÃO']:  
            return lista_clientes
        

def ranking(lista_clientes):
    resultados = []
    for cliente, compras in lista_clientes.items():
        if isinstance(compras, list):
            total_compras = sum(compras)
        else:
            total_compras = compras

        if total_compras >= 5001:
            categoria = 'Ouro'
        elif 1001 < total_compras <= 5000:
            categoria = 'Prata'
        else:
            categoria = 'Bronze'

        resultados.append((cliente, total_compras, categoria))
    return resultados




def imprimir(resultados):
    for cliente, total_compras, categoria in resultados:
        print(f'Cliente: {cliente} | Total de Compras: R${total_compras:.2f} | Categoria: {categoria}')
        