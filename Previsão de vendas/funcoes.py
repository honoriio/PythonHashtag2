# Local destinado as importações
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho():
    print('=' * 60)
    print('PREVISÃO DE VENDAS'.center(60))
    print('=' * 60)


def menu():
    previsoes_de_vendas = {}
    while True: 
        print('[1] - PREVISÃO DE VENDAS.')
        print('[2] - VER LISTA')
        print('[3] - VER LISTA DE PROJEÇÃO')
        print('[4] - SAIR')
        print('-' * 60)
        opc = int(input('Informe uma opção: '))

        if opc == 1:
            adicionar_item(previsoes_de_vendas)

        
        elif opc == 2:
            ver_lista(previsoes_de_vendas)
            
        elif opc == 3:
            calculo_taxa(previsoes_de_vendas)
        

        elif opc == 4:
            limpar_tela()
            print('=' * 60)
            print('O PROGRAMA FOI ENCERRADO')
            print('=' * 60)
            time.sleep(3)
            limpar_tela()
            break

        else:
            print('Escolha uma das opções disponiveis')
            

def adicionar_item(lista):
    produto = input('Digite o nome do produto: ')
    try:
        vendas = float(input('Informe as vendas do mes atual: '))
        taxa = float(input('Informe a taxa de crescimento: '))
        lista[produto] = vendas, taxa
    except ValueError:
        print('Valor ifnormado invalido, por favor informe somente números.')
    
    

def ver_lista(lista):
    if not lista:
        print("Previsão de vendas Vazia")
        return
    print("\nItens na sua lista:")
    print('-' * 30)
    for i, (produto, (vendas ,taxa)) in enumerate(lista.items(), start=1):
        print(f"{i}. {produto.capitalize()} — {vendas} unidade(s) taxa de crescimento {taxa}%")


def calculo_taxa(lista):
    for produto, (vendas, taxa) in lista.items():
        projecao_crescimento = vendas * (1 + taxa / 100)
        print(f"  Produto: {produto}")
        print(f"  Vendas atuais: R$ {vendas}")
        print(f"  Taxa de crescimento: {taxa}%")
        print(f"  Projeção de crescimento: R$ {projecao_crescimento:.2f}")
        print('-' * 60)

