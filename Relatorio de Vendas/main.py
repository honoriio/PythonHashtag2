# Local destinado as importações 
from funcoes import gerenciar_cadastro, imprimir


def main():
    gerenciar_cadastro()
    imprimir(gerenciar_cadastro)

if __name__ == '__main__':
    main()
