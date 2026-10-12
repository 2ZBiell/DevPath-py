import sqlite3
from colorama import Style, Fore, init
# funcionalidades para cadastro de conta 

def Conectar_Banco():
    return sqlite3.connect("data/usuarios.db")

def Criar_Tabela():
    #docstring

    conexao = Conectar_Banco()
    
    try:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            nome_de_usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
            )
        """)    

        conexao.commit()
    finally:
        conexao.close()

def Validacao_Cadastro(email, nome_de_usuario, senha):
    #docstring

    if len(nome_de_usuario.strip()) < 3:
        return False, "Nome de usuário muito curto."

    if len(senha) < 8 or len(senha) > 20:
        return False, "A senha deve ter entre 8 e 20 caracteres."

    if '@' not in email:
        return False, "E-mail inválido."

    return True, "Dados válidos"

def Cadastrar_Conta(email, nome_de_usuario, senha): 
    #docstring  
          
    valido, mensagem = Validacao_Cadastro(
        email, nome_de_usuario, senha 
    )
    
    if not valido:
        return False, mensagem 
    
    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios (email, nome_de_usuario, senha)
            VALUES (?, ?, ?)
        """, (email, nome_de_usuario, senha))

        conexao.commit()

        return True, "Conta cadastrada com sucesso!"

    except sqlite3.IntegrityError:
        return False, "email ou nome de usuário já cadastrado."

    finally:
        conexao.close()    

def ValidarLogin(nome_de_usuario, senha):
    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
        SELECT id
        FROM usuarios
        WHERE nome_de_usuario = ? AND senha = ?
        """, (nome_de_usuario, senha))

        usuario = cursor.fetchone()

        if usuario:
            return True, "login realizado com sucesso!"
        
        return False, "Email ou senha incorretos."
    
    finally:
        conexao.close()
        