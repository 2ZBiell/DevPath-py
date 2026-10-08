from cadastro_conta import ConectarBanco
def Deletar_Usuario():
    conexao = ConectarBanco()
    cursor = conexao.cursor()
    id = int(input("\nDigite o ID do usuário que deseja deletar: "))

    cursor.execute("""
    DELETE FROM nome_de_usuario
    WHERE id = ?
    """, (id,))

    conexao.commit()

    print("\nUsuários depois do DELETE:")

    cursor.execute("SELECT * FROM nome_de_usuario")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(usuario)