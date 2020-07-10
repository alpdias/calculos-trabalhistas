'''
@Autor: Paulo https://github.com/alpdias
'''
# Programa principal
from datetime import date # Biblioteca de datas
import os # Biblioteca de comandos do sistema
from time import sleep # Biblioteca de tempo
import calculos # Biblioteca de cálculos
import tratamento # Biblioteca de tratamento
tratamento.barraDeProgresso() # Carrega barra de progresso
menuCalculos = ['Salário liquido', # Lista com as opções de cálculos apresentada no menu inicial
                'Décimo terceiro', 
                'INSS', 
                'IRRF', 
                'FGTS', 
                'Férias', 
                'Hora Extra', 
                'Saldo FGTS'] 
while True: # Loop do menu principal
    tratamento.idenficação() # Função para fazer a identificação do usuário
    print('-' * 80)
    ano = date.today().year # Variável que recebe o ano atual
    print(' ' * 26 + f'\033[0;36mCÁLCULOS TRABALHISTAS {ano}\033[m') # Título do programa
    print('-' * 80)
    for indice, lista in enumerate(menuCalculos): # Laço para gerar um indice na lista de opções
        print(f'\033[0;34m[{indice}]\033[m {lista}') # Imprimir a lista de opções
    print('\033[0;31m[99] ENCERRAR PROGRAMA\033[m') # Opção para encerrar programa
    print('-' * 80)
    try: # Tente executar os comandos
        while True: # Loop das opcões de cálculos
            escolha = int(input('ESCOLHA UMA OPÇÃO ACIMA: ')) # Variável que recebe a opção a ser executada
            if escolha == 0: # Opção para o cálculo de salário líquido
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True: 
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO SALÁRIO LÍQUIDO\033[m') # Título
                            print('-' * 80)
                            salarioLiquido = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário bruto
                            numDependentesSL = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes
                            outrosDescontos = float(input('Outros descontos: ')) # Variável que recebe o valor de outros descontos
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'Valor do INSS é de \033[0;32mR$ {tratamento.milhares(calculos.inss(salarioLiquido)[0])}\033[m', end='') # Resultado do cálculo do INSS
                            print(f', alíquota de {calculos.inss(salarioLiquido)[1]}%') # Alíquota utilizada para cálcular o INSS
                            if calculos.irrf((salarioLiquido - calculos.inss(salarioLiquido)[0]) - calculos.dependentes(numDependentesSL))[0] == 0: # Opção caso não tenha desconto de IRRF
                                print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário
                            else:
                                print(f'Valor do IRRF é de \033[0;32mR$ {tratamento.milhares(calculos.irrf((salarioLiquido - calculos.inss(salarioLiquido)[0]) - calculos.dependentes(numDependentesSL))[0])}\033[m', end='') # Resultado do cálculo do IRRF
                                print(f', alíquota de {calculos.irrf((salarioLiquido - calculos.inss(salarioLiquido)[0]) - calculos.Dependentes(numDependentesSL))[1]}%',) # Alíquota utilizada para cálcular o IRRF
                            print(f'Número de dependetes: \033[0;32m{numDependentesSL}\033[m') # Mostra o número de dependentes utilizado
                            print(f'Outros descontos: \033[0;32mR$ {tratamento.milhares(outrosDescontos)}\033[m') # Mostra o valor de outros descontos sobre o salário
                            print(f'O valor do salário líquido é de \033[0;32mR$ {tratamento.milhares(calculos.salarioLiquido(salarioLiquido, numDependentesSL, outrosDescontos))}\033[m') # Mostra o valor final do salário líquido
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o loop de cálculo e voltar ao menu principal
                    break
            elif escolha == 1: # Opção para o cálculo de décimo terceiro salário
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 22 + '\033[0;36mCÁLCULO DO DÉCIMO TERCEIRO SALÁRIO\033[m') # Título
                            print('-' * 80)
                            decimoTerceiro = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário
                            numDependentesDecimo = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes
                            print('(\033[0;31mConsiderar para o cálculo apenas os meses em que o trabalhador tenha trabalhado')
                            print(' mais de 15 dias no mês!\033[m)') # Aviso ao usuário
                            mesesDecimo = float(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'Valor da 1ª parcela do 13º salário é de \033[0;32mR$ {tratamento.milhares(calculos.adiantamento(decimoTerceiro, mesesDecimo))}\033[m') # Mostra o valor da 1ª parcela do 13º salário (adiantamento)
                            print(f'Valor da 2ª parcela do 13º salário é de \033[0;32mR$ {tratamento.milhares(calculos.decimo(decimoTerceiro, mesesDecimo, numDependentesDecimo))}\033[m') # Mostra o valor da 2ª parcela do 13º salário
                            print(f'Valor total a receber do 13º salário é de \033[0;32mR$ {tratamento.milhares(calculos.adiantamento(decimoTerceiro, mesesDecimo) + calculos.decimo(decimoTerceiro, mesesDecimo, numDependentesDecimo))}\033[m') # Mostra o total a receber do 13º
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break         
            elif escolha == 2: # Opção para o cálculo de INSS
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos.
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO VALOR DO INSS\033[m') # Título
                            print('-' * 80)
                            salarioInss = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'O valor do INSS é de \033[0;32mR$ {tratamento.milhares(cálculos.Inss(salarioInss)[0])}\033[m', end='') # Mostra o resultado do cálculo do INSS
                            print(f', alíquota de {calculos.inss(salarioInss)[1]}%') # Alíquota utilizada para cálcular o INSS
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha == 3: # Opção para o cálculo de IRRF
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO VALOR DO IRRF\033[m') # Título
                            print('-' * 80)
                            salarioIrrf = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário
                            numDependentesIrrf = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1.5)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            if calculos.irrf((salarioIrrf - calculos.inss(salarioIrrf)[0]) - calculos.dependentes(numDependentesIrrf))[0] == 0: # Opção caso não tenha o desconto de IRRF
                                print('\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m') # Aviso ao usuário
                            else:
                                print(f'O valor do IRRF é de \033[0;32mR$ {tratamento.milhares(calculos.irrf((salarioIrrf - calculos.inss(salarioIrrf)[0]) - calculos.dependentes(numDependentesIrrf))[0])}\033[m', end='') # Mostra o resultado do cálculo do IRRF
                                print(f', alíquota de {calculos.Irrf((salarioIrrf - calculos.Inss(salarioIrrf)[0]) - calculos.dependentes(numDependentesIrrf))[1]}%') # Alíquota utilizada para cálcular o IRRF
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha == 4: # Opção para o cálculo de FGTS
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 28 + '\033[0;36mCÁLCULO DO VALOR DO FGTS\033[m') # Título
                            print('-' * 80)
                            salarioFgts = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário bruto
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'Valor do FGTS é de R$ \033[0;32m{tratamento.milhares(calculos.fgts(salarioFgts))}\033[m', end='') # Mostra o resultado do cálculo do FGTS
                            print(', alíquota de 8%') # Alíquota utilizada para o cálculo do FGTS
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N': # Termina o loop
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha == 5: # Opção para o cálculo de férias
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 30 + '\033[0;36mCÁLCULO DE FÉRIAS\033[m') # Título
                            print('-' * 80)
                            salarioFerias = float(input('Salário bruto: ')) # Variável que recebe o valor do salário bruto
                            dependentesFerias = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes
                            mediaExtraFerias = float(input('Valor médio de horas extras no ano: ')) # Variável que recebe o valor médio de horas extras
                            while True:
                                diasFerias = int(input('Dias de férias: ')) # Variável que recebe o números de dias de férias
                                if diasFerias > 30:
                                    print('(\033[1;31mO número de dias de férias deve estar entre 10 e 30\033[m)')
                                elif diasFerias < 10:
                                    print('(\033[1;31mO número de dias de férias deve estar entre 10 e 30\033[m)')
                                else:
                                    break
                            while True:
                                abono = str(input('Abono pecuniário (Vender 1/3) \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção de cálculo para o abono
                                if abono == 'N':
                                    break
                                elif abono != 'S':
                                    print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m')
                                elif diasFerias <= 20 and abono == 'S':
                                    break
                                elif diasFerias > 20 and abono == 'S':
                                    print('(\033[1;31mPara cálculos de férias com abono pecuniário (venda 1/3) o valor máximo de dias\033[m')
                                    print('\033[1;31m de férias (dias gozados) é de 20 dias\033[m)')
                            while True:
                                adiantarTerco = str(input('Adiantar a 1ª parcela do 13º salário \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção para adiantar o 13º
                                if adiantarTerco == 'N':
                                    break
                                elif adiantarTerco != 'S':
                                    print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m')
                                elif adiantarTerco == 'S':
                                    break
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'Valor férias é de \033[0;32mR$ {tratamento.milhares(calculos.valorFerias(salarioFerias, diasFerias, mediaExtraFerias))}\033[m') # Mostra o valor férias cálculado
                            print(f'Valor de 1/3 sobre as férias é de \033[0;32mR$ {tratamento.milhares(calculos.valorFerias(salarioFerias, diasFerias, mediaExtraFerias) / 3)}\033[m') # Mostra o valor de 1/3 sobre as férias cálculado
                            if abono == 'S' and diasFerias <= 20: # Mostrar o resultado do cálculo do abono de acordo com opção escolhida
                                print(f'Valor do abono pecuniário é de \033[0;32mR$ {tratamento.milhares(((salarioFerias + mediaExtraFerias) / 3))}\033[m') # Mostra o valor cálculado para o abono
                                print(f'Valor de 1/3 do abono pecuniário é de \033[0;32mR$ {tratamento.milhares((((salarioFerias + mediaExtraFerias) / 3) / 3))}\033[m') # Mostra o valor cálculado de 1/3 sobre o abono
                            if adiantarTerco == 'S': # Opção para mostrar ou não valor do adiantamento do 13º
                                print(f'Valor do adiantamento da 1ª parcela do 3º salário é de \033[0;32mR$ {tratamento.milhares(calculos.adiantamento(salarioFerias, 12))}\033[m')  # Mostra o valor cálculado do adiantamento do 13º salário
                            baseImpostoFerias = (calculos.valorFerias(salarioFerias, diasFerias, mediaExtraFerias)) + (calculos.valorFerias(salarioFerias, diasFerias, mediaExtraFerias) / 3) # Recebe o valor base para calcular o INSS e o IRRF sobre as férias
                            print(f'Valor do INSS é de \033[0;32mR$ {tratamento.milhares(calculos.inss(baseImpostoFerias)[0])}\033[m', end='') # Mostra o cálculo do valor do INSS
                            print(f', alíquota de {calculos.Inss(baseImpostoFerias)[1]}%') # Mostra a alíquota utilizada para calcular o INSS
                            if calculos.Irrf((baseImpostoFerias - calculos.inss(baseImpostoFerias)[0]) - calculos.dependentes(dependentesFerias))[0] == 0: # Recebe o valor base para o cálculo do IRRF
                                print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário
                            else:
                                print(f'Valor do IRRF é de \033[0;32mR$ {tratamento.milhares(calculos.irrf((baseImpostoFerias - calculos.inss(baseImpostoFerias)[0]) - calculos.dependentes(dependentesFerias))[0])}\033[m', end='') # Mostra o valor cálculado do IRRF
                                print(f', alíquota de {calculos.irrf((baseImpostoFerias - calculos.inss(baseImpostoFerias)[0]) - calculos.dependentes(dependentesFerias))[1]}%') # Mostra a alíquota utilizada para calcular o IRRF
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N': # Termina o loop
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha == 6: # Opção para o cálculo de hora extra
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 29 + '\033[0;36mCÁLCULO DE HORA EXTRA\033[m') # Título
                            print('-' * 80)
                            salarioExtra = float(input('Salário base: ')) # Variável que recebe o salário base para o cálculo da hora extra
                            jornadaHoras = float(input('Jornada mensal (horas): ')) # Variável que recebe a quantidade de horas da jornada de trabalho
                            porcentagemExtra = int(input('Adicional hora extra (%): ')) # Variável que recebe a porcentagem do adicional de hora extra
                            quantidadeExtra = float(input('Número de horas extras: ')) # Variável que recebe a quantidade de horas extra trabalhadas
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'O valor da sua hora é \033[0;32mR$ {tratamento.milhares(calculos.hora(salarioExtra, jornadaHoras))}\033[m') # Mostra o cálculo do valor da hora
                            print(f'O valor da sua hora extra com adicional de {porcentagemExtra}%', end=' ') # Mostra a porcentagem utilizada para cálcular a hora
                            print(f'é de \033[0;32mR$ {tratamento.milhares(calculos.horaExtra(calculos.hora(salarioExtra, jornadaHoras), porcentagemExtra) + calculos.hora(salarioExtra, jornadaHoras))}\033[m') # Mostra o valor da hora extra cálculado
                            print(f'Quantidade de horas trabalhadas: \033[0;32m{quantidadeExtra:.2f}\033[m'.replace('.',':')) # Mostra a quantidade de horas utilizadas para fazer o cálculo
                            print(f'Valor total das horas extras \033[0;32mR$ {tratamento.milhares(((calculos.horaExtra(calculos.hora(salarioExtra, jornadaHoras), porcentagemExtra) + calculos.hora(salarioExtra, jornadaHoras)) * quantidadeExtra))}\033[m') # Mostra o valor total de horas extras cálculados 
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N': # Terminar o loop
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha == 7: # Opção para o cálculo de saldo do FGTS
                os.system('cls') or None # Comando para limpar a tela do terminal
                while True:
                    while True:
                        try: # Tente executar os comandos.
                            os.system('cls') or None # Comando para limpar a tela do terminal
                            print('-' * 80)
                            print(' ' * 26  + '\033[0;36mCÁLCULO DO SALDO DO FGTS\033[m') # Título
                            print('-' * 80)
                            salarioSaldoFgts = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário
                            mesesFgts = int(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados
                        except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1.5)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos
                            print(f'O saldo do FGTS é de +/- \033[0;32mR$ {tratamento.milhares(calculos.fgts(salarioSaldoFgts) * mesesFgts)}\033[m') # Resultado do cálculo do saldo do FGTS
                            print('-' * 80)
                            break
                    while True:
                        pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar
                        if pergunta == 'S' or pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário
                    if pergunta == 'N': # Termina o loop
                        os.system('cls') or None # Comando para limpar a tela do terminal
                        break
                if pergunta == 'N': # Terminar o cálculo e voltar ao menu principal
                    break
            elif escolha not in [0, 1, 2, 3, 4, 5, 6, 7]: # Terminar o menu de opções
                if escolha == 99:
                    break
                else: 
                    print('\033[0;31mERRO! Opção inválida, tente novamente.\033[m') # Aviso de entrada inválida
        if escolha == 99: # Opção para terminar o programa geral
            break # Termina o loop do menu de opções e encerrar
    except (ValueError, NameError): # Caso aconteça um 'ValueError' ou 'NameError' informe
        print('\033[0;31mERRO! Digite apenas valores validos, tente novamente!\033[m')
        sleep(1.5)
        os.system('cls') or None # Comando para limpar a tela do terminal
    except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa
        print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
        sleep(1)
        break
print('-' * 80)
print(' ' * 30 + '\033[1;31mFIM DO PROGRAMA\033[m') # Aviso de fim do programa
sleep(2) # Temporizador de 1 segundo
os.system('cls') or None # Comando para limpar a tela do terminal
tratamento.fecharPrograma() # Função para fechar o terminal de comando no windowns
