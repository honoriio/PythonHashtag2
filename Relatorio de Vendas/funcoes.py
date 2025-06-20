# Lugar dedicado as importações
import os 


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastro():
    while True:
        vendedor = input('Informe o nome do vednedor: ')
        vendas = input('Informe as vendas: ')

        vendas_corrigido = float(vendas)
        opc = input('Deseja sair?')
        if opc.upper() == 'SIM' or opc.upper() == 'S':
            print('Programa encerrado')
            
            break
    
    imprimir(vendas_corrigido)


def imprimir (vendas_corrigido):
    print(vendas_corrigido)
