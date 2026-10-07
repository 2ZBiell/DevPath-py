import sqlite3
from colorama import Style, Fore, init
# Menu para cadastro de conta
def Conectar_Banco():
    return sqlite3.connect("data/usuarios.db")

def Criar_Tabela():
    conexao = Conectar_Banco()
    cur = conexao.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        nome_de_usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
        )
    """)

    conexao.commit()

def Cadastrar_Conta():        
    conexao = Conectar_Banco()
    cur = conexao.cursor()

    print(Fore.GREEN + '--CADASTRO DE CONTA--\n' + Style.RESET_ALL)
    email = input(Fore.CYAN +'Digite o seu email: ' + Style.RESET_ALL).strip()
    nome_de_usuario = input(Fore.CYAN +'Digite seu nome de usuário: ' + Style.RESET_ALL).strip()
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()

    cur.execute("""
        INSERT INTO usuarios (email, nome_de_usuario, senha)
        VALUES (?, ?, ?)
    """, (email, nome_de_usuario, senha))

    if Validacao_Cadastro(email, nome_de_usuario, senha):
        print(Fore.GREEN + '\nCONTA CADASTRADA COM SUCESSO!' + Style.RESET_ALL)

    conexao.commit()
    return True


def Validacao_Cadastro(email, nome_de_usuario, senha):
    #docstring

    if len(senha) < 8:
        print(Fore.RED + 'A senha deve conter no mínimo 8 caracteres.' + Style.RESET_ALL)
        return False

    if len(senha) > 20:
        print(Fore.RED + 'A senha deve conter no máximo 20 caracteres.' + Style.RESET_ALL)
        return False

    if '@' not in email:
        print(Fore.RED + 'E-mail inválido.' + Style.RESET_ALL)
        return False
