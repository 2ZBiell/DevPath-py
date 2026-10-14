from app.cadastro_conta import Conectar_Banco

def Deletar_Usuario(email, senha):
    conexao = Conectar_Banco()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id FROM usuarios
            WHERE email = ? AND senha = ?
        """, (email, senha))

        usuario = cursor.fetchone()

        if not usuario:
            return False, "E-mail ou senha incorretos."

        cursor.execute("""
            DELETE FROM usuarios
            WHERE id = ?
        """, (usuario[0],))

        conexao.commit()
        return True, "Conta removida com sucesso!"
    finally:
        conexao.close()
