# Lugar dedicado as importações
import os 


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastro(): # Essa função coleta os dados dos vendedores e suas vendas
        vendedor = input('Informe o nome do vendedor: ')
        vendas = input('Informe as vendas: ').replace("," , ".")

        vendas_corrigido = float(vendas)
        return vendedor, vendas_corrigido
        
    
    

def gerenciar_cadastro():
    lista_vendedores = []

    while True:
         vendedor, vendas = cadastro()
         lista_vendedores.append((vendedor, vendas))

         opc = input('Deseja sair?: ').upper()

         if opc == 'SIM' or opc == 'S':
              continue
         else:
              return lista_vendedores 


def imprimir (lista_vendedores):
    print('\nResumo dos cadastros:')
    for nome, valor in lista_vendedores:
        print(f'Vendedor: {nome} | Vendas: R$ {valor:.2f}')

