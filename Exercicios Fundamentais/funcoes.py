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
    resultado_trimestral = {}
    
    # Alíquotas
    ir = 0.048
    ir_adc = 0.10  # Adicional sobre o que passar de 20 mil trimestral
    csll = 0.0288

    imposto = ir + csll

    # Separar os meses por trimestre
    meses = list(dados.keys())
    
    for i in range(0, len(meses), 3):
        trimestre = meses[i:i+3]
        soma_trimestre = sum([dados[mes] for mes in trimestre])
        
        valor_imposto_tri = soma_trimestre * imposto

        # Se exceder 20 mil, calcular o IR adicional
        ir_adicional = 0
        if soma_trimestre > 20000:
            excesso = soma_trimestre - 20000
            ir_adicional = excesso * ir_adc
        
        resultado_trimestral[f'Trimestre {i//3 + 1}'] = {
            'Faturamento': soma_trimestre,
            'Imposto': valor_imposto_tri,
            'IR Adicional': ir_adicional,
            'Imposto Total': valor_imposto_tri + ir_adicional
        }

    return resultado_trimestral



def dicionario(resultado_imposto_mensal, resultado_imposto_trimestral, faturamentos):
    resultado = {}

    for mes in faturamentos.keys():
        resultado[mes] = (
            faturamentos[mes],  # Faturamento
            resultado_imposto_mensal.get(mes, 0),  # Imposto mensal
            resultado_imposto_trimestral.get(mes, 0)  # Imposto trimestral
        )

    return resultado
