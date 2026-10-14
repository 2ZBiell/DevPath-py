import sqlite3
import re
import secrets
import smtplib
from email.message import EmailMessage
from app.cadastro_conta import Conectar_Banco

EMAIL_REMETENTE = "rsla9931@gmail.com"

SENHA_APP_EMAIL = "keitusjrodpxcavo" 

def Enviar_email_smtp(destinatario, token):
    """
    Envia o código de verificação de 6 dígitos para o novo e-mail do usuário via SMTP do Gmail.
    Retorna True se enviado com sucesso, ou False em caso de erro.
    """
    msg = EmailMessage()
    msg['Subject'] = 'Alteração de E-mail no DevPath'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario

    # Mensagem do email
    msg.set_content(f"""
    Olá,
    Se você solicitou a alteração do e-mail da sua conta.
    Seu código de verificação de 6 dígitos é: {token}
    
    Se você não solicitou essa alteração, por favor ignore esta mensagem.
    """)

    try:
        # Conecta ao servidor SMTP do Gmail. Número é a porta de entrada para que o google aceite a ligação
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA_APP_EMAIL)
            smtp.send_message(msg)
        return True

    except Exception as erro:
        print(f"Erro ao enviar o e-mail via SMTP: {erro}")
        return False


def Solicitar_alteracao_email(email_atual, senha, novo_email):
    """
    Valida as credenciais do usuário, gera um token temporário e o salva no banco de dados.
    Em seguida, envia o token para o novo e-mail.
    Da return: (sucesso: bool, mensagem: str, id_do_usuario: int ou None)
    """
    # Validando o novo e-mail usando Regex
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(padrao, novo_email):
        return False, "Digite um formato de e-mail válido.", None

    if novo_email == email_atual:
        return False, "O e-mail novo não pode ser igual ao atual.", None

    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        # Verifica se o usuário e a senha existem no banco
        cursor.execute("SELECT id FROM usuarios WHERE email = ? AND senha = ?", (email_atual, senha))
        usuario = cursor.fetchone()

        if not usuario:
            return False, "E-mail atual ou senha incorretos.", None

        usuario_id = usuario[0]

        # Gera um token numérico seguro de 6 dígitos
        token = str(secrets.randbelow(900000) + 100000) 

        # Guarda o token e a intenção de troca temporariamente no banco

        cursor.execute("""
            UPDATE usuarios 
            SET novo_email_pendente = ?, token_verificacao = ? 
            WHERE id = ?
        """, (novo_email, token, usuario_id))
        conexao.commit()

        # 5. Envia o código para o NOVO e-mail
        if Enviar_email_smtp(novo_email, token):
            return True, "Código enviado com sucesso para o novo e-mail!", usuario_id
        else:
            return False, "Erro ao tentar enviar o código por e-mail.", None

    except Exception as erro:
        return False, f"Erro inesperado no banco: {erro}", None
    finally:
        conexao.close()


def Confirmar_codigo_email(usuario_id, token_digitado):
    """
    Verifica se o token digitado corresponde ao salvo no banco de dados.
    Se estiver correto, faz a troca para o novo e-mail e limpa os dados temporários.
    Da return: (Sucesso: bool, Mensagem: str)
    """
    if not usuario_id:
        return False, "Erro de identificação do usuário."

    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        # Busca o token e o e-mail pendente no banco
        cursor.execute("""
            SELECT novo_email_pendente, token_verificacao 
            FROM usuarios WHERE id = ?
        """, (usuario_id,))

        resultado = cursor.fetchone()

        if not resultado or not resultado[1]:
            return False, "Nenhuma solicitação de troca encontrada."

        novo_email_pendente, token_salvo = resultado

        # Compara o token digitado pelo usuário com o salvo no banco
        if str(token_digitado).strip() == str(token_salvo):

            # Se estiver correto, atualiza o email antigo e limpa os campos temporários
            cursor.execute("""
                UPDATE usuarios 
                SET email = ?, novo_email_pendente = NULL, token_verificacao = NULL 
                WHERE id = ?
            """, (novo_email_pendente, usuario_id))
            conexao.commit()

            return True, "E-mail alterado com sucesso!"
        else:
            return False, "Código de verificação incorreto."

    except sqlite3.IntegrityError:
        return False, "Este novo e-mail já está sendo utilizado por outra conta."
    except Exception as erro:
        return False, f"Erro inesperado no banco: {erro}"
    finally:
        conexao.close()


