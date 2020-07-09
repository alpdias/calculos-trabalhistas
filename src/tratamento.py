'''
@Autor: Paulo https://github.com/alpdias
'''
# Funções para tratamento e sistema.
def barraProgresso():
    """
    -> Função para mostrar uma barra de progresso.
    :param: 
    :return:
    """
    import os
    from time import sleep
    from tqdm import tqdm # Biblioteca para barra de carregamento.
    os.system('cls') or None # Comando para limpar a tela do terminal.
    print(' ')
    print(' ')
    print('Carregando o programa... Aguarde!') # Aviso de carregamento.
    print(' ')
    for x in tqdm(range(10)): # Barra de carregaemnto 'barra de progresso'.
        sleep(0.1)
        pass
    x = ''
    print(x)
    sleep(2) # Temporizador de 1 segundo.
    os.system('cls') or None # Comando para limpar a tela do terminal.


def fecharPrograma():
    """
    -> Função de fechar terminal aberto no windows.
    :param: 
    :return:
    """
    import os
    # Funções para rodar no windows.
    os.system('TASKKILL /F /IM cmd.exe') # Fechar o CMD.exe.
    os.system('TASKKILL /F /IM powershell.exe') # Fechar o PowerShell.exe.
    

def idenficaçao():
    """
    -> Função para identificar e apresentar usuário do programa.
    :param: 
    :return:
    """
    import os
    usuario = (os.getlogin()).upper() # Recebe a idenficação do usuário.
    print(' ')
    print(f'Usuário: \033[0;36m{usuario}\033[m') # Mostra o nome do usuário.


def milhares(numero=0):
    """
    -> Função tratar o número separando por milhares no padrão do local.
    :param numero: Número para ser formatado.
    :return: Número formatado.
    """
    import locale
    locale.setlocale(locale.LC_ALL, "pt-BR")
    return (locale.format_string("%.2f", numero, grouping=True, monetary=True))

