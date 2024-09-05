area_a_ser_pintada = float(input('Informe a Area em metros quadrados: '))

quantia_litro = 6

lata_grande = 18
valor_lata_grande = 80

galao = 3.6
valor_galao = 25


def calculo_litros(area, litros):  # Lembrete, Não preciso usar o nome externo das variaveis criadas enteriormente, usaremos somente parametros.
    litros_a_serem_usados = area / litros
    quantia_lata = litros_a_serem_usados / lata_grande
    quantia_galao = litros_a_serem_usados / galao

    if quantia_lata > int(quantia_lata):
        quantia_lata = int(quantia_lata) + 1

    if quantia_galao > int(quantia_galao):
        quantia_galao = int(quantia_galao) + 1

    print('-' * 60)
    print('Informe o que deseja'.center(60))
    print('-' * 60)
    print('[1] - Lata de 18 Litros')
    print('[2] - Galões de 3.6 litros')
    print('[3] - Misturar Galões e Latas "Essa opção gera menor desperdicio de tinta."')
    print('-' * 60)
    opcao = int(input('Opção: '))

    if opcao == 1:
        custo_lata_grande = quantia_lata * valor_lata_grande
        return custo_lata_grande, quantia_lata, "Latas de 18 Litros"
    elif opcao == 2:
        custo_galao = quantia_galao * valor_galao
        return custo_galao, quantia_galao, "Galões de 3.6 Litros"
    elif opcao == 3:
        pass



    return litros_a_serem_usados, quantia_lata, quantia_galao


resultado = calculo_litros(area_a_ser_pintada, quantia_litro)

print(f'Resultado: {resultado}')
