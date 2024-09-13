import random
# Tela de apresentação e escolhas de digitos.
print('=' * 42)
print(f'GERADOR DE CHAVES DE SEGURANÇA'.center(42))
print('=' * 42)
print(f'ESCOLHA QUANTOS DIGITOS DESEJA'.center(42))
print(f'[1]  6 DIGITOS'.center(42))
print(f'[2]  8 DIGITOS'.center(42))
print(f'[3] 10 DIGITOS'.center(42))
print(f'[4] 12 DIGITOS'.center(42))
print(f'[5] 14 DIGITOS'.center(42))
print(f'[6] 16 DIGITOS'.center(42))
print(f'=' * 42)
escolha = int(input('Informe o valor desejado: '))
digito = 0

#Condicional para atribuir o valor escolhido

if 1 <= escolha <= 6:
    if escolha == 1:
        digito = 6
    elif escolha == 2:
        digito = 8
    elif escolha == 3:
        digito = 10
    elif escolha == 4:
        digito = 12
    elif escolha == 5:
        digito = 14
    elif escolha == 6:
        digito = 16
else:
    print('Escolha inválida, usando o padrão de 6 dígitos.')
    digito = 6

# Dicionario feito para gerar as chaves aleatorias

dicionario = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    ',', '.', '<', '>', '/', '?'
]
# Ajusta a quantidade de números, letras e caracteres especiais com base no tamanho escolhido
qtd_numeros = digito // 3
qtd_letras = digito // 3
qtd_caracteres = digito - qtd_numeros - qtd_letras

# Gera a chave aleatória
chave = random.choices(dicionario[:10], k=qtd_numeros) + random.choices(dicionario[10:62], k=qtd_letras) + random.choices(dicionario[62:], k=qtd_caracteres)
resultado = ''.join(chave)

print('A opção {} que contem {} Digitos'.format(escolha, digito))
print(f'=' * 42)
print('\033[31mCHAVE GERADA:\033[0m', end=' ')
print('\033[32m', resultado, '\033[0m')
print(f'=' * 42)
print('PROGRAMA FINALIZADO')