from colorama import Style, Fore, init
import sqlite3

def Conectar_Banco_Cursos():
    return sqlite3.connect('data/cursos.db')


def Criar_Tabela_Favoritos():
    conexao = Conectar_Banco_Cursos()
    cursor = conexao.cursor()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS favoritos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome_do_curso TEXT NOT NULL,
plataforma TEXT NOT NULL,
linguagem TEXT NOT NULL,
gratuito BOOLEAN NOT NULL,
)
''')
    conexao.commit()

def Favoritar_cursos():
    conexao = Conectar_Banco_Cursos()
    cursor = conexao.cursor()

    print(Fore.GREEN + '\n--FAVORITANDO CURSO--\n' + Style.RESET_ALL)
    nome_do_curso = input(Fore.CYAN + 'Digite qual curso deseja favoritar: ' + Style.RESET_ALL).strip()

    cursor.execute('''
SELECT id FROM cursos
WHERE nome_do_curso = ?
''', (nome_do_curso))
 
    id_curso = cursor.fetchone()

    if id_curso:
        cursor.execute('''
INSERT INTO favoritos (id, nome_do_curso, plataforma, linguagem, gratuito)
VALUES ?, ?, ?, ?, ?
''' (id_curso[0], id_curso[1], id_curso[2], id_curso[3], id_curso[4]))
        conexao.commit()

        print(Fore.GREEN + '\nCURSO FAVORITADO!!\n' + Style.RESET_ALL)
        return True

    
    else:
        print(Fore.RED + '\nCURSO NÃO ENCONTRADO!!\n')
        return False

def Exibir_Cursos_Favoritos():
    conexao = Conectar_Banco_Cursos()
    cursor = conexao.cursor()

    cursor.execute('''
SELECT nome_do_curso 
FROM favoritos
''')

    cursos_favoritos = cursor.fetchall()

    for nome_do_curso in cursos_favoritos:
        print(nome_do_curso[0])