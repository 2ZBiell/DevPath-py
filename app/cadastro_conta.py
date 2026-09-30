# Menu para cadastro de conta

def Cadastrar_Conta():        
    #docstring

    print('Cadastro de conta\n')
    email = input('Digite o seu email: ')
    nome_de_usuario = input('Digite seu ome de usuário: ')
    senha = input('Digite sua senha: ')

    if Validacao_Cadastro(email, nome_de_usuario, senha):
        print('\nConta cadastrada com sucesso!')


def Validacao_Cadastro(email, nome_de_usuario, senha):
    #docstring

    if len(senha) < 8:
        print('A senha deve conter no mínimo 8 caracteres.')
        return False

    if len(senha) > 20:
        print('A senha deve conter no máximo 20 caracteres.')
        return False

    if '@' not in email:
        print('E-mail inválido.')
        return False

    return True


while True:

    print('Digite 1 - Cadastrar nova conta')
    print('Digite 2 - Sair\n')

    opcao = input('Digite um número: ')

    if opcao == '1':
        Cadastrar_Conta()

    elif opcao == '2':
        print('Encerrando. . . ')
        break
    
    else:
        print('Opção inválida. Tente novamente.')
