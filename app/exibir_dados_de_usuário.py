from colorama import Fore, Style, init
import sqlite3
from cadastro_conta import Conectar_Banco

def Ebixir_dados_usuário():
    conexao = Conectar_Banco()
    cursor = conexao.cursor()

    print(Fore.GREEN + '--EXIBIÇÃO DE DADOS--' + Style.RESET_ALL)
    email = input(Fore.CYAN + 'Digite o seu email: ' + Style.RESET_ALL).strip()
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()

    cursor.execute('''
SELECT id, email, senha, nome_de_usuario 
FROM usuarios
WHERE email = ?
AND senha = ?
''', (email, senha))

    dados_usuario = cursor.fetchone()

    if dados_usuario:
        print(Fore.GREEN + '---DADOS DA SUA CONTA---' + Style.RESET_ALL)
        print(Fore.CYAN + 'ID: ' + Style.RESET_ALL, dados_usuario[0])
        print(Fore.CYAN + 'EMAIL: ' + Style.RESET_ALL, dados_usuario[1])
        print(Fore.CYAN + 'NOME DE USUÁRIO: ' + Style.RESET_ALL, dados_usuario[2])
        print(Fore.CYAN + 'SUA SENHA: ' + Style.RESET_ALL, dados_usuario[3])
        return
    else:
        print(Fore.RED + 'CREDENCIAIS INVÁLIDAS, TENTE NOVAMENTE.' + Style.RESET_ALL)

Ebixir_dados_usuário()