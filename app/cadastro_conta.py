import sqlite3
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
        nome_de_usuario TEXT NOT NULL,
        senha TEXT NOT NULL
        )
    """)

    conexao.commit()

def Cadastrar_Conta():        
    conexao = Conectar_Banco()
    cur = conexao.cursor()

    print('Cadastro de conta\n')
    email = input('Digite o seu email: ')
    nome_de_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    cur.execute("""
        INSERT INTO usuarios (email, nome_de_usuario, senha)
        VALUES (?, ?, ?)
    """, (email, nome_de_usuario, senha))

    if Validacao_Cadastro(email, nome_de_usuario, senha):
        print('\nConta cadastrada com sucesso!')

    conexao.commit()
    return True


def Validacao_Cadastro(email, nome_de_usuario, senha):
    #docstring

    if len(senha) < 8:
        print('A senha deve conter no mínimo 8 caracteres.')
        return False

    if len(senha) > 20:
        print('A senha deve conter no máximo 20 caracteres.')
        return False

    if '@' not in email:
        print('E-mail inválido.')
        return False

    return True


while True:

    print('Digite 1 - Cadastrar nova conta')
    print('Digite 2 - Sair\n')

    opcao = input('Digite um número: ')

    if opcao == '1':
        Criar_Tabela()
        Cadastrar_Conta()

    elif opcao == '2':
        print('Encerrando. . . ')
        break

    else:
        print('Opção inválida. Tente novamente.')
        continue
