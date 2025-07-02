# Area destianda as importações
from funcoes import conversao, imposto_mensal, dicionario

# Dicionario de faturamento mensal
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

faturamento_convertido = conversao(faturamento)
imposto = imposto_mensal(faturamento_convertido)

dicionario(imposto, faturamento)
