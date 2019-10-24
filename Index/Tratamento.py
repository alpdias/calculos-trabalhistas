'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
# Funções para tratamento e sistema.
def Identificacao():
    """
    -> Função para identificar e apresentar usuário do programa.
    :param: 
    :return:
    """
    import os
    from time import sleep
    os.system('cls') or None # Comando para limpar a tela do terminal.
    Usuario = (os.getlogin()).upper() # Recebe a idenficação do usuário.
    print(' ')
    print('-' * 40)
    print(f'       Olá \033[0;36m{Usuario}\033[m! Seja bem-vindo.') # Mostra o usuário.
    print('-' * 40)
    print(' ')
    print('Carregando programa...')
    sleep(2.5) # Temporizador de  2.5 segundos.
    os.system('cls') or None # Comando para limpar a tela do terminal.


def Fechar():
    """
    -> Função de fechar terminal aberto.
    :param: 
    :return:
    """
    import os
    os.system('TASKKILL /F /IM cmd.exe') # Fechar o CMD.exe.
    os.system('TASKKILL /F /IM powershell.exe') # Fechar o PowerShell.exe.
    
    