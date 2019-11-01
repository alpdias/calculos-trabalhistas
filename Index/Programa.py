'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
# Programa principal.
from datetime import date # Biblioteca de datas.
import os # Biblioteca de comandos do sistema.
from time import sleep # Biblioteca de tempo.
import Cálculos # Biblioteca de cálculos.
import Tratamento # Biblioteca de tratamento.
Tratamento.BarraDeProgresso() # Carrega barra de progresso.
MenuCalculos = ['Salário liquido', # Lista com as opções de cálculos apresentada no menu inicial.
                'Décimo terceiro', 
                'INSS', 
                'IRRF', 
                'FGTS', 
                'Férias', 
                'Hora Extra', 
                'Saldo FGTS'] 
while True: # Loop do menu principal.
    Tratamento.Idenficação() # Função p/ Identificação do usuário.
    print('-' * 80)
    Ano = date.today().year # Variável que recebe o ano atual.
    print(' ' * 26 + f'\033[0;36mCÁLCULOS TRABALHISTAS {Ano}\033[m') # Título do programa.
    print('-' * 80)
    for Indice, Lista in enumerate(MenuCalculos): # Laço para gerar um indice na lista de opções.
            print(f'\033[0;34m[{Indice}]\033[m {Lista}') # Imprimir a lista de opções.
    print('\033[0;31m[99] ENCERRAR PROGRAMA\033[m') # Opção para encerrar programa.
    print('-' * 80)
    try: # Tente executar os comandos.
        while True: # Loop das opcões de cálculos.
            Escolha = int(input('ESCOLHA UMA OPÇÃO ACIMA: ')) # Variável que recebe a opção a ser executada.
            if Escolha == 0: # Opção para o cálculo de salário líquido.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True: 
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO SALÁRIO LÍQUIDO\033[m') # Título.
                            print('-' * 80)
                            SalarioLiquido = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário bruto.
                            NumDependentesSL = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes.
                            OutrosDescontos = float(input('Outros descontos: ')) # Variável que recebe o valor de outros descontos.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'Valor do INSS é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Inss(SalarioLiquido)[0])}\033[m', end='') # Resultado do cálculo do INSS.
                            print(f', alíquota de {Cálculos.Inss(SalarioLiquido)[1]}%') # Alíquota utilizada para cálcular o INSS.
                            if Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[0] == 0: # Opção caso não tenha desconto de IRRF.
                                print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário.
                            else:
                                print(f'Valor do IRRF é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[0])}\033[m', end='') # Resultado do cálculo do IRRF.
                                print(f', alíquota de {Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[1]}%',) # Alíquota utilizada para cálcular o IRRF.
                            print(f'Número de dependetes: \033[0;32m{NumDependentesSL}\033[m') # Mostra o número de dependentes utilizado.
                            print(f'Outros descontos: \033[0;32mR$ {Tratamento.Milhares(OutrosDescontos)}\033[m') # Mostra o valor de outros descontos sobre o salário.
                            print(f'O valor do salário líquido é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.SalarioLiquido(SalarioLiquido, NumDependentesSL, OutrosDescontos))}\033[m') # Mostra o valor final do salário líquido.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o loop de cálculo e voltar ao menu principal.
                    break
            elif Escolha == 1: # Opção para o cálculo de décimo terceiro salário.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 22 + '\033[0;36mCÁLCULO DO DÉCIMO TERCEIRO SALÁRIO\033[m') # Título.
                            print('-' * 80)
                            DecimoTerceiro = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário.
                            NumDependentesDecimo = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes.
                            print('(\033[0;31mConsiderar para o cálculo apenas os meses em que o trabalhador tenha trabalhado')
                            print(' mais de 15 dias no mês!\033[m)') # Aviso ao usuário.
                            MesesDecimo = float(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'Valor da 1ª parcela do 13º salário é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Adiantamento(DecimoTerceiro, MesesDecimo))}\033[m') # Mostra o valor da 1ª parcela do 13º salário (adiantamento).
                            print(f'Valor da 2ª parcela do 13º salário é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Decimo(DecimoTerceiro, MesesDecimo, NumDependentesDecimo))}\033[m') # Mostra o valor da 2ª parcela do 13º salário.
                            print(f'Valor total a receber do 13º salário é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Adiantamento(DecimoTerceiro, MesesDecimo) + Cálculos.Decimo(DecimoTerceiro, MesesDecimo, NumDependentesDecimo))}\033[m') # Mostra o total a receber do 13º.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break         
            elif Escolha == 2: # Opção para o cálculo de INSS.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO VALOR DO INSS\033[m') # Título.
                            print('-' * 80)
                            SalarioInss = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'O valor do INSS é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Inss(SalarioInss)[0])}\033[m', end='') # Mostra o resultado do cálculo do INSS.
                            print(f', alíquota de {Cálculos.Inss(SalarioInss)[1]}%') # Alíquota utilizada para cálcular o INSS.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break
            elif Escolha == 3: # Opção para o cálculo de IRRF.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 26 + '\033[0;36mCÁLCULO DO VALOR DO IRRF\033[m') # Título.
                            print('-' * 80)
                            SalarioIrrf = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário.
                            NumDependentesIrrf = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            if Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[0] == 0: # Opção caso não tenha o desconto de IRRF.
                                print('\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m') # Aviso ao usuário.
                            else:
                                print(f'O valor do IRRF é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[0])}\033[m', end='') # Mostra o resultado do cálculo do IRRF.
                                print(f', alíquota de {Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[1]}%') # Alíquota utilizada para cálcular o IRRF.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N':
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break
            elif Escolha == 4: # Opção para o cálculo de FGTS.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 28 + '\033[0;36mCÁLCULO DO VALOR DO FGTS\033[m') # Título.
                            print('-' * 80)
                            SalarioFgts = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário bruto.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'Valor do FGTS é de R$ \033[0;32m{Tratamento.Milhares(Cálculos.Fgts(SalarioFgts))}\033[m', end='') # Mostra o resultado do cálculo do FGTS.
                            print(', alíquota de 8%') # Alíquota utilizada para o cálculo do FGTS.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N': # Termina o loop.
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break
            elif Escolha == 5: # Opção para o cálculo de férias. 
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 33 + '\033[0;36mCÁLCULO DE FÉRIAS\033[m') # Título.
                            print('-' * 80)
                            SalarioFerias = float(input('Salário bruto: ')) # Variável que recebe o valor do salário bruto.
                            DependentesFerias = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes.
                            MediaExtraFerias = float(input('Valor médio de horas extras no ano: ')) # Variável que recebe o valor médio de horas extras.
                            while True:
                                DiasFerias = int(input('Dias de férias: ')) # Variável que recebe o números de dias de férias.
                                if DiasFerias > 30:
                                    print('(\033[1;31mO número de dias de férias deve estar entre 10 e 30\033[m)')
                                elif DiasFerias < 10:
                                    print('(\033[1;31mO número de dias de férias deve estar entre 10 e 30\033[m)')
                                else:
                                    break
                            while True:
                                Abono = str(input('Abono pecuniário (Vender 1/3) \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção de cálculo para o abono.
                                if DiasFerias > 20 and Abono == 'S':
                                    print('(\033[1;31mPara cálculos de férias com abono pecuniário (venda 1/3) o\033[m')
                                    print('\033[1;31mvalor máximo de dias de férias (dias gozados) é de 20 dias\033[m)')
                                else:
                                    break
                            AdiantarTerco = str(input('Adiantar a 1ª parcela do 13º salário \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção para adiantar o 13º.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'Valor férias é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias))}\033[m') # Mostra o valor férias cálculado.
                            print(f'Valor de 1/3 sobre as férias é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias) / 3)}\033[m') # Mostra o valor de 1/3 sobre as férias cálculado.
                            if Abono == 'S' and DiasFerias <= 20: # Mostrar o resultado do cálculo do abono de acordo com opção escolhida.
                                print(f'Valor do abono pecuniário é de \033[0;32mR$ {Tratamento.Milhares(((SalarioFerias + MediaExtraFerias) / 3))}\033[m') # Mostra o valor cálculado para o abono.
                                print(f'Valor de 1/3 do abono pecuniário é de \033[0;32mR$ {Tratamento.Milhares((((SalarioFerias + MediaExtraFerias) / 3) / 3))}\033[m') # Mostra o valor cálculado de 1/3 sobre o abono.
                            if AdiantarTerco == 'S': # Opção para mostrar ou não valor do adiantamento do 13º.
                                print(f'Valor do adiantamento da 1ª parcela do 3º salário é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Adiantamento(SalarioFerias, 12))}\033[m')  # Mostra o valor cálculado do adiantamento do 13º salário.
                            BaseImpostoFerias = (Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias)) + (Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias) / 3) # Recebe o valor base para calcular o INSS e o IRRF sobre as férias.
                            print(f'Valor do INSS é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Inss(BaseImpostoFerias)[0])}\033[m', end='') # Mostra o cálculo do valor do INSS.
                            print(f', alíquota de {Cálculos.Inss(BaseImpostoFerias)[1]}%') # Mostra a alíquota utilizada para calcular o INSS.
                            if Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[0] == 0: # Recebe o valor base para o cálculo do IRRF.
                                print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário.
                            else:
                                print(f'Valor do IRRF é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[0])}\033[m', end='') # Mostra o valor cálculado do IRRF.
                                print(f', alíquota de {Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[1]}%') # Mostra a alíquota utilizada para calcular o IRRF.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N': # Termina o loop.
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break
            elif Escolha == 6: # Opção para o cálculo de hora extra.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    print('-' * 80)
                    print(' ' * 29 + '\033[0;36mCÁLCULO DE HORA EXTRA\033[m') # Título.
                    print('-' * 80)
                    MenuHoraExtra = ['Valor HORA EXTRA', 'Total HORA EXTRA'] # Lista com as opções de para hora extra.
                    for IndiceExtra, ListaExtra in enumerate(MenuHoraExtra):
                        print(f'\033[0;34m[{IndiceExtra}]\033[m {ListaExtra}') # Imprimir a lista de opções.
                    print('\033[0;31m[88] VOLTAR AO MENU\033[m') # Opção para voltar ao menu principal.
                    print('-' * 80)
                    while True:
                        EscolhaExtra = int(input('ESCOLHA UMA OPÇÃO ACIMA: ')) # Variável que recebe a opção a ser executada.
                        if EscolhaExtra == 0: # Opção para o cálculo do valor da hora extra.
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            while True:
                                while True:
                                    try:
                                        os.system('cls') or None # Comando para limpar a tela do terminal.
                                        print('-' * 80)
                                        print(' ' * 26 + '\033[0;36mCÁLCULO DO VALOR HORA EXTRA\033[m') # Título.
                                        print('-' * 80)
                                        SalarioExtra = float(input('Salário base: ')) # Variável que recebe o salário base para o cálculo da hora extra.
                                        JornadaHoras = float(input('Jornada mensal (horas): ')) # Variável que recebe a quantidade de horas da jornada de trabalho.
                                        PorcentagemExtra = int(input('Adicional hora extra (%): ')) # Variável que recebe a porcentagem do adicional de hora extra.
                                    except ValueError: # Caso aconteça um 'ValueError' informe.
                                        print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                                        sleep(1)
                                        os.system('cls') or None
                                    except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                                        print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                                        sleep(1)
                                        print('-' * 80)
                                        break
                                    else:
                                        print(' ')
                                        print('Cálculando... Aguarde!')
                                        print(' ')
                                        sleep(0.75) # Temporizador de 0.75 segundos.
                                        print(f'O valor da sua hora é \033[0;32mR$ {Tratamento.Milhares(Cálculos.Hora(SalarioExtra, JornadaHoras))}\033[m') # Mostra o cálculo do valor da hora.
                                        print(f'O valor da sua hora extra com adicional de {PorcentagemExtra}%', end=' ') # Mostra a porcentagem utilizada para cálcular a hora.
                                        print(f'é de \033[0;32mR$ {Tratamento.Milhares(Cálculos.HoraExtra(Cálculos.Hora(SalarioExtra, JornadaHoras), PorcentagemExtra) + Cálculos.Hora(SalarioExtra, JornadaHoras))}\033[m') # Mostra o valor da hora extra cálculado.
                                        print('-' * 80)
                                        break
                                while True:
                                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o primeiro cálculo.
                                    if Pergunta == 'S' or Pergunta == 'N':
                                        print('-' * 80)
                                        break 
                                    print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                                if Pergunta == 'N': # Terminar o loop.
                                    os.system('cls') or None # Comando para limpar a tela do terminal.
                                    break
                            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu de hora extra.
                                break
                        elif EscolhaExtra == 1: # Opção para o cálculo do valor total da hora extra.
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            while True:
                                while True:
                                    try:
                                        os.system('cls') or None # Comando para limpar a tela do terminal.
                                        print('-' * 80)
                                        print(' ' * 24 + '\033[0;36mCÁLCULO DO VALOR TOTAL HORA EXTRA\033[m') # Título.
                                        print('-' * 80)
                                        SalarioExtra = float(input('Salário base: ')) # Variável que recebe o salário base para o cálculo da hora extra.
                                        JornadaHoras = float(input('Jornada mensal (horas): ')) # Variável que recebe a quantidade de horas da jornada de trabalho.
                                        PorcentagemExtra = int(input('Adicional hora extra (%): ')) # Variável que recebe a porcentagem do adicional de hora extra.
                                        QuantidadeExtra = float(input('Número de horas extras: ')) # Variável que recebe a quantidade de horas extra trabalhadas.
                                    except ValueError: # Caso aconteça um 'ValueError' informe.
                                        print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                                        sleep(1)
                                        os.system('cls') or None
                                    except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                                        print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                                        sleep(1)
                                        print('-' * 80)
                                        break
                                    else:
                                        print(' ')
                                        print('Cálculando... Aguarde!')
                                        print(' ')
                                        sleep(0.75) # Temporizador de 0.75 segundos.
                                        print(f'Quantidade de horas trabalhadas: \033[0;32m{QuantidadeExtra:.2f}\033[m'.replace('.',':')) # Mostra a quantidade de horas utilizadas para fazer o cálculo.
                                        print(f'Valor total das horas extras \033[0;32mR$ {Tratamento.Milhares(((Cálculos.HoraExtra(Cálculos.Hora(SalarioExtra, JornadaHoras), PorcentagemExtra) + Cálculos.Hora(SalarioExtra, JornadaHoras)) * QuantidadeExtra))}\033[m') # Mostra o valor total de horas extras cálculados.
                                        print('-' * 80)
                                        break
                                while True:
                                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o cálculo.
                                    if Pergunta == 'S' or Pergunta == 'N':
                                        print('-' * 80)
                                        break 
                                print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                                if Pergunta == 'N': # Terminar o loop.
                                    os.system('cls') or None # Comando para limpar a tela do terminal.
                                    break
                            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu de hora extra.
                                break
                        elif EscolhaExtra not in [0, 1]:
                            if EscolhaExtra == 88: # Opção para encerrar o menu de hora extra.
                                os.system('cls') or None # Comando para limpar a tela do terminal.
                                break
                            else:
                                print('\033[0;31mERRO! Opção inválida, tente novamente.\033[m') # Aviso de entrada inválida.
                    if EscolhaExtra == 88:
                        break
                if EscolhaExtra == 88: # Opção para encerrar o menu de hora extra e voltar ao menu principal.
                        break
            elif Escolha == 7: # Opção para o cálculo de saldo do FGTS.
                os.system('cls') or None # Comando para limpar a tela do terminal.
                while True:
                    while True:
                        try: # Tente executar os comandos.
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 80)
                            print(' ' * 26  + '\033[0;36mCÁLCULO DO SALDO DO FGTS\033[m') # Título.
                            print('-' * 80)
                            SalarioSaldoFgts = float(input('Valor do salário bruto: ')) # Variável que recebe valor do salário.
                            MesesFgts = int(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados.
                        except ValueError: # Caso aconteça um 'ValueError' informe.
                            print('\033[0;31mERRO! Digite apenas valores reais validos, tente novamente!\033[m')
                            sleep(1)
                            os.system('cls') or None
                        except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
                            print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
                            sleep(1)
                            print('-' * 80)
                            break
                        else:
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'O saldo do FGTS é de +/- \033[0;32mR$ {Tratamento.Milhares(Cálculos.Fgts(SalarioSaldoFgts) * MesesFgts)}\033[m') # Resultado do cálculo do saldo do FGTS.
                            print('-' * 80)
                            break
                    while True:
                        Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou para parar o programa.
                        if Pergunta == 'S' or Pergunta == 'N':
                            print('-' * 80)
                            break 
                        print('\033[0;31mERRO! Entrada inválida, tente novamente.\033[m') # Aviso ao usuário.
                    if Pergunta == 'N': # Termina o loop.
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        break
                if Pergunta == 'N': # Terminar o cálculo e voltar ao menu principal.
                    break
            elif Escolha not in [0, 1, 2, 3, 4, 5, 6, 7]: # Terminar o menu de opções.
                if Escolha == 99:
                    break
                else: 
                    print('\033[0;31mERRO! Opção inválida, tente novamente.\033[m') # Aviso de entrada inválida.
        if Escolha == 99: # Opção para terminar o programa geral.
            break # Termina o loop do menu de opções e encerrar.
    except ValueError: # Caso aconteça um 'ValueError' informe.
        print('\033[0;31mERRO! Digite apenas valores validos, tente novamente!\033[m')
        sleep(1)
        os.system('cls') or None # Comando para limpar a tela do terminal.
    except KeyboardInterrupt: # Caso usuário encerre pelo teclado, termine o programa.
        print('\033[0;31mO usuário encerrou o  programa pelo teclado!\033[m')
        sleep(1)
        break
print('-' * 80)
print(' ' * 30 + '\033[1;31mFIM DO PROGRAMA\033[m') # Aviso de fim do programa.
sleep(1) # Temporizador de 1 segundo.
os.system('cls') or None # Comando para limpar a tela do terminal.
Tratamento.FecharPrograma() # Função para fechar o terminal de comando no windowns.
