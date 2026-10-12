from database import Tabela_Cursos, ConectarCursos
# lógica de busca do DevPath + filtragem dinâmica

def BuscarCursos(
    nome_do_curso="",
    plataforma=None,
    linguagem=None,
    gratuito=None
):
    
    conexao = ConectarCursos()
    cursor = conexao.cursor()

    sql = """
        SELECT *
        FROM cursos
        WHERE nome_do_curso LIKE ?
    """

    parametros = [f'%{nome_do_curso}%']

    if plataforma is not None:
        sql += " AND plataforma = ?"
        parametros.append(plataforma)

    if linguagem is not None:
        sql += " AND linguagem = ?"
        parametros.append(linguagem)

    if gratuito is not None:
        sql += " AND gratuito = ?"
        parametros.append(linguagem)

    cursos.execute(sql, parametros)

    resultados = cursor.fetchall()

    conexao.close()
    return resultados  
