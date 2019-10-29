'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
# Programa principal.
from datetime import date # Biblioteca de datas.
import os # Biblioteca de comandos do sistema.
from time import sleep # Biblioteca de tempo.
import Cálculos # Biblioteca de cálculos.
import Tratamento # Biblioteca de tratamento.
Tratamento.Identificacao_Carregamento() # Identificação do usuário.
MenuCalculos = ['Sálario liquido', # Lista com as opções de cálculos apresentada no menu inicial.
                'Décimo terceiro', 
                'INSS', 
                'IRRF', 
                'FGTS', 
                'Férias', 
                'Hora Extra', 
                'Saldo FGTS',
                'Rescisão CLT',
                'Seguro Desemprego'] 
while True:
    print('-' * 30)
    Ano = date.today().year # Variável que recebe o ano atual.
    print(f'  \033[0;36mCÁLCULOS TRABALHISTAS {Ano}\033[m') # Título do programa inicial.
    print('-' * 30)
    for Indice, Lista in enumerate(MenuCalculos): # Laço para gerar um indice na lista de opções.
            print(f'\033[0;34m[{Indice}]\033[m {Lista}') # Imprimir a lista de opções.
    print('\033[0;31m[99] ENCERRAR PROGRAMA\033[m') # Opção para encerrar programa.
    print('-' * 30)
    while True:
        Escolha = int(input('ESCOLHA UMA OPÇÃO ACIMA: ')) # Variável que recebe a opção a ser executada.
        if Escolha == 0: # Opção para o cálculo de sálario líquido.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 50)
                print('           \033[0;36mCÁLCULO DO SALÁRIO LÍQUIDO\033[m') # Título.
                print('-' * 50)
                SalarioLiquido = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário bruto.
                NumDependentesSL = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes.
                OutrosDescontos = float(input('Outros descontos: ')) # Variável que recebe o valor de outros descontos.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'Valor do INSS é de \033[0;32mR$ {Cálculos.Inss(SalarioLiquido)[0]:.2f}\033[m'.replace('.',','), end='') # Resultado do cálculo do INSS.
                print(f', alíquota de {Cálculos.Inss(SalarioLiquido)[1]}%.') # Alíquota utilizada para cálcular o INSS.
                if Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[0] == 0: # Caso não tenha desconto de IRRF.
                    print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário.
                else:
                    print(f'Valor do IRRF é de \033[0;32mR$ {Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[0]:.2f}\033[m'.replace('.',','), end='') # Resultado do cálculo do IRRF.
                    print(f', alíquota de {Cálculos.Irrf((SalarioLiquido - Cálculos.Inss(SalarioLiquido)[0]) - Cálculos.Dependentes(NumDependentesSL))[1]}%.',) # Alíquota utilizada para cálcular o IRRF.
                print(f'Número de dependetes: \033[0;32m{NumDependentesSL}\033[m') # Mostra o número de dependentes.
                print(f'Outros descontos: \033[0;32mR$ {OutrosDescontos:.2f}\033[m'.replace('.',','), end='') # O valor de outros descontos sobre o salário.
                print('.')
                print(f'O valor do sálario líquido é de \033[0;32mR$ {Cálculos.SalarioLiquido(SalarioLiquido, NumDependentesSL, OutrosDescontos):.2f}\033[m!'.replace('.',',')) # Valor final do salário líquido.
                print('-' * 50)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N':
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 1: # Opção para o cálculo de décimo terceiro.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 70)
                print('                \033[0;36mCÁLCULO DO DÉCIMO TERCEIRO SÁLARIO\033[m') # Título.
                print('-' * 70)
                DecimoTerceiro = float(input('Valor do salário bruto: ')) # Variável que recebe o valor do salário.
                NumDependentesDecimo = int(input('Número de dependentes: ')) # Variável que recebe número de dependentes.
                print('(\033[0;31mConsiderar para o cálculo apenas os meses em que o')
                print(' trabalhador tenha trabalhado mais de 15 dias no mês!\033[m)') # Aviso ao usuário.
                MesesDecimo = float(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'Valor da primeira parcela do décimo terceiro sálario é \033[0;32mR$ {Cálculos.Adiantamento(DecimoTerceiro, MesesDecimo):.2f}\033[m!'.replace('.',',')) # Mostra o valor da primeira parcela do décimo terceiro (adiantamento).
                print(f'Valor da segunda parcela do décimo terceiro sálario é \033[0;32mR$ {Cálculos.Decimo(DecimoTerceiro, MesesDecimo, NumDependentesDecimo):.2f}\033[m!'.replace('.',',')) # Mostra o valor da segunda parcela do décimo terceiro.
                print(f'Total a receber \033[0;32mR$ {Cálculos.Adiantamento(DecimoTerceiro, MesesDecimo) + Cálculos.Decimo(DecimoTerceiro, MesesDecimo, NumDependentesDecimo):.2f}\033[m!'.replace('.',',')) # Mostra o total a receber do decimo terceiro.
                print('-' * 70)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N':
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break         
        elif Escolha == 2: # Opção para o cálculo de INSS.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 50)
                print('            \033[0;36mCÁLCULO DO VALOR DO INSS\033[m') # Título.
                print('-' * 50)
                SalarioInss = float(input('Valor do sálario bruto: ')) # Variável que recebe valor do salário.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'O valor do INSS é de \033[0;32mR$ {Cálculos.Inss(SalarioInss)[0]:.2f}\033[m'.replace('.',','), end='') # Resultado do cálculo do INSS.
                print(f', alíquota de {Cálculos.Inss(SalarioInss)[1]}%.') # Alíquota utilizada para cálcular o INSS.
                print('-' * 50)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N':
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 3: # Opção para o cálculo de IRRF.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 50)
                print('            \033[0;36mCÁLCULO DO VALOR DO IRRF\033[m') # Título.
                print('-' * 50)
                SalarioIrrf = float(input('Valor do sálario bruto: ')) # Variável que recebe valor do salário.
                NumDependentesIrrf = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                if Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[0] == 0: # Caso não tenha desconto de IRRF.
                    print('\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m') # Aviso ao usuário.
                else:
                    print(f'O valor do IRRF é de \033[0;32mR$ {Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[0]:.2f}\033[m'.replace('.',','), end='') # Resultado do cálculo do IRRF.
                    print(f', alíquota de {Cálculos.Irrf((SalarioIrrf - Cálculos.Inss(SalarioIrrf)[0]) - Cálculos.Dependentes(NumDependentesIrrf))[1]}%.') # Alíquota utilizada para cálcular o IRRF.
                print('-' * 50)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N':
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 4: # Opção para o cálculo de FGTS.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 50)
                print('            \033[0;36mCÁLCULO DO VALOR DO FGTS\033[m') # Título.
                print('-' * 50)
                SalarioFgts = float(input('Valor do sálario bruto: ')) # Variável que recebe valor do salário.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'Valor do FGTS é de R$ \033[0;32m{Cálculos.Fgts(SalarioFgts):.2f}\033[m'.replace('.',','), end='') # Resultado do cálculo do FGTS.
                print(', alíquota de 8%.') # Alíquota utilizada para o cálculo.
                print('-' * 50)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N': # T
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 5: # Opção para o cálculo de férias. 
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 60)
                print('                     \033[0;36mCÁLCULO DE FÉRIAS\033[m') # Título.
                print('-' * 60)
                SalarioFerias = float(input('Salário bruto: ')) # Variável que recebe o valor do salário bruto.
                DependentesFerias = int(input('Número de dependentes: ')) # Variável que recebe o número de dependentes.
                MediaExtraFerias = float(input('Valor médio de horas extras no ano: ')) # Variável que recebe o valor médio de horas extras.
                while True:
                    DiasFerias = int(input('Dias de férias: ')) # Variável que recebe o números de férias.
                    if DiasFerias > 30:
                        print('(\033[1;31mO número de dias deve estar entre 10 e 30\033[m)')
                    else:
                        break
                while True:
                    Abono = str(input('Abono pecuniário (Vender 1/3) \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção de cálculo para abono.
                    if DiasFerias == 30 and Abono == 'S':
                        print('(\033[1;31mPara cálculos de férias com abono pecuniário (venda 1/3) o\033[m')
                        print('\033[1;31mvalor máximo de dias de férias (dias gozados) é de 20 dias\033[m)')
                    else:
                        break
                AdiantarTerco = str(input('Adiantar a 1ª parcela do 13º salário \033[1;31m[S/N]\033[m: ')).strip().upper() # Variável que recebe a opção para adiantar o décimo terceiro.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'Valor férias é de \033[0;32mR$ {Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias):.2f}\033[m'.replace('.',',')) # Mostra o valor férias.
                print(f'Valor de 1/3 sobre as férias é de \033[0;32mR$ {Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias) / 3:.2f}\033[m'.replace('.',',')) # Mostra o valor de 1/3 sobre as férias.
                if Abono == 'S' and DiasFerias <= 20: # Mostrar o cálculo do abono de acordo com opção escolhida.
                    print(f'Valor do abono pecuniário é de \033[0;32mR$ {((SalarioFerias + MediaExtraFerias) / 3):.2f}\033[m'.replace('.',',')) # Mostra o valor do abono.
                    print(f'Valor de 1/3 do abono pecuniário é de \033[0;32mR$ {(((SalarioFerias + MediaExtraFerias) / 3) / 3):.2f}\033[m'.replace('.',',')) # Mostra o valor de 1/3 sobre o abono.
                if AdiantarTerco == 'S': # Opção para mostrar ou não valor do adiantamento de décimo terceiro.
                    print(f'Valor do adiantamento da 1ª parcela do 3º salário é de \033[0;32mR$ {Cálculos.Adiantamento(SalarioFerias, 12):.2f}\033[m'.replace('.',','))  # Mostra o valor do adiantamento do décimo terceiro.
                BaseImpostoFerias = (Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias)) + (Cálculos.ValorFerias(SalarioFerias, DiasFerias, MediaExtraFerias) / 3) # Recebe o valor base para calcular o INSS e IRRF sobre as férias.
                print(f'Valor do INSS é de \033[0;32mR$ {Cálculos.Inss(BaseImpostoFerias)[0]:.2f}\033[m'.replace('.',','), end='') # Mostra o valor do INSS.
                print(f', alíquota de {Cálculos.Inss(BaseImpostoFerias)[1]}%') # Mostra a alíquota utilizada no ISS.
                if Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[0] == 0: # Recebe o valor base para cálculo do IRRF.
                    print('(\033[0;31mA essa faixa salárial não é descontado o IRRF!\033[m)') # Aviso ao usuário.
                else:
                    print(f'Valor do IRRF é de \033[0;32mR$ {Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[0]:.2f}\033[m'.replace('.',','), end='') # Mostra o valor do IRRF.
                    print(f', alíquota de {Cálculos.Irrf((BaseImpostoFerias - Cálculos.Inss(BaseImpostoFerias)[0]) - Cálculos.Dependentes(DependentesFerias))[1]}%') # Mostra a alíquota utilizada no IRRF.
                print('-' * 60)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N': # T
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 6: # Opção para o cálculo de hora extra.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 35)
                print('       \033[0;36mCÁLCULO DE HORA EXTRA\033[m') # Título.
                print('-' * 35)
                MenuHoraExtra = ['Valor HORA EXTRA', 'Total HORA EXTRA'] # Lista com as opções de para hora extra.
                for IndiceExtra, ListaExtra in enumerate(MenuHoraExtra):
                    print(f'\033[0;34m[{IndiceExtra}]\033[m {ListaExtra}') # Imprimir a lista de opções.
                print('\033[0;31m[88] VOLTAR AO MENU\033[m') # Opção para voltar ao menu principal.
                print('-' * 35)
                while True:
                    EscolhaExtra = int(input('ESCOLHA UMA OPÇÃO ACIMA: ')) # Variável que recebe a opção a ser executada.
                    if EscolhaExtra == 0: # Opção para o cálculo do valor da hora extra.
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        while True:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 63)
                            print('                  \033[0;36mCÁLCULO DO VALOR HORA EXTRA\033[m') # Título.
                            print('-' * 63)
                            SalarioExtra = float(input('Salário base: ')) # Variável que recebe o salário base para o cálculo da hora extra.
                            JornadaHoras = float(input('Jornada mensal (horas): ')) # Variável que recebe a quantidade de horas da jornada de trabalho.
                            PorcentagemExtra = int(input('Adicional hora extra (%): ')) # Variável que a porcentagem do adicional de hora extra.
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'O valor da sua hora é \033[0;32mR$ {Cálculos.Hora(SalarioExtra, JornadaHoras):.2f}\033[m!'.replace('.',',')) # Mostra o valor da hora.
                            print(f'O valor da sua hora extra com adicional de {PorcentagemExtra}%', end=' ') # Mostra a porcentagem utilizada.
                            print(f'é de \033[0;32mR$ {Cálculos.HoraExtra(Cálculos.Hora(SalarioExtra, JornadaHoras), PorcentagemExtra) + Cálculos.Hora(SalarioExtra, JornadaHoras):.2f}\033[m!'.replace('.',',')) # Mostra o valor da hora extra.
                            print('-' * 63)
                            while True:
                                Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                                if Pergunta in 'SN':
                                    print('-' * 63)
                                    print(' ')
                                    break 
                            if Pergunta == 'N': # Terminar o loop.
                                os.system('cls') or None # Comando para limpar a tela do terminal.
                                break
                        if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                            break
                    elif EscolhaExtra == 1: # Opção para o cálculo do valor total da hora extra.
                        os.system('cls') or None # Comando para limpar a tela do terminal.
                        while True:
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            print('-' * 45)
                            print('      \033[0;36mCÁLCULO DO VALOR TOTAL HORA EXTRA\033[m') # Título.
                            print('-' * 45)
                            SalarioExtra = float(input('Salário base: ')) # Variável que recebe o salário base para o cálculo da hora extra.
                            JornadaHoras = float(input('Jornada mensal (horas): ')) # Variável que recebe a quantidade de horas da jornada de trabalho.
                            PorcentagemExtra = int(input('Adicional hora extra (%): ')) # Variável que a porcentagem do adicional de hora extra.
                            QuantidadeExtra = float(input('Número de horas extras: ')) # Variável que a quantidade de horas extra trabalhadas.
                            print(' ')
                            print('Cálculando... Aguarde!')
                            print(' ')
                            sleep(0.75) # Temporizador de 0.75 segundos.
                            print(f'Quantidade de horas trabalhadas: \033[0;32m{QuantidadeExtra:.2f}\033[m'.replace('.',':')) # Mostra a quantidade de horas utilizadas.
                            print(f'Valor total das horas extras \033[0;32mR$ {((Cálculos.HoraExtra(Cálculos.Hora(SalarioExtra, JornadaHoras), PorcentagemExtra) + Cálculos.Hora(SalarioExtra, JornadaHoras)) * QuantidadeExtra):.2f}\033[m!'.replace('.',',')) # Mostra o total de horas extras.
                            print('-' * 45)
                            while True:
                                Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                                if Pergunta in 'SN':
                                    print('-' * 50)
                                    print(' ')
                                    break 
                            if Pergunta == 'N': # Terminar o loop.
                                os.system('cls') or None # Comando para limpar a tela do terminal.
                                break
                        if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                            break
                    elif EscolhaExtra not in [0, 1]:
                        if EscolhaExtra == 88: # Opção para encerrar o menu de hora extra.
                            os.system('cls') or None # Comando para limpar a tela do terminal.
                            break
                        else:
                            print('\033[0;31mERRO! Entrada Inválida.\033[m') # Aviso de entrada inválida.
                if EscolhaExtra == 88:
                    break
            if EscolhaExtra == 88: # Opção para encerrar o menu de hora extra.
                    break
        elif Escolha == 7: # Opção para o cálculo de saldo do FGTS.
            os.system('cls') or None # Comando para limpar a tela do terminal.
            while True:
                os.system('cls') or None # Comando para limpar a tela do terminal.
                print('-' * 50)
                print('          \033[0;36mCÁLCULO DO SALDO DO FGTS\033[m') # Título.
                print('-' * 50)
                SalarioSaldoFgts = float(input('Valor do sálario bruto: ')) # Variável que recebe valor do salário.
                MesesFgts = int(input('Número de meses trabalhados: ')) # Variável que recebe o número de meses trabalhados.
                print(' ')
                print('Cálculando... Aguarde!')
                print(' ')
                sleep(0.75) # Temporizador de 0.75 segundos.
                print(f'O saldo do FGTS é de R$ \033[0;32m{Cálculos.Fgts(SalarioSaldoFgts) * MesesFgts:.2f}\033[m!'.replace('.',',')) # Resultado do cálculo do saldo do FGTS.
                print('-' * 50)
                while True:
                    Pergunta = str(input('Deseja fazer um novo cálculo? \033[0;31m[S/N]\033[m ')).strip().upper() # Loop para um novo cálculo ou parar o programa.
                    if Pergunta in 'SN':
                        print('-' * 50)
                        print(' ')
                        break 
                if Pergunta == 'N': # T
                    os.system('cls') or None # Comando para limpar a tela do terminal.
                    break
            if Pergunta == 'N': # Terminar o cálculo e voltar ao menu.
                break
        elif Escolha == 8: # Opção para o cálculo de rescisão CLT.
            continue
        elif Escolha == 9: # Opção para o cálculo de seguro desemprego.
            continue
        elif Escolha not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: # Terminar o menu de opções.
            if Escolha == 99:
                break
            else: 
                print('\033[0;31mERRO! Entrada Inválida.\033[m') # Aviso de entrada inválida.
    if Escolha == 99: # Opção para terminar o programa.
        break # Termina o loop do menu de opções.
print('-' * 30)
print('       \033[1;31mFIM DO PROGRAMA\033[m') # Aviso de fim do programa.
sleep(0.75) # Temporizador de 0.75 segundos.
os.system('cls') or None # Comando para limpar a tela do terminal.
Tratamento.Fechar()
