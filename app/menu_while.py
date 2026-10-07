from alterar_dados_da_conta import Alterar_senha, Alterar_nome_de_usuario, Alterar_email, Conectar_Banco
from cadastro_conta import Conectar_Banco, Criar_Tabela, Validacao_Cadastro, Cadastrar_Conta
from colorama import Fore, Style, init

# Menu improvisado usando o while
while True:

    print(Fore.GREEN + 'Digite 1 - Cadastrar nova conta')
    print('Digite 2 - Alterar dados de conta existente')
    print('Digite 0 - Sair\n' + Style.RESET_ALL)

    opcao = input(Fore.CYAN + 'Digite um número: ' + Style.RESET_ALL)

    if opcao == '1':
        Criar_Tabela()
        Cadastrar_Conta()
        break

    elif opcao == '2':
        print(Fore.GREEN + 'Digite 1 - Trocar Email')
        print('Digite 2 - Trocar Nome de Usuário')
        print('Digite 3 - Trocar Senha' + Style.RESET_ALL)
        alteracao_de_dados = input(Fore.CYAN + 'Digite um número: ' + Style.RESET_ALL)
        if alteracao_de_dados == '1':
            Alterar_email()
            break
        elif alteracao_de_dados == '2':
            Alterar_nome_de_usuario()
            break
        elif alteracao_de_dados == '3':
            Alterar_senha()
            break
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.' + Style.RESET_ALL)
            continue    

    elif opcao == '0':
        print(Fore.GREEN + 'Encerrando. . . ' + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + 'Opção inválida. Tente novamente.' + Style.RESET_ALL)
        continue