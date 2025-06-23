# Local destinado as importações 
from funcoes import gerenciar_cadastro, imprimir


def main():
    vendedores = gerenciar_cadastro()
    imprimir(vendedores)

if __name__ == '__main__':
    main()
