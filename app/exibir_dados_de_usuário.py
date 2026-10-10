from colorama import Fore, Style, init
import sqlite3
from cadastro_conta import Conectar_Banco

def Exibir_dados_usuário():
    conexao = Conectar_Banco()
    cursor = conexao.cursor()

    print(Fore.GREEN + '\n--EXIBIÇÃO DE DADOS--\n' + Style.RESET_ALL)
    email = input(Fore.CYAN + 'Digite o seu email: ' + Style.RESET_ALL).strip() # Usuário vai digitar o email e senha para indentifcar a conta.
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()

    cursor.execute('''
SELECT id, email, senha, nome_de_usuario 
FROM usuarios
WHERE email = ?
AND senha = ?
''', (email, senha)) # Onde será selecionada a conta. 

    dados_usuario = cursor.fetchone() # Caso o usuário tenha informado as credenciais corretas ele ira selecionar uma lista da tabela.

    if dados_usuario:
        print(Fore.GREEN + '\n---DADOS DA SUA CONTA---\n' + Style.RESET_ALL)
        print(Fore.CYAN + 'ID: ' + Style.RESET_ALL, dados_usuario[0])
        print(Fore.CYAN + 'EMAIL: ' + Style.RESET_ALL, dados_usuario[1])
        print(Fore.CYAN + 'NOME DE USUÁRIO: ' + Style.RESET_ALL, dados_usuario[2])
        print(Fore.CYAN + 'SUA SENHA: ' + Style.RESET_ALL, dados_usuario[3] ,'\n')
        print(Fore.GREEN + 'Digite - 1 para realizar outra operação.')
        print('Digite qualquer coisa para parar o programa.' + Style.RESET_ALL)
        voltar = input(Fore.CYAN + '\nOpção: ' + Style.RESET_ALL).strip()
        if voltar == '1':
            return True
        else:
            return False
    else:
        print(Fore.RED + 'CREDENCIAIS INVÁLIDAS, TENTE NOVAMENTE.' + Style.RESET_ALL)
        return True