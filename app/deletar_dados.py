from app.cadastro_conta import Conectar_Banco

class GerenciadorExclusaoConta:

    def __init__(self, conectar_banco=None):
        # Permite reutilizar a conexão atual ou fornecer outra em testes
        self.conectar_banco = conectar_banco or Conectar_Banco

    def deletar_usuario(self, email, senha):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE email = ? AND senha = ?
                """,
                (email, senha),
            )

            usuario = cursor.fetchone()

            if not usuario:
                return False, "E-mail ou senha incorretos."

            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id = ?
                """,
                (usuario[0],),
            )

            conexao.commit()
            return True, "Conta removida com sucesso!"

        finally:
            conexao.close()


# Instância compartilhada pelo sistema
gerenciador_exclusao = GerenciadorExclusaoConta()

def Deletar_Usuario(email, senha):
    return gerenciador_exclusao.deletar_usuario(email, senha)
