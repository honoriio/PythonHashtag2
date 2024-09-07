# Funções e variaveis locais
var = 7

def mudar_e_imprimir():
    global var
    var = 13
    print(f'Valor da variavel dentro da função: {var}')


print(f'Variavel fora da função: {var}')
mudar_e_imprimir()
print(f'Variavel depois de mudar {var}')