def Enviar_email_smtp_senha(destinatario, token):
    """
    Envia o código de verificação de 6 dígitos para o e-mail atual do usuário (especifico para a senha).
    Retorna True se enviado com sucesso, ou False em caso de erro.
    """
    msg = EmailMessage()
    msg['Subject'] = 'Alteração de Senha no DevPath'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario

    msg.set_content(f"""
    Olá,
    Se você solicitou a alteração de SENHA da sua conta,
    seu código de verificação de 6 dígitos é: {token}
    
    Se você não solicitou essa alteração, por favor ignore esta mensagem.
    """)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA_APP_EMAIL)
            smtp.send_message(msg)
        return True
    except Exception as erro:
        print(f"Erro ao enviar o e-mail via SMTP: {erro}")
        return False


def Solicitar_alteracao_senha(email_atual, senha_atual, nova_senha):
    """
    Valida as credenciais e as regras da nova senha, gera um token temporário e o salva no banco.
    Em seguida, envia o token para o e-mail atual do usuário.
    Da return: (sucesso: bool, mensagem: str, id_do_usuario: int ou None)
    """
    if senha_atual == nova_senha:
        return False, "A nova senha não pode ser igual à atual.", None

    if len(nova_senha) < 6:
        return False, "A nova senha deve ter pelo menos 6 caracteres.", None

    conexao = Conectar_Banco()
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ? AND senha = ?", (email_atual, senha_atual))
        usuario = cursor.fetchone()

        if not usuario:
            return False, "E-mail ou senha atuais incorretos.", None

        usuario_id = usuario[0]
        token = str(secrets.randbelow(900000) + 100000) 

        # Salva a intenção de troca de senha no banco
        cursor.execute("""
            UPDATE usuarios 
            SET nova_senha_pendente = ?, token_verificacao = ? 
            WHERE id = ?
        """, (nova_senha, token, usuario_id))
        conexao.commit()

        # Diferente do e-mail novo, aqui o código vai para o e-mail ATUAL do usuário
        if Enviar_email_smtp_senha(email_atual, token):
            return True, "Código enviado com sucesso para o seu e-mail!", usuario_id
        else:
            return False, "Erro ao tentar enviar o código por e-mail.", None

    except Exception as erro:
        return False, f"Erro inesperado no banco: {erro}", None
    finally:
        conexao.close()


def Confirmar_codigo_senha(usuario_id, token_digitado):
    """
    Verifica se o token digitado corresponde ao salvo no banco de dados para a troca de senha.
    Se correto, atualiza a senha oficial do usuário e limpa os dados temporários.
    Da Return: (sucesso: bool, mensagem: str)
    """
    conexao = Conectar_Banco()
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT nova_senha_pendente, token_verificacao 
            FROM usuarios WHERE id = ?
        """, (usuario_id,))
        resultado = cursor.fetchone()

        if not resultado or not resultado[1]:
            return False, "Nenhuma solicitação de troca encontrada."

        nova_senha_pendente, token_salvo = resultado

        if str(token_digitado).strip() == str(token_salvo):
            # Atualiza a senha e limpa os campos temporários
            cursor.execute("""
                UPDATE usuarios 
                SET senha = ?, nova_senha_pendente = NULL, token_verificacao = NULL 
                WHERE id = ?
            """, (nova_senha_pendente, usuario_id))
            conexao.commit()
            return True, "Senha alterada com sucesso!"
        else:
            return False, "Código de verificação incorreto."

    except Exception as erro:
        return False, f"Erro inesperado no banco: {erro}"
    finally:
        conexao.close()


def Alterar_nome_de_usuario(nome_atual, senha, nome_novo):
    """ Função para alterar o nome do Usuário. 
Usando o nome de usuário e a senha, para o cursor procurar uma conta na tabela.
Então ele irá selecionar a conta em forma de lista
onde será selecionado somente o primeiro elemento da lista que é o id da conta,
para ser utilizado como identificador na parte de atualizar o nome de usuário.
"""
    if nome_novo == nome_atual:
        return False, "Nome atual é igual ao nome novo."

    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()


        cursor.execute('''
            SELECT id FROM usuarios
            WHERE nome_de_usuario = ?
            AND senha = ?
        ''', (nome_atual, senha)) # Parte de indenticar qual a conta o usuário quer alterar.

        usuario = cursor.fetchone() # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

        if not usuario: 
            return False, "Nome de usuário ou senha incorretos."

        cursor.execute('''
            UPDATE usuarios
            SET nome_de_usuario = ?
            WHERE id = ? 
        ''', (nome_novo, usuario[0])) # Parte onde o nome de usuário será alterado.

        conexao.commit()
        return True, "Nome de usuário alterado com sucesso!"

    except sqlite3.IntegrityError:
        return False, "Esse nome de usuário já está cadastrado."

    finally:
        conexao.close()
        