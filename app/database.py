import sqlite3

# funcionalidades para categorizar os filtros

def ConectarCursos():
    return sqlite3.connect("data/cursos.db")

def Tabela_Cursos():

    conexao = ConectarCursos()

    try:
        cursor = conexao.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_do_curso TEXT NOT NULL,
                plataforma TEXT NOT NULL,
                linguagem TEXT NOT NULL,
                descricao TEXT NOT NULL,
                gratuito BOOLEAN DEFAULT 0
        ) 
        """)

        conexao.commit()

    finally:
        conexao.close()

def InserirCurso(nome, plataforma, linguagem,
                 descricao, gratuito):

    conexao = ConectarCursos()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO cursos (
                nome_do_curso,
                plataforma,
                linguagem,
                descricao,
                gratuito
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            nome,
            plataforma,
            linguagem,
            descricao,
            gratuito
        ))

        conexao.commit()

    finally:
        conexao.close()
        