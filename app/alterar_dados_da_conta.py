import sqlite3
from app.cadastro_conta import Conectar_Banco


def Alterar_email(email, senha, novo_email):
    """ Função para alterar email. 
Usando o email antigo e senha, para o cursor procurar uma conta na tabela.
Então ele irá selecionar a conta em forma de lista
onde será selecionado somente o primeiro elemento da lista que é o id da conta,
para ser utilizado como identificador na parte de atualizar o email.
"""
    if '@' not in novo_email: # O email deve ter '@', ser diferente do antigo e o usuário deve ser encontrado.
        return False, "Digite um email válido."
    
    if novo_email == email:  # O email também deve ser diferente do antigo e o usuário deve ser encontrado.
        return False, "O email novo é igual ao atual."

    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()
    
        cursor.execute("""
            SELECT id FROM usuarios
            WHERE email = ? AND senha = ?
        """, (email, senha))  # Parte de indenticar qual a conta o usuário quer alterar.

        usuario = cursor.fetchone()  # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

        if not usuario:
            return False, "email atual ou senha incorretos."

        cursor.execute("""
            UPDATE usuarios
            SET email = ?
            WHERE id = ?
        """, (novo_email, usuario[0])) # Parte onde o email será alterado.

        conexao.commit()
        return True, "email alterado com sucesso!"

    except sqlite3.IntegrityError:
        return False, "Esse email já está cadastrado."

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


def Alterar_senha(email, senha, nova_senha):
    """ Função para alterar a senha.
Usando o email e senha antiga, para o cursor procurar uma conta na tabela. 
Então ele irá selecionar a conta em forma de lista
onde será selecionado somente o primeiro elemento da lista que é o id da conta,
para ser utilizado como identificador na parte de atualizar a senha.
"""
    if not 8 <= len(nova_senha) <= 20:  # Senha nova deve seguir o padrao.
        return False, "A senha deve ter entre 8 e 20 caracteres."

    if nova_senha == senha:  # Senha nova deve ser diferente da antiga.
        return False, "A nova senha é igual à atual."

    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT id FROM usuarios
            WHERE email = ?
            AND senha = ?
        ''', (email, senha)) # Parte de indenticar qual a conta o usuário quer alterar.

        usuario = cursor.fetchone() # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

        if not usuario:
            return False, "email ou senha atual incorretos."

        cursor.execute('''
            UPDATE usuarios
            SET senha = ?
            WHERE id = ?
        ''',(nova_senha, usuario[0])) # Parte onde a senha será alterada.
       
        conexao.commit()
        return True, "Senha alterada com sucesso!"
    finally:
        conexao.close()
