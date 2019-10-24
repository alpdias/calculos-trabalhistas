'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
# Funções para realizar os cálculos trabalhistas.
def Inss(valor=0):
    """
    -> Função para cálcular o valor do INSS.
    :param valor: Valor do salário.
    :return: Retorna o valor do INSS e alíquota utilizada.
    """
    Inss = []
    if valor < 1751.81: 
        Inss.append((valor * 8) / 100) # Alíquota de 8%.
        Inss.append('8')
    elif valor >= 1751.81 and valor <= 2919.72:
        Inss.append((valor * 9) / 100) # Alíquota de 9%.
        Inss.append('9')
    elif valor >= 2919.72:
        Inss.append((valor * 11) / 100) # Alíquota de 11%.
        Inss.append('11')
    return Inss


def Dependentes(valor=0):
    """
    -> Função para cálcular o valor da dedução por dependetes.
    :param valor: Valor de base para o cálculo da dedução por dependetes.
    :return: Retorna o valor da dedução por dependentes.
    """
    Dependentes = 0
    if valor > 0:
        Dependentes = (valor * 189.59)
    return Dependentes


def Irrf(valor=0):
    """
    -> Função para cálcular o valor do IRRF.
    :param valor: Valor do salário.
    :return: Retorna o valor do IRRF e alíquota utilizada.
    """
    Irrf = []
    if valor < 1903.99:
        Irrf.append(0)
        Irrf.append(0)
    elif valor >= 1903.99 and valor <= 2826.65:
        Irrf.append((valor * 7.5) / 100 - 142.80) # Alíquota de 7.5% menos parcela de dedução.
        Irrf.append('7,5')
    elif valor >= 2826.66 and valor <= 3751.05:
        Irrf.append((valor * 15) / 100 - 354.80) # Alíquota de 15% menos parcela de dedução.
        Irrf.append('15')
    elif valor >= 3751.06 and valor <= 4664.68:
        Irrf.append((valor * 22.5) / 100 - 636.13) # Alíquota de 22.5% menos parcela de dedução.
        Irrf.append('22,5')
    elif valor > 4664.68:
        Irrf.append((valor * 27.5) / 100 - 869.36) # Alíquota de 27.5% menos parcela de dedução.
        Irrf.append('27,5')
    return Irrf 


def Fgts(valor=0):
    """
    -> Função para cálcular o valor do FGTS.
    :param valor: Valor do salário.
    :return: Retorna o valor do FGTS.
    """
    Fgts = (valor * 8) / 100
    return Fgts


def Adiantamento(valor=0, mes=0):
    """
    -> Função para cálcular o valor da primeira parcela do décimo terceiro (adiantamento).
    :param valor: Valor do salário.
    :param mes: Número de meses trabalhados.
    :return: Retorna o valor da primeira parcela do décimo terceiro (adiantamento).
    """
    Adiantamento = 0
    Adiantamento = (((valor / 12) * mes) / 2)
    return Adiantamento


def Decimo(valor=0, mes=0, dep=0):
    """
    -> Função para cálcular o valor da segunda parcela do décimo terceiro.
    :param valor: Valor do salário.
    :param mes: Número de meses trabalhados.
    :param dep: Número de dependentes.
    :return: Retorna o valor da segunda parcela do décimo terceiro.
    """
    Decimo = 0
    Decimo = ((valor / 12) * mes)
    CalculoBaseDependentes = Decimo - Inss(Decimo)[0]
    CalculoBaseIR = CalculoBaseDependentes - Dependentes(dep)
    CalculoDecimo = Decimo - Adiantamento(valor, mes) - Inss(Decimo)[0] - Irrf(CalculoBaseIR)[0]
    return CalculoDecimo


def SalarioLiquido(valor=0, dep=0, desc=0):
    """
    -> Função para cálcular o valor do salário líquido.
    :param valor: Valor do salário bruto.
    :param dep: Número de dependentes.
    :param desc: Valor de outros descontos.
    :return: Retorna o valor do salário liquido.
    """
    CalculoBaseIrrf = 0
    CalculoBaseIrrf = ((valor - Inss(valor)[0]) - Dependentes(dep))
    CalculoBaseSalario = Irrf(CalculoBaseIrrf)[0]
    CalculoFinalSalario = (((valor - Inss(valor)[0]) - CalculoBaseSalario) - desc)
    return CalculoFinalSalario


def Hora(valor=0, quant=0):
    """
    -> Função para cálcular o valor da hora/trabalho.
    :param valor: Valor do salário.
    :param quant: Quantidade da jornada de horas/trabalho no mês.
    :return: Retorna o valor da hora/trabalho.
    """
    Hora = (valor / quant)
    return Hora


def HoraExtra(valor=0, porc=0):
    """
    -> Função para cálcular o valor da hora extra.
    :param valor: Valor do salário.
    :param porc: Valor em porcentagem do adicional de hora extra.
    :return: Retorna o valor da hora extra.
    """
    HoraExtra = (valor * (porc / 100))
    return HoraExtra

    