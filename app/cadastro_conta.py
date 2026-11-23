import sqlite3

class BancoUsuarios:
    """Gerencia a conexão com o banco de dados dos usuários."""

    def __init__(self, caminho="data/usuarios.db"):
        self.caminho = caminho

    def conectar(self):
        return sqlite3.connect(self.caminho)


class GerenciadorUsuarios:
    """Gerencia o cadastro e a autenticação dos usuários."""

    def __init__(self, banco=None):
        self.banco = banco or BancoUsuarios()

    def criar_tabela(self):
        conexao = self.banco.conectar()

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

    @staticmethod
    def validar_cadastro(email, nome_de_usuario, senha):

        if len(nome_de_usuario.strip()) < 3:
            return False, "Nome de usuário muito curto."

        if len(senha) < 8 or len(senha) > 20:
            return False, "A senha deve ter entre 8 e 20 caracteres."

        if "@" not in email:
            return False, "E-mail inválido."

        return True, "Dados válidos"

    def cadastrar_conta(self, email, nome_de_usuario, senha):

        valido, mensagem = self.validar_cadastro(
            email, nome_de_usuario, senha
        )

        if not valido:
            return False, mensagem

        conexao = self.banco.conectar()

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

    def validar_login(self, email, senha):

        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id
                FROM usuarios
                WHERE email = ? AND senha = ?
            """, (email, senha))

            usuario = cursor.fetchone()

            if usuario:
                return True, "login realizado com sucesso!"

            return False, "Email ou senha incorretos."

        finally:
            conexao.close()

    def adicionar_coluna_tipo_usuario(self):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                PRAGMA table_info(usuarios)
            """)

            colunas = [coluna[1] for coluna in cursor.fetchall()]

            if "tipo_usuario" not in colunas:
                cursor.execute("""
                    ALTER TABLE usuarios
                    ADD COLUMN tipo_usuario TEXT DEFAULT 'usuario'
                """)

            conexao.commit()

        finally:
            conexao.close()

    def autorizar_gerente(self, email_alvo, email_administrador):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            # Verifica se quem está autorizando é administrador
            cursor.execute("""
                SELECT tipo_usuario
                FROM usuarios
                WHERE email = ?
            """, (email_administrador,))

            administrador = cursor.fetchone()

            if not administrador or administrador[0] != "administrador":
                return False, "Você não tem permissão para isso."

            # Verifica se a conta que receberá a permissão existe
            cursor.execute("""
                SELECT id
                FROM usuarios
                WHERE email = ?
            """, (email_alvo,))

            usuario = cursor.fetchone()

            if not usuario:
                return False, "Usuário não encontrado."

            cursor.execute("""
                UPDATE usuarios
                SET tipo_usuario = 'gerente'
                WHERE email = ?
            """, (email_alvo,))

            conexao.commit()

            return True, "Gerente autorizado com sucesso!"

        finally:
            conexao.close()


    def remover_permissao_gerente(self, email_alvo, email_administrador):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT tipo_usuario
                FROM usuarios
                WHERE email = ?
            """, (email_administrador,))

            administrador = cursor.fetchone()

            if not administrador or administrador[0] != "administrador":
                return False, "Você não tem permissão para isso."

            cursor.execute("""
                UPDATE usuarios
                SET tipo_usuario = 'usuario'
                WHERE email = ? AND tipo_usuario = 'gerente'
            """, (email_alvo,))

            if cursor.rowcount == 0:
                return False, "Gerente não encontrado."

            conexao.commit()

            return True, "Permissão de gerente removida!"

        finally:
            conexao.close()

    def obter_usuario(self, email, senha):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT id, email, nome_de_usuario, tipo_usuario
                FROM usuarios
                WHERE email = ? AND senha = ?
            """, (email, senha))

            usuario = cursor.fetchone()

            if usuario:
                return {
                    "id": usuario[0],
                    "email": usuario[1],
                    "nome": usuario[2],
                    "tipo": usuario[3]
                }

            return None

        finally:
            conexao.close()

    def listar_usuarios(self):
        conexao = self.banco.conectar()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT email, nome_de_usuario, tipo_usuario
                FROM usuarios
                ORDER BY nome_de_usuario
            """)

            return cursor.fetchall()

        finally:
            conexao.close()

banco_usuarios = BancoUsuarios()
gerenciador_usuarios = GerenciadorUsuarios(banco_usuarios)

def Conectar_Banco():
    return banco_usuarios.conectar()


def Criar_Tabela():
    return gerenciador_usuarios.criar_tabela()


def Validacao_Cadastro(email, nome_de_usuario, senha):
    return gerenciador_usuarios.validar_cadastro(
        email, nome_de_usuario, senha
    )


def Cadastrar_Conta(email, nome_de_usuario, senha):
    return gerenciador_usuarios.cadastrar_conta(
        email, nome_de_usuario, senha
    )


def ValidarLogin(email, senha):
    return gerenciador_usuarios.validar_login(email, senha)
