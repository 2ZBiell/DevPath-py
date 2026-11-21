import sqlite3

class BancoDeDados():

    def __init__(self, caminho):
        self.caminho = caminho

    def conectar(self):
        return sqlite3.connect(self.caminho)

def ConectarCursos():
    return banco_cursos.conectar()

class GerenciadorCursos():
    def __init__(self, banco):
        self.banco = banco

    def tabela_cursos(self):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cursos (
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

    def inserir_curso(self, nome, plataforma, linguagem,
                      descricao, gratuito):
        conexao = self.banco.conectar()

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
            """, (nome, plataforma, linguagem, descricao, gratuito))

            conexao.commit()

        finally:
            conexao.close()

    def buscar_cursos(
    self,
    nome_do_curso="",
    plataforma=None,
    linguagem=None,
    gratuito=None
):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            sql = """
                SELECT *
                FROM cursos
                WHERE nome_do_curso LIKE ?
            """

            parametros = [f"%{nome_do_curso}%"]

            if plataforma is not None:
                sql += " AND plataforma = ?"
                parametros.append(plataforma)

            if linguagem is not None:
                sql += " AND linguagem = ?"
                parametros.append(linguagem)

            if gratuito is not None:
                sql += " AND gratuito = ?"
                parametros.append(gratuito)

            cursor.execute(sql, parametros)

            return cursor.fetchall()

        finally:
            conexao.close()

banco_cursos = BancoDeDados("data/cursos.db") # Instância
gerenciador_cursos = GerenciadorCursos(banco_cursos)