import sqlite3
from colorama import Fore, Back, Style, init
def Conectar_Banco():
    return sqlite3.connect("data/usuarios.db")


"""Função para alterar email. 
Usando o email antigo e a senha para indentificar a conta."""
def Alterar_email():
    conexao = Conectar_Banco()
    cursor = conexao.cursor()

    print(Fore.GREEN + '\n--ALTERANDO EMAIL--\n' + Style.RESET_ALL)
    email = input(Fore.CYAN + 'Digite seu email atual: ' + Style.RESET_ALL).strip()
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()
    novo_email = input(Fore.CYAN + 'Digite o novo email para troca: ' + Style.RESET_ALL).strip()

    cursor.execute('''
SELECT id FROM usuarios
WHERE email = ?
AND senha = ?
''', (email, senha) # Parte de indenticar qual a conta o usuário quer alterar.
)
    usuario = cursor.fetchone() # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

    if '@' in novo_email and novo_email != email and usuario: # O email deve ter '@', ser diferente do antigo e o usuário deve ser encontrado.
        id = usuario[0]
        cursor.execute('''
UPDATE usuarios
SET email = ?
WHERE id = ?
''', (novo_email, id)) # Parte onde o email será alterado de acordo com o id do usuário.
        conexao.commit()

        print(Fore.GREEN + '\n--EMAIL ALTERADO!--\n' + Style.RESET_ALL)
        print(Fore.GREEN + 'Digite - 1 para realizar outra operação.')
        print('Digite qualquer coisa para parar o programa.' + Style.RESET_ALL)
        voltar = input(Fore.CYAN + '\nOpção: ' + Style.RESET_ALL).strip()
        if voltar == '1':
            return True
        else:
            return False
    
    elif novo_email == email and not usuario:
        print(Fore.RED + '\n--CREDENCIAIS INVÁLIDAS, TENTE NOVAMENTE!--' + Style.RESET_ALL) # Caso o email seja igual ao antigo e as credenciais estejam erradas.
        return True
    
    elif novo_email == email:
        print(Fore.RED + '\n--EMAIL NOVO IGUAL AO ATUAL!--' + Style.RESET_ALL) # Caso o email seja igual ao antigo e as credenciais estejam corretas.
        return True

    
"""Função para alterar o nome do Usuário. 
Usando o nome antigo e a senha para indentificar a conta."""
def Alterar_nome_de_usuario():
    conexao = Conectar_Banco()
    cursor = conexao.cursor()

    print(Fore.GREEN + '\n--ALTERANDO NOME DE USUÁRIO--\n' + Style.RESET_ALL)
    nome_de_usuario = input(Fore.CYAN + 'Digite seu nome de usuário atual: ' + Style.RESET_ALL).strip()
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()
    novo_username = input(Fore.CYAN + 'Digite o novo nome de usuário para troca: ' + Style.RESET_ALL).strip()

    cursor.execute('''
SELECT id FROM usuarios
WHERE nome_de_usuario = ?
AND senha = ?
''', (nome_de_usuario, senha)) # Parte de indenticar qual a conta o usuário quer alterar.

    usuario = cursor.fetchone() # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

    if nome_de_usuario != novo_username and usuario: # Nome de usuário deve ser diferente e o usuário deve ser encontrado.
        id = usuario[0]
        cursor.execute('''
UPDATE usuarios
SET nome_de_usuario = ?
WHERE id = ? 
''', (novo_username, id)) # Parte onde o nome de usuário será alterado de acordo com o id do usuário.
        conexao.commit()

        print(Fore.GREEN + '\n--USUÁRIO ALTERADO!--\n' + Style.RESET_ALL) 
        print(Fore.GREEN + 'Digite - 1 para realizar outra operação.')
        print('Digite qualquer coisa para parar o programa.' + Style.RESET_ALL)
        voltar = input(Fore.CYAN + '\nOpção: ' + Style.RESET_ALL).strip()
        if voltar == '1':
            return True
        else:
            return False
    
    elif novo_username == nome_de_usuario and not usuario:
        print(Fore.RED + '\n--CREDENCIAIS INVÁLIDAS, TENTE NOVAMENTE!--' + Style.RESET_ALL) # Caso o nome de usuário seja igual ao antigo e as credencieis estejam incorretas. 
        return True
    
    elif novo_username == nome_de_usuario:
        print(Fore.RED + '\n--NOME DE USUÁRIO NOVO IGUAL AO ANTIGO!--' + Style.RESET_ALL) # Caso o nome de usuário seja igual ao antigo e as credenciais estejam corretas.
        return True


"""Função para alterar a senha.
Usando o email e senha antiga para indentificar a conta."""
def Alterar_senha():

    conexao = Conectar_Banco()
    cursor = conexao.cursor()

    print(Fore.GREEN + '\n--ALTERANDO SENHA--\n' + Style.RESET_ALL)
    email = input(Fore.CYAN + 'Digite seu email atual: ' + Style.RESET_ALL).strip()
    senha = input(Fore.CYAN + 'Digite sua senha: ' + Style.RESET_ALL).strip()
    nova_senha = input(Fore.CYAN + 'Digite sua nova senha para troca(MIN-8 MAX-20): ' + Style.RESET_ALL).strip()  

    cursor.execute('''
SELECT id FROM usuarios
WHERE email = ?
AND senha = ?
''', (email, senha)) # Parte de indenticar qual a conta o usuário quer alterar.

    usuario = cursor.fetchone() # Caso as Credenciais estejam corretas ele ira encontrar um id e selecionar ele pra váriavel.

    if 8 <= len(nova_senha) <= 20 and nova_senha != senha and usuario: # Senha nova deve seguir o padrao e ser diferente da antiga e o usuário deve ser encontrado.
        id = usuario[0]
        cursor.execute('''
UPDATE usuarios
SET senha = ?
WHERE id = ?
''',(nova_senha, id)) # Parte onde a senha será alterada de acordo com o id do usuário.
        conexao.commit()

        print(Fore.GREEN + '\n--SENHA ALTERADA COM SUCESSO!--\n' + Style.RESET_ALL)
        print(Fore.GREEN + 'Digite - 1 para realizar outra operação.')
        print('Digite qualquer coisa para parar o programa.' + Style.RESET_ALL)
        voltar = input(Fore.CYAN + '\nOpção: ' + Style.RESET_ALL).strip()
        if voltar == '1':
            return True
        else:
            return False

    elif len(nova_senha) < 8 or len(nova_senha) > 20 and not usuario:
        print(Fore.RED + '\n--SENHA FORA DO PADRÃO!--' + Style.RESET_ALL)
    
    elif nova_senha == senha and not usuario:
        print(Fore.RED + '\n--CREDENCIAIS INVÁLIDAS, TENTE NOVAMENTE!--' + Style.RESET_ALL) # Caso as senhas sejam iguais mas o usuário não foi encontrado. 
        return True   
    
    elif nova_senha == senha: 
        print(Fore.RED + '\n--SENHAS IGUAIS, NADA SERÁ ALTERADO!--' + Style.RESET_ALL) # Caso as senhas sejam iguais e o usuário foi encontrado.
        return True