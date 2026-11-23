import sqlite3

class GerenciadorFavoritos:

    def __init__(self):
        self.caminho_usuarios = "data/usuarios.db"
        self.caminho_cursos = "data/cursos.db"

    def conectar_usuarios(self):
        conexao = sqlite3.connect(self.caminho_usuarios)
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao

    def conectar_cursos(self):
        return sqlite3.connect(self.caminho_cursos)

    def criar_tabela(self):
        conexao = self.conectar_usuarios()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cursos_favoritos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    curso_id INTEGER NOT NULL,

                    FOREIGN KEY (usuario_id)
                        REFERENCES usuarios(id),

                    UNIQUE (usuario_id, curso_id)
                )
            """)

            conexao.commit()

        finally:
            conexao.close()

    def favoritar_curso(self, usuario_id, curso_id):

        # Verifica se o usuário existe
        conexao_usuarios = self.conectar_usuarios()

        try:
            cursor = conexao_usuarios.cursor()

            cursor.execute(
                "SELECT id FROM usuarios WHERE id = ?",
                (usuario_id,)
            )

            if cursor.fetchone() is None:
                return False, "Usuário não encontrado."

        finally:
            conexao_usuarios.close()

        # Verifica se o curso existe
        conexao_cursos = self.conectar_cursos()

        try:
            cursor = conexao_cursos.cursor()

            cursor.execute(
                "SELECT id FROM cursos WHERE id = ?",
                (curso_id,)
            )

            if cursor.fetchone() is None:
                return False, "Curso não encontrado."

        finally:
            conexao_cursos.close()

        # Registra o favorito
        conexao = self.conectar_usuarios()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO cursos_favoritos (usuario_id, curso_id)
                VALUES (?, ?)
            """, (usuario_id, curso_id))

            conexao.commit()

            return True, "Curso adicionado aos favoritos!"

        except sqlite3.IntegrityError:
            return False, "Esse curso já está nos seus favoritos."

        finally:
            conexao.close()

    def desfavoritar_curso(self, usuario_id, curso_id):

        conexao = self.conectar_usuarios()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                DELETE FROM cursos_favoritos
                WHERE usuario_id = ? AND curso_id = ?
            """, (usuario_id, curso_id))

            conexao.commit()

            if cursor.rowcount > 0:
                return True, "Curso removido dos favoritos."

            return False, "Esse curso não está nos seus favoritos."

        finally:
            conexao.close()
 
    def listar_favoritos(self, usuario_id):

        conexao = self.conectar_usuarios()

        try:
            cursor = conexao.cursor()

            cursor.execute(
                "ATTACH DATABASE ? AS banco_cursos",
                (self.caminho_cursos,)
            )

            cursor.execute("""
                SELECT
                    cursos.id,
                    cursos.nome_do_curso,
                    cursos.plataforma,
                    cursos.linguagem,
                    cursos.descricao,
                    cursos.gratuito

                FROM banco_cursos.cursos AS cursos

                INNER JOIN main.cursos_favoritos AS favoritos
                    ON cursos.id = favoritos.curso_id

                WHERE favoritos.usuario_id = ?

                ORDER BY favoritos.id DESC
            """, (usuario_id,))

            resultados = cursor.fetchall()

            favoritos = []

            for curso in resultados:
                favoritos.append({
                    "id": curso[0],
                    "nome": curso[1],
                    "plataforma": curso[2],
                    "linguagem": curso[3],
                    "descricao": curso[4],
                    "gratuito": curso[5]
                })

            return favoritos

        finally:
            conexao.close()

    def verificar_favorito(self, usuario_id, curso_id):

        conexao = self.conectar_usuarios()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id
                FROM cursos_favoritos
                WHERE usuario_id = ? AND curso_id = ?
            """, (usuario_id, curso_id))

            return cursor.fetchone() is not None

        finally:
            conexao.close()


gerenciador_favoritos = GerenciadorFavoritos()
