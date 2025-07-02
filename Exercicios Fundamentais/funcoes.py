# Local dedicado as importações 


# Função criada para percorrer e converter os valores para float
def conversao(faturamento):
    dados_convertidos = {}

    for mes, valor in faturamento.items():
        valor = valor.replace('R$', '').replace('.', '').replace(',', '.').strip()
        valor_num = float(valor)
        
        dados_convertidos[mes] = valor_num  # Guarda o mês e o valor tratado
    
    return dados_convertidos  # Retorna tudo no final


def imposto_mensal(dados):
    iss = 0.05
    pis = 0.0065
    confis = 0.03 

    imposto = iss + pis + confis
    resultado_imposto_mensal = {}  # Cirado para armazenar o imposto calculado mensalmente. 
    
    for mes, valor in dados.items():
        valor_imposto_mensal = valor * imposto
        resultado_imposto_mensal[mes] = valor_imposto_mensal
        
    return resultado_imposto_mensal # retorna o imposto calculado mensalmente 
    

def imposto_trimestral(dados):
    # Valores dos impostos trimestrais. 
    ir = 0.048
    ir_adc = 0.10
    csll = 0.0288
    
    # Criar a função que faz o calculo do imposto trimestral
    return None



def dicionario(resultado_imposto_mensal, faturamentos):
    resultado = {}

    for mes in faturamentos.keys():
        resultado[mes] = {
            'faturamento': faturamentos[mes],
            'imposto_mensal': resultado_imposto_mensal.get(mes, 0)  # Caso não tenha imposto, usa 0
        }

    return resultado
