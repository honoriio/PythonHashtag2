# Local destinado às importações
from funcoes import gerenciar_cadastro, imprimir, ranking

def main():
    clientes = gerenciar_cadastro()
    resultados = ranking(clientes)
    imprimir(resultados)

if __name__ == '__main__':
    main()
