import sqlite3

# funcionalidades para categorizar os filtros

def ConectarCursos():
    return sqlite3.connect("data/cursos.db")

def Tabela_Cursos():
    conexao = ConectarCursos()
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_do_curso TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            linguagem TEXT NOT NULL,
            gratuito INTEGER NOT NULL CHECK (gratuito IN 0, 1)
    ) 
    """)

    conexao.commit()
