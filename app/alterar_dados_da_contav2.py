import re
import secrets
import sqlite3

from app.cadastro_conta import Conectar_Banco

# Carrega as variáveis do arquivo .env.
# A senha do aplicativo NÃO fica escrita neste arquivo.

class ServicoEmail:
    """Simula o envio dos códigos de verificação por e-mail."""

    def enviar_codigo(self, destinatario, token, tipo):
        if tipo not in ("email", "senha"):
            print("Tipo de verificação inválido.")
            return False

        print("\n========== DEVPATH ==========")
        print(f"Destinatário: {destinatario}")
        print(f"Tipo de verificação: {tipo}")
        print(f"Código de verificação: {token}")
        print("=============================\n")

        return True

class GerenciadorConta:
    """Reúne as operações de alteração dos dados de uma conta."""

   
    def __init__(self, servico_email=None, conectar_banco=None):
        self.servico_email = servico_email or ServicoEmail()
        self.conectar_banco = conectar_banco or Conectar_Banco

        self.garantir_colunas_verificacao()


    def garantir_colunas_verificacao(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("PRAGMA table_info(usuarios)")
            colunas = [coluna[1] for coluna in cursor.fetchall()]

            novas_colunas = {
                "novo_email_pendente": "TEXT",
                "nova_senha_pendente": "TEXT",
                "token_verificacao": "TEXT"
            }

            for nome, tipo in novas_colunas.items():
                if nome not in colunas:
                    cursor.execute(
                        f"ALTER TABLE usuarios ADD COLUMN {nome} {tipo}"
                    )

            conexao.commit()

        finally:
            conexao.close()

    @staticmethod
    def _gerar_token():
        """Gera um código numérico seguro com seis dígitos."""
        return str(secrets.randbelow(900000) + 100000)

    def solicitar_alteracao_email(self, email_atual, senha, novo_email):
        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(padrao_email, novo_email):
            return False, "Digite um formato de e-mail válido.", None, None

        if novo_email == email_atual:
            return False, "O e-mail novo não pode ser igual ao atual.", None, None

        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE email = ? AND senha = ?
                """,
                (email_atual, senha),
            )
            usuario = cursor.fetchone()

            if not usuario:
                return False, "E-mail atual ou senha incorretos.", None, None

            usuario_id = usuario[0]
            token = self._gerar_token()

            cursor.execute(
                """
                UPDATE usuarios
                SET novo_email_pendente = ?, token_verificacao = ?
                WHERE id = ?
                """,
                (novo_email, token, usuario_id),
            )
            conexao.commit()

            if self.servico_email.enviar_codigo(novo_email, token, "email"):
                return (
                    True,
                    "Código de demonstração gerado com sucesso!",
                    usuario_id,
                    token
                )

            return False, "Erro ao tentar gerar o código de verificação.", None, None

        except Exception as erro:
            return False, f"Erro inesperado no banco: {erro}", None, None

        finally:
            conexao.close()

    def confirmar_codigo_email(self, usuario_id, token_digitado):
        if not usuario_id:
            return False, "Erro de identificação do usuário."

        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT novo_email_pendente, token_verificacao
                FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,),
            )
            resultado = cursor.fetchone()

            if not resultado or not resultado[1]:
                return False, "Nenhuma solicitação de troca encontrada."

            novo_email_pendente, token_salvo = resultado

            if str(token_digitado).strip() != str(token_salvo):
                return False, "Código de verificação incorreto."

            cursor.execute(
                """
                UPDATE usuarios
                SET email = ?,
                    novo_email_pendente = NULL,
                    token_verificacao = NULL
                WHERE id = ?
                """,
                (novo_email_pendente, usuario_id),
            )
            conexao.commit()
            return True, "E-mail alterado com sucesso!"

        except sqlite3.IntegrityError:
            return False, "Este novo e-mail já está sendo utilizado por outra conta."

        except Exception as erro:
            return False, f"Erro inesperado no banco: {erro}"

        finally:
            conexao.close()

    def solicitar_alteracao_senha(self, email_atual, senha_atual, nova_senha):
        if senha_atual == nova_senha:
            return False, "A nova senha não pode ser igual à atual.", None, None

        if len(nova_senha) < 6:
            return False, "A nova senha deve ter pelo menos 6 caracteres.", None, None

        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE email = ? AND senha = ?
                """,
                (email_atual, senha_atual),
            )
            usuario = cursor.fetchone()

            if not usuario:
                return False, "E-mail ou senha atuais incorretos.", None, None

            usuario_id = usuario[0]
            token = self._gerar_token()

            cursor.execute(
                """
                UPDATE usuarios
                SET nova_senha_pendente = ?, token_verificacao = ?
                WHERE id = ?
                """,
                (nova_senha, token, usuario_id),
            )
            conexao.commit()

            if self.servico_email.enviar_codigo(email_atual, token, "senha"):
                return (
                    True,
                    "Código de demonstração gerado com sucesso!",
                    usuario_id,
                    token
                )

            return False, "Erro ao tentar gerar o código de verificação.", None, None

        except Exception as erro:
            return False, f"Erro inesperado no banco: {erro}", None, None

        finally:
            conexao.close()

    def confirmar_codigo_senha(self, usuario_id, token_digitado):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT nova_senha_pendente, token_verificacao
                FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,),
            )
            resultado = cursor.fetchone()

            if not resultado or not resultado[1]:
                return False, "Nenhuma solicitação de troca encontrada."

            nova_senha_pendente, token_salvo = resultado

            if str(token_digitado).strip() != str(token_salvo):
                return False, "Código de verificação incorreto."

            cursor.execute(
                """
                UPDATE usuarios
                SET senha = ?,
                    nova_senha_pendente = NULL,
                    token_verificacao = NULL
                WHERE id = ?
                """,
                (nova_senha_pendente, usuario_id),
            )
            conexao.commit()
            return True, "Senha alterada com sucesso!"

        except Exception as erro:
            return False, f"Erro inesperado no banco: {erro}"

        finally:
            conexao.close()

    def alterar_nome_de_usuario(self, nome_atual, senha, nome_novo):
        if nome_novo == nome_atual:
            return False, "Nome atual é igual ao nome novo."

        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE nome_de_usuario = ? AND senha = ?
                """,
                (nome_atual, senha),
            )
            usuario = cursor.fetchone()

            if not usuario:
                return False, "Nome de usuário ou senha incorretos."

            cursor.execute(
                """
                UPDATE usuarios
                SET nome_de_usuario = ?
                WHERE id = ?
                """,
                (nome_novo, usuario[0]),
            )
            conexao.commit()
            return True, "Nome de usuário alterado com sucesso!"

        except sqlite3.IntegrityError:
            return False, "Esse nome de usuário já está cadastrado."

        finally:
            conexao.close()


# Instância compartilhada pelas telas do sistema.
gerenciador_conta = GerenciadorConta()


# Funções de compatibilidade:
# mantêm os nomes antigos para que as telas atuais continuem funcionando.
def Enviar_email_smtp(destinatario, token):
    return gerenciador_conta.servico_email.enviar_codigo(
        destinatario, token, "email"
    )


def Enviar_email_smtp_senha(destinatario, token):
    return gerenciador_conta.servico_email.enviar_codigo(
        destinatario, token, "senha"
    )


def Solicitar_alteracao_email(email_atual, senha, novo_email):
    return gerenciador_conta.solicitar_alteracao_email(
        email_atual, senha, novo_email
    )


def Confirmar_codigo_email(usuario_id, token_digitado):
    return gerenciador_conta.confirmar_codigo_email(
        usuario_id, token_digitado
    )


def Solicitar_alteracao_senha(email_atual, senha_atual, nova_senha):
    return gerenciador_conta.solicitar_alteracao_senha(
        email_atual, senha_atual, nova_senha
    )


def Confirmar_codigo_senha(usuario_id, token_digitado):
    return gerenciador_conta.confirmar_codigo_senha(
        usuario_id, token_digitado
    )


def Alterar_nome_de_usuario(nome_atual, senha, nome_novo):
    return gerenciador_conta.alterar_nome_de_usuario(
        nome_atual, senha, nome_novo
    )
