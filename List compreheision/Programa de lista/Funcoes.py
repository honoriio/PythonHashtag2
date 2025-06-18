# area destinada as importações
import os

def cabecalho(): # mostra a apresentação do programa e o seu menu.
    print('-' * 60)
    print('LISTA DE COMRPAS'.center(60))
    print('-' * 60)
        

def menu():
    lista_de_compras = {}
    while True:
        print('[1] - ADICIONAR ITEM')
        print('[2] - REMOVER ITEM')
        print('[3] - VER LISTA')
        print('[4] - SAIR')
        print('-' * 60) 
        opc = int(input('OPÇÃO: '))

        if opc == 1:
            limpar_tela()
            cabecalho()
            adicionar_item(lista_de_compras)

        elif opc == 2: 
            remover_item(lista_de_compras)


        elif opc == 3:
            ver_lista(lista_de_compras)
            
        elif opc == 4:
            print('*' * 60)
            print('PROGRAMA ENCERRADO')
            print('*' * 60)
            break
        else: 
            print('ESCOLHA UMA DAS OPÇÕES DISPONIVEIS')
    

def adicionar_item(lista):
    item = input('Informe o item: ')
    try:
        quantidade = int(input('Informe a quantidade: '))
    except ValueError:
        print("Quantidade inválida. Use apenas números inteiros.")
        return
    
    if item in lista: # se ja existe o item, o mesmo adiciona a quantia no intem existente
        lista[item] += quantidade
    else:
        lista[item] = quantidade


def remover_item(lista):
    item = input("Informe o nome do item que deseja remover: ").strip().lower()
    
    if item in lista:
        confirmacao = input(f"Tem certeza que deseja remover '{item}' da lista? (sim/não): ").strip().lower()
        if confirmacao == "sim":
            del lista[item]
            print(f"'{item}' removido da lista.")
        else:
            print("Remoção cancelada.")
    else:
        print("Item não encontrado na lista.")



def ver_lista(lista):
    if not lista:
        print("Lista de compras vazia.")
        return
    print("\nItens na sua lista:")
    print('-' * 30)
    for i, (item, qtd) in enumerate(lista.items(), start=1):
        print(f"{i}. {item.capitalize()} — {qtd} unidade(s)")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')