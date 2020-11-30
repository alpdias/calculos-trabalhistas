'''
@Autor: Paulo https://github.com/alpdias
'''

def inss(valor=0):
    
    """
    -> Função para cálcular o valor do INSS.
    :param valor: Valor do salário.
    :return: Retorna o valor do INSS e alíquota utilizada.
    """
    
    inss = []
    if valor < 1751.81: 
        inss.append((valor * 8) / 100) # Alíquota de 8%.
        inss.append('8')
        
    elif valor >= 1751.81 and valor <= 2919.72:
        inss.append((valor * 9) / 100) # Alíquota de 9%.
        inss.append('9')
        
    elif valor >= 2919.72:
        inss.append((valor * 11) / 100) # Alíquota de 11%.
        inss.append('11')
        
    return inss


def dependentes(valor=0):
    
    """
    -> Função para cálcular o valor da dedução por dependetes.
    :param valor: Valor de base para o cálculo da dedução por dependetes.
    :return: Retorna o valor da dedução por dependentes.
    """
    
    dependentes = 0
    
    if valor > 0:
        dependentes = (valor * 189.59)
        
    return dependentes


def irrf(valor=0):
    
    """
    -> Função para cálcular o valor do IRRF.
    :param valor: Valor base do salário para cálculo do IRRF.
    :return: Retorna o valor do IRRF e alíquota utilizada.
    """
    
    irrf = []
    
    if valor < 1903.99:
        irrf.append(0)
        irrf.append(0)
        
    elif valor >= 1903.99 and valor <= 2826.65:
        irrf.append((valor * 7.5) / 100 - 142.80) # Alíquota de 7.5%, menos parcela de dedução.
        irrf.append('7,5')
        
    elif valor >= 2826.66 and valor <= 3751.05:
        irrf.append((valor * 15) / 100 - 354.80) # Alíquota de 15%, menos parcela de dedução.
        irrf.append('15')
        
    elif valor >= 3751.06 and valor <= 4664.68:
        irrf.append((valor * 22.5) / 100 - 636.13) # Alíquota de 22.5%, menos parcela de dedução.
        irrf.append('22,5')
        
    elif valor > 4664.68:
        irrf.append((valor * 27.5) / 100 - 869.36) # Alíquota de 27.5%, menos parcela de dedução.
        irrf.append('27,5')
        
    return irrf 


def fgts(valor=0):
    
    """
    -> Função para cálcular o valor do FGTS.
    :param valor: Valor do salário.
    :return: Retorna o valor do FGTS.
    """
    
    fgts = (valor * 8) / 100
    
    return fgts


def adiantamento(valor=0, mes=0):
    
    """
    -> Função para cálcular o valor da primeira parcela do décimo terceiro (adiantamento).
    :param valor: Valor do salário.
    :param mes: Número de meses trabalhados.
    :return: Retorna o valor da primeira parcela do décimo terceiro (adiantamento).
    """
    
    adiantamento = 0
    
    adiantamento = (((valor / 12) * mes) / 2)
    
    return adiantamento


def decimo(valor=0, mes=0, dep=0):
    
    """
    -> Função para cálcular o valor da segunda parcela do décimo terceiro.
    :param valor: Valor base do salário para cálcular a segunda parcela do décimo terceiro.
    :param mes: Número de meses trabalhados.
    :param dep: Número de dependentes.
    :return: Retorna o valor da segunda parcela do décimo terceiro.
    """
    
    decimo = 0
    
    decimo = ((valor / 12) * mes)
    
    calculoBaseDependentes = decimo - inss(decimo)[0]
    
    calculoBaseIR = calculoBaseDependentes - dependentes(dep)
    
    calculoDecimo = decimo - adiantamento(valor, mes) - inss(decimo)[0] - irrf(calculoBaseIR)[0]
    
    return calculoDecimo


def salarioLiquido(valor=0, dep=0, desc=0):
    
    """
    -> Função para cálcular o valor do salário líquido.
    :param valor: Valor do salário bruto.
    :param dep: Número de dependentes.
    :param desc: Valor de outros descontos.
    :return: Retorna o valor do salário liquido.
    """
    
    calculoBaseIrrf = 0
    
    calculoBaseIrrf = ((valor - inss(valor)[0]) - dependentes(dep))
    
    calculoBaseSalario = irrf(calculoBaseIrrf)[0]
    
    calculoFinalSalario = (((valor - inss(valor)[0]) - calculoBaseSalario) - desc)
    
    return calculoFinalSalario


def hora(valor=0, quant=0):
    
    """
    -> Função para cálcular o valor da hora/trabalho.
    :param valor: Valor do salário.
    :param quant: Quantidade da jornada de hora/trabalho no mês.
    :return: Retorna o valor da hora/trabalho.
    """
    
    hora = (valor / quant)
    
    return hora


def horaExtra(valor=0, porc=0):
    
    """
    -> Função para cálcular o valor da hora extra.
    :param valor: Valor do salário.
    :param porc: Valor em porcentagem do adicional de hora extra.
    :return: Retorna o valor da hora extra.
    """
    
    horaExtra = (valor * (porc / 100))
    
    return horaExtra


def valorFerias(valor=0, dias=0, extra=0):
    
    """
    -> Função para cálcular o valor férias.
    :param valor: Valor do salário base.
    :param dias: Quantidade de dias de férias.
    :param extra: Valor da média de horas extras no ano.
    :return: Retorna o valor férias.
    """
    
    baseValorFerias = ((valor / 30) * dias)
    
    baseValorExtra = ((extra / 30) * dias)
    
    valorFerias = (baseValorFerias + baseValorExtra)
    
    return valorFerias

